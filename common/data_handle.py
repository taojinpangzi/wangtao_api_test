from random import *
from datetime import *


def get_date_random_number():
    return str(date.today()) + "-" + str(randint(1, 1000000))


if __name__ == '__main__':
    print(get_date_random_number())
