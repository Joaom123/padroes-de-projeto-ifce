from abc import abstractmethod, ABC


# Also called Observer
class Subscriber(ABC):

    @abstractmethod
    def update(self, ibm_price: float, google_price: float) -> None:
        pass
