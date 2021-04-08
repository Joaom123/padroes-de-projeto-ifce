from abc import ABC

from button.Button import Button


class WinButton(Button):
    def paint(self) -> None:
        print("Rendering a windows style button.")
