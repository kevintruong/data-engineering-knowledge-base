import abc
import os
import re
from keybert import KeyBERT


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

    def regex_replace(self, source, target):
        def replace_by_target(match_object):
            return f"{target['prefix']}{match_object.group(target['match_group'])}{target['suffix']}"

        self.question = re.sub(source, replace_by_target, self.question, 0, re.MULTILINE)

    def refill_correct_options(self, option_regex):
        def replace_collect_option(match_object):
            return f"- [x] {match_object}"

        options = re.findall(option_regex, self.question, re.MULTILINE)
        for each_correct_option_index in self.correct_ops:
            correct_ops = options[each_correct_option_index - 1][0]
            re_fill = replace_collect_option(options[each_correct_option_index - 1][2])
            self.question = self.question.replace(correct_ops, re_fill)

    def add_explain_link_type(self, link_type, target_fmt):
        append_link_type = "\n\n- {link_type} ".format(link_type=link_type) + target_fmt.format(
            question_title=self.title)
        self.question += append_link_type

    def add_tags_with_bert(self):
        kw_model = KeyBERT()
        keywords = kw_model.extract_keywords(docs=self.question)
        tags = "\n\n"
        for each_keyword in keywords:
            tags += f"#{each_keyword[0]} "
        self.question += tags

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
                            "name": "regex_replace"
                            "kwargs": {
                                "source":"^(\d): (.*$)",
                                "target": "- [ ] $2
                            }
                        },
                        {
                            "name":refill_correct_options
                            "option_regex": "^\-\[ \] (.*$)"

                        }

                    ]
                },
                {
                    "type": "explanation",
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

            card_determiners = re.search(self.rule["separator"],
                                         self.content,
                                         flags=re.MULTILINE)
            if card_determiners:
                self.quiz_explaination = self.content[card_determiners.end() + 1:].rstrip("\n").lstrip("\n")
                quiz_explaination_mark = card_determiners.start() - 1
                self.question = self.content[:quiz_explaination_mark]
                self.correct_ops = list(map(int, card_determiners[1].strip().split(",")))
            else:
                raise Exception("not found answer separator")
            for each_transforms_type in self.rule['transforms']:
                each_transforms_type: dict
                if each_transforms_type['type'] == "question":
                    for each_transform in each_transforms_type['transform_rules']:
                        if hasattr(self, each_transform['name']):
                            transform_func = getattr(self, each_transform['name'])
                            transform_func(**each_transform['kwargs'])
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
            explan_note_file = f"{root_path}/explanation_{self.title}.md"
            self.format()
            with open(note_file, 'w') as note_fd:
                note_fd.write(self.question)
            with open(explan_note_file, 'w') as explanation_fd:
                explanation_fd.write(self.quiz_explaination)

        pass
