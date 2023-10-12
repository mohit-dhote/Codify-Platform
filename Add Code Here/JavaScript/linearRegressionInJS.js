function linearRegression(x, y) {
    const n = x.length;

    let sumX = 0;
    let sumY = 0;
    let sumXY = 0;
    let sumX2 = 0;

    for (let i = 0; i < n; i++) {
        sumX += x[i];
        sumY += y[i];
        sumXY += x[i] * y[i];
        sumX2 += x[i] ** 2;
    }

    const m = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX ** 2);
    const b = (sumY - m * sumX) / n;

    return { slope: m, intercept: b };
}

function predict(x, slope, intercept) {
    return slope * x + intercept;
}

// Example usage
const x = [1, 2, 3, 4, 5];
const y = [2, 3, 3, 4, 5];

const result = linearRegression(x, y);
console.log(`Slope: ${result.slope}, Intercept: ${result.intercept}`);

// Make a prediction
const xPrediction = 6;
const yPrediction = predict(xPrediction, result.slope, result.intercept);
console.log(`Prediction for x=${xPrediction}: ${yPrediction}`);

// Plotting the data
const canvas = document.getElementById('scatterPlot');
const ctx = canvas.getContext('2d');

canvas.width = 400;
canvas.height = 400;

const scaleX = canvas.width / (Math.max(...x) - Math.min(...x));
const scaleY = canvas.height / (Math.max(...y) - Math.min(...y));

for (let i = 0; i < x.length; i++) {
    ctx.fillStyle = 'blue';
    ctx.fillRect((x[i] - Math.min(...x)) * scaleX, canvas.height - y[i] * scaleY, 5, 5);
}

ctx.beginPath();
ctx.moveTo(0, canvas.height - predict(0, result.slope, result.intercept) * scaleY);
ctx.lineTo(canvas.width, canvas.height - predict(canvas.width / scaleX, result.slope, result.intercept) * scaleY);
ctx.strokeStyle = 'red';
ctx.stroke();
