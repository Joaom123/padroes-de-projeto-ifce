import platform
from WinFactory import WinFactory
from CinnamonFactory import CinnamonFactory
from MacFactory import MacFactory


def os_system_configuration():
    os_system = platform.system()

    if os_system == 'Linux':
        return CinnamonFactory()
    if os_system == 'Windows':
        return WinFactory()
    if os_system == "Darwin":
        return MacFactory()


gui_factory = os_system_configuration()

checkbox_a = gui_factory.create_checkbox()
checkbox_b = gui_factory.create_checkbox()
button = gui_factory.create_button()

checkbox_a.paint()
checkbox_b.paint()
button.paint()
