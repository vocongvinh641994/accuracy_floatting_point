import numpy as np

def printBigNumber(bigNumber):
    for number in range(bigNumber):
        print('power: ',number, ', value: ', np.power(0.2, number), )

if __name__ == '__main__':
    printBigNumber(100)

