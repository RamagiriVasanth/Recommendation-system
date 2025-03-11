import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import heapq
from functools import lru_cache

# Load data
data = pd.read_csv('data/user_data.csv')

# Initialize hashmap to store user-product interactions
user_product_map = {}

# Fill the hashmap with data
for index, row in data.iterrows():
    user_id = row['user_id']
    product_id = row['product_id']
    price = row['price']
    
    if user_id not in user_product_map:
        user_product_map[user_id] = {}
    user_product_map[user_id][product_id] = price

# Convert user-product map into a matrix for K-D Tree
user_ids = list(user_product_map.keys())
product_ids = list({product for products in user_product_map.values() for product in products.keys()})
user_item_matrix = np.zeros((len(user_ids), len(product_ids)))

# Create user-item matrix
for i, user_id in enumerate(user_ids):
    for j, product_id in enumerate(product_ids):
        user_item_matrix[i][j] = user_product_map[user_id].get(product_id, 0)

# Perform K-D Tree based nearest neighbor search
neigh = NearestNeighbors(n_neighbors=5, algorithm='kd_tree')
neigh.fit(user_item_matrix)

# Function to recommend products based on similar users
@lru_cache(maxsize=128)  # Cache the results for the most queried users
def recommend_products(user_id, num_recommendations=3):
    user_index = user_ids.index(user_id)
    distances, indices = neigh.kneighbors([user_item_matrix[user_index]], n_neighbors=6)  # include the user itself
    
    similar_users = indices.flatten()[1:]  # exclude the user itself
    recommended_products = set()
    
    for similar_user in similar_users:
        similar_user_products = list(user_product_map[user_ids[similar_user]].keys())
        recommended_products.update(similar_user_products)
        
        if len(recommended_products) >= num_recommendations:
            break
    
    return list(recommended_products)[:num_recommendations]

# Function to recommend products using priority queue (heap)
def recommend_products_using_heap(user_id, num_recommendations=3):
    user_index = user_ids.index(user_id)
    distances, indices = neigh.kneighbors([user_item_matrix[user_index]], n_neighbors=6)
    
    similar_users = indices.flatten()[1:]
    recommended_products = []

    for similar_user in similar_users:
        similar_user_products = list(user_product_map[user_ids[similar_user]].keys())
        
        for product in similar_user_products:
            # Push products into a min-heap based on their frequency of being recommended
            heapq.heappush(recommended_products, product)
            
            if len(recommended_products) > num_recommendations:
                heapq.heappop(recommended_products)

    return recommended_products
