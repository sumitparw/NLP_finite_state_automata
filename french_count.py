import sys
from fst import FST
from fsmutils import composewords, trace

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                  "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                     "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                     "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'


def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)


def french_count():
    f = FST('french')
    f.add_state('start')
    f.add_state('final')
    f.add_state('1')
    f.add_state('2')
    f.add_state('3')
    f.add_state('4')
    f.add_state('5')
    f.add_state('6')
    f.add_state('7')
    f.add_state('8')
    f.initial_state = 'start'
    f.set_final('final')

    # for 0 at hundreds place
    for ii in range(1):
        f.add_arc('start', '1', [str(ii)], ())
    # for 1 at hundreds place "cent"
    for ii in range(1, 2):
        f.add_arc('start', '7', [str(ii)], [kFRENCH_TRANS[100]])
    # for 2-9 at hundreds place "deux-neuf"+"cent"
    for ii in range(2, 10):
        f.add_arc('start', '7', [str(ii)], [kFRENCH_TRANS[ii]] + [kFRENCH_TRANS[100]])

    # ten's place when hundred's place was 0
    for ii in range(0, 10):
        # if ten's place is 0 state transfer 1-->2  with empty string
        if ii == 0:
            f.add_arc('1', '2', [str(ii)], ())
        # if ten's place is 1 state transfer 1-->3  with empty string
        if ii == 1:
            f.add_arc('1', '3', [str(ii)], ())
        # if ten's place is 2-6 state transfer 1-->4  with a string at location ii*10
        if ii > 1 and ii < 7:
            f.add_arc('1', '4', [str(ii)], [kFRENCH_TRANS[ii * 10]])
        # if ten's place is 7 state transfer 1-->5  with a string at location 60
        if ii == 7:
            f.add_arc('1', '5', [str(ii)], [kFRENCH_TRANS[60]])
        # if ten's place is 8 state transfer 1-->6  with a string at location 4 +20
        if ii == 8:
            f.add_arc('1', '6', [str(ii)], [kFRENCH_TRANS[4]] + [kFRENCH_TRANS[20]])
        # if ten's place is 9 state transfer 1-->3  with a string at location 4 + 20
        if ii == 9:
            f.add_arc('1', '3', [str(ii)], [kFRENCH_TRANS[4]] + [kFRENCH_TRANS[20]])

        # ten's place when hundred's place was 1-9
    for ii in range(0, 10):
        if ii == 0:
            f.add_arc('7', '8', [str(ii)], ())
        if ii == 1:
            f.add_arc('7', '3', [str(ii)], ())
        if ii > 1 and ii < 7:
            f.add_arc('7', '4', [str(ii)], [kFRENCH_TRANS[ii * 10]])
        if ii == 7:
            f.add_arc('7', '5', [str(ii)], [kFRENCH_TRANS[60]])
        if ii == 8:
            f.add_arc('7', '6', [str(ii)], [kFRENCH_TRANS[4]] + [kFRENCH_TRANS[20]])
        if ii == 9:
            f.add_arc('7', '3', [str(ii)], [kFRENCH_TRANS[4]] + [kFRENCH_TRANS[20]])

        # ones place
        # state 8-->final
    for ii in xrange(0, 10):
        if ii == 0:
            f.add_arc('8', 'final', [str(ii)], ())
        else:
            f.add_arc('8', 'final', [str(ii)], [kFRENCH_TRANS[ii]])

        # state 2-->final
    for ii in xrange(0, 10):
        f.add_arc('2', 'final', [str(ii)], [kFRENCH_TRANS[ii]])

        # state 3-->final
    for ii in range(0, 10):
        if ii < 7:
            f.add_arc('3', 'final', [str(ii)], [kFRENCH_TRANS[10 + ii]])
        else:
            f.add_arc('3', 'final', [str(ii)], [kFRENCH_TRANS[10]] + [kFRENCH_TRANS[ii]])

        # state 4-->final
    for ii in range(0, 10):
        if ii == 0:
            f.add_arc('4', 'final', [str(ii)], ())
        if ii == 1:
            f.add_arc('4', 'final', [str(ii)], [kFRENCH_AND] + [kFRENCH_TRANS[ii]])
        if ii > 1:
            f.add_arc('4', 'final', [str(ii)], [kFRENCH_TRANS[ii]])
        # state 5-->final
    for ii in range(0, 10):
        if ii == 1:
            f.add_arc('5', 'final', [str(ii)], [kFRENCH_AND] + [kFRENCH_TRANS[10 + ii]])
        elif ii > 1 and ii < 7:
            f.add_arc('5', 'final', [str(ii)], [kFRENCH_TRANS[10 + ii]])
        elif ii == 0:
            f.add_arc('5', 'final', [str(ii)], [kFRENCH_TRANS[10 + ii]])
        else:
            f.add_arc('5', 'final', [str(ii)], [kFRENCH_TRANS[10]] + [kFRENCH_TRANS[ii]])

        # state 6-->final
    for ii in xrange(0, 10):
        if ii == 0:
            f.add_arc('6', 'final', [str(ii)], ())
        else:
            f.add_arc('6', 'final', [str(ii)], [kFRENCH_TRANS[ii]])
    return f


if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',

        print " ".join(f.transduce(prepare_input(user_input)))