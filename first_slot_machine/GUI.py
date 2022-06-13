# GUI
import slot
import payout
import numpy as np
from variables import cost, n, k

sevens, aces, kings, queens, jacks, tens = [], [], [], [], [], []
for i in range(k):
    sevens.append('7')
    aces.append('A')
    kings.append('K')
    queens.append('Q')
    jacks.append('J')
    tens.append('10')





#characters = '█ ▄ ▀ ■ ┐ └ ┴ ┬ ├ ─ ┼ │ ┤ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╣ ║ ╗ ╝ ▓ ▒ ░'

# Possible solution to losing memory is to just
# write the cash and win amounts to a text file
# every spin.
# this works great.

#for i in range(1, 7):
#    print(round((i/21)**k,10))

def main(spin):
    spin = np.asarray(spin).T.tolist()
    # fixed spins:
    #spin[1] = sevens
    #spin[1] = aces
    #spin[1] = kings
    #spin[1] = queens
    #spin[1] = jacks
    #spin[1] = tens
    win = payout.main(spin)
    return slot_display(spin, spin_colors(spin), my_cash(win), win)

def spin_colors(spin):
    fix = np.asarray(spin).tolist()
    spin_color = np.asarray(spin).T.tolist()
    for i in range(n):
        for j in range(k):
            if fix[i].count(fix[i][j]) >= k//2+1:
                spin_color[j][i] = '\x1b[92m' + spin_color[j][i] + '\033[0;0m'
    return spin_color

def slot_display(spin, spin_color, cash, win):
    # Max item size
    m = 0
    for reel in spin:
        for result in reel:
            m = max(m, len(result))

    i, j = 0, 0

    spin = np.asarray(spin).T.tolist()

    while i < len(spin):
        while j < len(spin[0]):
            for l in range(1, m + 1):
                if len(spin[i][j]) == l:
                    spin[i][j] = f' {spin_color[i][j]} ' \
                                 f'{" " * (m-l)}'
            j += 1
        i += 1
        j = 0

    # This can definitely be optimized,
    # maybe using np.asarray(spin).T.tolist()
    # to shorten the code
    # Header
    border = '█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█'
    welcome = f'{border}\n' \
              f'█ Welcome to my Casino! █\n' \
              f'{border}'
    graphics = '╔'
    # Slot machine graphics
    for column in range(k):
        graphics += '═' * (m + 2) + '╦'
    output = graphics[:-1] + '╗\n'
    i, j = 0, 0
    while j < n:
        output += '║'
        while i < k:
            output += f'{spin[i][j]}║'
            i += 1
        output += '\n'
        if j != n - 1:
            output += '╠'
            for l in range(k):
                output += '═' * (m + 2) + '╬'
            output = f'{output[:-1]}╣\n'
        elif j == n - 1:
            output += '╚'
            for l in range(k):
                output += '═' * (m + 2) + '╩'
            output = f'{output[:-1]}╝\n'
        j += 1
        i = 0



    if win == 0:
        win_or_loss = 'You didn\'t win.'
    else:
        win_or_loss = f'You just won: \033[92m${round(win,2)}\033[0;0m'
    output = f'{welcome}\n' \
             f'{output[:-1]}\n' \
             f'Cash: ${str(round(cash,2))}\n' \
             f'{win_or_loss}\n' \
             f'Spin again? ${cost}'

    # BIG WIN!!
    if win > 100:
        output += '\033[92m\n\033[1mBIG WIN!!\033[0;0m'
    return output

# create a way to reset game state

def my_cash(win):
    cash_txt_r = open('cash.txt', 'r')
    total =  float(cash_txt_r.readlines()[0]) + win - cost
    cash_txt_r.close()

    cash_txt_w = open('cash.txt', 'w')
    cash_txt_w.write(f'{total}')
    cash_txt_w.close()

    return total




if __name__ == '__main__':
    print(main(slot.main()))