triangular = [ (x*(x+1) `div` 2) | x <- [1, 2..]]

primes = 2 : primes'
  where isPrime (p:ps) n = p*p > n || n `rem` p /= 0 && isPrime ps n
        primes' = 3 : filter (isPrime primes') [5, 7 ..]

primeFactors n = factor n primes
  where
    factor n (p:ps) 
        | p*p > n        = [n]
        | n `mod` p == 0 = p : factor (n `div` p) (p:ps)
        | otherwise      =     factor n ps

main = print $ problem_12

problem_12 = head $ filter ((> 500) . nDivisors) triangleNumbers
  where nDivisors n = product $ map ((+1) . length) (group (primeFactors n))    
        triangleNumbers = scanl1 (+) [1..]
