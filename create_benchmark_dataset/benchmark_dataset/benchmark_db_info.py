import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


final_df = pd.read_csv('./fishnet-fl 2.csv')
final_df.head()

# Get a dictionary mapping the count of images in the habitat with the respected habitat_id
hist = final_df[['image', 'habitat_id']].groupby('habitat_id').agg('count').to_dict()['image']
# Sort the values for better visualization
sorted_by_values = dict(sorted(hist.items(), key=lambda item: item[1], reverse=True))


values = list(sorted_by_values.values())
print(f'Max:\t {np.max(values)}')
print(f'Min:\t {np.min(values)}')
print(f'Mean:\t{np.mean(values): 0.2f}')
print(f'Median:\t{np.median(values): 0.2f}')



# Visualize
plt.figure(figsize=(15, 5))
plt.bar(range(len(list(sorted_by_values.keys()))), sorted_by_values.values())
plt.xlabel('Habitat ID')
plt.ylabel('Image Count')
plt.xticks(range(len(list(sorted_by_values.keys()))), labels=list(sorted_by_values.keys()), rotation=90)
plt.title('Num Images for Each Habitat')

for i, v in enumerate(sorted_by_values.values()):
    plt.text(i, v + 0.5, str(v), ha='left', rotation=45)


# Get a dictionary mapping the number of families in the habitat with the respected habitat_id
hist = final_df[['Family', 'habitat_id']].groupby('habitat_id').nunique().to_dict()['Family']
# Sort the values for better visualization
sorted_by_values = dict(sorted(hist.items(), key=lambda item: item[1], reverse=True))


values = list(sorted_by_values.values())
print(f'Max:\t {np.max(values)}')
print(f'Min:\t {np.min(values)}')
print(f'Mean:\t{np.mean(values): 0.2f}')
print(f'Median:\t{np.median(values): 0.2f}')


# Visualize
plt.figure(figsize=(15, 5))
plt.bar(range(len(list(sorted_by_values.keys()))), sorted_by_values.values())
plt.xlabel('Habitat ID')
plt.ylabel('Family Count')
plt.xticks(range(len(list(sorted_by_values.keys()))), labels=list(sorted_by_values.keys()), rotation=90)
plt.title('Num Families for Each Habitat')

for i, v in enumerate(sorted_by_values.values()):
    plt.text(i, v + 0.5, str(v), ha='left', rotation=45)



# Get a dictionary mapping the number of orders in the habitat with the respected habitat_id
hist = final_df[['Order', 'habitat_id']].groupby('habitat_id').nunique().to_dict()['Order']
# Sort the values for better visualization
sorted_by_values = dict(sorted(hist.items(), key=lambda item: item[1], reverse=True))


values = list(sorted_by_values.values())
print(f'Max:\t {np.max(values)}')
print(f'Min:\t {np.min(values)}')
print(f'Mean:\t{np.mean(values): 0.2f}')
print(f'Median:\t{np.median(values): 0.2f}')


# Visualize
plt.figure(figsize=(15, 5))
plt.bar(range(len(list(sorted_by_values.keys()))), sorted_by_values.values())
plt.xlabel('Habitat ID')
plt.ylabel('Order Count')
plt.xticks(range(len(list(sorted_by_values.keys()))), labels=list(sorted_by_values.keys()), rotation=90)
plt.title('Num Orders for Each Habitat')

for i, v in enumerate(sorted_by_values.values()):
    plt.text(i, v + 0.5, str(v), ha='left', rotation=45)



    log_scale = np.log(list(sorted_by_values.values()))


plt.figure(figsize=(15, 5))
plt.bar(range(len(list(sorted_by_values.keys()))), log_scale)
plt.xlabel('Habitat ID')
plt.ylabel('Order Count')
plt.xticks(range(len(list(sorted_by_values.keys()))), labels=list(sorted_by_values.keys()), rotation=90)
plt.title('Num Orders for Each Habitat')

for i, (v, lv) in enumerate(zip(sorted_by_values.values(), log_scale)):
    plt.text(i, lv + 0.1, str(v), ha='left', rotation=45)



# Get a dictionary mapping the count of images in each family with the respected habitat_id
hist = final_df[['image', 'Family']].groupby('Family').agg('count').to_dict()['image']
# Sort the values for better visualization
sorted_by_values = dict(sorted(hist.items(), key=lambda item: item[1], reverse=True))


# Get a dictionary mapping the count of images in each order with the respected habitat_id
hist = final_df[['image', 'Order']].groupby('Order').agg('count').to_dict()['image']
# Sort the values for better visualization
sorted_by_values = dict(sorted(hist.items(), key=lambda item: item[1], reverse=True))


values = list(sorted_by_values.values())
print(f'Max:\t {np.max(values)}')
print(f'Min:\t {np.min(values)}')
print(f'Mean:\t{np.mean(values): 0.2f}')
print(f'Median:\t{np.median(values): 0.2f}')
print(f'Total Orders: {len(list(sorted_by_values.keys()))}')



# Visualize
plt.figure(figsize=(15, 10))
plt.bar(range(len(hist)), sorted_by_values.values())
plt.xlabel('Order')
plt.ylabel('Image Count')
plt.xticks(range(len(hist)), labels=list(sorted_by_values.keys()), rotation=90, font={'size': 7})
plt.title('Num Images for Each Order')

for i, v in enumerate(sorted_by_values.values()):
    plt.text(i, v + 5, str(v), ha='left', rotation=45, font={'size': 7})