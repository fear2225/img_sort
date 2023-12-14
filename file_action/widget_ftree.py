__version__ = '0.1.0'
__author__ = 'https://github.com/fear2225'

# External
import tkinter as tk
from tkinter.ttk import Treeview

# Internal
from file_action.file_target import TargetFiles
from pathlib import Path

# Consts
log = False


# ============================================================
class ContainerTree(tk.Frame):
    tree: TargetFiles

    def __init__(self, master: tk.Misc, root: Path):
        super().__init__(master=master)

        self.tree = TargetFiles(root_dir=root)

        self.wTree = Treeview(master=self)
        # self.wTree.bind('<<TreeviewSelect>>', self.on_select)

    def set_tree(self) -> None:
        """ set file tree """
        self.tree.update_tree()
        for key, row in self.tree.as_dict().items():
            if log:
                print(f'{key}: {row}')
            self.wTree.insert(**row())
        self.wTree.pack()

    def on_select(self, event: tk.Event):
        """ test function """
        # ignore many inputs
        print(self.tree[self.wTree.selection()[-1]].path)


# ============================================================
if __name__ == '__main__':
    log = True

    app = tk.Tk()

    path_root = Path.cwd().parent

    tree = ContainerTree(app, path_root)
    tree.set_tree()
    tree.pack()

    app.mainloop()
    pass
