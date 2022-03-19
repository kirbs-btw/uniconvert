def combinations(rangeMin, rangeMax, char_Set):
    possibleComb = []
    for i in range(rangeMin, rangeMax):
        possibleComb.append(convert(i, char_Set))

    return possibleComb


def findExponent(num, len):
    exponent = 0
    run = True

    while run:
        calc = num / (len ** exponent)
        if calc > 1:
            exponent += 1
        else:
            run = False
    exponent -= 1
    if exponent < 0:
        exponent = 0
    return exponent

def convert(num, char):
    #char = 'abcdefghijklmnopqrstuvwxyz'
    highestExponent = findExponent(num, len(char))
    exponent = highestExponent
    text = ""

    while exponent > -1:
        count = num // len(char) ** exponent
        num = num - (len(char) ** exponent * count)
        text += char[count-1]
        exponent -= 1
    return text

if __name__ == '__main__':
    char_set = "01"
    num = 50
    convert(num, char_set)

    print(combinations(0, 9999, char_set))