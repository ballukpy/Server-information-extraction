import subprocess
import re
class win_sec:
    def __init__(self):
        self.win_sec_db={}
        
    def run(self):
        self.completed = subprocess.check_output(["powershell", "-Command", "Get-MpComputerStatus"]).decode("utf-8")
        return self.completed
    
    
    def win_sec_db_creat(self):
        output = self.run()
        search_term = ["AMEngineVersion","AMProductVersion","AMRunningMode","AntivirusEnabled","ComputerID","FullScanEndTime","FullScanRequired","RealTimeProtectionEnabled","SmartAppControlState"]
        for i in range(len(search_term)):
            # search on output data
            matches = re.findall(f"{search_term[i]}\s+:\s+(\w+)", output)
            self.win_sec_db["p"+str(len(self.win_sec_db))]={search_term[i]:matches}
        return self.win_sec_db


windowssecurity=win_sec()

print(windowssecurity.win_sec_db_creat())

