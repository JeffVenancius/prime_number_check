# prime_number_check
A lazy aproach to discover if a number is a prime or not.

# this algorithm has many aproaches, each one more complex than the previous.
# the idea is to discover if the number is not a prime with the less calculations possible.

let's say the input is between 1 and 1000:
- The first aproach checks if the number is even, if it is then it's not a prime.
490 numbers dealed, 510 to go.
- Second checks if the square root is an integer, more 15 numbers.
- Third we take the rounded square root and get the prime factors between, notice that we only need the square. 
As even numbers are dealt with, you don't need to get the number 2 either.
Now finally we check if input % == factor 0 with a Lazy aproach.
if none of these aproaches were enough, then it must be a prime.
