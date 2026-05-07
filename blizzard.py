from Storm import Storm


class Blizzard(Storm):
    def __init__(self, name, wind_speed, temp):
        self.temp = temp
        super().__init__(name, wind_speed)

    def calculate_classification(self) -> str:
        if self.wind_speed >= 45 and self.temp <= -12: # moved this condition to top
            return "Severe Blizzard"
        elif self.wind_speed >= 35:
            return "Blizzard" # capitalised "blizzard"
        return "Snow Storm"

    def get_advice(self) -> str:
        classification = self.calculate_classification()

        if classification == "Severe Blizzard":
            return "Keep warm, avoid all travel."
        # inserted below condition for Blizzard
        elif classification == "Blizzard":
            return "Keep warm, Do not travel unless absolutely essential."
        return "Take care and avoid travel if possible."
