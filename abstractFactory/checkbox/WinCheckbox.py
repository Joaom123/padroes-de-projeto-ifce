from abc import ABC

from checkbox.Checkbox import Checkbox


class WinCheckbox(Checkbox):
    def paint(self) -> None:
        print("Rendering a windows style checkbox.")
