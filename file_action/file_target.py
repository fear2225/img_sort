__version__ = '0.1.0'
__author__ = 'https://github.com/fear2225'

# External
import dataclasses
import typing
from pathlib import Path
import shutil

# Internal

# Consts


# ============================================================
@dataclasses.dataclass
class BranchObj:
    """Path to ttk.Treeview obj\n
    path: Path -> path to dir\n
    parent: str -> parent iid ('' for root)\n
    iid: str -> object name """

    path: Path
    parent: str
    iid: str
    index: int | str = -1
    open_: bool = True

    def __call__(self) -> dict:
        """ Return folder data in Treeview kwargs format """
        return {'parent': self.parent,
                'index': -1,
                'iid': self.iid,
                'text': self.path.name,
                'open': self.open_
                }


class TargetFiles:
    root: Path
    tree: dict
    current_seq: typing.Iterator

    def __init__(self, root_dir: Path):
        # set root path
        self.root = root_dir

    def __repr__(self) -> str:
        return str(self.root.absolute())

    def __getitem__(self, item) -> BranchObj:
        return self.tree[item]

    def as_dict(self) -> dict:
        """ dict view 'iid': 'BranchObj' """
        return self.tree

    @staticmethod
    def __seq_gen() -> typing.Iterator:
        """ str iid generator """
        i = 0
        while True:
            yield str(i)
            i += 1

    def __update(self, parent: Path, parent_iid) -> None:
        """ recursive traversal through dir """
        for folder in parent.iterdir():
            if not folder.is_dir():
                continue        # skip files
            # get file iid
            file_iid = next(self.current_seq)
            # add current branch
            self.tree |= {file_iid: BranchObj(folder, parent_iid, file_iid)}
            # traversal step
            self.__update(folder, file_iid)

    def update_tree(self) -> None:
        """ update tree """
        # create key generator
        self.current_seq = self.__seq_gen()
        # get zero iid for root
        root_iid = next(self.current_seq)
        # set root obj with no parent
        self.tree = {root_iid: BranchObj(self.root, '', root_iid)}
        # recursive traversal root directory
        self.__update(self.root, root_iid)

    def move_to(self, source_file: Path, iid: str) -> bool:
        """
        move file to new dir with original name
        :param source_file:
        :param iid: folder iid in tree
        :return: True on success
        """
        try:
            source_file.rename(self.tree[iid].path / source_file.name)
            return True
        except Exception as e:
            print(e)
            return False

    def copy_to(self, source_file: Path, iid: str) -> bool:
        """
        copy file to new dir with original name
        :param source_file:
        :param iid: folder iid in tree
        :return: True on success
        """
        try:
            shutil.copy(str(source_file), str(self.tree[iid].path))
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def remove_file(target: Path) -> bool:
        """
        unlink file
        :param target:
        :return: True on success
        """
        try:
            target.unlink()
            return True
        except Exception as e:
            print(e)
            return False

    def add_dir(self, target: Path) -> bool:
        """
        add new dir and update tree
        :param target:
        :return: True on success
        """
        # todo later
        try:
            # try to create new dir
            self.update_tree()
            return True
        except Exception as e:
            print(e)
            return False

    def rm_dir(self, target: Path) -> bool:
        """
        remove dir and update tree
        :param target:
        :return: True on success
        """
        # todo later
        try:
            self.update_tree()
            return True
        except Exception as e:
            print(e)
            return False


# ============================================================
if __name__ == '__main__':
    # todo add tests
    tf = TargetFiles(Path.cwd().parent)
    tf.update_tree()
    print(tf)
    from pprint import pprint

    pprint(tf.tree)
    pass
