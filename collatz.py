def collatz(n):
	while True:
		steps = 0
		while n > 1:
			n = n/2 if n%2==0 else n*3+1
			steps += 1
		yield steps
		n += 1



col = 1
max = 0;

while True:
	current = next(collatz(col))
	if current > max:
		max = current
		print(f"New max found: Number {col}, max {current}")
	col += 1