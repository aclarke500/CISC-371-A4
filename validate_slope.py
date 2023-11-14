import math
import matplotlib.pyplot as plt
y = [
    -1.85840734641021,
    5.85987448204884,
    8.57815631050788,
    11.2964381389669,
    14.0147199674260,
    16.7330017958850,
    19.4512836243441,
    22.1695654528031,
    24.8878472812622,
    30.6061291097212
]

x = []

for i in range(0,10):
  x.append(i)


def get_slope(x1, y1, x2, y2):
  return (y2 - y1) / (x2 - x1)


slopes = []
for i in range(len(y)-1):
  slopes.append(get_slope(i, y[i], i+1, y[i+1]))

slopes_inside=[]
for i in range(1, len(y)-2):
  slopes_inside.append(get_slope(i, y[i], i+1, y[i+1]))

print(sum(slopes)/len(slopes))
print(sum(slopes_inside)/len(slopes_inside))

# plot to compare numbers
# plt.scatter(x,y)
# plt.show()


