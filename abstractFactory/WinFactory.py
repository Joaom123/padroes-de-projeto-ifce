from abc import ABC

from GUIFactory import GUIFactory
from button.WinButton import WinButton
from checkbox.WinCheckbox import WinCheckbox


class WinFactory(GUIFactory, ABC):
    def create_button(self) -> WinButton:
        return WinButton()

    def create_checkbox(self) -> WinCheckbox:
        return WinCheckbox()
