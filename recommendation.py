# recommendation.py
import pandas as pd

# Load data
data = pd.read_csv('data/user_data.csv')

# Display the data to check the structure
print(data.head())

# Create a user-item matrix
user_item_matrix = data.pivot_table(index='user_id', columns='product_id', values='price', aggfunc='mean', fill_value=0)

# Display user-item matrix
print(user_item_matrix)
# recommendation.py (continued)
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Calculate similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# Convert similarity to DataFrame for better readability
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

print(user_similarity_df)
# recommendation.py (continued)
def recommend_products(user_id, num_recommendations=3):
    # Find similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    
    # Get products interacted by similar users
    recommended_products = set()
    for similar_user in similar_users.index[1:]:
        similar_user_products = data[data['user_id'] == similar_user]['product_id']
        recommended_products.update(similar_user_products)
        
        if len(recommended_products) >= num_recommendations:
            break
    
    return list(recommended_products)[:num_recommendations]

# Example: Recommend products for user 1
user_id = 1
recommended_products = recommend_products(user_id)
print(f"Recommended products for user {user_id}: {recommended_products}")
