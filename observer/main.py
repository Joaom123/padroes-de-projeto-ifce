from observer.StockGrabber import StockGrabber
from observer.StockSubscriber import StockSubscriber

if __name__ == "__main__":
    stock_grabber = StockGrabber()

    stock_subscriber_one = StockSubscriber("Stock Subscriber One")
    stock_grabber.subscribe(stock_subscriber_one)

    stock_subscriber_two = StockSubscriber("Stock Subscriber Two")
    stock_grabber.subscribe(stock_subscriber_two)

    stock_grabber.set_google_price(1000)
    stock_grabber.set_ibm_price(2.0)

    stock_grabber.unsubscribe(stock_subscriber_two)

    stock_grabber.set_google_price(2500)
