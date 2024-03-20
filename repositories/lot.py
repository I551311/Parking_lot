from models.floor import Floor
from models.slot import Slot

class LotRepository():
    def __init__(self):
        self.curr_lot = []

    def get_curr_lot(self):
        return self.curr_lot
    
    def create_parking_lot(self,lot):
        floors = self.initialise_floors(lot)
        self.curr_lot = floors

    def initialise_floors(self,lot):
        floors = []
        for floor_num in range(1,lot.no_of_floors+1):
            slots = self.initialise_slots(lot,floor_num)
            curr_floor = Floor(floor_num,slots)
            floors.append(curr_floor)
        return floors

    def initialise_slots(self,lot,floor_num):
        slots = list()
        for slot_num in range(1,lot.no_of_slots+1):
            if slot_num==1:
                curr_slot = Slot(slot_num,"Truck",floor_num)

            elif slot_num==2 or slot_num==3:
                curr_slot = Slot(slot_num,"Bike",floor_num)

            else:
                curr_slot = Slot(slot_num,"Car",floor_num)

            slots.append(curr_slot)

        return slots
    
    def park_vehicle(self,vehicle,spot):
        book_spot = self.curr_lot[spot.floor-1].slots[spot.id-1]
        book_spot.available = False
        book_spot.vehicle = vehicle
    
    def unpark_vehicle(self,spot):
        spot.available = True
        spot.vehicle = {}