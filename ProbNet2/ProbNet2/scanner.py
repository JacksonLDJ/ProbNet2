# Import necessary modules and classes
import nmap3
from core.models import Device_Data, OS_Info, Port
from django.utils import timezone



class NMAP_Scanner():

    def NMAP_Scan_And_Save(self, target, args="-A"):
        scan_result = self.NMAP_Scan(target, args)
        self.save_data(scan_result)

    def save_data(self, scan_result):
        for host_key, host_data in scan_result['hosts'].items(): 
            device_data = self.extract_operating_system(host_data, host_key)
            self.extract_port_data(host_data, device_data)
            

    def NMAP_Scan(self, target, args="-A"):
        scan = nmap3.Nmap()
        result = {
            'hosts': scan.nmap_version_detection(target, args=args)
        }
        return result

    def extract_operating_system(self, host_data, host_key):
        if 'osmatch' in host_data and len(host_data['osmatch']) > 0: #Checks for osmatch in host_data, length of osmatch array is greater than 0
            osmatch = host_data['osmatch'][0]

            if 'osclass' in osmatch:
                osclass_data = osmatch['osclass']

                os_info_instance = OS_Info.objects.create(
                    type=osclass_data.get('type', ''),
                    vendor=osclass_data.get('vendor', ''),
                    osfamily=osclass_data.get('osfamily', ''),
                    osgen=osclass_data.get('osgen', ''),
                    accuracy=osclass_data.get('accuracy', '')
                )

                # Create Device_Data entry
                device_data = Device_Data.objects.create(
                    IP_Address=host_key,
                    Operating_System=os_info_instance,  # Associate the OS_Info instance
                )

                # Save the entry
                device_data.save()
                return device_data

        return None
    

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


    def netsweeper(self, target):
        scan = nmap3.NmapHostDiscovery()

        net_scan = scan.nmap_no_portscan(target)



