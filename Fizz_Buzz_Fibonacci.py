#In the programming language of your choice, write a program generating the first n Fibonacci numbers F(n), printing

#"Buzz" when F(n) is divisible by 3.
#"Fizz" when F(n) is divisible by 5.
#"FizzBuzz" when F(n) is divisible by 15.
#"BuzzFizz" when F(n) is prime.
#the value F(n) otherwise.
#We encourage you to compose your code for this question in a way that represents the quality of 
#code you produce in the workplace - e.g. tests, documentation, linting, dependency management 
#(though there's no need to go this far).



# >>>>>> SOLUTION <<<<<<	

# Method checks if the given number is a Prime number
def checkPrime(N):
	flag = False
	# Try finding a factor of the number other than itself
	if N > 1:
	 	for x in range(2,N):
	  		if (N % x) == 0:
	  			return flag	
	   	flag = True
	  	return flag

# This is our function F(n) described in the problem statement 
def F(num):
	buff = []
	# Condition checks if given number is divisible by 3,5, 15 or prime.
	#If not calculates Fibonacci series which reduces computations
	if num%3 == 0 or num%5 == 0 or num%15 == 0 or checkPrime(num):
		if num%3 == 0:
			buff.append("Buzz")
		if num%5 == 0:
			buff.append("Fizz")
		if num%15 == 0:
			buff.append("FizzBuzz")
		if checkPrime(num):
			buff.append("BuzzFizz")
		for i in buff:
			print i

	else:
		fibo = []
		a = 0
		b = 1
		for i in range(0,num):
			if i == 0:
				fibo.append(a)
			if i == 1:
				fibo.append(b)
			if i > 1:
				c = a+b
				fibo.append(c)
				a=b
				b=c

		print fibo

# Main() function
if __name__ == '__main__':
	# The program takes input from the user
	print "How many fibonacci numbers do you want to see? "
	n = input()
	F(n)