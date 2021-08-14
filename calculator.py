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

            numbers[operatorIndex - 1] = str(firstNum / secondNum)
        elif ('×' in numbers):
            operatorIndex = numbers.index("×")
            firstNum = float(numbers[operatorIndex - 1])
            secondNum = float(numbers.pop(operatorIndex + 1))

            numbers.pop(operatorIndex)

            numbers[operatorIndex - 1] = str(firstNum * secondNum)
        elif ('-' in numbers):
            operatorIndex = numbers.index("-")
            firstNum = float(numbers[operatorIndex - 1])
            secondNum = float(numbers.pop(operatorIndex + 1))

            numbers.pop(operatorIndex)

            numbers[operatorIndex - 1] = str(firstNum - secondNum)
        elif ('+' in numbers):
            operatorIndex = numbers.index("+")
            firstNum = float(numbers[operatorIndex - 1])
            secondNum = float(numbers.pop(operatorIndex + 1))

            numbers.pop(operatorIndex)

            numbers[operatorIndex - 1] = str(firstNum + secondNum)
    
    return numbers[0]