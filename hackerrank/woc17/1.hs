str :: (Int, Int) -> String
str (a,b) = show a ++  " " ++ show b

computeRobot :: Int -> (Int, Int)
computeRobot 0 = (0,0)
computeRobot n = nextPath (computeRobot (n-1)) n


nextPath :: (Int, Int) -> Int -> (Int, Int)
nextPath (x,y) n  | n `mod` 4 == 1 = (x+n,y)
                  | n `mod` 4 == 2 = (x,y+n)
                  | n `mod` 4 == 3 = (x-n,y)
                  | n `mod` 4 == 0 = (x,y-n)


main = do
  test <- readLn :: IO Int
  inputdata <- getContents
  mapM_ putStrLn $ map str $ map computeRobot $ map (read :: String -> Int) $ lines inputdata
