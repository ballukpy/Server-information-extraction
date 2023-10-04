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
            
            print(Fore.RED+"1 .",Fore.BLUE+"Start Scan IP Servers")
            print(Fore.RED+"99 .",Fore.BLUE+"Exit")
            while True:
                try:
                    khadamat_num=int(input(Fore.WHITE+"Enter the desired option number------> "))
                    if khadamat_num == 1  :
                        self.database()
                        self.viewinforamtion()
                        break
                    if khadamat_num == 99:
                        self.exit()
                        break                      
                except:
                    self.meno()
    def viewinforamtion(self):
        try:
            for self.num_ip in range(len(self.db)):  #Show IPs
                print(f"""{self.num_ip}.  {self.db["p"+str(self.num_ip)]["ip"]}""")
            pick_ip=int(input(Fore.WHITE+"Select the IP number to see IP information ----------->"))
            if pick_ip < len(self.db):
                print(f"""\nip : {self.db["p"+str(pick_ip)]["ip"]}
                      
                        continent name : {self.db["p"+str(pick_ip)]["continent_name"]}
                        country code : {self.db["p"+str(pick_ip)]["country_code"]}
                        country name : {self.db["p"+str(pick_ip)]["country_name"]}
                        country capital : {self.db["p"+str(pick_ip)]["country_capital"]}
                        city : {self.db["p"+str(pick_ip)]["city"]}
                        calling code : {self.db["p"+str(pick_ip)]["calling_code"]}
                        isp : {self.db["p"+str(pick_ip)]["isp"]}
                        connection type : {self.db["p"+str(pick_ip)]["connection_type"]}
                        organization : {self.db["p"+str(pick_ip)]["organization"]}""")
            else:
                print(Fore.RED+"Please choose from the available options.")
                os.system("cls")
                self.viewinforamtion()
            while True:  
                wanna=input(Fore.CYAN+"Do you want to return to the selection menu? y/n ---> ")
                if wanna != "":   
                    if wanna == "y":
                        os.system("cls")
                        self.viewinforamtion()
                        break
                    elif wanna == "n":
                        self.exit()
                        break
                    else:
                        wanna=input(Fore.CYAN+"Do you want to return to the selection menu? y/n ---> ")

        except:
            os.system("cls")
            self.viewinforamtion()

    def exit(self):  
        """  میخوای لخت منو ببینی  """  

        """ سخنی از پاندای کونگفوکار """  
          
        print(Fore.RED+"I hope there is no problem :)")
        os._exit(0)  

ipex=IPextraction()
ipex.meno()


