
num_paths x y n  
    | (x==n && y==n) = 1
    | x==n           = num_paths x (y+1) n
    | y==n           = num_paths (x+1) y n
    | otherwise      = (num_paths x (y+1) n) + (num_paths (x+1) y n)

factorial n
    | n==0      = 1
    | otherwise = n*factorial (n-1)

nCr n r = (factorial n) `div` (factorial r * factorial (n-r))

main = print $ nCr 40 20
