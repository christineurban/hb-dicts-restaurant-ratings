

def build_dict(file_name):
    rest_dictionary = {}

    restaurant_ratings = open(file_name)

    for line in restaurant_ratings:
        rest_name, rating = line.strip().split(':')

        rest_dictionary[rest_name] = int(rating)

    restaurant_ratings.close()

    return rest_dictionary


def alpha_rest_ratings(rest_dictionary):
    """ Alphabetizes restaurant ratings """
        
    rest_by_alpha = sorted(rest_dictionary.items())
    
    for restaurant, rating in rest_by_alpha:
        print "%s is rated at %d" % (restaurant, rating)    


def user_rest_ratings(rest_dictionary):
    user_rest_name = raw_input("Enter your restaurant name: ")
    
    print "How would you rate this restaurant from 1 to 5?"
    user_rest_rating = int(raw_input("1 = terrible, 5 = excellent: "))

    rest_dictionary[user_rest_name] = user_rest_rating

    alpha_rest_ratings(rest_scores)


rest_dictionary = build_dict('scores.txt')

       






    