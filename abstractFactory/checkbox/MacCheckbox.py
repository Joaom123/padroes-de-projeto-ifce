from abc import ABC

from checkbox.Checkbox import Checkbox


class MacCheckbox(Checkbox, ABC):
    def paint(self) -> None:
        print("Rendering a mac style checkbox.")
