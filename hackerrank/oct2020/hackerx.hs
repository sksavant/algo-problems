hackerxnum x = length $ hackx x []

hackx :: [[Int]] -> [(Bool,Int)] -> [(Bool,Int)]
hackx [] a = a
hackx ([t,f]:xs) a  | (False,f) `elem` a = hackx xs a
                    | (False,f-1) `elem` a = hackx xs a
                    | (False,f+1) `elem` a = hackx xs a
                    | otherwise = hackx xs ((False,f):a)


main = do
    n <- readLn :: IO Int
    inputData <- getContents
    putStrLn $ show $ hackerxnum $ map (map (read :: String -> Int) . words) $ lines inputData
