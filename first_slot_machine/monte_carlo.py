# Monte Carlo Simulation
import numpy as np
import slot
import time
import payout
from variables import expected_return, cost

def main():
    toc = time.perf_counter()
    N = 100000
    win = 0
    #K = []
    for i in range(N):
        spin = np.asarray(slot.main()).T.tolist()
        win += payout.main(spin)
        #K.append(payout.main(spin)) # takes 1.4x longer to compute this

    tic = time.perf_counter()
    return f'Monte Carlo Results:\n' \
           f'Expected Value: {round(expected_return * cost - cost, 2)}\n' \
           f'Estimated Value: {round(win/N - cost, 2)} \n' \
           f'Expected Profit: {N * (cost - cost * expected_return)}\n' \
           f'Profit: {N * cost - win}\n' \
           f'Run Time: {round(tic-toc, 4)}s\n' \
           #f'Top Spins: {sorted(K, reverse = True)[:10]}'

if __name__ == '__main__':
    print(main())


# k = 4
# Monte Carlo Results N = 10,000,000:
# Expected Value: -0.5
# Estimated Value: -0.44
# Expected Profit: 5000000.0
# Profit: 4351000.478492215
# Run Time: 572.7969s

# k = 5
# Monte Carlo Results:
# Expected Value: -0.5
# Estimated Value: -0.07
# Expected Profit: 5000000.0
# Profit: 684125.4957317859
# Run Time: 759.8991s
