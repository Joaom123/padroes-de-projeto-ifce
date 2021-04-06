from abc import abstractmethod, ABC

from observer import Subscriber


# Also called Subject
class Publisher(ABC):

    @abstractmethod
    def subscribe(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def notify_subscribers(self) -> None:
        pass
