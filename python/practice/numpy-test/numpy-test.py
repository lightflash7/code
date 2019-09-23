import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(0,10,0.1)
    plt.plot(x,x**2)
    plt.show()

if __name__ == '__main__':
    main()