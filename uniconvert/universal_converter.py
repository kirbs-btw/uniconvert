def combinations(rangeMin, rangeMax, char_Set):
    """
    get a combinations of a charset in a specific range
    :param rangeMin: start
    :param rangeMax: endpoint
    :param char_Set: set of characters
    :return: returns the combinations in an array - large quantities should be split up to not over fill the storage
    """
    possibleComb = []
    for i in range(rangeMin, rangeMax):
        possibleComb.append(convert(i, char_Set))

    return possibleComb


def findExponent(num, len):
    """
    finds the highest exponent to divide the string
    :param num:
    :param len:
    :return:
    """
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
    """
    convters any number to with a charset to a string -
    useful to get all possible combinations of something
    :param num: integer
    :param char: a string of characters
    :return:
    """
    highestExponent = findExponent(num, len(char))
    exponent = highestExponent
    text = ""

    while exponent > -1:
        count = num // len(char) ** exponent
        num = num - (len(char) ** exponent * count)
        text += char[count-1]
        exponent -= 1
    return text

def numCombine(num ,char_set):
    """
    takes a num as the length the combinations has

    e.g.
    num = 3

    aaa
    aab
    aac
    ...
    ffk
    ...
    zzz
    
    :param num: integer
    :param char_set: set of characters in a string
    :return:
    """
    min = len(char_set) ** (num - 1)
    max = len(char_set) ** num

    combSet = combinations(min, max, char_set)

    return  combSet

if __name__ == '__main__':
    char_set = "abcdefghijklmnopqrstuvwxyz"
    num = 50
    #convert(num, char_set)

    #print(combinations(0, 9999, char_set))

    print(numCombine(2, char_set))

####
# fixes - the first z has to go some how
# enter specific num of char - calc what nums these are...
###