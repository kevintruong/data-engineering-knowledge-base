import os.path

from utils.md_utils.md_tree import MarkdownTree
from utils.md_utils.standard_quiz_fmt import StandardQuizFormatter

md_file = '../aws/aws-sa-training/resource/aws_csaa_practice_question.md'
parser = MarkdownTree()
with open(md_file, encoding="utf-8-sig") as md_test_file:
    cardsdeck_layout = parser.register(md_test_file.read())
    md_test_file.seek(0)
    lines = md_test_file.readlines()
    list_quiz = parser.convert_to_deck(cardsdeck_layout, lines, md_file)
    for each_quiz in list_quiz:
        each_quiz: StandardQuizFormatter
        each_quiz.dump(os.path.dirname(md_file))
