import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
from tabulate import tabulate

J45_asthma_age=pd.read_csv('J45_asthma_age.csv')

print(tabulate(J45_asthma_age, headers='keys', tablefmt='pretty'))


