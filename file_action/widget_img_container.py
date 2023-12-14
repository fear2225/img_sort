__version__ = '0.1.0'
__author__ = 'https://github.com/fear2225'

# External
import tkinter as tk
from pathlib import Path

from PIL import Image, ImageTk

# Internal

# Consts


# ============================================================
class ContainerImage(tk.Frame):
    photo: ImageTk.PhotoImage
    label: tk.Label

    def __init__(self, master: tk.Misc, width: int=300, height: int=300):
        """
        image tk container class
        :param master: parent widget
        :param width: image resize width
        :param height: image resize height
        """
        super().__init__(master=master)
        self.width, self.height = width, height

    def update_image(self, path: Path) -> None:
        """
        update image in container
        :param path: path to image
        :return: None
        """
        # todo add animation support

        image = Image.open(path)
        # resize image
        image.thumbnail((self.height, self.width))
        self.photo = ImageTk.PhotoImage(image)

        if hasattr(self, 'label'):
            # update image
            self.label.configure(image=self.photo)
        else:
            # set image
            self.label = tk.Label(master=self, image=self.photo,
                                  height=self.height, width=self.width
                                  )
            self.label.pack()


# ============================================================
if __name__ == '__main__':
    app = tk.Tk()

    file1 = Path('ph3.gif')
    file2 = Path('/home/kali/Рабочий стол/amogus.gif')
    container = ContainerImage(app, 400, 500)
    container.pack()

    container.update_image(file1)

    def action(event: tk.Event):
        container.update_image(file2)

    container.label.bind('<Button-1>', action)

    app.mainloop()
    pass
