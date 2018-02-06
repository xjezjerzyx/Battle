from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


# Black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 12, 120, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# create items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("HI-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
hielixer = Item("MEGA Elixer", "elixer", "Fully restore HP/MP of party", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Wykład 40 5:50 - koniec oglądania
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# magic = [{"name": "Fire", "cost": 10, "dmg": 100},
#          {"name": "Thunder", "cost": 12, "dmg": 80},
#          {"name": "Blizzard", "cost": 10, "dmg": 180}]

# initiate people
player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 4}]

player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, player_spells, player_items)

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
    elif index == 1:
        player.choose_magic()
        magic_choice = int( input("Choose magic: ")) - 1

        if magic_choice == -1:
            continue

        # magic_dmg = player.generate_spell_damage(magic_choice)
        # spell = player.get_spell_name(magic_choice)
        # cost = player.get_spell_mp_cost(magic_choice)

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        # magic_dmg = player.magic[magic_choice].generate_damage()
        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for ", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type == "black":
            player.reduce_mp(spell.cost)
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n " + spell.name + " deals " + str(magic_dmg), "points of damage" + bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) -1
        # item section

        if item_choice == -1:
            continue

        item = player.items[item_choice]["item"]

        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "\nNo more items left..." + bcolors.ENDC)
            continue

        player.items[item_choice]["quantity"] -= 1

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for ", str(item.prop), " HP" + bcolors.ENDC)
        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + item.name + " fully restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " deals ", str(item.prop), "points of damage" + bcolors.ENDC)



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

    # running = False


'''
print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
'''
