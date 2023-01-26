import time
import random


class Creator():  # Створюємо класс істот
    def __init__(self, life, defence, damage):
        self.level = 1
        self.boss_level = 1
        self.experience = 0
        self.life = life
        self.defence = defence
        self.damage = damage
        self.critical = 10  # Шанс критичного урону
        self.penetrating = 15  # Шанс игнорування броні

    def attack(self, user):  # функція атаки
        if random.randint(1, 100) <= self.critical:  # перевірка на 10-ти відсотковий критичний удар
            if random.randint(1, 100) <= self.penetrating:
                user.life -= self.damage * 2
            else:
                user.life -= (self.damage - user.defence) * 2
        else:
            if random.randint(1, 100) <= self.penetrating:  # перевірка на 15-ти відсотковий удар крізь броню
                user.life -= self.damage
            else:
                user.life -= self.damage - user.defence


hero = Creator(100, 10, 40)  # параметри героя
creature = Creator(40, 10, 20)  # параметри істоти

def show(name):
    print(f'''
    life: {name.life}
    defence: {name.damage}
    damage: {name.defence}
    critical hit: {name.critical}
    penetrating: {name.penetrating}
    ''')

def attacking_boss():
    boss = Creator(100 + hero.boss_level * 10, 20 + hero.boss_level * 2, 35 + hero.boss_level * 3)
    print('Hero parameters:')
    show(hero)
    print('Boss parameters:')
    show(boss)
    hero_life = hero.life
    version = int(input('''
        1. Show the details
        2. Don`t show the details
        '''))
    # детальний бій (кто кого б'є і т.д.)
    if version == 1:
        while True:
            input('Press Enter to attack')
            time.sleep(2)
            hero.attack(boss)
            if boss.life <= 0:
                print('The boss is dead')
                hero.life = hero_life
                hero.boss_level +=1
                break

            print(f'Boss has {boss.life} life')
            time.sleep(2)
            print('Now the boss is attacking you.')
            time.sleep(2)
            boss.attack(hero)

            if hero.life <= 0:
                print('Hero is dead')
                hero.life = hero_life
                break
            print(f'Hero has {hero.life} life')

    # прискорена версія бою (треба пофіксити)
    elif version == 2:
        pass
    if hero.boss_level > 99:
        print('It is the last boss`')

def increase_level():
    hero.level += 1
    print(f'Your Lvl is {hero.level}')
    print("""
    1. Life
    2. Defence
    3. Damage
    4. Critical hit chance
    5. Penetrating
    """)
    option = int(input('Which one do you choose?'))
    if option == 1:
        hero.life += 10
        print(f'Now you have {hero.life} life')
    elif option == 2:
        hero.defence += 2
        print(f'Now you have {hero.defence} defence')
    elif option == 3:
        hero.damage += 2
        print(f'Now you have {hero.damage} damage')
    elif option == 4:
        hero.critical += 1
        print(f'Now you have {hero.critical} critical')
    elif option == 5:
        hero.penetrating += 1
        print(f'Now you have {hero.penetrating} penetrating')


def attack_creature():
    creature_number = int(input('How many creatures do you want to attack?'))
    number_expirience = creature_number
    hero_life = hero.life
    version = int(input('''
    1. Show the details
    2. Don`t show the details
    '''))
    # детальний бій (кто кого б'є і т.д.)
    if version == 1:
        while True:
            input('Press Enter to attack')
            time.sleep(2)
            hero.attack(creature)
            if creature.life <= 0 and creature_number == 1:

                hero.experience += number_expirience*50
                hero.life = hero_life
                if hero.experience >= hero.level*100:

                    increase_level()
                    hero.experience = 0

                print('Creature is dead, You Won!')

                break
            elif creature.life <= 0 and creature_number > 1:
                creature_number -= 1
                print(f'You killed 1 creature and {creature_number} creatures are left')
                creature.life = 40

            print(f'Creature has {creature.life} life')
            time.sleep(2)
            print('Now creature are attacking you.')
            time.sleep(2)
            for i in range(creature_number):
                creature.attack(hero)

            if hero.life <= 0:
                print('Hero is dead')
                hero.life = hero_life
                break
            print(f'Hero has {hero.life} life')

    # прискорена версія бою (треба пофіксити)
    elif version == 2:
        pass


def main():
    while True:

        print('''
        1 Attack Creatures
        2 Attack Boss
        3 Exit
        ''')
        choice = int(input('What do you want to do?'))
        if choice == 1:
            attack_creature()
        elif choice == 2:
            attacking_boss()
        elif choice == 3:
            break



main()
