from datetime import date
from engine.model import calliope, glissade, palindrome, rorschach, thovex

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return calliope(last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return glissade(last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        return palindrome(last_service_date, warning_light_on)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return rorschach(last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return thovex(last_service_date, current_mileage, last_service_mileage)