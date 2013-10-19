f :: [[Int]] -> [Int]
f x = map g x

g :: [Int] -> Int
g [n,c,m] = getchoc n c m 0

getchoc n c m w | (n<c && w<m) = 0
                | otherwise =  n `div` c + w `div` m + getchoc (n `mod` c) c m (n `div` c + w `div` m + w `mod` m)

main = do
    t<- readLn :: IO Int
    inputData <- getContents
    mapM_ putStrLn $ map show $ f $ map (map (read :: String -> Int) . words) $ lines inputData
