# Fizz_Buzz_Fibonacci

In the programming language of your choice, write a program generating the first n Fibonacci numbers F(n), printing

"Buzz" when F(n) is divisible by 3 | "Fizz" when F(n) is divisible by 5 | "FizzBuzz" when F(n) is divisible by 15 | "BuzzFizz" when F(n) is prime | the value F(n) otherwise.

CODE:

Method checkPrime(N) checks if the given integer number N is a prime number. This method is called by the method F(n).
F(n) will first check if the generated F(n) will be divisible 3,5 or 15 and if F(n) will be prime. This helps eliminate the generation of sequence when it is not needed.
If yes, it prints out the appropriate words, else it generates the fibonacci sequence of given length.
Main program takes the length of the fibonacci sequence to be generated from the user.
