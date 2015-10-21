def powers_of_two(number):
    return [2 ** (index) for index, value
            in enumerate(reversed("{0:b}".format(number))) if int(value) == 1]


def powers_of_two_remain(numbers):
    remaining_powers_of_two = []
    for number in numbers:
        for power_of_two in powers_of_two(number):
            remaining_powers_of_two.append(power_of_two)
    for element in set(remaining_powers_of_two):
        if remaining_powers_of_two.count(element) % 2 == 1:
            return True
    return False
