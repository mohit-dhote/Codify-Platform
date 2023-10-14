import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        # Add a column of ones to the feature matrix for the bias term
        X = np.insert(X, 0, 1, axis=1)
        self.theta = np.zeros(X.shape[1])

        for _ in range(self.num_iterations):
            z = np.dot(X, self.theta)
            h = self.sigmoid(z)
            gradient = np.dot(X.T, (h - y)) / len(y)
            self.theta -= self.learning_rate * gradient

    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        probabilities = self.sigmoid(np.dot(X, self.theta))
        return [1 if p >= 0.5 else 0 for p in probabilities]

if __name__ == "__main__":
    # Sample data
    X = np.array([[2.5, 3.5], [1.5, 2.5], [3.5, 4.5], [2.5, 2.5]])
    y = np.array([0, 0, 1, 1])

    # Create and train the logistic regression model
    model = LogisticRegression(learning_rate=0.1, num_iterations=1000)
    model.fit(X, y)

    # Make predictions
    new_data = np.array([[2.0, 3.0], [4.0, 4.0]])
    predictions = model.predict(new_data)

    print("Predictions:", predictions)
