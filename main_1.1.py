import random
from pprint import pprint

template_1 = ("It was about {} {} ago when I arrived at the hospital in a {}. "
              "The hospital is a/an {} place, there are a lot of {} {} here. There are nurses here who have {} {}. "
              "If someone wants to come into my room I told them that they have to {} first. "
              "I’ve decorated my room with {} {}. Today I talked to a doctor and they were wearing a {} on their {}. "
              "I heard that all doctors {} {} every day for breakfast. "
              "The most {} thing about being in the hospital is the {} {} !")
template_2 = ('This weekend I am going camping with (). I packed my lantern, '
              'sleeping bag, and (). I am so () to () in a tent. '
              'I am () we might see a(n) (), I hear they’re kind of dangerous. '
              'While we’re camping, we are going to hike, fish, and (). '
              'I have heard that the () lake is great for (). '
              'Then we will () hike through the forest for () (). '
              'If I see a () () while hiking, I am going to bring it home as a pet! At night '
              'we will tell () () stories and roast () around the campfire!!')
template_3 = ('Dear (), I am writing to you from a () castle in an enchanted '
              'forest. I found myself here one day after going for a ride on a () () in (). There '
              'are () () and () () here! In the () there is a pool full of (). '
              'I fall asleep each night on a () of () and dream of () (). '
              'It feels as though I have lived here for () (). '
              'I hope one day you can visit, although the only way to get here now is () on a () ()!!')

word_descriptions_1 = ["number_1",
                       "measure_of_time",
                       "mode_of_transportation",
                       "adjective_1",
                       "adjective_2",
                       "noun_1",
                       "color",
                       "part_of_the_body",
                       "verb_1",
                       "number_2",
                       "noun_2",
                       "noun_3",
                       "part_of_the_body_2",
                       "verb_2",
                       "noun_4",
                       "adjective_3",
                       'silly_word',
                       'noun_5']
word_descriptions_2 = ('Proper Noun (Person’s Name)',
                       'Noun',
                       'Adjective (Feeling)',
                       'Verb',
                       'Adjective (Feeling) 2',
                       'Animal',
                       'Verb2',
                       'Color',
                       'Verb (ending in ing) ',
                       'Adverb (ending in ly)',
                       'Number',
                       'Measure of Time',
                       'Color',
                       'Animal',
                       'Number',
                       'Silly Word',
                       'Noun2',)
word_descriptions_3 = ('Proper Noun (Person’s Name) ',
                       'Adjective',
                       'Color',
                       'Animal',
                       'Place',
                       'Adjective2',
                       'Magical Creature (Plural)',
                       'Adjective3',
                       'Magical Creature (Plural)2',
                       'Room in a House',
                       'Noun',
                       'Noun2',
                       'Noun(Plural)3',
                       'Adjective4',
                       'Noun (Plural)4',
                       'Number',
                       'Measure of time',
                       'Verb (ending in ing)',
                       'Adjective5',
                       'Noun5')


def start_game():
    templates = ("template_1", "template_2", "template_3")
    user_template = input(f"Select template{templates}: ")
    user_input = {}
    if user_template in templates:
        for word in word_descriptions_1:
            user_input[word] = input(f'Input {word}: ')
        sorted_input = {i: user_input[i] for i in user_input.keys()}
        sorted_input_keys = dict(sorted_input.items())
        pprint(sorted_input_keys)
        formatted_template = template_1.format(*user_input.values())
        print(formatted_template)
    else:
        raise ValueError('Type the right template name')


start_game()
