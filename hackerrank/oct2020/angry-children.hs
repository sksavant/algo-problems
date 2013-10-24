
minunfair k x = f (choose x k) (maximum x)

f (x:xs) a = min (fairness x) $ f xs a
f [] a = a

fairness a = (maximum a) - (minimum a)

-- Choose gives subsets of size k
choose :: [b] -> Int -> [[b]]
_      `choose` 0       = [[]]
[]     `choose` _       =  []
(x:xs) `choose` k       =  (x:) `fmap` (xs `choose` (k-1)) ++ xs `choose` k

main = do
    n <- readLn :: IO Int
    k <- readLn :: IO Int
    inputData <- getContents
    putStrLn $ show $ minunfair k $ map (read :: String -> Int) $ lines inputData
