# nxk slot machine
import random
import math
from variables import n, k


# Returns outcome of spin
def main():
    return reel()

    #return reel_probability()


# Returns k reels of length n
def reel():
    # Converts reel_dict into an array
    reel_array = []
    for entry in reel_dict():
        for num in range(reel_dict()[entry]):
            reel_array.append(entry)

    # Shuffles reel
    result = []
    for i in range(k):
        shuffled_reel = list(reel_array);
        random.shuffle(shuffled_reel)
        result.append(shuffled_reel[:n])

    return result


# What is on the reel
def reel_dict():
    reel_dictionary = {
        '10'      : 6, # P(10) = 6/21
        'J'       : 5, # P(J)  = 5/21
        'Q'       : 4, # P(Q)  = 4/21
        'K'       : 3, # P(K)  = 3/21
        'A'       : 2, # P(A)  = 2/21
        '7'       : 1,  # P(7)  = 1/21
    }
    return reel_dictionary


# Probability dictionary
def reel_probability():
    # frequency dictionary
    total = sum(reel_dict().values())
    probability_dict = {}
    for element in reel_dict():
        probability_dict[element] = reel_dict()[element] / total

    # probability of winning outcomes
    prob_of_win = {}
    for element in probability_dict:
        prob = probability_dict[element]
        for i in range(k // 2 + 1,k+1): # using k//2+1 is kind of cheating, it makes it so there can only be one win in the row
            # Computational bottleneck with binomial function:
            prob_of_win[f'{element}~{i}'] = math.comb(k, i) * prob**i * (1-prob)**(k-i)
            # using scipy.stats.binom.pmf(k, i, prob)
            #               1000 spins in 19 seconds
            # using scipy.special.binom(k, i) * prob**i * (1-prob)**(k-i)
            #               1000 spins in 0.71 seconds
            # using math.factorial(k) // math.factorial(i) // math.factorial(k-i) * prob**i * (1-prob)**(k-i)
            #               1000 spins in 0.341 seconds
            # using math.comb(k, i) * prob**i * (1-prob)**(k-i)
            #               1000 spins in 0.317 seconds
            # using a "fast" binomial function found online:
            #               1000 spins in 0.4247 seconds
            # I guess it isn't surprising that scipy is slower than math...
            # But seriously its 60x slower
    return prob_of_win


if __name__ == '__main__':
    print(main())