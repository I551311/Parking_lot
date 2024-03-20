class Slot():
    def __init__(self,id,type,floor,vehicle={},available=True):
        self.id = id
        self.type = type
        self.floor = floor
        self.vehicle = vehicle
        self.available = available
        
        