from models.lot import Lot
from models.vehicle import Vehicle
from services.parking_lot import ParkingLot

def main():
    parking_lot = ParkingLot()
    while True:
        print("1. CREATE PARKING LOT")
        print("2. PARK")
        print("3. UNPARK")
        print("4. DISPLAY")
        print("5. EXIT")

        command = input("Enter command: ") 
        if command == "1":
            lot_id = input("Enter lot id: ") 
            no_of_floors = input("Enter no of floors: ") 
            no_of_slots = input("Enter no of slots: ") 
            lot = Lot(lot_id,no_of_floors,no_of_slots)
            parking_lot.create_lot(lot)

        elif command == "2":
            reg_num = input("Enter Reg Number: ") 
            color = input("Enter color of vehicle: ") 
            type = input("Enter type of vehicle: ") 
            vehicle = Vehicle(reg_num,color,type)
            parking_lot.park_vehicle(vehicle)

        elif command == "3":
            reg_num = input("Enter Reg Number: ") 
            parking_lot.unpark_vehicle(reg_num)
        elif command == "4":
            type = input("Enter type of vehicle: ") 
            parking_lot.display_free_slot(type)
        elif command == "5":
            break

if __name__== "__main__":
    main()