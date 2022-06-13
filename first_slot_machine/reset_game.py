# resets cash in GUI.py
from variables import starting_cash

def main():
    cash_txt = open('cash.txt', 'w')
    cash_txt.write(f'{starting_cash}')
    cash_txt.close()

if __name__ == '__main__':
    main()

