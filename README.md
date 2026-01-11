<h1 align="center"> Prime number checker </h1>

<div  align="center">
<img src=https://github.com/JeffVenancius/prime_number_check/assets/43701418/093a2520-aca1-4ac3-a2d0-412b7a7811c3 width=50%/>
</div>
<p align="center">Father Pucci from Jojo's Bizarre Adventure</p>

This algorithm has many aproaches, each one more complex than the previous.
the idea is to discover if the number is not a prime with the less calculations possible.

## Before doing the hard work, we test:
- it's an odd number.
- it's atleast 10.
- It's not divisable by 2,3 or 5, which are the prime factors who can divide the most. We know this because:
    - 2 is the even divisor, it divides by any even number. That's 5 numbers divisable by it for each tenth.
    - 5 is half a decimal, so you can garantee that between every decimal, one number will be divisable by 5.
    - 3 follows a pattern of multiplication: odd, even, odd. You can garantee that for each ten, you'll have at the worst case scenario one odd number divisable by 3 and, in the best one, 2 numbers. 
    - You can test this by doing 0 + 3, 1 + 3, 2 + 3... You will allways get the pattern.
- it's not a perfect square

## Forget all that, now we do this:
- Every number which ends with 1, 3, 7 or 9 might be a prime number. If it's not the case, than it's not one at all - unless we're talking about the first numbers, but oh well, we have a list for that.
- We find the primes between the list that we already have and the square root of the number we want to check, all non-prime numbers are divisable by prime ones because a prime number is a root of division (don't know the names, it is what it is). We already have a tiny list, so we try to divide the prompted number by the numbers in it. No? Well then we have to expand it, as we know that the last digit counts as a might, we just need to test the numbers with that special digit, 11, 13, 17 and 19 and so on, we test it against the numbers in our list until we get to the square root of the number we are testing, if we can't divide it by any of them, then we add it to the list, we add it to the list but we also try to divide this new prime number against the prompted one, that until we reach the square root of the prompt. And... That's it. 
