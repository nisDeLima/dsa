class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking_spaces = [big, medium, small]
    def addCar(self, carType: int) -> bool:
        if self.parking_spaces[carType - 1]:
            self.parking_spaces[carType - 1] -= 1
            return True
        return False
