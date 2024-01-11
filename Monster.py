from Magic import *
from Mount import *
from Weapon import *

Mount = Mount()
Magic = Magic()
Weapon = Weapon()


class Monster:
    def __init__(self):
        self.name = "Default_player"
        self.specialSkill = "Default_mastery"
        self.attack_point = 10
        self.health = 100
        self.mana = 100
        self.speed = 100
        self.type = "Default_type"
        # Weapon
        self.weapon = None
        self.weapon_type = None
        self.weapon_characteristic = "No characteristic"
        # Mount
        self.mount = "Default_mount"
        self.mount_ability = None

    # change Mount
    def rideMount(self, new_mount):
        Monster.mount = Mount.changeMount(new_mount)
        Monster.mount_ability = Mount.changeMountAbility(new_mount)
        Monster.speed += Mount.mountSpeed(new_mount)

    # change Weapon
    def selectWeapon(self, new_weapon):
        Monster.weapon = new_weapon

    # use Weapon
    def useWeapon(self, user_weapon):
        characteristic, attack_point = Weapon.changedWeapon(user_weapon)
        Monster.weapon_characteristic = characteristic
        Monster.attack_point += attack_point

    # attack
    def attack(self):
        return Monster.attack_point
