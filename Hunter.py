from Magic import *
from Mount import *
from Weapon import *

Mount = Mount()
Magic = Magic()
Weapon = Weapon()


class Hunter:
    def __init__(self):
        self.name = "Default_player"
        self.specialSkill = "Default_mastery"
        self.attack_point = 10
        self.health = 100
        self.mana = 100
        self.speed = 100
        self.sorcery = None
        # Weapon
        self.weapon = None
        self.weapon_type = None
        self.weapon_characteristic = "No characteristic"
        # Mount
        self.mount = "Default_mount"
        self.mount_ability = None

    # change Mount
    def rideMount(self, new_mount):
        Hunter.mount = Mount.changeMount(new_mount)
        Hunter.mount_ability = Mount.changeMountAbility(new_mount)
        Hunter.speed += Mount.mountSpeed(new_mount)

    # change Weapon
    def selectWeapon(self, new_weapon):
        Hunter.weapon = new_weapon

    # use Weapon
    def useWeapon(self, user_weapon):
        characteristic, attack_point = Weapon.changedWeapon(user_weapon)
        Hunter.weapon_characteristic = characteristic
        Hunter.attack_point += attack_point

    # use magic
    def use_magic(self, type):
        if type == "Therapy":
            Hunter.health += Magic.gainHealth()
        elif type == "Destroyer":
            Hunter.health -= Magic.loseHealth()

    # attack
    def attack(self):
        return Hunter.attack_point
