import re
import subprocess
import req 

class IPextraction:


    def ip(self):
        output = subprocess.check_output(["netstat", "-a", "-n"]).decode("utf-8")
        pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

        ip_addresses = re.findall(pattern, output)

        for ip_address in ip_addresses:
            if ip_address == "0.0.0.0" :
                continue
            if ip_address == "127.0.0.1":
                continue
            
            return ip_address


