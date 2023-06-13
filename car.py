from abc import ABC, abstractmethod
import Serviceable
from engine import Engine
from battery import Battery

class Car(Serviceable, Engine, Battery):
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    # @property
    # def engine(self):
    #     return self._engine

    # @property
    # def battery(self):
    #     return self._battery
    
    @abstractmethod
    def needs_service(self) -> bool:
        engine_service = self._engine.needs_service()
        battery_service = self._battery.needs_service()

        # Implement your logic based on the engine and battery service conditions
        # For example, return True if either engine or battery needs service

        return engine_service or battery_service  