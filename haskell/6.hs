squares = [x*x | x<-[1, 2..]]
naturals = [1, 2..]

squareSum n = sum (take n squares)
naturalSum n = sum (take n naturals)

main = print $ (naturalSum 100 * naturalSum 100) - squareSum 100
