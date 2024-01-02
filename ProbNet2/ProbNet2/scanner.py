# Import necessary modules and classes
import nmap3
from dataclasses import dataclass
from typing import List, Optional, Dict
from core.models import Device_Data, OS_Info, Port
from django.utils import timezone
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Define data classes and NMAP_Scanner class
@dataclass
class OsClass:
    type: str
    vendor: str
    osfamily: str
    osgen: str
    accuracy: str

@dataclass
class OsMatch:
    name: str
    accuracy: str
    line: str
    osclass: OsClass
    cpe: str

@dataclass
class Service:
    name: str
    product: str
    ostype: str
    method: str
    conf: str

@dataclass
class Script:
    name: str
    raw: str
    data: Dict[str, str]

@dataclass
class Port:
    protocol: str
    portid: str
    state: str
    reason: str
    reason_ttl: str
    service: Service
    cpe: List[Dict[str, Optional[str]]]
    scripts: List[Script]

@dataclass
class Host:
    osmatch: List[OsMatch]
    ports: List[Port]

@dataclass
class Root:
    hosts: Dict[str, Host]

class NMAP_Scanner():

    def NMAP_Scan_And_Save(self, target, args="-A"):
        scan_result = self.NMAP_Scan(target, args)
        logger.debug(scan_result)
        self.save_data(scan_result)

    def save_data(self, scan_result):
        for host_key, host_data in scan_result['hosts'].items(): 
            os_info_instance = self.extract_operating_system(host_data)
            #If nothing returns, it's not a host so we want to ignore the data
            if os_info_instance is not None:
                # Create Device_Data entry
                device_data = Device_Data.objects.create(
                    IP_Address=host_key,
                    Operating_System=os_info_instance,  # Associate the OS_Info instance
                )

                # Save the entry
                device_data.save()
            

    def NMAP_Scan(self, target, args="-A"):
        scan = nmap3.Nmap()
        result = {
            'hosts': scan.nmap_version_detection(target, args=args)
        }
        return result

    def extract_operating_system(self, host_data):
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

                return os_info_instance

        return None
    

    def extract_port_data(self, host_data):
        if "ports" in host_data["ports"]:
            for port_data in host_data["ports"]:
                port = Port(
                    protocol=port_data.get("protocol", ''),
                    protid=port_data.get('portid', ''),
                    reason=port_data.get('reason',''),
                    reason_ttl=port_data.get('reason.ttl',''),
                )

                port.save()

