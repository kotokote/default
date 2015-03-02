__author__ = 'evebodnia'
import matplotlib.pyplot as plt
import re as re
with open('SExtractorConfigFiles/test.cat', 'r') as f:
    read_data = f.read()
    read_data = read_data.split('\n')
    y = [re.split(" +", row)[14] for row in read_data[26:-1]]
    x = [re.split(" +", row)[23] for row in read_data[26:-1]]

   # plt.plot(x, y, 'ro')
    plt.xlabel("Flux-radius")
    plt.ylabel("Mag")
    plt.ylim([-20, -5])
    plt.xlim([0, 4])
    plt.scatter(x, y, marker='s', s=1)
    ay = plt.gca()
    ay.set_ylim(ay.get_ylim()[::-1])
    plt.show()


