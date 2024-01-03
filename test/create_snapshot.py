import sys

import matplotlib.pyplot as plt
import matplotlib_fontja

snapshot_path = sys.argv[1]

plt.figure()
plt.plot(list(range(10)), list(range(10)), label="IPAexゴシック")
plt.legend()
plt.xlabel("㍾㍽㍼㍻㋿XYZ")
plt.ylabel("あいうえおABC")
plt.savefig(snapshot_path)
