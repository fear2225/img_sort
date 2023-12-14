__version__ = '0.2.0'
__author__ = 'https://github.com/fear2225'

# External
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import sys

# Internal
from file_action.file_source import SourceFiles
from file_action.widget_ftree import ContainerTree
from file_action.widget_img_container import ContainerImage

# Consts
current_image: Path

# todo more stability
# todo multi type text support
# todo skipp button
# todo copy button and re:update stack
# todo delete button
# ============================================================


def choose_root_dir() -> Path:
    """ source directory file dialog """
    try:
        return Path(filedialog.askdirectory(title='source dir'))
    except Exception as e:
        print(e)
        sys.exit(1)


def exit_dialog(message: str, title: str='closing', status_code=0) -> None:
    """
    show dialog and exit
    :param message: message to show
    :param title: dialog title
    :param status_code: 0 if exit with error
    :return: None
    """
    messagebox.showwarning(title, message)
    sys.exit(status_code)


# ============================================================
def run_app():
    # chose root directory
    path_root = choose_root_dir()
    fsrc = SourceFiles(path_root)

    # check for empty SourceFiles error
    if not len(fsrc):
        exit_dialog(
            'No valid type files in chosen directory!'
        )

    # define main window
    app = tk.Tk()

    # set first image
    global current_image
    current_image = fsrc.get()

    # set container tree
    widget_tree = ContainerTree(app, path_root)
    widget_tree.set_tree()

    # set container first image
    widget_image = ContainerImage(app)
    widget_image.update_image(current_image)

    # pack
    widget_tree.pack(side='left')
    widget_image.pack(side='left')

    # action
    def next_file(event: tk.Event):
        # todo add exceptions
        global current_image
        print(current_image)
        widget_tree.tree.move_to(current_image, widget_tree.wTree.selection()[-1])
        current_image = fsrc.get()

        if current_image is None:
            exit_dialog('All images sorted!', status_code=1)
        widget_image.update_image(current_image)

    # bind action
    widget_tree.wTree.bind('<<TreeviewSelect>>', next_file)

    # start app
    app.mainloop()


# ============================================================
if __name__ == '__main__':
    run_app()
    pass
