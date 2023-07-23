import pandas as pd
from scipy.stats import f_oneway

# Örnek veri
data = {'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D' , 'D', 'D'],
        'Value': [10, 9, 5, 11, 16, 9, 13, 8, 9, 18 , 23 , 25]}
df = pd.DataFrame(data)

# Gruplara göre değerleri ayrı ayrı almak
group1 = df[df['Group'] == 'A']['Value']
group2 = df[df['Group'] == 'B']['Value']
group3 = df[df['Group'] == 'C']['Value']
group4 = df[df['Group'] == 'D']['Value']
# ANOVA testi
f_value, p_value = f_oneway(group1, group2, group3 , group4)

# ANOVA özet tablosunu yazdırma
anova_table = pd.DataFrame({'F value': [f_value],
                            'p value': [p_value]})
print(anova_table)



