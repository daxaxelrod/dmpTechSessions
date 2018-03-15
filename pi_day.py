class Vehicle:
    capicity = 4

    def move(self, number):
        print("The vehicle has moved {} spaces.".format(number))

    def get_capacity(self):
        print("We can hold {} people.".format(self.capacity))


class Car(Vehicle):
    number_of_wheels = 4
    car_color = "red"

    def repaint(self, color):
        self.car_color = color



my_yellow_car = Car()

# my_yellow_car.move(3)
print(my_yellow_car.car_color)
my_yellow_car.repaint("yellow")
print(my_yellow_car.car_color)
