class Restaurant:
    def __init__(self, restaurant_name, cusine_type, rating=0):
        self.name = restaurant_name
        self.cusine_type = cusine_type
        self.rating = rating

    def describe_restaurant(self):
        print(self.name, self.cusine_type)

    def open_restaurant(self):
        print('Restaurant is open')

    def update_rating(self, new_rating):
        print('rating update from' + str(self.rating) + 'to' + str(new_rating), end='')
        self.rating = new_rating


newRestaurant = Restaurant('macdonalds', 'fast food')

print(newRestaurant.name, newRestaurant.cusine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

rest1 = Restaurant('burget_king', 'fast food')
rest2 = Restaurant('KFC', 'fast-fast food')
rest3 = Restaurant('Teremok', 'russian')

rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()

rest1.update_rating(123)
