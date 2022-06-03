class Resistor:

    def __init__(self, model, value, power, accuracy):
        self.model = model
        self.value = value
        self.power = power
        self.accuracy = accuracy

    def __str__(self):
        return f"Model : {self.model}, Value : {self.value}, Power : {self.power}, Accuracy in percent : {self.accuracy}"