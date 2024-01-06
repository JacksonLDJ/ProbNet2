# Import necessary modules and classes
import nmap3
from core.models import Device_Data, OS_Info, Port, Netsweeper_Result
from django.utils import timezone

#Resources used for NMAP Scanner: https://pypi.org/project/python-nmap/ | Neo1277's GitHub NMAP Scanner Project: https://github.com/Neo1277/nmap-scanner-django/tree/main#pip-install--r-requirementstxt


#Creates the NMAP Scanner class
class NMAP_Scanner():

    #Function to perform NMAP Scan and then save results
    def NMAP_Scan_And_Save(self, target, args="-A"):
        scan_result = self.NMAP_Scan(target, args)
        self.save_data(scan_result)

    #Function to perform NMAP scan and then save to the database.
    def save_data(self, scan_result):
        for host_key, host_data in scan_result['hosts'].items(): 
            device_data = self.extract_operating_system(host_data, host_key)
            self.extract_port_data(host_data, device_data)
            
    #Function to perform the NMAP scan
    def NMAP_Scan(self, target, args="-A"):
        scan = nmap3.Nmap()
        result = {
            'hosts': scan.nmap_version_detection(target, args=args)
        }
        return result
    
    """Function to extract operating_system information from the NMAP Scan. 
    Resources used: https://github.com/Neo1277/nmap-scanner-django/tree/main#pip-install--r-requirementstxt 
    https://stackoverflow.com/a/35485003/9655579
    https://stackoverflow.com/a/2710949/9655579"""
    def extract_operating_system(self, host_data, host_key):
        if 'osmatch' in host_data and len(host_data['osmatch']) > 0: #Checks for osmatch in host_data, length of osmatch dictionary is greater than 0
            osmatch = host_data['osmatch'][0]

            if 'osclass' in osmatch:
                osclass_data = osmatch['osclass']
                #Enters the OS information gathered from the NMAP scan and writes it to the OS_Info table..
                os_info_instance = OS_Info.objects.create(
                    type=osclass_data.get('type', ''),
                    vendor=osclass_data.get('vendor', ''),
                    osfamily=osclass_data.get('osfamily', ''),
                    osgen=osclass_data.get('osgen', ''),
                    accuracy=osclass_data.get('accuracy', '')
                )

                #Extract MAC Address
                mac_address = host_data.get('macaddress', {}).get('addr', '')
                


                # Create Device_Data entry and write host information to the Device_Data table.
                device_data = Device_Data.objects.create(
                    IP_Address=host_key,
                    Operating_System=os_info_instance,  # Associate the OS_Info instance
                    MAC_Address = mac_address


                )
                

                # Save the entries for both the OS and device data
                os_info_instance.save()
                device_data.save()
                return device_data

        return None
    
    #Function to extract ports from NMAP scan
    def extract_port_data(self, host_data, device_data):
        if "ports" in host_data:
            for port_data in host_data["ports"]:
                port = Port.objects.create(
                    protocol=port_data.get("protocol", ''),
                    portid=port_data.get('portid', ''),
                    reason=port_data.get('reason',''),
                    reason_ttl=port_data.get('reason_ttl',''),
                    device_data = device_data
                )

                port.save()


    def netsweeper(self, target, customer_id):
        scan = nmap3.NmapHostDiscovery()

        net_scan = scan.nmap_no_portscan(target)

        for ip_address, data in net_scan.items():
                 if 'macaddress' not in data: #Ensures that MAC address is in data generated, resolves ARP issue
                     continue 
                 mac_address_data = data.get('macaddress', {})
                 mac_address = mac_address_data.get('addr', '') if mac_address_data else ''

                 hostname_data = data.get('hostname', [{}])
                 hostname = hostname_data[0].get('name', '') if hostname_data else ''

                 vendor_data = data.get('vendor', {})
                 vendor = vendor_data.get('name', '') if vendor_data else ''
                 
                 state_data = data.get('state', {})
                 state = state_data.get('state', '') if state_data else ''

                 ip_address = ip_address

                 customer_id_checked = customer_id if customer_id and customer_id != 1 else None
                 if state.lower() == 'up':
                     Netsweeper_Result.objects.create(
                         ip_address = ip_address,
                         mac_address = mac_address,
                         hostname = hostname,
                         vendor = vendor,
                         state = state, 
                         customer_data_id = customer_id_checked
                     )
