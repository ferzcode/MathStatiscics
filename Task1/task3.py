import scipy.stats as stats

selection = [1.669, 1.439, -0.775, -1.662, 2.089, -0.997, 1.840, 1.177, -0.085, 1.778,
             -0.193, 2.243, 0.487, 0.725, 0.108, 1.537, 0.107, -0.868, -0.953, -0.122,
             2.884, 1.105, 0.731, 0.965, 2.244, 1.306, 0.643, 2.333, 0.241, 0.555,
             1.246, 1.928, 0.985, 1.728, 1.308, 1.804, 0.777, -0.105, 0.007, 1.138,
             2.081, -1.246, 2.274, 1.986, 2.024, 1.181, 0.714, 0.240, 0.194, 3.066
             ]
a = 1
epsilon = 0.15
N = 50

def calculateСonfidenceIntervalLeftBoard(selection, a, h_left):
    summa = sum((x - a) ** 2 for x in selection)
    return summa / h_left

def calculateСonfidenceIntervalRightBoard(selection, a, h_right):
    summa = sum((x - a) ** 2 for x in selection)
    return summa / h_right

averageX = sum(selection) / N
print("AverageX :", averageX)

SelectiveDispersion = sum((x - averageX) ** 2 for x in selection) / N
CorrectedDispersion = (N * SelectiveDispersion) / (N - 1)

print("CorrectedDispersion: ", CorrectedDispersion)
print("SelectiveDispersion: ", SelectiveDispersion)

hLeft = stats.chi2.ppf(1 - epsilon / 2, N)
hRight = stats.chi2.ppf(epsilon / 2, N)

print("Left : ", hLeft)
print("Right: ", hRight)

leftInterval = calculateСonfidenceIntervalLeftBoard(selection, a, hLeft)
rightInterval = calculateСonfidenceIntervalRightBoard(selection, a, hRight)

print("LeftSideDI: ", leftInterval)
print("RightSideDI: ", rightInterval)
