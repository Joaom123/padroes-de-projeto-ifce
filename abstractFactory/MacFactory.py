from abc import ABC

from GUIFactory import GUIFactory
from button.MacButton import MacButton
from checkbox.MacCheckbox import MacCheckbox


class MacFactory(GUIFactory, ABC):
    def create_button(self) -> MacButton:
        return MacButton()

    def create_checkbox(self) -> MacCheckbox:
        return MacCheckbox()
