class Magic:
    def __init__(self):
        # Magic default name
        self.name = "Default_magic"
        # Magic types
        self.type = ["Therapy", "Destroyer"]

    # Therapy
    def gainHealth(self):
        return 10

    # Destroyer
    def loseHealth(self):
        return 10
