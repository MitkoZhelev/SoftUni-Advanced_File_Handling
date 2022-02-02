num = [int(word) for word in input().split()]

def negative(number):
    negative = 0
    for i in number:
        if i < 0:
            negative +=i

    return negative

def positive(number):

    positive = 0
    for i in number:
        if i > 0:
            positive += i

    return positive


def which_is_stronger (positive,negative):
    if abs(positive) > abs(negative):
        return True
    else:
        return False


print(negative(num))
print(positive(num))

if(which_is_stronger(positive(num),negative(num))):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")