import os.path

import utils.mdtoc
from utils.md_utils.md_tree import MarkdownTree
from utils.md_utils.standard_quiz_fmt import StandardQuizFormatter, StandardNoteFormatter

rule = {
    "transforms": [
        {
            "type": "note",
            "transform_rules":
                [
                    {
                        "name": "regex_replace",
                        "kwargs": {
                            "source": r'^(\d): (.*$)',
                            "target": {
                                "prefix": "- [ ] ",
                                "suffix": "",
                                "match_group": 2
                            }
                        }
                    }
                ]
        }
    ]
}
md_file = '../aws/aws-sa-training/resource/CSAA_Training_Note/csaa_training_note.md'
parser = MarkdownTree()
with open(md_file, encoding="utf-8-sig") as md_test_file:
    cardsdeck_layout = utils.mdtoc.get_md_headlist(md_file)
    md_test_file.seek(0)
    lines = md_test_file.readlines()
    list_quiz = parser.convert_to_deck(cardsdeck_layout[0],
                                       lines,
                                       md_file,
                                       note_format_rule=rule,
                                       card_class=StandardNoteFormatter)
    for each_quiz in list_quiz:
        each_quiz: StandardNoteFormatter
        each_quiz.dump(os.path.dirname(md_file))
