def count_characters(string):

    count_dict = {}

    for c in string.lower():

        if c in count_dict:
            count_dict[c] += 1

        else:
            count_dict[c] = 1

    print(count_dict)


count_characters("Anticipation")