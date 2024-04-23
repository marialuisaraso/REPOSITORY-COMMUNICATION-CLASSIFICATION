import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    values = [float(line.strip()) for line in lines]
    return pd.DataFrame({'Values': values})

filename = 'Tools/Index/VSCODEcompounds.txt'

data = read_file(filename)

data['Values'] = np.log10(data['Values'])

sns.boxplot(data=data)
plt.title('COMPOUNDS (LOG NOTATION)')
plt.show()
