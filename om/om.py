from datetime import datetime
from random import randint


class Game(object):
    def __init__(self):
        timestamp = datetime.now()
        self.used_questions = []
        self.life = 5
        self.scenario = None
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

    def take_scenario(self):
        scenario = randint(0, 10)
        while scenario in self.used_questions:
            scenario = randint(0, 10)
        self.scenario = scenario

    def challenge(self):
        while str(input(self.questions[self.scenario][0])).lower() not in self.questions[self.scenario][1].lower():
            self.life -= 1
            print(f'You have {self.life} tries left')

        print("That's right you smarty dude!")

    def start(self):
        print('Rules: game time...')


g = Game()

g.start()
g.take_scenario()
g.challenge()
