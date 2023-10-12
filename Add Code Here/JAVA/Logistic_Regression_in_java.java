import java.util.Arrays;

public class LogisticRegression {
    private double[] weights;

    public LogisticRegression(int numFeatures) {
        weights = new double[numFeatures];
    }

    public void train(double[][] X, int[] y, double learningRate, int numIterations) {
        int numSamples = X.length;
        int numFeatures = X[0].length;

        for (int iteration = 0; iteration < numIterations; iteration++) {
            for (int i = 0; i < numSamples; i++) {
                double predicted = predict(X[i]);
                double error = y[i] - predicted;

                for (int j = 0; j < numFeatures; j++) {
                    weights[j] += learningRate * error * X[i][j];
                }
            }
        }
    }

    public double predict(double[] x) {
        double z = dotProduct(weights, x);
        return sigmoid(z);
    }

    private double sigmoid(double z) {
        return 1.0 / (1.0 + Math.exp(-z));
    }

    private double dotProduct(double[] a, double[] b) {
        double result = 0.0;
        for (int i = 0; i < a.length; i++) {
            result += a[i] * b[i];
        }
        return result;
    }

    public static void main(String[] args) {
        double[][] X = {
            {1.0, 2.0, 3.0},
            {2.0, 3.0, 4.0},
            {3.0, 4.0, 5.0}
        };

        int[] y = {0, 1, 1}; // Binary classification labels

        int numFeatures = X[0].length;
        LogisticRegression model = new LogisticRegression(numFeatures);

        double learningRate = 0.1;
        int numIterations = 1000;
        model.train(X, y, learningRate, numIterations);

        // Make predictions
        double[] sampleX = {1.0, 2.5, 4.0};
        double predictedY = model.predict(sampleX);

        System.out.println("Prediction for input: " + predictedY);
    }
}
