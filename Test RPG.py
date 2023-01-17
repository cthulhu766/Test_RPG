import time


class Creator():
    def __init__(self, life, defence, damage):
        self.level = 1
        self.experience = 0
        self.life = life
        self.defence = defence
        self.damage = damage
        self.critical = 10

    def attack(self, user):
        user.life -= self.damage - user.defence


hero = Creator(100, 10, 40)
creature = Creator(40, 10, 20)


def attack_creature():
    creature_number = int(input('How many creatures do you want to attack?'))
    version = int(input('''
    1. Show the details
    2. Don`t show the details
    '''))
    if version == 1:
        while True:
            input('Press Enter to attack')
            time.sleep(2)
            hero.attack(creature)
            if creature.life <= 0 and creature_number == 1:
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
                break
            print(f'Hero has {hero.life} life')

    # Ускореная версия боя, без событий
    elif version == 2:
        while True:
            hero.attack(creature)
            if creature.life <= 0 and creature_number == 1:
                print('Creature is dead, You Won!')
                break
            elif creature.life <= 0 and creature_number > 1:
                creature_number -= 1

            for i in range(creature_number):
                creature.attack(hero)

            if hero.life <= 0:
                print('Hero is dead')
                break


def main():
    print('''
    1 Attack Creatures
    2 Attack Boss
    ''')
    choice = int(input('What do you want to do?'))
    if choice == 1:
        attack_creature()


while True:
    main()

