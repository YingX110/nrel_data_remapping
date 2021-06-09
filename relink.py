import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

traci = pd.read_csv('TRACI_2.csv')
emission = pd.read_csv('NG_flow.csv')
df = traci.merge(emission, how='inner', on=['Flow', 'Category', 'Sub-category'])

df['Unit'] = 'kg'
df['Flow impact (kg CO2eq)'] = df['factor (kg CO2 eq)'] * df['Result']
df.to_csv(r'C:\Users\bourg\Desktop\test.csv', index=True)

df_new = df[['Flow', 'Flow impact (kg CO2eq)']].copy()
df1 = df_new.set_index(['Flow'])
df2 = df1.T
ax1 = df2.plot.bar(stacked=True, rot=0, colormap='tab20')

ax2 = df1.plot.bar(rot=0)
plt.bar(range(len(df1)), df1['Flow impact (kg CO2eq)'], color=plt.cm.Paired(np.arange(len(df1))))

process = pd.read_csv('process_flow.csv')
pcs = traci.merge(process, how='inner', on=['Flow', 'Category', 'Sub-category'])
pcs['Flow impact (kg CO2eq)'] = pcs.iloc[:, 5:].sum(axis=1) * df['factor (kg CO2 eq)']

pcs_new = pcs[['Flow', 'Flow impact (kg CO2eq)']].copy()
