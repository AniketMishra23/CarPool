import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
from scipy.spatial.distance import cosine

# Sample user dataset
data = {
    'User ID': [1, 2, 3, 4, 5],
    'Start Latitude': [40.7128, 34.0522, 40.7489, 37.7749, 41.8781],
    'Start Longitude': [-74.0060, -118.2437, -73.9873, -122.4194, -87.6298],
    'Dest Latitude': [40.7489, 34.0522, 40.7128, 34.0522, 42.3601],
    'Dest Longitude': [-73.9873, -118.2437, -74.0060, -118.2437, -71.0589],
    'Preferred Time': ['Morning', 'Evening', 'Morning', 'Morning', 'Evening'],
}

df = pd.DataFrame(data)

# Encode categorical preferences
encoder = LabelEncoder()
df['Preferred Time'] = encoder.fit_transform(df['Preferred Time'])

# User-based collaborative filtering
def user_similarity(user1, user2):
    # Calculate cosine similarity between user preferences
    user1_pref = df[df['User ID'] == user1]['Preferred Time'].values
    user2_pref = df[df['User ID'] == user2]['Preferred Time'].values
    return 1 - cosine(user1_pref, user2_pref)

def get_similar_users(user_id, num_users=3):
    similarities = []
    for other_user_id in df['User ID']:
        if other_user_id != user_id:
            similarity = user_similarity(user_id, other_user_id)
            similarities.append((other_user_id, similarity))
    
    # Sort users by similarity
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Get the most similar users
    similar_users = [user for user, _ in similarities[:num_users]]
    return similar_users

user_id = 1  # User for whom we want to find carpool matches
similar_users = get_similar_users(user_id, num_users=3)

# Clustering users using K-Means
X = df[['Start Latitude', 'Start Longitude', 'Dest Latitude', 'Dest Longitude', 'Preferred Time']]
kmeans = KMeans(n_clusters=2)  # You can adjust the number of clusters as needed
df['Cluster'] = kmeans.fit_predict(X)

# Find users in the same cluster
cluster_id = df[df['User ID'] == user_id]['Cluster'].values[0]
users_in_same_cluster = df[df['Cluster'] == cluster_id]['User ID'].tolist()

print(f"User {user_id}'s similar users based on preferences: {similar_users}")
print(f"User {user_id}'s users in the same cluster: {users_in_same_cluster}")
