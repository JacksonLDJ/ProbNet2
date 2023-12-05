import nmap3
from .models import (
    Customer_data,
    Device_Data,
    Vulnerability_Data,
    Network_Services,
)
import MySQLdb

class NmapScanner(object):

    def __init__(self, db_host, db_user, db_password, db_name):
        self.db_host = "localhost"
        self.db_port = 3306
        self.db_user = "root"
        self.db_password = "aJ941S@>A/<+"
        self.db_name = "probnet2"

    def connect_to_database(self):
        return MySQLdb.connect(host=self.db_host, user=self.db_user, passwd=self.db_password, db=self.db_name)

    def perform_full_scan_and_save(self, target, args="-A"):
        nmap = nmap3.Nmap()
        scan_result = nmap.nmap
