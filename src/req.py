import requests
class reqip:
    def __init__(self,ip):
        self.ip=ip
    def getinformation(self):
        url="https://api.ipgeolocation.io/ipgeo?apiKey="
        api_key="edbe5ec010a3457a82ef63b56acad5f2"
        response=requests.get(url + api_key + "&ip=" + self.ip)
        self.dict_infodict_info=response.json()
        return self.dict_infodict_info
    

