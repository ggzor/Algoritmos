import           Data.Char (digitToInt, isNumber)
import           Text.Read (readMaybe)

transformElement' "" = ""
transformElement' s = 
  let (result, rest) = break isNumber s
      (number, finalRest) = span isNumber rest
      numberExtra = if null number then "" else show (read number + 1)
  in result ++ numberExtra ++ transformElement' finalRest

transformElement :: String -> String
transformElement s =
  let func (r, Nothing) c =
        if isNumber c
          then (r, Just (digitToInt c))
          else (r ++ [c], Nothing)
      func (r, Just n) c =
        if isNumber c
          then (r, Just (n * 10 + digitToInt c))
          else (r ++ show (n + 1) ++ [c], Nothing)
      result = foldl func ("", Nothing) s
      join (r, Nothing) = r
      join (r, Just n)  = r ++ show (n + 1)
   in join result

transformList :: [String] -> [String]
transformList = map transformElement'

main = do
  putStr "Give me a list of strings with numbers: "
  value <- readMaybe <$> getLine
  case value of
    Just l  -> putStrLn $ "The modified list is: " ++ show (transformList l)
    Nothing -> putStrLn "The value provided is not a list." >> main
