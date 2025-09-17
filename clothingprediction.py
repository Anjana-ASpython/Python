
'''
✅ 12. Outfit Combination Suggestions

Goal: Predict which pieces of clothing go well together.

Features:

Past outfit combinations

Style preferences

Color matching rules

Seasonal trends

Use Case:
Apps and stylists use prediction to suggest outfits for events or daily wear.
'''

# Import necessary libraries
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Sample dataset – past outfit combinations
outfit_data = [
    ['jeans', 'white shirt', 'sneakers'],
    ['floral dress', 'sandals', 'sunhat'],
    ['navy dress', 'heels', 'clutch'],
    ['jeans', 'white shirt', 'jacket'],
    ['floral dress', 'jacket', 'boots'],
    ['jeans', 'black t-shirt', 'sneakers'],
    ['navy dress', 'sandals', 'sunhat'],
    ['floral dress', 'sandals', 'clutch'],
    ['jeans', 'white shirt', 'boots']
]

# Step 1 – Transform the data into one-hot encoded format
te = TransactionEncoder()
te_data = te.fit(outfit_data).transform(outfit_data)
df = pd.DataFrame(te_data, columns=te.columns_)

print("One-hot Encoded Dataset:")
print(df)

# Step 2 – Find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Step 3 – Generate association rules from frequent itemsets
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)
print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Step 4 – Filter rules for 'jeans'
print("\nRules involving 'jeans':")
jeans_rules = rules[rules['antecedents'].apply(lambda x: 'jeans' in x)]
print(jeans_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Step 5 – Plot the frequent items as a bar chart
item_support = frequent_itemsets.set_index('itemsets')['support']
item_support = item_support.apply(lambda x: x)

plt.figure(figsize=(10,6))
item_support.sort_values(ascending=True).plot(kind='barh', color='skyblue')
plt.title('Frequent Outfit Items')
plt.xlabel('Support')
plt.ylabel('Itemsets')
plt.tight_layout()
plt.show()

# Step 6 – Visualize the association rules as a network graph
G = nx.DiGraph()

# Add edges with lift as weight
for _, row in rules.iterrows():
    antecedent = next(iter(row['antecedents']))
    consequent = next(iter(row['consequents']))
    G.add_edge(antecedent, consequent, weight=row['lift'])

plt.figure(figsize=(12,8))
pos = nx.spring_layout(G, k=1)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightgreen')

# Draw edges
edges = G.edges(data=True)
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='->', arrowsize=20, edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Draw edge labels (lift value)
edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("Association Rules Network Graph")
plt.axis('off')
plt.tight_layout()
plt.show()
