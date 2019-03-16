from math import gcd as bltin_gcd
from math import sqrt as sqrt

n = 2531257
e = 43
d = ''

possible_p_q = list()
new_n = int(sqrt(n)) 

for i in range(2, new_n):
	if n % i ==0:
		possible_p_q.append([i, int(n/i)])

for val in possible_p_q:
	p,q = val
	tot = (p-1)*(q-1)
	for i in range(2, n):
		if e*i % tot == 1:
			d = i
			enc = [906851, 991083, 1780304, 2380434, 438490, 356019, 921472, 822283, 817856, 556932, 2102538, 2501908, 2211404, 991083, 1562919, 38268]
			dec = [pow(x,d)%n for x in enc]
			
			# [103, 105103, 101109, 12383, 97118, 97103, 10195, 83105, 12095, 70108, 121105, 110103, 9584, 105103, 101114, 115125]

			msg = [103, 105, 103, 101, 109, 123, 83, 97, 118, 97, 103, 101, 95, 83, 105, 120, 95, 70, 108, 121, 105, 110, 103, 95, 84, 105,103, 101, 114, 115, 125]
			print (''.join([chr(c) for c in msg]))




# gigem{Savage_Six_Flying_Tigers}