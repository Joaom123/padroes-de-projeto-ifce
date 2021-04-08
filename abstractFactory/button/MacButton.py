from abc import ABC

from button.Button import Button


class MacButton(Button, ABC):
    def paint(self) -> None:
        print("Rendering a mac style button.")
