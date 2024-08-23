#Key Scenarios
# When Keys Overlap:
# answer: If both dictionaries have the same keys, the values in dict1 are replaced with the values from dict2.

# When Keys Do Not Overlap:
# answer: If there are no shared keys, dict2's key-value pairs are simply added to dict1 without replacing any of the existing key-value pairs in dict1

def main():
    dict1 = {"name": "Aishwarya", "city" : "pune"}
    dict2 = {"name1": "Shubham", "city1" : "Manali"}

    dict1.update(dict2)
    print(dict1)


    dict3 = dict1 | dict2
    print(dict3)

   #using integers
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}

    dict1.update(dict2)
    print(dict1)

    dict3 = dict1 | dict2
    print(dict3)

main()

