from tire import Tire

class Carrigan(Tire):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        for tire in self.wear:
            if tire >= 0.9:
                return True
        return False