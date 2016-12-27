import Data.Char 
import Data.List 
 
euler_8 = do
   str <- readFile "number.txt"
   print . maximum . map product
         . foldr (zipWith (:)) (repeat [])
         . take 13 . tails . map (fromIntegral . digitToInt)
         . concat . lines $ str

main = euler_8
