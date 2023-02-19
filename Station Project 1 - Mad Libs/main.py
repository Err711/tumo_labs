import random


# number_1 = ''
# number_2 = ''
# measure_of_time = ''
# mode_of_transportation = ''
# adjective_1 = ''
# adjective_2 = ''
# adjective_3 = ''
# noun_1 = ''
# noun_2 = ''
# noun_3 = ''
# noun_4 = ''
# color = ''
# part_of_the_body_1 = ''
# part_of_the_body_2 = ''
# verb = ''
# color = ''
# silly_word = ''
#
# TEMPLATES = {
#     1: f'It was about {number_1} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}.'
#        f'The hospital is a/an {adjective_1} place, there are a lot of {adjective_2} {noun_1} here. '
#        f'There are nurses here who have {color} {part_of_the_body_1}. '
#        f'If someone wants to come into my room I told them that they have to {verb} first. '
#        f'I’ve decorated my room with {number_2} {noun_2}.'
#        f'Today I talked to a doctor and they were wearing a {noun_3} on their {part_of_the_body_2}. '
#        f'I heard that all doctors {verb} {noun_4} every day for breakfast. '
#        f'The most {adjective_3} thing about being in the hospital is the {silly_word} {noun_1}!',
#     2: f'',
#     3: f''
# }


class Game:
    def __init__(self):
        self.user_template = None
        self.templates = {
            1: 'It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of '
               'Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. '
               'There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I '
               'told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I '
               'talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all '
               'doctors (Verb) (Noun4) every day for breakfast. The most ( Adjective3) thing about being in the '
               'hospital is the (Silly Word ) (Noun) !',
            2: 'This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, '
               'sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective ('
               'Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, '
               'we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb ('
               'ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure '
               'of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we '
               'will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!',
            3: 'Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted '
               'forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There '
               'are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In '
               'the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of ('
               'Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for '
               '(Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is ('
               'Verb (ending in ing)) on a (Adjective5) (Noun5)!!',
        }

    def start_game(self):
        print(f'1 - {self.templates[1]}')
        print(f'2 - {self.templates[2]}')
        print(f'3 - {self.templates[3]}')
        self.user_template = int(input('Chose the template. '))
        print(self.user_template)

    def first_template(self):
        pass

    def second_template(self):
        pass

    def third_template(self):
        pass


a = Game()
print(a.start_game())
