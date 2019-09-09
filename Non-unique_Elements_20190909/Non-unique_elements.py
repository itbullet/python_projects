#Your optional code here
#You can import some modules or create additional functions


def checkio(data: list) -> list:

    #This is first solution using copy of list for iteration while removing in origin of list
    """for item in list(data):

        if data.count(item) == 1:

            data.remove(item)"""

    #This is second solution using range function in order to iterate backwards to avoid conflict with size of list
    for i in range(len(data)-1, -1, -1):

        if data.count(data[i]) == 1:

            data.remove(data[i])

    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.

    #replace this for solution
    return data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
