import os

story_1 = {
    "word_descriptions":
        [
            "number_1",
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
            "noun_4", "adjective_3"
        ],
    "template": "It was about {} {} ago when I arrived at the hospital in a {}."
                "The hospital is a/an {} place, there are a lot of {} {} here. There are nurses here who have {} {}. "
                "If someone wants to come into my room I told them that they have to {} first. "
                "I’ve decorated my room with {} {}. Today I talked to a doctor and they were wearing a {} on their {}. "
                "I heard that all doctors {} {} every day for breakfast. "
                "The most {} thing about being in the hospital is the {} {} !"
}

story_2 = {
    "word_descriptions":
        [
            'Proper Noun (Person’s Name)',
            'Noun',
            'Adjective (Feeling)',
            'Verb',
            'Adjective (Feeling) 2',
            'Animal',
            'Verb2',
            'Color',
            ' Verb (ending in ing) ',
            'Adverb (ending in ly)',
            'Number',
            'Measure of Time',
            'Color',
            'Animal',
            'Number',
            'Silly Word',
            'Noun2',
        ],
    "template": 'This weekend I am going camping with (). I packed my lantern, '
                'sleeping bag, and (). I am so () to () in a tent. '
                'I am () we might see a(n) (), I hear they’re kind of dangerous. '
                'While we’re camping, we are going to hike, fish, and (). '
                'I have heard that the () lake is great for (). '
                'Then we will () hike through the forest for () (). '
                'If I see a () () while hiking, I am going to bring it home as a pet! At night '
                'we will tell () () stories and roast () around the campfire!! '
}
story_3 = {
    "word_descriptions":
        [
            'Proper Noun (Person’s Name) ',
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
            'Noun5',
        ],
    "template": 'Dear (), I am writing to you from a () castle in an enchanted '
                'forest. I found myself here one day after going for a ride on a () () in (). There '
                'are () () and () () here! In the () there is a pool full of (). '
                'I fall asleep each night on a () of () and dream of () (). '
                'It feels as though I have lived here for () (). '
                'I hope one day you can visit, although the only way to get here now is () on a () ()!! '
}

STORIES = [story_1, story_2, story_3]


class MadLibs:
    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions
        self.user_input = []
        self.stories = STORIES
        self.user_story = None

    def text_fill(self, ):
        pass

    # def from_json(cls, name, stories=None):
    #     if not STORIES:
    #         stories = cls.stories
    #     fpath = os.path.join(stories, name)
    #     with open(fpath, "r") as f:
    #         data = json.load(f)
    #     mad_libs = cls(**data)
    #     return mad_libs

    def get_user_words(self):
        print("Please add words: ")
        for i in self.word_descriptions:
            user_input = input(i + ' ')
            self.user_input.append(user_input)
        return self.user_input

    def story_builder(self):
        self.user_story = self.template.format(*self.user_input)
        return self.user_story

    @staticmethod
    def story_present():
        print(story)


def select_template():
    print("Select a Mad Lib from the following list:")
    templates = os.listdir(MadLibs.path)
    template = input(str(templates) + " ")
    return template


temp_name = select_template()
mad_lib = MadLibs.from_json(temp_name)
words = mad_lib.get_user_words()
story = mad_lib.story_builder()
mad_lib.story_present()
