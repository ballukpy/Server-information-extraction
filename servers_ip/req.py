import requests
class reqip:
    def __init__(self,ip):
        self.ip=ip
   
    def getinformation(self):
        url="https://api.ipgeolocation.io/ipgeo?apiKey="
        api_key="c3a30ca5d83d4b6c9e761577d754cebb"
        response=requests.get(url + api_key + "&ip=" + self.ip)
        self.dict_infodict_info=response.json()
        return self.dict_infodict_info

    def viewinformation(self):
        info=self.getinformation()
        print(f"""ip : {info["ip"]}
continent name : {info["continent_name"]}
country code : {info["country_code2"]}
country name : {info["country_name"]}
country capital : {info["country_capital"]}
city : {info["city"]}
calling code : {info["calling_code"]}
isp : {info["isp"]}
connection type : {info["connection_type"]}
organization : {info["organization"]}""")
        

def final():
    ipaddresses=['35.186.224.25', '172.67.17.71', '162.159.134.234', '20.198.119.84', '138.199.12.82', '104.20.62.122']
    for ipaddress in ipaddresses:
        info=reqip(ipaddress)
        print(info.viewinformation())

final()