# calculate max area from all possible rectangles, where each side can be reduced by atmost 1.
# THese are sticks, that we need to use to form rectangeles.


def getMaxTotalArea(sideLengths):
    """ sort the lengths
     we need 2 sides of 1 size and 2 sides of another size. Get area and keep track of max area
     [2,2,3,5,6,6]
     """

    # traverse from the end, we want max area.
    max_area = 0
    pairs = []  # to keep track of pairs
    i = len(sideLengths) - 1

    sideLengths.sort()  # sort the list

    while i > 0:
        if sideLengths[i] == sideLengths[i - 1] or sideLengths[i] - 1 == sideLengths[i - 1]:
            # if there is an exact pair present, or if there is a pair present if we reduce the current number
            # make pair
            pairs.append(sideLengths[i - 1])  # store the number which matched. means we have a pair of it.
            # since we took the pair now, go one more number back
            i = i - 1

        if len(pairs) == 2:
            # means we can get the area of rectangle
            max_area = pairs[0] * pairs[1]

        i -= 1

    return max_area


print(getMaxTotalArea([2, 6, 6, 2, 3, 5]))  # answer 6*2 = 12
print(getMaxTotalArea([2, 4, 6, 1, 3, 5]))  # answer 5*3 = 15
