import sys 
filename = sys.argv[1]

print "this is the arguments", sys.argv
print "this is the file with the function:", sys.argv[0]
print "this is the text file i'm inputting:", sys.argv[1]
"""Restaurant rating lister."""


# put your code here
filename = open(filename)


def user_rating(restaurant_dict):
    """ User enters own restaurant & rating, validates entry and
    adds to dict
    """
    while True:
        prompt = raw_input("Hello. Do you want to (A) enter a rating, (B): view ratings, or (Q): Quit? ")

        if prompt.lower() == "q":
            print "Goodbye!"
            break
        elif prompt.lower() == "a":
            user_rest = raw_input("Enter new restaurant name: ")
            user_score = int(raw_input("Enter its rating between 1 and 5: "))
            
            while True:
                user_score = int(raw_input("TRy again with the rating! Enter its rating between 1 and 5: "))
                #if int(user_score) > 6 or int(user_score) < 1:
                if int(user_score) > 6 or int(user_score) < 1:
                    print "Invalid! Please enter a rating between 1 and 5"
                    continue
                else:
                    restaurant_dict[user_rest] = restaurant_dict.get(user_rest, user_score)
                    print_ratings(restaurant_dict)
                    break
            # continue
        elif prompt.lower() == "b":
            print_ratings(restaurant_dict)
            continue
        else:
            print "Not a valid entry."
            continue

def print_ratings(restaurant_dict):
    for key, value in sorted(restaurant_dict.items()):
        print "{} is rated at {}.".format(key, value)


def get_ratings(filename):
    """ Processes a file and sorted restaurants & rating """
       
    new_list = []
    for line in filename:
        restaurant = line.rstrip().split(":")
        if restaurant[0][0:4] == "The ":
            print restaurant[0][0:4]
            w = restaurant[0][4:]
            new_list.append([w, restaurant[1]])
        else:
            new_list.append(restaurant)
    sorted_new_list = sorted(new_list)
    #print sorted_new_list

    restaurant_dict = {}

    for restaurant in sorted_new_list:
        print restaurant
        # print restaurant[0]
        # print restaurant[1]
        restaurant_dict[restaurant[0]] = restaurant[-1]

    return restaurant_dict

restaurant_dict = get_ratings(filename)
# user_rating(restaurant_dict)

strin = "he l loasdf;alsdkfja;dlkj"
print strin[0:4]
strang = strin[4:]
print strang
