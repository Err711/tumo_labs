import random


class MadLips:
    def __init__(self):
        self.user_input = []
        self.user_template = ''

    @staticmethod
    def user_template():
        input(f'Select the template form list: ')

    def template_1(self):
        story_1 = ("It was about {} {} ago when I arrived at the hospital in a {}."
                   "The hospital is a/an {} place, there are a lot of {} {} here. There are nurses here who have {} {}."
                   "If someone wants to come into my room I told them that they have to {} first. "
                   "I’ve decorated my room with {} {}."
                   "Today I talked to a doctor and they were wearing a {} on their {}."
                   "I heard that all doctors {} {} every day for breakfast."
                   "The most {} thing about being in the hospital is the {} {} !")
        words_1 = ("number_1",
                   "measure_of_time",
                   "mode_of_transportation",
                   "adjective_1",
                   "adjective_2",
                   "noun_1",
                   "color",
                   "part_of_the_body",
                   "verb",
                   "number_2",
                   "noun_2",
                   "noun_3",
                   "part_of_the_body_2",
                   "noun_4",
                   "adjective_3")

        self.user_input.append(*words_1)

    def template_2(self):
        pass

    def template_3(self):
        pass


a = MadLips
print(a.user_template())
