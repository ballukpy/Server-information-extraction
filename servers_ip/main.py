import re
import subprocess
import req 

class IPextraction:
    def __init__(self) :
        self.db={}

    def ip(self):
        output = subprocess.check_output(["netstat", "-a", "-n"]).decode("utf-8")
        pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'  #pattern for find ips

        ip_addresses = re.findall(pattern, output)
        unique_ips = set(ip_addresses)  #Remove additional IPs 
        filtered_ips = []                
        for ip_address in unique_ips:
            if ip_address == "0.0.0.0" or ip_address == "127.0.0.1":
                continue
            if ip_address.startswith("192.") or ip_address.startswith("10.") or ip_address.startswith("172.") == True: #filter local ips
                continue
            filtered_ips.append(ip_address)

        return filtered_ips

    def database(self):
        ipaddresses = self.ip()
        for ipaddress in ipaddresses:
            info=req.reqip(ipaddress)
            main_db=info.getinformation()
            self.db["p"+str(len(self.db))]={
            "ip":main_db["ip"],
            "continent_name":main_db["continent_name"],
            "country_code":main_db["country_code2"],
            "country_name":main_db["country_name"],
            "country_capital":main_db["country_capital"],
            "city":main_db["city"],
            "calling_code":main_db["calling_code"],
            "isp":main_db["isp"],
            "connection_type":main_db["connection_type"],
            "organization":main_db["organization"]}
        return self.db



ipex=IPextraction()
print(ipex.database())

