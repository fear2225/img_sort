__version__ = '0.1.0'
__author__ = 'https://github.com/fear2225'

# External
from pathlib import Path
import queue

# Internal


# ============================================================
class SourceFiles:
    path: Path
    valid_types = ['.png', '.jpg', '.jpeg', '.gif']
    file_stack = queue.Queue()

    def __init__(self, path: Path, valid_types: list=None):
        """
        Create stack of files in path folder. Put only valid type files.
        :param path: path to folder
        :param valid_types: list of valid types (with dot '.jpg') | if None use default img formats
        """
        self.path = path  # file container path

        if valid_types is not None:
            self.valid_types = valid_types

        self.update()

    def __repr__(self) -> str:
        return self.file_stack.queue

    def __len__(self) -> int:
        return self.file_stack.qsize()

    def update(self) -> int:
        """ update stack with valid type files """
        for file_ in self.path.iterdir():
            if self._is_valid_type(file_):
                self.file_stack.put(file_)
                print(file_)

        return len(self)

    def get(self) -> Path | None:
        """ get file path | None if stack empty """
        return self.file_stack.get() if len(self) else None

    def _is_valid_type(self, file_: Path) -> bool:
        """ return True if type is valid """
        return True if file_.suffix in self.valid_types else False


# ============================================================
if __name__ == '__main__':
    root_dir = Path.cwd()
    fsource = SourceFiles(root_dir)
    print(len(fsource))
    while file := fsource.get():
        print(file)
    print('[*] nice')
    print(type(fsource.valid_types))
    pass
