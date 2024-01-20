import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import pandas_datareader.data as web


# plt.plot([1, 2, 3, 4 , 5], [20, 30, 10 ,50 ,40])
# plt.show()


def rub_usd():
    yf.pdr_override()
    a = web.DataReader('USDRUB=X', datetime.datetime.today() - datetime.timedelta(days=10))
    plt.plot(a.index, a['Close'])
    plt.show()






def usd_btc():
    yf.pdr_override()
    a = web.DataReader('BTC-USD', datetime.datetime.today() - datetime.timedelta(days=365))
    plt.plot(a.index, a['Close'])
    plt.show()
