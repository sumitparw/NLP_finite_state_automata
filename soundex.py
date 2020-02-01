from fst import FST
import string, sys
from fsmutils import composechars, trace


def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """
    # Let's define our first FST
    f1 = FST('soundex-generate')
    # Indicate that '1' is the initial state
    # for list_start
    f1.add_state('start')
    #for list_1
    f1.add_state('1')
    # for list_2
    f1.add_state('2')
    # for list_3
    f1.add_state('3')
    # for list_4
    f1.add_state('4')
    # for list_5
    f1.add_state('5')
    # for list_6
    f1.add_state('6')
    # for list_final
    f1.add_state('final')
    # for list_transition
    f1.add_state('next')
    f1.initial_state = 'start'
    # Set all the final states
    f1.set_final('final')
    # setting the rules
    # b, f, p, v = 1
    #  c, g, j, k, q, s, x, z = 2
    #  d, t = 3
    #  l = 4
    #  m, n = 5
    # r = 6
    vowles_plus = ['a', 'e', 'i', 'o', 'u', 'h', 'w', 'y', 'A', 'E', 'I', 'O', 'U', 'H', 'W', 'Y']
    list_1 = ['b', 'f', 'p', 'v', 'B', 'F', 'P', 'V']
    list_2 = ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z', 'C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z']
    list_3 = ['d', 't', 'D', 'T']
    list_4 = ['l', 'L']
    list_5 = ['m', 'n', 'M', 'N']
    list_6 = ['r', 'R']

    # for first letter in the string
    for letter in string.ascii_letters:
        if letter in vowles_plus:
            f1.add_arc('start', 'next', (letter), (letter))
        if letter in list_1:
            f1.add_arc('start', '1', (letter), (letter))
        if letter in list_2:
            f1.add_arc('start', '2', (letter), (letter))
        if letter in list_3:
            f1.add_arc('start', '3', (letter), (letter))
        if letter in list_4:
            f1.add_arc('start', '4', (letter), (letter))
        if letter in list_5:
            f1.add_arc('start', '5', (letter), (letter))
        if letter in list_6:
            f1.add_arc('start', '6', (letter), (letter))
    # for first letter in the string
    for letter in string.ascii_letters:
        if letter in vowles_plus:
            f1.add_arc('next', 'next', (letter), ())
        if letter in list_1:
            f1.add_arc('next', '1', (letter), ('1'))
        if letter in list_2:
            f1.add_arc('next', '2', (letter), ('2'))
        if letter in list_3:
            f1.add_arc('next', '3', (letter), ('3'))
        if letter in list_4:
            f1.add_arc('next', '4', (letter), ('4'))
        if letter in list_5:
            f1.add_arc('next', '5', (letter), ('5'))
        if letter in list_6:
            f1.add_arc('next', '6', (letter), ('6'))

    f1.add_arc('next', 'final', (), ())

    for letter in string.ascii_letters:
        if letter in vowles_plus:
            f1.add_arc('1', 'next', (letter), ())
        if letter in list_1:
            f1.add_arc('1', '1', (letter), ())
        if letter in list_2:
            f1.add_arc('1', '2', (letter), ('2'))
        if letter in list_3:
            f1.add_arc('1', '3', (letter), ('3'))
        if letter in list_4:
            f1.add_arc('1', '4', (letter), ('4'))
        if letter in list_5:
            f1.add_arc('1', '5', (letter), ('5'))
        if letter in list_6:
            f1.add_arc('1', '6', (letter), ('6'))
    f1.add_arc('1', 'final', (), ())

    for letter in string.ascii_letters:
        if letter in vowles_plus:
            f1.add_arc('2', 'next', (letter), ())
        if letter in list_1:
            f1.add_arc('2', '1', (letter), ('1'))
        if letter in list_2:
            f1.add_arc('2', '2', (letter), ())
        if letter in list_3:
            f1.add_arc('2', '3', (letter), ('3'))
        if letter in list_4:
            f1.add_arc('2', '4', (letter), ('4'))
        if letter in list_5:
            f1.add_arc('2', '5', (letter), ('5'))
        if letter in list_6:
            f1.add_arc('2', '6', (letter), ('6'))

    f1.add_arc('2', 'final', (), ())

    for letter in string.ascii_letters:
        if letter in vowles_plus:
            f1.add_arc('3', 'next', (letter), ())
        if letter in list_1:
            f1.add_arc('3', '1', (letter), ('1'))
        if letter in list_2:
            f1.add_arc('3', '2', (letter), ('2'))
        if letter in list_3:
            f1.add_arc('3', '3', (letter), ())
        if letter in list_4:
            f1.add_arc('3', '4', (letter), ('4'))
        if letter in list_5:
            f1.add_arc('3', '5', (letter), ('5'))
        if letter in list_6:
            f1.add_arc('3', '6', (letter), ('6'))
    f1.add_arc('3', 'final', (), ())

    for letter in string.ascii_letters:
        if letter in vowles_plus:
            f1.add_arc('4', 'next', (letter), ())
        if letter in list_1:
            f1.add_arc('4', '1', (letter), ('1'))
        if letter in list_2:
            f1.add_arc('4', '2', (letter), ('2'))
        if letter in list_3:
            f1.add_arc('4', '3', (letter), ('3'))
        if letter in list_4:
            f1.add_arc('4', '4', (letter), ())
        if letter in list_5:
            f1.add_arc('4', '5', (letter), ('5'))
        if letter in list_6:
            f1.add_arc('4', '6', (letter), ('6'))
    f1.add_arc('4', 'final', (), ())

    for letter in string.ascii_letters:
        if letter in vowles_plus:
            f1.add_arc('5', 'next', (letter), ())
        if letter in list_1:
            f1.add_arc('5', '1', (letter), ('1'))
        if letter in list_2:
            f1.add_arc('5', '2', (letter), ('2'))
        if letter in list_3:
            f1.add_arc('5', '3', (letter), ('3'))
        if letter in list_4:
            f1.add_arc('5', '4', (letter), ('4'))
        if letter in list_5:
            f1.add_arc('5', '5', (letter), ())
        if letter in list_6:
            f1.add_arc('5', '6', (letter), ('6'))
    f1.add_arc('5', 'final', (), ())

    for letter in string.ascii_letters:
        if letter in vowles_plus:
            f1.add_arc('6', 'next', (letter), ())
        if letter in list_1:
            f1.add_arc('6', '1', (letter), ('1'))
        if letter in list_2:
            f1.add_arc('6', '2', (letter), ('2'))
        if letter in list_3:
            f1.add_arc('6', '3', (letter), ('3'))
        if letter in list_4:
            f1.add_arc('6', '4', (letter), ('4'))
        if letter in list_5:
            f1.add_arc('6', '5', (letter), ('5'))
        if letter in list_6:
            f1.add_arc('6', '6', (letter), ())
    f1.add_arc('6', 'final', (), ())

    return f1


def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    f2.initial_state = '1'
    f2.set_final('4')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '1', (letter), (letter))
    f2.add_arc('1', '4', (), ())
    for n in range(10):
        f2.add_arc('1', '2', (str(n)), (str(n)))
    f2.add_arc('2', '4', (), ())
    for n in range(10):
        f2.add_arc('2', '3', (str(n)), (str(n)))
    f2.add_arc('3', '4', (), ())
    for n in range(10):
        f2.add_arc('3', '4', (str(n)), (str(n)))
    for n in range(10):
        f2.add_arc('4', '4', (str(n)), ())
    return f2


def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('2')
    f3.add_state('3')
    f3.add_state('4')

    f3.initial_state = '1'
    f3.set_final('4')

    f3.add_arc('1', '2', (), ('0'))
    f3.add_arc('2', '3', (), ('0'))
    f3.add_arc('3', '4', (), ('0'))
    for letter in string.letters:
        f3.add_arc('1', '1', (letter), (letter))

    for n in range(10):
        f3.add_arc('1', '2', (str(n)), (str(n)))

    for n in range(10):
        f3.add_arc('2', '3', (str(n)), (str(n)))

    for n in range(10):
        f3.add_arc('3', '4', (str(n)), (str(n)))
    for n in range(10):
        f3.add_arc('4', '4', (str(n)), ())
    return f3
    #
    # for letter in string.letters:
    #     f3.add_arc('1', '1', (letter), (letter))
    #     f3.add_arc('4', '4', (letter), ())
    #
    # for number in xrange(10):
    #     f3.add_arc('1', '2', (str(number)), (str(number)))
    #
    # for number in xrange(10):
    #     f3.add_arc('2', '3', (str(number)), (str(number)))
    #
    # for number in xrange(10):
    #     f3.add_arc('3', '4', (str(number)), (str(number)))
    #
    # return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!


if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        # print trace(f1, user_input)
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))