import nmap3

class NMAP_Scanner():

    def NMAP_Full_Scan_Save(self, target, args="-A"):

        scan = nmap3()
        resulst = nmap.nmap_version