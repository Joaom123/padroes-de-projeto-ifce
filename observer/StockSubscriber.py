from abc import ABC

from observer.Subscriber import Subscriber


class StockSubscriber(Subscriber, ABC):
    def __init__(self, name: str):
        self.name = name
        self.ibm_price = 0.0
        self.google_price = 0.0

    def update(self, ibm_price: float, google_price: float) -> None:
        print(self.name)
        print('Actual state of stock')
        self.print_stock()

        print('Updating stock')
        self.ibm_price = ibm_price
        self.google_price = google_price
        self.print_stock()
        print("---------------------------")

    def print_stock(self):
        print('IBM price: {}'.format(self.ibm_price))
        print('GOOGLE price: {}'.format(self.google_price))
