import math

# Some math stuff
n = int(input("n: "))
result = round(math.sqrt((n*(n-1))/2))
print(round(n - result))
