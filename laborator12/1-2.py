class Restaurant:
    def init(self, restaurant_name, cusine_type, rating=0):
        self.name = restaurant_name
        self.cusine_type = cusine_type
        self.rating = rating

    def describe_restaurant(self):
        print(self.name, self.cusine_type)

    def open_restaurant(self):
        print('Restaurant is open')

    def update_rating(self, new_rating):
        print('rating update from {} to {}'.format(self.rating, new_rating), end='')
        self.rating = new_rating


class IceCreamStand(Restaurant):
    def init(self, name, ctype, flav, location, work_time, rating=0):
        super().init(name, ctype, rating)
        self.flavors = flav
        self.location = location
        self.work_time = work_time

    def out_flavors(self):
        print(*self.flavors)

    def add_flavor(self, ftype):
        self.flavors.append(ftype)

    def remove_flavor(self, ftype):
        self.flavors.remove(ftype)

    def check_flavor(self, ftype):
        return ftype in self.flavors


a = IceCreamStand("name", "ctype", ['Магнат', 'Коровка', 'Вологодский пломбир', 'Карамелька', 'Шоколадная крошка', 'Макфлури'], "location", "work_time", 0)
a.out_flavors()

a.add_flavor('сортсорт')
a.out_flavors()
if a.check_flavor('сортсорт'):
    print('check = true')
    a.remove_flavor('сортсорт')
a.out_flavors()
