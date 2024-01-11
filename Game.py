# Author by Nikola(軟體三 蔡岳哲).
# NKNU SEM 411077010.
# Wrote from 2024/1/10 to 2024/1/11(beta ver.).
# This is final project of "軟體需求"'s lab.4's first homework.
# Any questions or suggestions, please feel free to contact me at aaron911024@gmail.com, thank you!

"""
For players and professors:
To start the game, run this python file(Game.py)
"""

# Edit history:
# 2024/1/10
# Had done all without:
# 1.Monster type: Ground, Water, Air.
# 2.Hunter's specialSkill.
# 3.Hunter's magic.

# 2024/1/11
# Finish Monster type.
# Finish Hunter's specialSkill.
# Finish Hunter's magic.
# Beta ver. has finished.


from Hunter import *
from Monster import *
from Mount import *
from Weapon import *

Hunter = Hunter()
Monster = Monster()
Mount = Mount()
Weapon = Weapon()


class Game:
    def __init__(self):
        self.name = "A Role Play Game!"

    # Game Start
    def start_game(self):
        print("Game start!")
        print("--------------------------------")

        # Set name
        print("Enter Hunter's name:")
        Hunter.name = input()
        print("Enter Monster's name:")
        Monster.name = input()

        # Playing Game
        while 1:
            break_signal = Game.toChoice()
            # if someone is dead
            if break_signal == False:
                break

        # Game End
        print("Game over!")

    # Back to Choice without fight
    def toChoice(self):
        print(
            "Choose your choice!:\n1: Show Hunter's information.\n2: Show Monster's information.\n3: Select Mount.\n4: Select Weapon.\n5: Fighting!"
        )
        user_choice = input()
        while Game.choice(user_choice) == True:
            print(
                "Choose your choice!:\n1: Show Hunter's information.\n2: Show Monster's information.\n3: Select Mount.\n4: Select Weapon.\n5: Fighting!"
            )
            user_choice = input()

        # Start Fight(choice == 5)
        if Game.choice(user_choice) == False:
            # Choose the attacker
            print(
                "Choose attacker or Heal the Health!\n1: Hunter.\n2: Monster.\n3: Eat medicine and sleep."
            )
            fight_choice = input()

            # Attacker == Hunter
            if fight_choice == "1":
                if Game.fight("Hunter") == False:
                    return False
                else:
                    return True

            # Attacker == Monster
            elif fight_choice == "2":
                if Game.fight("Monster") == False:
                    return False
                else:
                    return True

            # Hunter heal the Health
            elif fight_choice == "3":
                Hunter.health += 50
                if Hunter.health >= 100:
                    Hunter.health = 100
                print(
                    f"Hunter heal the Health!\nHunter's health is now {Hunter.health}!"
                )
                return True

    # Choices without fight(if choice == 5, break and goto fight())
    def choice(self, user_choice):
        # Show Mount namelist
        def mount_namelist():
            return Mount.namelist

        # Show Weapon namelist
        def weapon_namelist():
            return Weapon.namelist

        # Show Hunter's information(user_choice == 1)
        if user_choice == "1":
            print("Hunter's information:")
            print(
                f"Name: {Hunter.name}\nSpecial Skill: {Hunter.specialSkill}\nAttack Point: {Hunter.attack_point}\nHealth: {Hunter.health}\nMana: {Hunter.mana}\nSpeed: {Hunter.speed}\nMagic Power: {Hunter.sorcery}\nWeapon: {Hunter.weapon}\nWeapon Characteristic: {Hunter.weapon_characteristic}\nWeapon Type: {Hunter.weapon_type}\nMount: {Hunter.mount}\nMount Ability: {Hunter.mount_ability}"
            )
            print("Do you want to change Hunter's special skill?\n1. Yes\n2. No")
            skill_change_choice = input()
            if skill_change_choice == "1":
                print(
                    "Hunter's special skill:\n1. Sword mastery.\n2. Spear mastery.\n3. Bow mastery."
                )
                skill_choice = input()
                if skill_choice == "1":
                    Hunter.specialSkill = "Sword mastery"
                elif skill_choice == "2":
                    Hunter.specialSkill = "Spear mastery"
                elif skill_choice == "3":
                    Hunter.specialSkill = "Bow mastery"
                print("Changed successfully!")
            return True

        # Show Monster's information(user_choice == 2)
        elif user_choice == "2":
            print("Monster's information:")
            print(
                f"Name: {Monster.name}\nSpecial Skill: {Monster.specialSkill}\nAttack Point: {Monster.attack_point}\nHealth: {Monster.health}\nMana: {Monster.mana}\nSpeed: {Monster.speed}\nType: {Monster.type}\nWeapon: {Monster.weapon}\nWeapon Characteristic: {Monster.weapon_characteristic}\nWeapon Type: {Monster.weapon_type}\nMount: {Monster.mount}\nMount Ability: {Monster.mount_ability}"
            )
            print("Do you want to change Monster's type?\n1. Yes\n2. No")
            type_change_choice = input()
            if type_change_choice == "1":
                print("Monster's type:\n1. Ground.\n2. Water.\n3. Air.\n4. Fire.")
                type_choice = input()
                if type_choice == "1":
                    Monster.type = "Ground"
                elif type_choice == "2":
                    Monster.type = "Water"
                elif type_choice == "3":
                    Monster.type = "Air"
                elif type_choice == "4":
                    Monster.type = "Fire"
                print("Changed successfully!")
            return True

        # Select Mount(user_choice == 3)
        elif user_choice == "3":
            # Who's Mount
            print("Who's Mount?\n1.Hunter's Mount\n2.Monster's Mount")
            mount_choice = input()

            # define namelist of mount
            namelist = mount_namelist()

            # Show Mount's information
            print("Show Mount's information:?\n1.Yes\n2.No")
            information_choice = input()

            while 1:
                # Show Mount's information
                if information_choice == "1":
                    for i in range(len(namelist)):
                        print(
                            f"{Mount.namelist[i]}:\nSpeed: {Mount.speed[Mount.namelist[i]]}.\nAbility: {Mount.ability[Mount.namelist[i]]}."
                        )
                    information_choice = "2"

                # Select Mount
                elif information_choice == "2":
                    print("Which Mount do you want?")

                    # Show Mount's list
                    for i in range(len(namelist)):
                        print(f"{i+1}: {namelist[i]}")
                    # Mount's select
                    mount_select = int(input()) - 1

                    # Hunter's Mount
                    if mount_choice == "1":
                        # change Hunter mount name
                        Hunter.mount = namelist[mount_select]
                        # change Hunter mount ability
                        Hunter.mount_ability = Mount.ability[namelist[mount_select]]
                        # change Hunter speed
                        Hunter.speed += Mount.speed[namelist[mount_select]]
                        break

                    # Monster's Mount
                    elif mount_choice == "2":
                        # change Monster mount name
                        Monster.mount = namelist[mount_select]
                        # change Monster mount ability
                        Monster.mount_ability = Mount.ability[namelist[mount_select]]
                        # change Monster speed
                        Monster.speed += Mount.speed[namelist[mount_select]]
                        break
            return True

        # Select Weapon(user_choice == 4)
        elif user_choice == "4":
            print("Who's Weapon?\n1.Hunter's Weapon\n2.Monster's Weapon")
            weapon_choice = input()

            # define namelist of weapon
            namelist = weapon_namelist()

            # Show Weapon's information
            print("Show Weapon's information:?\n1.Yes\n2.No")
            information_choice = input()

            while 1:
                # Show Weapon's information
                if information_choice == "1":
                    for i in range(len(namelist)):
                        print(
                            f"{Weapon.namelist[i]}:\nCharacteristic: {Weapon.characteristic[Weapon.namelist[i]]}.\nType: {Weapon.type[Weapon.namelist[i]]}.\nAttack: {Weapon.attack[Weapon.namelist[i]]}."
                        )
                    information_choice = "2"

                # Select Weapon
                elif information_choice == "2":
                    print("Which Weapon do you want?")

                    # Show Weapon's list
                    for i in range(len(namelist)):
                        print(f"{i+1}: {namelist[i]}")
                    # Weapon's select
                    weapon_select = int(input()) - 1

                    # Hunter's Weapon
                    if weapon_choice == "1":
                        Hunter.weapon = namelist[weapon_select]
                        Hunter.weapon_characteristic = Weapon.characteristic[
                            namelist[weapon_select]
                        ]
                        Hunter.weapon_type = Weapon.type[namelist[weapon_select]]
                        Hunter.attack_point = (
                            Weapon.attack[namelist[weapon_select]] + 10
                        )
                        Hunter.speed -= 10
                        break

                    # Monster's Weapon
                    elif weapon_choice == "2":
                        Monster.weapon = namelist[weapon_select]
                        Monster.weapon_characteristic = Weapon.characteristic[
                            namelist[weapon_select]
                        ]
                        Monster.weapon_type = Weapon.type[namelist[weapon_select]]
                        Monster.attack_point = (
                            Weapon.attack[namelist[weapon_select]] + 10
                        )
                        Monster.speed -= 10
                        break
            return True

        # Fight!(user_choice == 5)
        elif user_choice == "5":
            return False

    # fight fight fgihththt!
    def fight(self, user):
        # Hunter attack
        if user == "Hunter":
            print("Do you want to attack or use the magic?\n1. Attack.\n2. Use magic.")
            hunter_attack_choice = input()
            if hunter_attack_choice == "1":
                original_health = Monster.health
                Monster.health -= Hunter.attack_point

                # if Monster died
                if Monster.health <= 0:
                    Monster.health == 0
                    print(
                        f"Monster's health has decrease from {original_health} into {Monster.health}!\nMonster has dead!"
                    )
                    return False

                # if Monster not died
                else:
                    print(
                        f"Monster's health has decrease from {original_health} into {Monster.health}!"
                    )
                    return True

            elif hunter_attack_choice == "2":
                print("Want magic do you want to use?\n1. Therapy\n2. Destroyer")
                hunter_magic_choice = input()

                # Hunter health heal
                if hunter_magic_choice == "1":
                    original_health = Hunter.health
                    Hunter.health += 10

                    if Hunter.health >= 100:
                        Hunter.health = 100
                    print(
                        f"Hunter's health has increased from {original_health} to {Hunter.health}"
                    )
                    return True

                elif hunter_magic_choice == "2":
                    original_health = Monster.health
                    Monster.health -= 10

                    # if Monster died
                    if Monster.health <= 0:
                        Monster.health == 0
                        print(
                            f"Monster's health has decrease from {original_health} into {Monster.health}!\nMonster has dead!"
                        )
                        return False

                    # if Monster not died
                    else:
                        print(
                            f"Monster's health has decrease from {original_health} into {Monster.health}!"
                        )
                        return True

        # Monster attack
        elif user == "Monster":
            original_health = Hunter.health
            Hunter.health -= Monster.attack_point

            # if Hunter died
            if Hunter.health <= 0:
                Hunter.health == 0
                print(
                    f"Hunter's health has decrease from {original_health} into {Hunter.health}!\nHunter has dead!"
                )
                return False

            # if Hunter not died
            else:
                print(
                    f"Hunter's health has decrease from {original_health} into {Hunter.health}!"
                )
                return True


# Run game
if __name__ == "__main__":
    Game = Game()
    Game.start_game()
