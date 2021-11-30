from tkinter import Tk
from ui import UI


def main():
    window = Tk()
    window.title('Much secrets..')
    window.resizable(False, False)

    user_interface = UI(window)
    user_interface.start()
    window.mainloop()


if __name__ == "__main__":
    main()
