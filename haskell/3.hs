import Data.List

bigNum = 600851475143

allPrimes = 2 : primes'
  where isPrime (p:ps) n = p*p > n || n `rem` p /= 0 && isPrime ps n
        primes' = 3 : filter (isPrime primes') [5, 7 ..]


primes = takeWhile (\p -> p^2<=bigNum) allPrimes
 
primeFactors n = factor n primes
  where
    factor n (p:ps) 
        | p*p > n        = [n]
        | n `mod` p == 0 = p : factor (n `div` p) (p:ps)
        | otherwise      =     factor n ps
 
problem_3 = last (primeFactors 600851475143)

main = print $ problem_3
