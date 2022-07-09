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
    def __init__(self, content=None, title=None, childs=None):
        super().__init__()
        self.content = content
        self.title = title
        self.childs = childs

    def format(self):
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
                note_fd.write(self.content)

        pass
