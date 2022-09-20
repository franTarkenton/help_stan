
def whatQuad(x, y):
    if x > 0:
        if y > 0:
            location = 'quad 1'
        elif y < 0:
            location = 'quad 4'
        elif y == 0:
            location = 'on y axis'
    elif x < 0:
        if y < 0:
            location = 'quad 3'
        elif y > 0:
            location = 'quad 2'
        elif y == 0:
            location = 'on y axis'
    elif x == 0:
        if y == 0:
            location = 'on origin'
        elif y != 0:
            location = 'on x axis'
    return location

testData = [[-3, 3, 'quad 2'],
            [3, -3, 'quad 4'],
            [-3, -3, 'quad 3']]

for currentTestData in testData:
    x = currentTestData[0]
    y = currentTestData[1]
    expected = currentTestData[2]
    quadVal = whatQuad(x, y)
    if expected != quadVal:
        print(f"x: {x}")
        print(f"y: {y}")
        print(f"{quadVal} != {expected}")

    else:
        print(f"x = {x}; y = {y}; quad: {quadVal}")






