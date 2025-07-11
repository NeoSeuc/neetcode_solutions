import numpy as np
from numpy.typing import NDArray


# https://neetcode.io/problems/linear-regression-forward
class Solution:
    # I could do this with a single line using np.matmul, but I want to show the step-by-step process
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        answers = []
        for i in range(X.shape[0]):
            sum = 0
            for j in range(X.shape[1]):
                sum += X[i][j] * weights[j]
            answers.append(sum)

        return np.round(np.array(answers), 5)

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        answers = []

        for i in range(model_prediction.shape[0]):
            for j in range(model_prediction.shape[1]):
                answers.append(np.square(model_prediction[i][j] - ground_truth[i][j]))

        return round(np.mean(answers), 5)


solution = Solution()
X = np.array([[0.3745401188473625, 0.9507143064099162, 0.7319939418114051]])
weights = np.array([1.0, 2.0, 3.0])
assert np.array_equal(solution.get_model_prediction(X, weights), np.array([4.47195]))

model_prediction = np.array([[0.37454012], [0.95071431], [0.73199394]])
ground_truth = np.array([[0.59865848], [0.15601864], [0.15599452]])
assert solution.get_error(model_prediction, ground_truth=ground_truth) == 0.33785
