def alpha_rest_ratings(rest_scores):
    """ Alphabetizes restaurant ratings """

    restaurant_ratings = open(rest_scores)

    rate_restaurants = {}

    for line in restaurant_ratings:
        rest_name, rating = line.strip().split(':')

        rate_restaurants[rest_name] = int(rating)

    restaurant_ratings.close()    

    user_rest_name = raw_input("Enter your restaurant name: ")
    
    print "How would you rate this restaurant from 1 to 5?"
    user_rest_rating = int(raw_input("1 = terrible, 5 = excellent: "))

    rate_restaurants[user_rest_name] = user_rest_rating
        
    rest_by_alpha = sorted(rate_restaurants.items())
    
    for restaurant, rating in rest_by_alpha:
        print "%s is rated at %d" % (restaurant, rating)    


alpha_rest_ratings('scores.txt')

       






    