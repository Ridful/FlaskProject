from datetime import datetime
import hashlib

class Agent:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.joindate = datetime.now()  # .strptime("%d/%m/%Y, %H:%M:%S")
        self.uuid = self.generate_unique_id()
        
    def generate_unique_id(self):
        posix_timestamp = str(int(self.joindate.timestamp()))
        unique_id = (posix_timestamp + "sv_SE" + str("-idk")).encode('ascii')
        hash_object = hashlib.md5(unique_id)
        return hash_object.hexdigest()
    
    def display_result(self):
        print(f"Name: {self.name}, IP: {self.ip}, joindate: {self.joindate}, uuid: {self.uuid}")
        
class Results(Agent):
    def __init__(self, name, ip, result):
        super().__init___(name, ip)    #this will init the parent
        self.result = result
    
    def display_result(self):
        print(f"Name: {self.name}, IP: {self.ip}, Result: {self.result}")