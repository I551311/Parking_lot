from repositories.lot import LotRepository

class ParkingLot():
    def __init__(self):
        self.lot_repository = LotRepository()

    def create_lot(self,lot):
        self.lot_repository.create_parking_lot(lot)
        print("Lot Created")

    def park_vehicle(self,vehicle):
        spot = self.find_available_spot(vehicle)
        if spot is not None:
            self.lot_repository.park_vehicle(vehicle,spot)
            print(f"Slot Booked on {spot.floor} floor, with id {spot.id}")
        else:
            print("Parking Lot Full")

    def unpark_vehicle(self,reg_num):
        spot = self.find_vehicle_spot(reg_num)
        if spot is not None:
            self.lot_repository.unpark_vehicle(spot)
            print(f"Slot is unbooked on {spot.floor} floor, with id {spot.id}")
        else:
            print("Vehicle Not found")

    def display_free_slot(self,type):
        curr_lot = self.lot_repository.get_curr_lot()
        is_available = 0
        for floor in curr_lot:
            for slot in floor.slots:
                if slot.type == type and slot.available:
                    is_available=1
                    print(f"Slot is available on floor {floor.id} with slot id {slot.id} ")

        if not is_available:
            print("No slot is available")
        

    def find_available_spot(self,vehicle):
        curr_lot = self.lot_repository.get_curr_lot()
        for floor in curr_lot:
            for slot in floor.slots:
                if slot.type == vehicle.type and slot.available:
                    return slot

        return None
    
    def find_vehicle_spot(self,reg_num):
        curr_lot = self.lot_repository.get_curr_lot()
        for floor in curr_lot:
            for slot in floor.slots:
                if slot.vehicle.registration_number == reg_num:
                    return slot

        return None

