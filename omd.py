from datetime import datetime
from random import randint


class Game(object):
    def __init__(self):
        timestamp = datetime.now()
        self.type = {
            'location': [],
            'scenario': []
        }
        self.life = 5
        self.difficulty = None
        self.questions = [
            ('Из какого слова из семи букв можно убрать одну "букву", чтобы осталось две буквы?', 'букварь'),
            ('Больше часа, меньше минуты.', 'секундная стрелка'),
            ('На каком языке говорят молча? ', 'язык жестов'),
            ('Мальчик заплатил за бутылку с пробкой 11 рублей. Бутылка стоит на 10 рублей больше, чем пробка. '
             'Сколько стоит пробка?', '50 копеек'),
            ('В каком городе спрятались мужское имя и сторона света?', 'владивосток'),
            ('Семь сестер находятся на даче, где каждая занята каким-то делом. '
             'Первая сестра читает книгу, вторая — готовит еду, третья — играет в шахматы,'
             ' четвертая — разгадывает судоку, пятая — занимается стиркой, шестая — ухаживает за растениями. '
             'А чем занимается седьмая сестра? ', 'играет в шахматы'),
            ('По чему ходят часто, а ездят редко?', 'по лестнице'),
            ('Идет то в гору, то с горы, но остается на месте', 'дорога'),
            ('В каком слове 5 "е" и никаких других гласных?', 'переселенец'),
            ('Где встречается такое, что конь через коня перепрыгивает?', 'шахматы')
        ]
        self.locations = ('Описание комнаты №1',
                          'Описание комнаты №2',
                          'Описание комнаты №3',
                          'Описание комнаты №4',
                          'Описание комнаты №5',
                          'Описание комнаты №6',
                          'Описание комнаты №7',
                          'Описание комнаты №8',
                          'Описание комнаты №9',
                          'Описание комнаты №10')

    def take_step(self, module=None):
        value = randint(0, 9)
        while value in self.type[module]:
            value = randint(0, 9)
        self.type[module].append(value)

    def challenge(self):
        while str(input(self.questions[self.type['scenario'][-1]][0])).lower() not in \
                self.questions[self.type['scenario'][-1]][1].lower() and g.life > 0:
            self.life -= 1
            print(f'You have {self.life} tries left')
        if g.life <= 0:
            print('Oh no!')
        else:
            print("That's right you smarty dude!")

    def chapter_enter(self):
        print(self.locations[self.type['location'][-1]], 'Да начнется испытание!\n')

    def start(self):
        print('Добро пожаловать в игру, Мисетр Утка. У тебя есть 5 жизней, чтобы отгадать несколько загадок и выбраться'
              'на свободу.\nВыбери уровень сложности:\n1 - Я слаб духом\n2 - Нормал мод\n3 - Хочу страдать')
        while self.difficulty not in (1, 2, 3):
            self.difficulty = int(input('Введи цифру!\n'))


if __name__ == '__main__':
    g = Game()
    g.start()
    for mode in range(g.difficulty * 3):
        g.take_step('location')
        g.take_step('scenario')
        g.chapter_enter()
        g.challenge()
        if g.life <= 0:
            input('Game over!')
            exit()
    print("You nailed it!")

