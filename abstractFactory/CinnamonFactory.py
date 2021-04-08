from abc import ABC

from GUIFactory import GUIFactory
from button.CinnamonButton import CinnamonButton
from checkbox.CinnamonCheckbox import CinnamonCheckbox


class CinnamonFactory(GUIFactory, ABC):
    def create_button(self) -> CinnamonButton:
        return CinnamonButton()

    def create_checkbox(self) -> CinnamonCheckbox:
        return CinnamonCheckbox()
