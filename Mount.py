class Mount:
    def __init__(self):
        # Mount default name
        self.name = "Default_mount"
        # Mount namelist
        self.namelist = ["Mount1", "Mount2", "Mount3"]
        # Mount speedlist
        self.speed = {"Default_mount": 10, "Mount1": 30, "Mount2": 50, "Mount3": 70}
        # Mount abilitylist
        self.ability = {
            "Default_mount": "No skill",
            "Mount1": "Speed_up",
            "Mount2": "Attack_up",
            "Mount3": "Defense_up",
        }

    # change Mount's name
    def changeMount(self, mount):
        Mount.name = mount
        return mount

    # change Mount's Speed
    def mountSpeed(self, mount):
        return_speed = Mount.speed[mount]
        return return_speed

    # change Mount's Ability
    def changeMountAbility(self, mount):
        return_ability = Mount.ability[mount]
        return return_ability
