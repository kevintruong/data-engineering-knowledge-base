import re

import os

import abc


class CardObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class BaseQuizFormater(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def format(self):
        pass


class StandardQuizFormatter(BaseQuizFormater):
    """
    format rule:

    """
    full_opts_reg = r'^-{0,1}[\s*]{0,}\[[xX\s\]]{0,1}\]\s*'
    not_correct_opts_reg = r'^-{0,1}[\s*]{0,}\[[\s\]]{0,1}\]\s*'
    correct_opts_reg = r'^-{0,1}[\s*]{0,}\[[xX]\]\s*'

    def __init__(self, content=None, title=None, childs=None, rule=None):
        super().__init__()
        self.content = content
        self.title = title
        self.childs = childs
        self.rule = rule

    def format(self):
        """

        ```json
        {
            "separator": "Answer: ((\d+,\s*)+\d+)" ,
            "transforms":[
                {
                    "type": "question",
                    "transform_rules": [
                        {
                            "source":"",
                            "target":""
                        }
                    ]
                }
            ]
        }

        ```

        :return:
        """
        try:
            # parse non correct quizzes
            # first_options = re.search(self.full_opts_reg, self.content, re.MULTILINE)
            self.card_name = self.title
            # self.question = self.content[:first_options.start()].rstrip("\n").lstrip("\n")

            card_determiners = re.search(self.rule['separator'],
                                         self.content,
                                         flags=re.MULTILINE)
            if card_determiners:
                quiz_explaination = self.content[card_determiners.end() + 1:].rstrip("\n").lstrip("\n")
                quiz_explaination_mark = card_determiners.start() - 1
                question = self.content[:quiz_explaination_mark]
                correct_ops = list(map(int, card_determiners[1].strip().split(",")))
            else:
                raise Exception("not found answer separator")
            pass
        except  Exception as e:
            pass

    def dump(self, root_path):
        if self.childs and len(self.childs):
            next_root = os.path.join(root_path, self.title)
            os.makedirs(next_root, exist_ok=True)
            for each_note in self.childs:
                each_note: StandardQuizFormatter
                each_note.dump(next_root)
        else:
            note_file = f"{root_path}/{self.title}.md"
            with open(note_file, 'w') as note_fd:
                self.format()
                note_fd.write(self.content)

        pass
