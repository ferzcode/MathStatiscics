import scipy.stats as stats

selection = [1.669, 1.439, -0.775, -1.662, 2.089, -0.997, 1.840, 1.177, -0.085, 1.778,
             -0.193, 2.243, 0.487, 0.725, 0.108, 1.537, 0.107, -0.868, -0.953, -0.122,
             2.884, 1.105, 0.731, 0.965, 2.244, 1.306, 0.643, 2.333, 0.241, 0.555,
             1.246, 1.928, 0.985, 1.728, 1.308, 1.804, 0.777, -0.105, 0.007, 1.138,
             2.081, -1.246, 2.274, 1.986, 2.024, 1.181, 0.714, 0.240, 0.194, 3.066
             ]
a = 1
delta = 0.9
epsilon = 0.15
N = 50


def calculateСonfidenceIntervalLeftBoard(averageX, delta, N, quantile):
    return (averageX - ((delta ** 0.5) / (N ** 0.5)) * quantile)


def calculateСonfidenceIntervalRightBoard(averageX, delta, N, quantile):
    return (averageX + ((delta ** 0.5) / (N ** 0.5)) * quantile)


averageX = sum(selection) / N
print("AverageX :", averageX)

diffX = []
for i in range(N):
    diffX.append(selection[i] - averageX)

SelectiveDispersion = 0
for i in range(N):
    SelectiveDispersion += (diffX[i] ** 2)

SelectiveDispersion = SelectiveDispersion / N
CorrectedDispersion = (N * SelectiveDispersion) / (N - 1)

print("CorrectedDispersion: ", CorrectedDispersion)
print("SelectiveDispersion: ", SelectiveDispersion)

lastParam = 0
for i in range(N):
    lastParam += (selection[i] - a) ** 2

lastParam = lastParam / 50
print("LastParam: ", lastParam)

quantile = stats.norm.ppf(1 - (epsilon / 2))
print("Quantile: ", quantile)

print("LeftSideDI: ", calculateСonfidenceIntervalLeftBoard(averageX, delta, N, quantile))
print("RightSideDI: ", calculateСonfidenceIntervalRightBoard(averageX, delta, N, quantile))