from abc import ABC, abstractmethod


class Storm(ABC):
    def __init__(self, name, wind_speed):
        self.name = name
        self.wind_speed = wind_speed
        super().__init__()

    @abstractmethod
    def calculate_classification(self):
        pass

    @abstractmethod
    def get_advice(self):
        pass
