# Import necessary modules and classes
import nmap3
from dataclasses import dataclass
from typing import List, Optional, Dict
from core.models import Device_Data
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
        self.save_device_data(scan_result)

    def save_device_data(self, scan_result):
        for host_key, host_data in scan_result['hosts'].items():
            # Create Device_Data entry
            device_data = Device_Data.objects.create(
                Device_ID=host_key,
                IP_Address=host_key,
                Operating_Sytem=self.extract_operating_system(host_data),
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
        if 'osmatch' in host_data and host_data['osmatch']:
            # Assuming the first osmatch entry has the operating system information
            osmatch = host_data['osmatch'][0]
            if 'name' in osmatch:
                return osmatch['name']
        return ""