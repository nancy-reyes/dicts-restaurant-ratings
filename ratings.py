import sys 
filename = sys.argv[1]

print "this is the arguments", sys.argv
print "this is the file with the function:", sys.argv[0]
print "this is the text file i'm inputting:", sys.argv[1]
"""Restaurant rating lister."""


# put your code here
filename = open(filename)

def user_rating(restaurant_dict):
    """ User enters own restaurant & rating, adds to dict """

    user_rest = raw_input("Enter new restaurant name: ")
    user_score = raw_input("Enter its rating: ")
    restaurant_dict[user_rest] = restaurant_dict.get(user_rest, user_score)



def get_ratings(filename):
    """ Prints restaurant and its rating """

       
    new_list = []
    for line in filename:
        restaurant = line.rstrip().split(":")
        if restaurant[0:3] == "The":
            restaurant = restaurant[3:]
            new_list.append(restaurant)
        else:
            new_list.append(restaurant)
    new_list = sorted(new_list)
    print new_list

    restaurant_dict = {}

    for restaurant in new_list:
        restaurant_dict[restaurant[0]] = restaurant[-1]

    user_rating(restaurant_dict)

    for key, value in sorted(restaurant_dict.items()):
        print "{} is rated at {}.".format(key, value)


get_ratings(filename)


