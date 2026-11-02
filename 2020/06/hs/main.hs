import Data.List (findIndices, tails, isPrefixOf, uncons, singleton)
import Data.Bifunctor (Bifunctor(first, second))
import Data.Maybe (fromMaybe)
import Data.Set (fromList, unions, intersection)



firstArray :: (a -> a) -> [a] -> [a]
firstArray f [] = []
firstArray f (x:xs) = f x : xs


m = main



splitMulti :: (Eq a) => [[a]] -> [a] -> [[a]]
splitMulti _ [] = [[]]
splitMulti seps xx@(x:xs) = if cut then [] : nn else firstArray (x :) nn
    where
        cs = filter (flip isPrefixOf xx) seps
        cut = not $ null cs
        nn = splitMulti seps $ if cut then drop (length $ head cs) xx else xs

split :: (Eq a) => [a] -> [a] -> [[a]]
split = splitMulti . singleton

cutn :: (Eq a) => [[a]] -> [a] -> Maybe [[a]]
cutn [] [] = Just []
cutn _ [] = Nothing
cutn seps@(sep:sept) xx@(x:xs) = if isPrefixOf sep xx then ([] :) <$> cutn sept (drop (length sep) xx) else firstArray (x :) <$> cutn seps xs

cut2 :: (Eq a) => [a] -> [a] -> Maybe ([a], [a])
cut2 sep x = (\[a, b] -> (a, b)) <$> cutn [sep] x

cut3 :: (Eq a) => ([a], [a]) -> [a] -> Maybe ([a], [a], [a])
cut3 (sepa, sepb) x = (\[a, b, c] -> (a, b, c)) <$> cutn [sepa, sepb] x

cut4 :: (Eq a) => ([a], [a], [a]) -> [a] -> Maybe ([a], [a], [a], [a])
cut4 (sepa, sepb, sepc) x = (\[a, b, c, d] -> (a, b, c, d)) <$> cutn [sepa, sepb, sepc] x

cut5 :: (Eq a) => ([a], [a], [a], [a]) -> [a] -> Maybe ([a], [a], [a], [a], [a])
cut5 (sepa, sepb, sepc, sepd) x = (\[a, b, c, d, e] -> (a, b, c, d, e)) <$> cutn [sepa, sepb, sepc, sepd] x

cut6 :: (Eq a) => ([a], [a], [a], [a], [a]) -> [a] -> Maybe ([a], [a], [a], [a], [a], [a])
cut6 (sepa, sepb, sepc, sepd, sepe) x = (\[a, b, c, d, e, f] -> (a, b, c, d, e, f)) <$> cutn [sepa, sepb, sepc, sepd, sepe] x


map3 :: (a0 -> b0, a1 -> b1, a2 -> b2) -> (a0, a1, a2) -> (b0, b1, b2)
map3 (f0, f1, f2) (a0, a1, a2) = (f0 a0, f1 a1, f2 a2)

map4 :: (a0 -> b0, a1 -> b1, a2 -> b2, a3 -> b3) -> (a0, a1, a2, a3) -> (b0, b1, b2, b3)
map4 (f0, f1, f2, f3) (a0, a1, a2, a3) = (f0 a0, f1 a1, f2 a2, f3 a3)

map5 :: (a0 -> b0, a1 -> b1, a2 -> b2, a3 -> b3, a4 -> b4) -> (a0, a1, a2, a3, a4) -> (b0, b1, b2, b3, b4)
map5 (f0, f1, f2, f3, f4) (a0, a1, a2, a3, a4) = (f0 a0, f1 a1, f2 a2, f3 a3, f4 a4)

map6 :: (a0 -> b0, a1 -> b1, a2 -> b2, a3 -> b3, a4 -> b4, a5 -> b5) -> (a0, a1, a2, a3, a4, a5) -> (b0, b1, b2, b3, b4, b5)
map6 (f0, f1, f2, f3, f4, f5) (a0, a1, a2, a3, a4, a5) = (f0 a0, f1 a1, f2 a2, f3 a3, f4 a4, f5 a5)


firstLine :: [a] -> Maybe (a, [a])
firstLine = uncons

removeLastEmpty :: [[a]] -> [[a]]
removeLastEmpty [] = []
removeLastEmpty [[]] = []
removeLastEmpty (x:xs) = x : removeLastEmpty xs


parenlr :: (Eq a) => a -> a -> [a] -> Bool
parenlr lp rp s = length s >= 2 && head s == lp && last s == rp

paren :: (Eq a) => a -> [a] -> Bool
paren = parenlr <*> id

cutParen :: ([a] -> Bool) -> [a] -> [a]
cutParen p s = if p s then tail $ init s else s

unparenlr :: (Eq a) => a -> a -> [a] -> [a]
unparenlr = (cutParen .) . parenlr

unparen :: (Eq a) => a -> [a] -> [a]
unparen = cutParen . paren

unstring :: String -> String
unstring = cutParen $ flip any [paren '\'', paren '\"'] . flip ($)


translate :: (Eq a) => [(a, b)] -> [a] -> [Maybe b]
translate _ [] = []
translate t (x:xs) = lookup x t : translate t xs

translateDefualt :: (Eq a) => b -> [(a, b)] -> [a] -> [b]
translateDefualt d = (map (fromMaybe d) .) . translate


count :: (a -> Bool) -> [a] -> Int
count = (length .) . filter

inRange :: Ord a => a -> a -> a -> Bool
inRange mi ma x = mi <= x && x <= ma

binDigitRead :: Char -> Int
binDigitRead '0' = 0
binDigitRead '1' = 1

binToInt :: String -> Int
binToInt = foldl (\n c -> 2 * n + binDigitRead c) 0


loadInpFile :: String -> IO String
loadInpFile = readFile



type AOCResult = Int
type AOCInput = [[String]]



main :: IO ()
main = do
    inp <- parseInput <$> loadInpFile "inp.txt"
    print $ solveA inp
    putStrLn "  -------------------------------  "
    print $ solveB inp


parseInput :: String -> AOCInput
parseInput = map (removeLastEmpty . split "\n") . removeLastEmpty . split "\n\n"

solveA :: AOCInput -> AOCResult
solveA = sum . map (length . unions . map fromList)

solveB :: AOCInput -> AOCResult
solveB = sum . map (length . foldl intersection (fromList "abcdefghijklmnopqrstuvwxyz") . map fromList)