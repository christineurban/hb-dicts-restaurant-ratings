
def alpha_rest_ratings(rest_scores):
    restaurant_ratings = open(rest_scores)

    rate_restaurants = {}

    for line in restaurant_ratings:
        rest_name, rating = line.strip().split(':')

        rate_restaurants[rest_name] = rating

    rest_by_alpha = sorted(rate_restaurants.items())
    


    for restaurant, rating in rest_by_alpha:
        print "%s is rated at %s" % (restaurant, rating)    

alpha_rest_ratings('scores.txt')    




    