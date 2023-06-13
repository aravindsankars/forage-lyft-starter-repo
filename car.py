import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def needs_service(self) -> bool:
        engine_service = self._engine.needs_service()
        battery_service = self._battery.needs_service()

        # Implement your logic based on the engine and battery service conditions
        # For example, return True if either engine or battery needs service

        return engine_service or battery_service  