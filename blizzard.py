from Storm import Storm


class Blizzard(Storm):
    def __init__(self, name, wind_speed, temp):
        self.temp = temp
        super().__init__(name, wind_speed)

    def calculate_classification(self) -> str:
        if self.wind_speed >= 35:
            return "blizzard"
        elif self.wind_speed >= 45 and self.temp <= -12:
            return "Severe Blizzard"
        return "Snow Storm"

    def get_advice(self) -> str:
        classification = self.calculate_classification()

        if classification == "Severe Blizzard":
            return "Keep warm, avoid all travel."
        return "Take care and avoid travel if possible."
