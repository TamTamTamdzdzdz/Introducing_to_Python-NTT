import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from ipython.
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split


class DataPreprocessing():

    def __init__(self):
        # Auto initialize necessary attributes of the object
        self.dataframe = None
        self.X = None
        self.y = None

    def read_from_csv(self):
        # Read data from .csv file into the dataframe and display the first 5 rows
        df = pd.read_csv('real_estate.csv', index_col='No')
        self.dataframe = df
        display(self.dataframe.head())

    def set_attributes_and_output(self):
        # Set X and y to data attributes and output from the dataframe
        pass

    def visualize_data(self):
        # Visualize relation between each attribute and output
        columns_plot = np.array(self.dataframe.columns)[:-1].reshape(3, -1)
        fig, ax = plt.subplots(3, 2, figsize=(10, 8), sharey=True)
        fig.suptitle('Correlation between each attribute and the house price of unit area')

        for i in range(3):
            for j in range(2):
                ax[i, j].scatter(self.X[:, i * 2 + j], self.y, s=10, color="bgrcmy"[i * 2 + j])
                ax[i, j].set_xlabel(columns_plot[i, j].split(' ', 1)[1].title())

        fig.tight_layout()
        fig.add_subplot(111, frameon=False)
        plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)
        plt.ylabel(self.dataframe.columns[-1].split(' ', 1)[1].title())
        plt.show()

    def final_train_test_data(self, attributes_list=[0, 1, 2, 3, 4, 5], test_size=0.2):
        # Split the data X and output y into training data and testing data
        # Output: a tuple (X_train, X_test, y_train, y_test), using train_test_split with random_state=42
        pass


temp=DataPreprocessing()
temp.read_from_csv()