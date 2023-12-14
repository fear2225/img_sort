__version__ = '0.0.0'
__author__ = 'https://github.com/fear2225'

# External
import sys
import queue

import tkinter as tk
import typing
from tkinter import filedialog

from pathlib import Path

# Internal

# Consts

# TODO
# start directory
# show img
# move to dir
# new dir
# rename file

# todo
# recursive dir
# tree dir
# image formats filter

# ============================================================
class SourceFiles:
    # TODO write error handlers
    path: Path
    valid_types = ['.png', '.jpg', '.jpeg', '.gif']
    file_stack = queue.Queue()

    def __init__(self, path: Path, valid_types=None):
        self.path = path            # file container path

        if valid_types is not None:
            self.valid_types = valid_types

        self.update()

    def __repr__(self) -> str:
        return self.file_stack.queue

    def __len__(self) -> int:
        return self.file_stack.qsize()

    def update(self) -> None:
        """ update stack with valid type files """
        for file in self.path.iterdir():
            if self.is_valid_type(file):
                self.file_stack.put(file)

    def get(self) -> Path:
        return self.file_stack.get()

    def is_valid_type(self, file: Path) -> bool:
        """ return True if type is valid """
        return True if file.suffix in self.valid_types else False


# ============================================================
class ImageContainer(tk.Frame):
    """ Open image container """
    def __init__(self, master):
        super().__init__(master=master)
        # todo relative size

    def open_image(self, path: Path):
        """ Update image """
        pass


class ActionContainer(tk.Frame):
    """ Button and option container """
    def __init__(self, master):
        super().__init__(master=master)

    def place_folder_buttons(self):
        pass


class MainContainer(tk.Frame):
    """ Main frame container to hold image and buttons """
    path_source = None
    path_target = None

    def __init__(self, master):
        super().__init__(master=master)
        self.container_img = ImageContainer(self)
        self.container_opt = ActionContainer(self)

    def place_containers(self):
        self.container_img.pack()
        self.container_opt.pack()

    def choose_root_dir(self):
        try:
            self.path_source = Path(
                filedialog.askdirectory(title='source dir')
            )
            self.path_target = Path(
                filedialog.askdirectory(title='target dir')
            )
        except Exception as e:
            print(e)
            sys.exit(1)

        print(f'source: {self.path_source}',
              f'target: {self.path_target}',
              sep='\n')


def main_test():
    root = tk.Tk()

    main_window = MainContainer(root)
    main_window.choose_root_dir()

    root.mainloop()
    pass


# ============================================================
if __name__ == '__main__':
    main_test()
    pass
