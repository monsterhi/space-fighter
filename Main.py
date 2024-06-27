from tkinter import Tk
from MainFrame import MainFrame

def main():
    """
    The main function that initializes the application.

    This function creates a Tkinter root window, instantiates the MainFrame class,
    sets the window size and position, and starts the main event loop.

    Args:
        None

    Returns:
        None
    """
    root = Tk()
    ex = MainFrame()
    root.geometry("800x600+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
