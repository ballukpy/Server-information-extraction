import re
import subprocess
import req 

class IPextraction:


    def ip(self):
        output = subprocess.check_output(["netstat", "-a", "-n"]).decode("utf-8")
        pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'  #pattern for find ips

        ip_addresses = re.findall(pattern, output)
        unique_ips = set(ip_addresses)  #Remove additional IPs 
        filtered_ips = []                
        for ip_address in unique_ips:
            if ip_address == "0.0.0.0" or ip_address == "127.0.0.1":
                continue
            if ip_address.startswith("192.168") or ip_address.startswith("192.18.0") or ip_address.startswith("192.0") == True: #filter local ips
                continue
            filtered_ips.append(ip_address)

        return filtered_ips

    def final(self):
        ipaddresses = self.ip()
        for ipaddress in ipaddresses:
            info=req.reqip(ipaddress)
            print(info.viewinformation())
        

ipex=IPextraction()
ipex.final()
# print(ipex.ip())
