from classes.game import Person, bcolors
from classes.magic import Spell

#Black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 12, 120, "black")

#Wykład 40 5:50 - koniec oglądania

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 12, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 180}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("==================")
    player.choose_action()
    #player.choose_magic()
    choice = input("Choose action: ")
    index = int(choice) - 1
    # print("You chose", index)
    #print("You choose", player.get_spell_name(int(choice)))

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg)
    elif index ==1:
        player.choose_magic()
        magic_choice = int( input("Choose magic: ")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n " + spell + " deals " + str(magic_dmg), "points of damage" + bcolors.ENDC)



    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ", enemy_dmg)

    print("-----------------------------------------------")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + " of " + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + " of " + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lose! :( " + bcolors.ENDC)
        running = False
    else:
        running = True

    #running = False


'''
print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
'''
