import pandas as pd

url = (
    "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"
)
# Load data
dataframe = pd.read_csv(url)


def uppercase(x):
    return x.upper()


# Apply function, show two rows
dataframe["Name"].apply(uppercase)

dataframe.groupby("Sex").apply(lambda x: x.count())

import numpy as np

new_name = np.array(np.arange(1, 20))


def outliers(x):
    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1
    lower_bond = q1 - (iqr * 1.5)
    upper_bond = q3 + (iqr * 1.5)
    return x[np.where((x > upper_bond) | (x < lower_bond))]


outliers(new_name)

# Import libraries
import numpy as np
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer

# Create feature
feature = np.array([["Texas"], ["California"], ["Texas"], ["Delaware"], ["Texas"]])
# Create one-hot encoder
one_hot = LabelBinarizer()
# One-hot encode feature
one_hot.fit_transform(feature)

one_hot.classes_

empty = pd.get_dummies(feature[:, 0])

print(empty)

import numpy as np

ar = np.array([2, 4])

ar_sum = ar.sum()

k = np.random.rand(2)

print("the value of ranom value is ", k)

