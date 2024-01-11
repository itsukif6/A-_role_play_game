class Weapon:
    def __init__(self):
        # Weapon default name
        self.name = "Default_weapon"
        # Weapon namelist
        self.namelist = ["Weapon1", "Weapon2", "Weapon3"]
        # Weapon characteristics
        self.characteristic = {
            "Default_weapon": "No characteristic",
            "Weapon1": "Ice_attack",
            "Weapon2": "Fire_attack",
            "Weapon3": "Wind_attack",
        }
        # Weapon type
        self.type = {
            "Default_weapon": "Sword",
            "Weapon1": "Spear",
            "Weapon2": "Sword",
            "Weapon3": "Bow",
        }
        # Weapon attack points
        self.attack = {
            "Default_weapon": 10,
            "Weapon1": 30,
            "Weapon2": 35,
            "Weapon3": 40,
        }

    # change Weapon data
    def changedWeapon(self, new_weapon):
        Weapon.name = new_weapon
        return Weapon.characteristic[new_weapon], Weapon.attack[new_weapon]
