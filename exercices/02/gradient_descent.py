from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

next_x = 6  # We start the search at x=6
gamma = 0.01  # Step size multiplier
precision = 0.00001  # Desired precision of result
max_iters = 10000  # Maximum number of iterations



#points = [(1,7), (2,3), (3,1)]
points = [(0,4), (1,5), (2,3), (3,5), (4,8), (5,2), (6,1), (7,1), (8,3), (9,1), (10,3)]
teta_0 = next_0 = 1
teta_1 = next_1 = 1

# Derivative function
df_0 = lambda x, y: reduce(lambda x,y : x+y,[(x + y * a) - b for a,b in points])
df_1 = lambda x, y: reduce(lambda x,y : x+y,[((x + y * a) - b) * a for a,b in points])

for i in range(max_iters):
    teta_0 = next_0
    teta_1 = next_1
    next_0 = teta_0 - (gamma/len(points)) * df_0(teta_0,teta_1)
    next_1 = teta_1 - (gamma/len(points)) * df_1(teta_0,teta_1)
    step = next_0 - teta_0
    if abs(step) <= precision:
        break



plt.figure(1)
sub_1 = plt.subplot(311)
x,y = [elem[0] for elem in points], [elem[1] for elem in points]
plt.scatter(x, y)

x = np.arange(0,15,0.1)
y = [ next_0 + next_1 * elem for elem in x]
plt.plot(x,y)

sub_1 = plt.subplot(212)

x,y = [elem[0] for elem in points], [elem[1] - (next_0 + next_1 * elem[0]) for elem in points]
plt.scatter(x,y)

x = np.arange(0,15,0.1)
y = [0]*150


plt.plot(x,y)


plt.show()

print("Minimum at", next_0, next_1)

# The output for the above will be something like
# "Minimum at 2.2499646074278457"
