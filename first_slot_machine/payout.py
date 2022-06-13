import numpy as np
import slot
from variables import expected_return, cost, n, k

# used for testing functions in payout.py
spin = np.asarray(slot.main()).T.tolist()


# Returns the amount won from spin
def main(spin):
    win = 0
    for i in range(n):
        win += sum(payout_function(spin[i]).values())
    return win

# pays out a precise amount so that the expected return of each outcome is the same
# more importantly this makes expected value calculation easy
def payout_dictionary():
    payout = slot.reel_probability()
    total_wins = len(payout)
    for element in payout:
        payout[element] = (expected_return * cost) / (total_wins * n * payout[element])
    return payout

# determines how much is won on a row
def payout_function(row):
    element_payout = how_many_of_each_row(row)
    for element in element_payout:
        if element_payout[element] > k//2: # >k//2 makes it so that only one win per row is possible
            element_payout[element] = payout_dictionary()[f'{element}~{element_payout[element]}']
        else:
            element_payout[element] = 0
    return element_payout

# determines how many of each possible outcome is in a row
def how_many_of_each_row(row):
    dict = slot.reel_dict()

    # Number of occurences for each possible outcome:
    for entry in dict:
        dict[entry] = 0
        dict[entry] += row.count(entry)

    return dict



# Creates a dictionary with the number of wins per entry
#def payout_dict(spin):
#    # zero's dict entries
#    dict = slot.reel_payout()
#    for element in dict:
#        dict[element] = 0
#
#    # finds the number of wins
#    for i in range(len(spin)):
#        for element in dict:
#            if how_many_of_each_row(spin[i])[element] >= 3:
#                # Implements higher payout for bigger hits
#                dict[element] += (how_many_of_each_row(spin[i])[element] - 2)*slot.reel_payout()[element]
#
#    return dict


# Only use on payout outcomes
# How many times does each thing happen per row?



# How many of each outcome?
#def how_many_of_each_total(spin):
#    dict = slot.reel_dict()
#    for entry in dict:
#        dict[entry] = 0
#    for entry in dict:
#        count = 0
#        for line in spin:
#            count += line.count(entry)
#        dict[entry] = count
#    return dict


# How many 2x multipliers?
#def number_of_2x(spin):
#    no_of_2x = how_many_of_each_total(spin)['2x']
#    no_of_jackpot = how_many_of_each_total(spin)['7']
#    if no_of_jackpot >= 3:
#        return no_of_2x * 5
#    else:
#        return max(1, no_of_2x) # avoid multiplying by zero


# How many respins?
#def number_of_respin(spin):
#    # How many 'RESPIN', how many 'JACKPOT'
#    no_of_respin = how_many_of_each_total(spin)['RESPIN']
#    no_of_jackpot = how_many_of_each_total(spin)['JACKPOT']
#
#    # Crazy re-spin bonus if jackpot is hit
#    if no_of_jackpot >= 3:
#        return no_of_respin * 5
#    else:
#        return no_of_respin


# Jackpot Multiplier
#def jackpot_multiplier():
#    number_of_jackpot = how_many_of_each_total(spin)['7']
#    if number_of_jackpot >= 3:
#        return math.factorial(number_of_jackpot)
#    else:
#        return 1


# Implements all multipliers
#def multiplier(element, spin):
#    return payout_dict(spin)[element] * jackpot_multiplier()


if __name__ == '__main__':
    print(main(spin))