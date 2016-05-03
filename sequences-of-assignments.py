# c can be any number so we set c to be any random number 1-10
# we want (a)x + b to be divisible by whatever random number c is generated
	# so and and b need to be multiples of c
	# for this to happen we can take any number u and multiply it by c to create a new number that is a multiple of c
		# this gives us a
		# we do the same thing for b using a new number v and multiplying it by c 

import random

# A sequence of assignments to generate a random problem:
c = random.randint(1, 10) #random.randint(1, 10) produces a random integer from 1 to 10, endpoints included
u = random.randint(1, 10)
v = random.randint(1, 10)
a = u * c
b = v * c

print('Problem: ({a}x + {b}) / {c} = ?' .format(a = a, b = b, c = c))
print('Answer: {u}x + {v}' .format(u = u, v = v))

