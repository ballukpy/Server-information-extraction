import os
import re
import subprocess
from colorama import Fore, Back, Style
from src import req 
from src import artwork
os.system("cls")  



print(Fore.BLUE+artwork.balluk_art)
print()
print()
print()
print(Fore.YELLOW+"---------------------Hello, welcome to Bulluk security tool------------------------")
print()   
print(Fore.YELLOW+"------------------------https://github.com/ballukpy--------------------------------")
print()
print(Fore.RED+"---------------------------The more anonymous safer---------------------------------")
print()
class IPextraction:
    def __init__(self) :
        self.db={}

    def ip(self):  #find ips
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

    def database(self):   #creat database
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


    def meno(self):
        try:
            print(Fore.RED+"1 .",Fore.BLUE+"Start Scan IP Servers")
            print(Fore.RED+"99 .",Fore.BLUE+"Exit")
            while True:
                khadam_num=int(input(Fore.YELLOW+"Enter the desired option number------> "))
                if khadam_num == 1  :
                    print("tabe fal mishavad")
                    break
                if khadam_num == 99:
                    self.exit()
                    break                      
        except:
            self.meno()
    
    def viewinforamtion(self):
        pass
        #namayesh ip ha !!!!!!!!!!!
    
    
    def exit(self):
        print("I hope there is no problem :)")
        os._exit(0)  

ipex=IPextraction()
ipex.meno()


