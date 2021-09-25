def Calculator(input):
    if ('AC' in input):
        return ''

    numbers = input.split(" ")
    while (len(numbers) > 1):
        if ('÷' in numbers):
            operatorIndex = numbers.index("÷")
            firstNum = float(numbers[operatorIndex - 1])
            secondNum = float(numbers.pop(operatorIndex + 1))

            numbers.pop(operatorIndex)

            numbers[operatorIndex - 1] = firstNum / secondNum
        elif ('×' in numbers):
            operatorIndex = numbers.index("×")
            firstNum = float(numbers[operatorIndex - 1])
            secondNum = float(numbers.pop(operatorIndex + 1))

            numbers.pop(operatorIndex)

            numbers[operatorIndex - 1] = firstNum * secondNum
        elif ('-' in numbers):
            operatorIndex = numbers.index("-")
            firstNum = float(numbers[operatorIndex - 1])
            secondNum = float(numbers.pop(operatorIndex + 1))

            numbers.pop(operatorIndex)

            numbers[operatorIndex - 1] = firstNum - secondNum
        elif ('+' in numbers):
            operatorIndex = numbers.index("+")
            firstNum = float(numbers[operatorIndex - 1])
            secondNum = float(numbers.pop(operatorIndex + 1))

            numbers.pop(operatorIndex)

            numbers[operatorIndex - 1] = firstNum + secondNum
    
    finalNumber = str("{:.5}".format((numbers[0])))
    # Taken from https://ask.sagemath.org/question/11051/cutting-unnecessary-zeroes-in-float-numbers/

    if (".0" in finalNumber):
        if (finalNumber.split(".0")[1] == ""):
            return finalNumber.split(".0")[0]
    else:
        return finalNumber