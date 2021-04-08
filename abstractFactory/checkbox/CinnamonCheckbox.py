from abc import ABC

from checkbox.Checkbox import Checkbox


class CinnamonCheckbox(Checkbox, ABC):
    def paint(self) -> None:
        print("Rendering a cinnamon style checkbox.")
