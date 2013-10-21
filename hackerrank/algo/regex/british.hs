import Data.List
number d t = map(\a -> numberof a d) t

numberof a d = sum $ map(\x-> (findall a x)+(findall (zeify a) x)) d

findall a  =length . filter (==a) . concatMap inits . tails

zeify a = (init $ init a)  ++ "se"

main = do
    n <- readLn :: IO Int
    inputData <- mapM (const getLine) [1..n]
    t <- readLn :: IO Int
    testData <- getContents
    mapM_ putStrLn $ map show $ number inputData $ lines testData
