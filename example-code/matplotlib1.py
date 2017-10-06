from matplotlib import pyplot as plt
import numpy as np

tt = np.linspace(0, 2, 100)
xx = np.sin(np.pi*tt)

plt.plot(tt, xx)

# add some candy
plt.grid()
plt.xlabel("$t$ in s")
plt.ylabel("$x(t)$")

plt.title(r"$x(t)=\sin(\pi \cdot t)$")
# note the usage of a raw-string
# (beginning with r")
# -> no special meaning of
# backslash-character (\)

plt.show()
