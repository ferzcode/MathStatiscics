import scipy.stats as stats
import math

selection = [1.669, 1.439, -0.775, -1.662, 2.089, -0.997, 1.840, 1.177, -0.085, 1.778,
             -0.193, 2.243, 0.487, 0.725, 0.108, 1.537, 0.107, -0.868, -0.953, -0.122,
             2.884, 1.105, 0.731, 0.965, 2.244, 1.306, 0.643, 2.333, 0.241, 0.555,
             1.246, 1.928, 0.985, 1.728, 1.308, 1.804, 0.777, -0.105, 0.007, 1.138,
             2.081, -1.246, 2.274, 1.986, 2.024, 1.181, 0.714, 0.240, 0.194, 3.066
             ]
a = 1
epsilon = 0.15
N = 50

def calculateConfidenceIntervalLeftBoard(averageX, SelectiveDispersion, N, quantile):
    return averageX - (quantile * math.sqrt(SelectiveDispersion / (N - 1))) / math.sqrt(N)

def calculateConfidenceIntervalRightBoard(averageX, SelectiveDispersion, N, quantile):
    return averageX + (quantile * math.sqrt(SelectiveDispersion / (N - 1))) / math.sqrt(N)

averageX = sum(selection) / N
print("AverageX :", averageX)

diffX = [x - averageX for x in selection]

SelectiveDispersion = sum([diff ** 2 for diff in diffX]) / (N - 1)
print("SelectiveDispersion: ", SelectiveDispersion)

# Calculate the quantile using the condition T_{n-1}(t) = 1 - epsilon/2
quantile = stats.t.ppf(1 - epsilon/2, N - 1)
print("Quantile: ", quantile)

left_board = calculateConfidenceIntervalLeftBoard(averageX, SelectiveDispersion, N, quantile)
right_board = calculateConfidenceIntervalRightBoard(averageX, SelectiveDispersion, N, quantile)

print("Confidence interval for a: [{:.4f}, {:.4f}]".format(left_board, right_board))
