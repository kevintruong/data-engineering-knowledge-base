import os.path

from utils.md_utils.md_tree import MarkdownTree
from utils.md_utils.standard_quiz_fmt import StandardQuizFormatter

md_file = '../aws/aws-sa-training/resource/aws_csaa_practice_question.md'
parser = MarkdownTree()
with open(md_file, encoding="utf-8-sig") as md_test_file:
    rule = {
        "separator": r"Answer: ([\d ,]+)",
        "transforms": [
            {
                "type": "question",
                "transform_rules": [
                    {
                        "name": "regex_replace",
                        "kwargs": {
                            "source": r'^(\d:)',
                            "target": {
                                "prefix": "- [ ] : ",
                                "suffix": "",
                                "match_group": None
                            }
                        }
                    },
                    {
                        "name": "refill_correct_options",
                        "kwargs": {
                            "option_regex": r"^(\- \[ \] \: )",
                            "correct_ops": "- [x] :  "
                        }
                    },
                    {
                        "name": "add_separator",
                        "kwargs": {
                            "sep": "----"
                        }
                    },
                    {
                        "name": "add_tags_with_bert",
                        "kwargs": {

                        }
                    },
                    {
                        "name": "add_explain_link_type",
                        "kwargs": {
                            "link_type": "hasExplain::",
                            "target_fmt": "[[explanation_{question_title}.md]]"
                        }
                    },
                ]
            },
            {
                "type": "explanation",
                "transform_rules": [
                    {
                        "name": "regex_replace",
                        "kwargs": {
                            "source": r'^\- CORRECT',
                            "target": {
                                "prefix": "- ✅ : ",
                                "suffix": "",
                                "match_group": None
                            }
                        }
                    },
                    {
                        "name": "regex_replace",
                        "kwargs": {
                            "source": r'^\- INCORRECT',
                            "target": {
                                "prefix": "- ❌ : ",
                                "suffix": "",
                                "match_group": None
                            }
                        }
                    },
                    {
                        "name": "add_separator",
                        "kwargs": {
                            "sep": "\n\n----"
                        }
                    },
                    {
                        "name": "add_tags_with_bert",
                        "kwargs": {
                        }

                    }
                ]
            }
        ]
    }
    cardsdeck_layout = parser.register(md_test_file.read())
    md_test_file.seek(0)
    lines = md_test_file.readlines()
    list_quiz = parser.convert_to_deck(cardsdeck_layout,
                                       lines,
                                       md_file,
                                       note_format_rule=rule,
                                       card_class=StandardQuizFormatter)

    for bar in map(lambda f: f.dump(os.path.dirname(md_file)), list_quiz):
        pass
