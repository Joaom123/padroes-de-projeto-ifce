from abc import ABC

from observer.Publisher import Publisher
from observer.Subscriber import Subscriber


class StockGrabber(Publisher, ABC):
    def __init__(self):
        self.subscribers = []
        self.ibm_price = 0.0
        self.google_price = 0.0

    def set_ibm_price(self, ibm_price: float):
        self.ibm_price = ibm_price
        self.notify_subscribers()

    def set_google_price(self, google_price: float):
        self.google_price = google_price
        self.notify_subscribers()

    def subscribe(self, subscriber: Subscriber) -> None:
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        self.subscribers.remove(subscriber)

    def notify_subscribers(self) -> None:
        for subscriber in self.subscribers:
            subscriber.update(self.ibm_price, self.google_price)
