## 1) Create a Python Class called Circle with Constructor which will take a List as an argument for the task.
# The List is [10, 501, 22, 37, 100, 999, 87, 351]

# Here's a Python class called Circle with a constructor that takes a list as an argument:

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = []
        for radius in self.radius_list:
            area = 3.14159 * radius * radius  # Using the approximate value of pi
            areas.append(area)
        return areas

# Example usage:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)
areas = circle.calculate_area()
print("Areas of circles with given radii:", areas)


# This class, Circle, takes a list of radii as input and has a method calculate_area that calculates the areas of circles with those radii using the formula A = π * r^2,
# where π is approximately 3.14159.

print('****'*20)

## 2) Create proper member variables inside the task if required and use them when necessary.
#  For example for this task create a class private variable named pi = 3.141

## Certainly, you can create a private class variable named pi and use it within the class to calculate circle areas.
#  Here's the modified Circle class:

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = []
        for radius in self.radius_list:
            area = Circle.pi * radius * radius  # Using the class variable for pi
            areas.append(area)
        return areas

    # Private class variable
    pi = 3.141

# Example usage:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)
areas = circle.calculate_area()
print("Areas of circles with given radii:", areas)


## In this version of the Circle class, pi is a private class variable,
#  and it's used to calculate the areas of circles within the calculate_area method.

print('****'*20)

## 3) From the given List create two class Methods Area and Perimeter
#  which will be going to calculate the Area and Perimeter.

##  You can add two class methods, area and perimeter,
#  to calculate the area and perimeter of circles based on their radii.
#  Here's the modified Circle class with these methods:

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = []
        for radius in self.radius_list:
            area = Circle.pi * radius * radius
            areas.append(area)
        return areas

    @classmethod
    def area(cls, radius):
        return cls.pi * radius * radius

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius

    # Private class variable
    pi = 3.141

# Example usage:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Calculate and print areas using the class method
print("Areas of circles with given radii:")
for radius in radius_list:
    area = Circle.area(radius)
    print(f"Radius: {radius}, Area: {area:.2f}")

# Calculate and print perimeters using the class method
print("\nPerimeters of circles with given radii:")
for radius in radius_list:
    perimeter = Circle.perimeter(radius)
    print(f"Radius: {radius}, Perimeter: {perimeter:.2f}")


## In this updated Circle class, the area and perimeter methods are class methods that can be called on the class itself to calculate the area and perimeter of circles with a given radius.
#  The example usage shows
#  how to use these methods to calculate and print the areas and perimeters for the list of radii.

print('****'*20)

## 4) Kindly visit the below URL and convert the UML diagram into a Python Class and its methods.
## https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md




# Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. Specify brand in a constructor parameter. Channel should be 1 by default. Volume should be 50 by default.
# Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
# Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will stay at the current channel.
# Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor).
# It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75".

class TV:
    def __init__(self, brand, channel=1, price=None, inches=None):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.volume = 50  # Default volume
        self.on = False

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def power_on(self):
        self.on = True

    def power_off(self):
        self.on = False

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

# Example usage:
panasonic_tv = TV(brand="Panasonic")
panasonic_tv.increase_volume()
panasonic_tv.increase_volume()
panasonic_tv.set_channel(8)
panasonic_tv.power_on()

print(panasonic_tv.status())  # Output: "Panasonic at channel 8, volume 52"

panasonic_tv.reset_tv()
print(panasonic_tv.status())  # Output: "Panasonic at channel 1, volume 50"


# This TV class has properties for brand, channel, price, inches, volume, and on/off status.
#  It provides methods to increase and decrease the volume,
#  set the channel within the valid range, reset the TV, and get the TV's status.
