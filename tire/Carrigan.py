from tire import Tire

class Carrigan(Tire):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        return self.wear