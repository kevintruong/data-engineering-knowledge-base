#  Copyright (c) 2021 Vu Truong - kevin.truong.ds@gmail.com all rights reserved
import re

from utils.md_utils.standard_quiz_fmt import BaseQuizFormater


class Node:
    def __init__(self, rank, line, title, children):
        self.rank = rank
        self.line = line
        self.title = title
        self.children = children


class MarkdownTree:
    def __init__(self):
        self.dircount = 0
        self.filecount = 0
        self.titleTree = []
        # self.filename = filename

    def get_deck_title(self):
        pass

    def is_heading_level(self, line, level):
        heading_regex_list = [
            r'(^#{1} \s{0,})(.*)',
            r'(^#{2} \s{0,})(.*)',
            r'(^#{3} \s{0,})(.*)',
            r'(^#{4} \s{0,})(.*)',
            r'(^#{5} \s{0,})(.*)',
            r'(^#{6} \s{0,})(.*)'
        ]
        highest_heading = re.search(heading_regex_list[level - 1], line, flags=re.MULTILINE)
        if highest_heading:
            return True
        return

    def get_headers(self, md_text, max_priority=6):
        """
        Retrieves a list of header, priority pairs in a given Markdown text.
        Format: (Header Title, Priority)
        """
        # lines_iter = iter(md_text.splitlines())

        # Skip the first line because it's the Title
        # next(lines_iter)

        # List of Tuples: (Header Title, Number of #)
        header_priority_pairs = []
        in_code_block = False
        for index, line in enumerate(md_text.splitlines()):
            if line.startswith('```'):
                in_code_block = not in_code_block

            elif not in_code_block and line.startswith('#') and ' ' in line:
                md_header, header_title = line.split(' ', 1)

                # Check if md_header has all '#'
                if md_header != md_header[0] * len(md_header):
                    continue

                # Check if md_header is of lower priority than listed
                if len(md_header) > max_priority:
                    continue

                if header_title.lower() != 'table of contents' and len(header_title) > 1:
                    header_priority_pairs.append(Node(header_title, len(md_header), index, []))

        return self.sequentialize_header_priorities(header_priority_pairs)

    def sequentialize_header_priorities(self, header_priority_pairs):
        """
        In a case where a H3 or H4 succeeds a H1, due to the nature of the Table of Contents generator\
        which adds the number of tabs corresponding to the header priority/strength, this will sequentialize\
        the headers such that all headers have a priority of atmost 1 more than their preceeding header.
        [('Header 1', 1), ('Header 3', 3), ('Header 4', 4)] -> [('Header 1', 1), ('Header 2', 2), ('Header 3', 3)]
        """
        # Go through each header and and if we see a pair where the difference in priority is > 1, make them sequential
        # Ex: (H1, H3) -> (H1, H2)
        for i in range(len(header_priority_pairs) - 1):
            header, priority = header_priority_pairs[i]
            next_header, next_priority = header_priority_pairs[i + 1]

            if (next_priority - priority > 1):
                header_priority_pairs[i + 1] = (next_header, priority + 1)

        return header_priority_pairs

    def walk(self, node, prefix=""):
        if node.children:
            count = 0
            for child in node.children:
                count += 1
                if count == len(node.children):
                    print(prefix + "└───" + child.title)
                    if child.children:
                        self.walk(child, prefix + "    ")
                else:
                    print(prefix + "├───" + child.title)
                    if child.children:
                        self.walk(child, prefix + "│   ")

    def convert_to_deck(self,
                        node: Node,
                        deck_lines,
                        file_name,
                        line_scope=-1,
                        user=Node,
                        deck_tags: list = None,
                        note_format_rule=None,
                        card_class=BaseQuizFormater):
        cards = []
        for index in range(0, len(node.children), 1):
            if index + 1 >= len(node.children):
                current, next_ = node.children[index].line - 1, line_scope
                next_line_scope = line_scope
                title = node.children[index].title
            else:
                current, next_ = node.children[index].line - 1, node.children[index + 1].line - 1
                next_line_scope = node.children[index + 1].line - 1
                title = node.children[index].title

            if len(node.children[index].children):
                next_ = node.children[index].children[0].line - 1

                card_content = "\n".join(deck_lines[current:next_]).replace("\n\n\n", "\n\n")

                new_cards = self.convert_to_deck(node.children[index],
                                                 deck_lines,
                                                 file_name,
                                                 line_scope=next_line_scope,
                                                 user=user,
                                                 deck_tags=deck_tags,
                                                 note_format_rule=note_format_rule,
                                                 card_class=card_class)
                try:
                    card = card_class(content=card_content,
                                      title=title,
                                      childs=new_cards,
                                      rule=note_format_rule)
                    cards.append(card)
                except Exception as e:
                    raise e
                    pass
            else:
                card_content = "\n".join(deck_lines[current:next_]).replace("\n\n\n", "\n\n")
                try:
                    card = card_class(content=card_content, title=title, rule=note_format_rule)
                    if card:
                        cards.append(card)
                except:
                    continue
        return cards
