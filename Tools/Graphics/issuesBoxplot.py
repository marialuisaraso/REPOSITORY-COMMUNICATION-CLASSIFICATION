import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    values = [float(line.strip()) for line in lines]
    return pd.DataFrame({'Values': values})

file_name = 'Tools/Graphics/issuesComments.txt'

data = read_file(file_name)

data['Values'] = np.log10(data['Values'])

sns.boxplot(data=data)
plt.title('COMMENTS PER ISSUE (LOG NOTATION)')
plt.show()
