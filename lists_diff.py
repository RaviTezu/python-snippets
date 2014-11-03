#!/usr/bin/python
# Generate a list which is the element by element difference between 2 lists:

import numpy as np
l1 = range(1,31)
l2 = range(31,61)

diff = list(np.array(l2) - np.array(l1))
print diff
