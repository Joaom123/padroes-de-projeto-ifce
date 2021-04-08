from abc import ABC

from button.Button import Button


class CinnamonButton(Button, ABC):
    def paint(self) -> None:
        print("Rendering a cinnamon style button.")
