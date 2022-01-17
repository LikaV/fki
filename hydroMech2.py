# import pandas as pd
import numpy as np
import math
import sys

def main(argv):
    # '''
    # Usage: python3 transaq.py config.json [-d]
    # Args:
    #     config: path to json configuration file
    #     flag -d: print debug info
    # '''

    try:
        # print(argv[0],argv[1])
        l = 400 # cm
        g = 1000 # cm / c^2
        d = 1 # cm

        delta_h = float(argv[1])
        v = float(argv[2])
        Re = float(argv[3])

        lambd = delta_h / l * (2 * g * d) / v / v
        lambd_b = 0.3164 / math.sqrt(math.sqrt(Re))

        print(f"{lambd:10.4f} {lambd_b:10.4f}")

    except Exception as ex:
        print("An exception caught: ", ex, file=sys.stderr)
        return 1

    return 0

if __name__ == "__main__":
    main(sys.argv[:])