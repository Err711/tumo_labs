import json
import os


class MadLibs:
    path = "./templates"

    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions
        self.user_input = []
        self.story = []

    @classmethod
    def from_json(cls, name, path=None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_libs = cls(**data)
        return mad_libs

    def get_user_words(self):
        print("Please add words: ")
        for i in self.word_descriptions:
            user_input = input(i + ' ')
            self.user_input.append(user_input)
        return self.user_input

    def story_builder(self):
        self.story = self.template.format(*self.user_input)
        return self.story

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
