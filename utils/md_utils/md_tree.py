#  Copyright (c) 2021 Vu Truong - kevin.truong.ds@gmail.com all rights reserved
import re

from utils.logger.logger import app_logger
from utils.md_utils.standard_quiz_fmt import StandardQuizFormatter


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
        self.titleTree = {}
        # self.filename = filename

    def get_deck_title(self):
        pass

    def get_heading_level(self, line, level):
        heading_regex_list = [
            r'(^#{1} \s{0,})(.*)',
            r'(^#{2} \s{0,})(.*)',
            r'(^#{3} \s{0,})(.*)',
            r'(^#{4} \s{0,})(.*)',
            r'(^#{5} \s{0,})(.*)',
            r'(^#{5} \s{0,})(.*)',
            r'(^#{6} \s{0,})(.*)'
        ]
        highest_heading = re.search(heading_regex_list[level - 1], line, flags=re.MULTILINE)
        if highest_heading:
            return True
        return

    def register(self, lines):
        last_node = {}
        current_prior_node_dict = {}
        # using to find the prior node by recording all the current prior node at all # levels
        commit_checking_point = 0  # avoid commit in code block surrounded by ```
        for index, line in enumerate(lines.splitlines(), start=1):
            if "```" in line:
                commit_checking_point ^= 1
                continue
            if commit_checking_point == 1:
                continue

            titlecount = 0
            for char in line:
                if char == '#':
                    titlecount += 1
                else:
                    break
            if titlecount != 0:
                if not self.get_heading_level(line, titlecount):
                    titlecount = 0

            if titlecount != 0:
                temp_node = {"rank": titlecount,
                             "line": index,
                             "title": line[titlecount + 1:].strip(),
                             "children": []}
                temp_node = Node(titlecount, index, line[titlecount + 1:].strip(), [])

                if self.titleTree == {}:
                    if temp_node.rank:
                        self.titleTree = temp_node
                        current_prior_node_dict[titlecount] = temp_node
                    else:
                        self.titleTree = Node(1, index, "No Title", [])
                        current_prior_node_dict[1] = self.titleTree
                        for i in range(2, titlecount):
                            fake_node = Node(i, index, "┐", [])
                            current_prior_node_dict[i - 1].children.append(fake_node)
                            current_prior_node_dict[i] = fake_node
                        current_prior_node_dict[titlecount - 1].children.append(temp_node)
                        current_prior_node_dict[titlecount] = temp_node

                else:
                    if titlecount < last_node.rank:
                        parent_rank = self.titleTree.rank
                        for each_range in range(titlecount - 1, self.titleTree.rank, -1):
                            if current_prior_node_dict.get(each_range, None):
                                parent_rank = each_range
                        current_prior_node_dict[parent_rank].children.append(temp_node)
                        current_prior_node_dict[titlecount] = temp_node
                        # update current_prior_node_dict to delete low rank node
                        current_prior_node_dict = {key: current_prior_node_dict[key] for key in current_prior_node_dict
                                                   if
                                                   key <= titlecount}
                    elif titlecount == last_node.rank:
                        parent_rank = self.titleTree.rank
                        for each_range in range(titlecount - 1, self.titleTree.rank, -1):
                            if current_prior_node_dict.get(each_range, None):
                                parent_rank = each_range
                        current_prior_node_dict[parent_rank].children.append(temp_node)
                        current_prior_node_dict[titlecount] = temp_node
                    elif titlecount > last_node.rank:
                        if titlecount - last_node.rank == 1:
                            current_prior_node_dict[titlecount - 1].children.append(temp_node)
                            current_prior_node_dict[titlecount] = temp_node
                        else:
                            # script will hit this when the rank difference between
                            # titlerank & lastnode is more than one, because you need to fill fake node.
                            # tempRank = last_node["rank"]
                            # we don't need fake_node there,
                            current_prior_node_dict[last_node.rank].children.append(temp_node)
                            current_prior_node_dict[titlecount] = temp_node

                    else:
                        print("Error Occurs! Have no idea.")
                last_node = temp_node
        try:
            app_logger.info(self.titleTree.title)  # print first title
            return self.titleTree
        except Exception:
            app_logger.info("***Error Occurs!***:")
            app_logger.info("Please make sure input file satisfied Markdown format. At least it should hava one "
                            "markdown title. : )")
            return None

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
                        note_format_rule=None):
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
                                                 note_format_rule=note_format_rule
                                                 )
                card = StandardQuizFormatter(content=card_content,
                                             title=title, childs=new_cards,
                                             rule=note_format_rule)
                cards.append(card)
            else:
                card_content = "\n".join(deck_lines[current:next_]).replace("\n\n\n", "\n\n")

                card = StandardQuizFormatter(content=card_content, title=title, rule=note_format_rule)
                if card:
                    cards.append(card)
        return cards
