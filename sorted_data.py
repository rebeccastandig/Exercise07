from sys import argv

script, filename = argv

def main_dict():
    f = open(filename)
    dict_of_rest = {}

    for line in f:
        line = line.strip("\n")
        split_line = line.split(":")
        dict_of_rest[split_line[0]] = split_line[1]

    return dict_of_rest

def sort_alphabetically(dictionary):
    keys = dictionary.keys()
    sorted_keys = sorted(keys)

    for key in sorted_keys:
        print key + " is rated at " + dictionary[key]

def sort_by_rating(dictionary):
    reversed_dict = {}
    for key, value in dictionary.iteritems():
        if value not in reversed_dict:
            reversed_dict[value] = [key]
        else:
            reversed_dict[value].append(key)

    sorted_ratings = sorted(reversed_dict.keys(), reverse=True)

    for rating in sorted_ratings:
        for restaurant in reversed_dict[rating]:
            if "'" in restaurant:
                print "Restaurant " + "\"" + restaurant + "\"" + " is rated at " + rating
            else:
                print "Restaurant " + '\'' + restaurant + '\'' + " is rated at " + rating


sort_by_rating(main_dict())
