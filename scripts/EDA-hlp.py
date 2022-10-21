<<<<<<< HEAD
import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer, MinMaxScaler
import pickle


class Helper:

    def __init__(self):
        pass

    def custome_normalizer(self, df):
        return (df - df.mean()) / (df.std())

    def normalizer(self, df, columns):
        norm = Normalizer()
        return pd.DataFrame(norm.fit_transform(df), columns=columns)

    def scaler(self, df, columns):
        minmax_scaler = MinMaxScaler()
        return pd.DataFrame(minmax_scaler.fit_transform(df), columns=columns)

    def scale_and_normalize(self, df, columns):
        return self.normalizer(self.scaler(df, columns), columns)
=======
from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import numpy as np


GOOG["Signal"] = np.random.randint(-1,2,len(GOOG))

print(GOOG)

class SignalStrategy(Strategy):
    '''
    use a Signal value of 1 to mean buy, -1 is sell, 
    and 0 is do nothing.
    '''
    def init(self):
        pass

    def next(self):
        current_signal= self.data.Signal[-1]
        if current_signal == 1:
            if not self.position:
                self.buy()
        elif current_signal == -1:
            if self.position:
                self.position.close()

bt = Backtest(GOOG, SignalStrategy, cash=10_000)

stats = bt.run()
print(stats)
bt.plot()
>>>>>>> 58d4d2f1a2ecfa6da3c52a080ed733334bdaff97
