# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
# More examples in the test cases below.

# Good luck!

def repeats(arr): #
    sum = 0
    unique = [] # store non-repeated numbers
    arr.sort()
    arrLen = len(arr)
    indx = 0
    arrRange = range(len(arr))
    while indx < arrLen:
        if arr[indx] != arr[indx+1]:
            unique.append(arr[indx])
            indx += 1
            if indx == arrLen - 1:
                unique.append(arr[indx])
                indx += 1
        else:
            if indx == arrLen - 1: # The last two numbers in the list are repeated 
                indx += 1 
            else:
                if indx + 2 == arrLen - 1: # last number in list but not repeated
                    indx += 2
                    unique.append(arr[indx])
                    indx += 1
                else:
                    indx +=2
    for indx in range(len(unique)):
        sum += unique[indx]
    return sum
