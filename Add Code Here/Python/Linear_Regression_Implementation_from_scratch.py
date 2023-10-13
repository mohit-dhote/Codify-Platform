import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        num_samples, num_features = X.shape
        self.weights = np.zeros(num_features)
        self.bias = 0

        for _ in range(self.num_iterations):
            # Linear equation: y = wx + b
            linear_model = np.dot(X, self.weights) + self.bias
            # Calculate gradients
            dw = (1 / num_samples) * np.dot(X.T, (linear_model - y))
            db = (1 / num_samples) * np.sum(linear_model - y)
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

# Example usage:
if __name__ == "__main__":
    # Generate some random data for demonstration
    np.random.seed(0)
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)

    model = LinearRegression(learning_rate=0.01, num_iterations=1000)
    model.fit(X, y)

    # Make predictions
    sample_X = np.array([[2.0]])
    predicted_y = model.predict(sample_X)
    print(f"Prediction for input {sample_X[0, 0]}: {predicted_y[0]}")
