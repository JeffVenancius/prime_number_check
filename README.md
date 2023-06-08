# prime_number_check

![Father Pucci from Jojo's Bizarre Adventure](https://github.com/JeffVenancius/prime_number_check/assets/43701418/093a2520-aca1-4ac3-a2d0-412b7a7811c3)

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
