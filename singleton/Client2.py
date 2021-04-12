from Singleton import Singleton


class Client2:
    def __init__(self):
        self.singleton = Singleton()

    def get_singleton(self):
        return self.singleton
