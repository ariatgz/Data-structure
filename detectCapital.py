
def detector(word):
    upperCaseLength = 0

    for i in word:
        if i.isupper():
            upperCaseLength += 1

    if upperCaseLength == len(word):
        return True

    elif upperCaseLength == 0:
        return True

    elif upperCaseLength == 1:
        if word[0].isupper():
            return True

    return False


print(detector("USA"))
