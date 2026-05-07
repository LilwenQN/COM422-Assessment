from Storm import Storm


class Tornado(Storm):
    def __init__(self, name, wind_speed):
        super().__init__(name, wind_speed)

    def calculate_classification(self) -> str:
        if self.wind_speed < 40: # changed <= to <
            return "Unclassified"
        elif self.wind_speed <= 72:
            return "F0"
        elif self.wind_speed in range(73, 113):
            return "F1"
        elif self.wind_speed in range(113, 158):
            return "F2"
        elif self.wind_speed in range(158, 206):
            return "F3"
        elif self.wind_speed in range(206, 261):
            return "F4"
        elif self.wind_speed >= 261:
            return "F5"
        return "Unclassified"

    def get_advice(self) -> str:
        classification = self.calculate_classification()

        if classification in ["F0", "F1"]: # removed "Unclassified"
            return "Find safe room/shelter, shield yourself from debris"
        elif classification in ["F2", "F3", "F4", "F5"]: # added comma between "F4" and "F5"
            return "Find underground shelter, crouch near to the floor covering your head with your hands"
        return "There is no need to panic"
