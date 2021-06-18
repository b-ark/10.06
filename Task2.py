# Implement a class Mathematician which is a helper class for doing math operations on lists

# The class doesn't take any attributes and only has methods:

# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
class Mathematician:
    @staticmethod
    def square_nums(temp):
        return [item ** 2 for item in temp]

    @staticmethod
    def remove_positives(temp):
        return [item for item in temp if item < 0]

    @staticmethod
    def filter_leaps(temp):
        return [item for item in temp if item % 4 == 0]


m = Mathematician()
assert m.square_nums([7, 11, 5, 4])
assert m.remove_positives([26, -11, -8, 13, -90])
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020])
