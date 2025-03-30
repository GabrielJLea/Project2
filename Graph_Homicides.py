import matplotlib.pyplot as plt
import numpy as np


countries = ['Honduras', 'El Salvador', 'Guatemala', 'Jamaica', 'Colombia']
homicide_rate_2005 = [85.5, 72.1, 54.4, 60.3, 45.6]  
homicide_rate_2010 = [82.2, 68.5, 51.9, 58.4, 39.7]  


bar_width = 0.35


index = np.arange(len(countries))

fig, ax = plt.subplots(figsize=(10, 6))


bar1 = ax.bar(index - bar_width / 2, homicide_rate_2005, bar_width, label='2005', color='blue')
bar2 = ax.bar(index + bar_width / 2, homicide_rate_2010, bar_width, label='2010', color='red')


ax.set_xlabel('Country')
ax.set_ylabel('Homicide Rate (per 100,000 people)')
ax.set_title('Homicide rates in 2005 and 2010 of 5 countries')
ax.set_xticks(index)
ax.set_xticklabels(countries)


ax.legend()


plt.tight_layout()
plt.show()