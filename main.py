import numpy as np
import csv
from sklearn.neighbors import KNeighborsClassifier

class KNNModel:
    def __init__(self, csv_file_path):
        # Load the CSV file.
        with open(csv_file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            dataset = np.array(list(reader))

        # Split the dataset into features and labels.
        features = dataset[:, :-1]
        labels = dataset[:, -1]

        # Train the KNN model.
        self.knn = KNeighborsClassifier(n_neighbors=3)
        self.knn.fit(features, labels)

    def predict_nearby(self, user_location):
        """Predicts whether the user is near the carpooler.

        Args:
            user_location: A tuple containing the user's latitude and longitude.

        Returns:
            A boolean value indicating whether the user is near the carpooler.
        """

        # Find the K nearest neighbors of the user location in the dataset.
        neighbors = self.knn.kneighbors([user_location], return_distance=False)[0]

        # Calculate the probability that the user is near the carpooler based on the
        # K nearest neighbors.
        probability = np.mean([labels[neighbor] for neighbor in neighbors])

        # Return the probability.
        return probability

def check_nearby_continuously(knn_model, user_location, carpooler_location):
    """Continuously checks if the user is near the carpooler.

    Args:
        knn_model: A KNNModel object.
        user_location: A tuple containing the user's latitude and longitude.
        carpooler_location: A tuple containing the carpooler's latitude and longitude.
    """

    # Get the user's current location.
    user_latitude, user_longitude = user_location

    # Get the carpooler's current location.
    carpooler_latitude, carpooler_longitude = carpooler_location

    # Predict whether the user is near the carpooler.
    probability = knn_model.predict_nearby((user_latitude, user_longitude))

    # If the user is near the carpooler, take appropriate action (e.g., send a notification to the user).
    if probability > 0.5:
        # The user is near the carpooler.
        print("The user is near the carpooler!")

    # Set a timer to call the check_nearby_continuously function again in the future.
    timer = Timer(10, check_nearby_continuously, args=[knn_model, user_location, carpooler_location])
    timer.start()


# Load the CSV file.
csv_file_path = "data.csv"

# Train the KNN model.
knn_model = KNNModel(csv_file_path)

# Start continuously checking if the user is near the carpooler.
user_location = (37.7833, -122.4167)
carpooler_location = (37.7869, -122.4222)
check_nearby_continuously(knn_model, user_location, carpooler_location)
