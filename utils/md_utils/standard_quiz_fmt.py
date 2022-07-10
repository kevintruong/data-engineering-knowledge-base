import abc
import os
import re
from keybert import KeyBERT

from utils.logger.logger import app_logger
from utils.vocabulary import vectorizer, full_vocob_list


class CardObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class BaseQuizFormater(abc.ABC):
    def __init__(self, content=None,
                 title=None,
                 childs=None,
                 rule=None):
        self.content = content
        self.title = title
        self.childs = childs
        self.rule = rule

    def regex_replace(self, content, source, target):
        def replace_by_target(match_object):
            if not target['match_group']:
                return f"{target['prefix']}{target['suffix']}"
            else:
                return f"{target['prefix']}{match_object.group(target['match_group'])}{target['suffix']}"

        return re.sub(source, replace_by_target, content, 0, re.MULTILINE)

    def add_explain_link_type(self, content, link_type, target_fmt):
        append_link_type = "\n- {link_type} ".format(link_type=link_type) + target_fmt.format(
            question_title=self.title)
        content += append_link_type
        return content

    def add_tags_with_bert(self, content):
        kw_model = KeyBERT()
        keywords = kw_model.extract_keywords(docs=content,
                                             keyphrase_ngram_range=(1, 2),
                                             vectorizer=vectorizer,
                                             seed_keywords=full_vocob_list
                                             )
        if len(keywords):
            tags = "\n- "
            for each_keyword in keywords:
                tags += f"#{each_keyword[0].replace(' ', '_')} "
            content += tags
        return content

    def add_separator(self, content, sep: str):
        content += sep
        return content

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

    def __init__(self,
                 content=None,
                 title=None,
                 childs=None,
                 rule=None
                 ):
        super().__init__(content, title, childs, rule)
        self.card_name = self.title
        # self.question = self.content[:first_options.start()].rstrip("\n").lstrip("\n")

        card_determiners = re.search(self.rule["separator"],
                                     self.content,
                                     flags=re.MULTILINE)
        if card_determiners:
            self.is_quiz = True
            self.quiz_explanation = self.content[card_determiners.end() + 1:].rstrip("\n").lstrip("\n")
            quiz_explaination_mark = card_determiners.start() - 1
            self.question = self.content[:quiz_explaination_mark]
            self.correct_ops = list(map(int, card_determiners[1].strip().split(",")))
            self.correct_ops.sort()
        else:
            app_logger.warning(f"{self.title} is not valid quiz format")
            self.is_quiz = False

    def refill_correct_options(self, content, option_regex, correct_ops):
        def replace_collect_option(match_object):
            return f"- [x]:"

        def replace_str_index(text, start_index=0, end_index=-1, replacement=''):
            return '%s%s%s' % (text[:start_index], replacement, text[end_index + 1:])

        options = re.finditer(option_regex, content, re.MULTILINE)
        all_options_match = [x for x in options]
        for each_correct_option_index in self.correct_ops:
            correct_match_options = all_options_match[each_correct_option_index - 1]
            content = replace_str_index(content, start_index=correct_match_options.start(),
                                        end_index=correct_match_options.end(),
                                        replacement=correct_ops)
        return content

    def format(self):
        try:
            app_logger.info(f"formatting for {self.title}")
            # parse non correct quizzes
            # first_options = re.search(self.full_opts_reg, self.content, re.MULTILINE)
            for each_transforms_type in self.rule['transforms']:
                each_transforms_type: dict
                if each_transforms_type['type'] == "question":
                    for each_transform in each_transforms_type['transform_rules']:
                        app_logger.info(
                            f"run transform {each_transform['name']} - kwargs {each_transform['kwargs']}")
                        if hasattr(self, each_transform['name']):
                            transform_func = getattr(self, each_transform['name'])
                            self.question = transform_func(self.question,
                                                           **each_transform['kwargs'])
                        pass
                if each_transforms_type['type'] == "explanation":
                    for each_transform in each_transforms_type['transform_rules']:
                        if hasattr(self, each_transform['name']):
                            app_logger.info(
                                f"run transform {each_transform['name']} - kwargs {each_transform['kwargs']}")
                            transform_func = getattr(self, each_transform['name'])
                            self.quiz_explanation = transform_func(self.quiz_explanation,
                                                                   **each_transform['kwargs'])
        except  Exception as e:
            raise e

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
            if self.is_quiz:
                self.format()
                with open(note_file, 'w') as note_fd:
                    note_fd.write(self.question)
                with open(explan_note_file, 'w') as explanation_fd:
                    explanation_fd.write(self.quiz_explanation)
            else:
                with open(note_file, 'w') as note_fd:
                    note_fd.write(self.content)


class StandardNoteFormatter(BaseQuizFormater):
    """
    format rule:

    """
    full_opts_reg = r'^-{0,1}[\s*]{0,}\[[xX\s\]]{0,1}\]\s*'
    not_correct_opts_reg = r'^-{0,1}[\s*]{0,}\[[\s\]]{0,1}\]\s*'
    correct_opts_reg = r'^-{0,1}[\s*]{0,}\[[xX]\]\s*'

    def __init__(self,
                 content=None,
                 title=None,
                 childs=None,
                 rule=None
                 ):
        super().__init__(content, title, childs, rule)
        self.card_name = self.title

    def format(self):
        try:
            # parse non correct quizzes
            # first_options = re.search(self.full_opts_reg, self.content, re.MULTILINE)

            for each_transforms_type in self.rule['transforms']:
                each_transforms_type: dict
                pass
        except:
            pass

    def dump(self, root_path):
        note_file = f"{root_path}/{self.title}.md"
        if self.childs and len(self.childs):
            next_root = os.path.join(root_path, self.title)
            os.makedirs(next_root, exist_ok=True)
            for each_note in self.childs:
                each_note.dump(next_root)
            with open(note_file, 'w') as note_fd:
                note_fd.write(self.content)
        else:
            self.format()
            with open(note_file, 'w') as note_fd:
                note_fd.write(self.content)
