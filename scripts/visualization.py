<<<<<<< HEAD
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class VisualiseDf:
    def __init__(self, df):
        self.df = df.copy()

    # plots a distribution (frequency of a variable)
    # better results on continuous variables (not so much on continuous
    # variables)
    # parameters: dataframe, column title, color (of hist)
    # returns: histogram plot (in the color green by default)
    def plot_hist(self, df: pd.DataFrame, column: str,
                  color: str = 'cornflowerblue') -> None:
        sns.displot(data=df, x=column, color=color,
                    kde=True, height=5, aspect=2)
        plt.xticks(rotation=90, fontsize=14)
        plt.yticks(fontsize=14)

    def plot_hist(df: pd.DataFrame, column: str, color: str) -> None:
        sns.displot(data=df, x=column, color=color,
                    kde=True, height=5, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.xticks(rotation=75, fontsize=14)
        plt.show()

    # plots a bar graph
    # parameters: dataframe, dependent col, independent col, xlabel, ylabel
    # returns: plot of bar graph
    def plot_bar(df, x_col: str, y_col: str, title: str, xlabel: str,
                 ylabel: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.barplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel(xlabel, fontsize=16)
        plt.ylabel(ylabel, fontsize=16)
        plt.show()

    def plot_heatmap(df: pd.DataFrame, title: str, cbar=False) -> None:
        plt.figure(figsize=(12, 7))
        sns.heatmap(df, annot=True, cmap='viridis', vmin=0,
                    vmax=1, fmt='.2f', linewidths=.7, cbar=cbar)
        plt.title(title, size=18, fontweight='bold')
        plt.show()

    # plots a box plot
    # parameters: dataframe, dependent col, title of box plot
    # returns: a box plot
    def plot_box(df: pd.DataFrame, x_col: str, title: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.show()

    def plot_box_multi(df: pd.DataFrame, x_col: str, y_col: str,
                       title: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

    def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, title: str,
                     hue: str, style: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

    # plots a distribution (frequency of a variable)
    # better results on discrete variables e.g categorical variables
    # parameters: dataframe, column title
    # returns: histogram count plot
    def plot_count(df: pd.DataFrame, column: str) -> None:
        plt.figure(figsize=(12, 7))
        sns.countplot(data=df, x=column)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()

    # Draw a nested violinplot and split the violins for easier comparison
    def plot_violin(df, x_col: str, y_col: str, hue: str, inner: str):

        sns.violinplot(data=df, x=x_col, y=y_col, hue=x_col,
                       split=True, inner=y_col, linewidth=1,
                       palette={"Yes": "b", "No": ".85"})
        sns.despine(left=True)

    # to make it esly discriptive we can represent it as folows
    # function
    def plot_discriptive_count(df: pd.DataFrame, column: pd.DataFrame) -> None:
        base_color = sns.color_palette()[0]
        type_counts = column.value_counts()
        type_order = type_counts.index
        ax = sns.countplot(
            data=df, x=column.loc[0:], color=base_color, order=type_order)
        n_user = column.value_counts().sum()

        # get the current tick locations and labels
        locs, labels = plt.xticks(rotation=0)

        # loop through each pair of locations and labels
        for loc, label in zip(locs, labels):

            # get the text property for the label to get the correct count
            count = type_counts[label.get_text()]
            pct_string = '{:0.1f}%'.format(100*count/n_user)
            plt.text(loc, count-8, pct_string, va='top',
                     ha='center', color='w', fontsize=12)
        # plt.title(f'Distribution', size=20, fontweight='bold')
    # Remove unnecessary features
        ax.spines['top'].set_visible(True)
        ax.spines['right'].set_visible(True)
        ax.spines['left'].set_visible(True)
        plt.yticks([])
        # plt.ylabel("t")
        # plt.xlabel('')
        # plt.legend()

        # Show the plot
        plt.show()
    # code for

    def bar_plot(df, column, orders, heu1, title):
        plt.figure(figsize=(10, 6))
        plt.title(title, size=20, fontweight='bold')
        chart = sns.countplot(data=df, x=column, order=orders, hue=heu1)

        chart.set(xlabel=column, ylabel='')

        # Remove legend title
        sns.despine(fig=None, ax=None, top=True, right=True,
                    left=True, bottom=False, offset=None, trim=False)
        plt.gca().legend().set_title(column)
    # pie plot

    def pie_plot(column: pd.DataFrame, title):
        plt.figure(figsize=(10, 6))
        sorted_counts = column.value_counts()
        plt.pie(sorted_counts, labels=sorted_counts.index, startangle=90,
                counterclock=False, autopct='%1.2f%%')
        plt.axis('square')
        # plt.legend('user_type')
        plt.title(title, fontsize=15, fontweight='bold')
        plt.show()

    def plot_layout(df, column, title):
        ax = sns.countplot(x=column, hue=column, dodge=False, data=df)
        ax.set_title(title, fontsize=18, fontweight='bold', color='black')
        ax.set_xlabel('member_gender', fontsize=15, color='black')
        ax.set_ylabel('count', fontsize=15, color='black')
        ax.figure.set_facecolor('0.7')
        plt.tight_layout()
        plt.show()
=======
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

# Import the backtrader platform
import backtrader as bt


# Create a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close

        # To keep track of pending orders and buy price/commission
        self.order = None
        self.buyprice = None
        self.buycomm = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        # Check if we are in the market
        if not self.position:

            # Not yet ... we MIGHT BUY if ...
            if self.dataclose[0] < self.dataclose[-1]:
                    # current close less than previous close

                    if self.dataclose[-1] < self.dataclose[-2]:
                        # previous close less than the previous close

                        # BUY, BUY, BUY!!! (with default parameters)
                        self.log('BUY CREATE, %.2f' % self.dataclose[0])

                        # Keep track of the created order to avoid a 2nd order
                        self.order = self.buy()

        else:

            # Already in the market ... we might sell
            if len(self) >= (self.bar_executed + 5):
                # SELL, SELL, SELL!!! (with all possible default parameters)
                self.log('SELL CREATE, %.2f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()


if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Add a strategy
    cerebro.addstrategy(TestStrategy)

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, '../data/MSFT.csv')

    # Create a Data Feed
    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        # Do not pass values before this date
        fromdate=datetime.datetime(2021, 1, 1),
        # Do not pass values before this date
        todate=datetime.datetime(2022, 8, 31),
        # Do not pass values after this date
        reverse=False)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Set the commission - 0.1% ... divide by 100 to remove the %
    cerebro.broker.setcommission(commission=0.001)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()
    # cerebro.plot()

    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
>>>>>>> 58d4d2f1a2ecfa6da3c52a080ed733334bdaff97
