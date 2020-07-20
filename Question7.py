import math
C = 50
H = 30
d = input("Type numbers that represent D : ")
d = d.split(',')
result = []
for D in d:
             Q = round(math.sqrt(2*C*int(D)/H))
             result.append(str(Q))
print(','.join(result))
             
