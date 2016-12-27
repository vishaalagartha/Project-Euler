main = print $ (sum . takeWhile (<1000) ) [3, 6..] + (sum . takeWhile (<1000)) [5, 10..] - (sum . takeWhile (<1000)) [15, 30..]
