import Data.List (findIndices, tails, isPrefixOf, uncons, singleton, lookup, transpose)
import Data.Bifunctor (Bifunctor(), first, second, bimap)
import Data.Maybe (fromMaybe, fromJust)
import Data.Char (toUpper, toLower, digitToInt)
import Data.Set (fromList, intersection, union, unions, difference)

import qualified Data.Set as S

import Control.Applicative (liftA2, liftA3, ZipList(ZipList))

import Debug.Trace (traceShowId, traceShow)



--  ===================================================  helpers  ===================================================

firstArray :: (a -> a) -> [a] -> [a]
firstArray f [] = []
firstArray f (x:xs) = f x : xs


m = main


--  ===================================================  split  ===================================================

splitMulti :: (Eq a) => [[a]] -> [a] -> [[a]]
splitMulti _ [] = [[]]
splitMulti seps xx@(x:xs) = if cut then [] : nn else firstArray (x :) nn
    where
        cs = filter (`isPrefixOf` xx) seps
        cut = not $ null cs
        nn = splitMulti seps $ if cut then drop (length $ head cs) xx else xs

split :: (Eq a) => [a] -> [a] -> [[a]]
split = splitMulti . singleton


--  ===================================================  cuts  ===================================================

cutn :: (Eq a) => [[a]] -> [a] -> Maybe [[a]]
cutn [] x = Just [x]
cutn _ [] = Nothing
cutn seps@(sep:sept) xx@(x:xs) = if sep `isPrefixOf` xx then ([] :) <$> cutn sept (drop (length sep) xx) else firstArray (x :) <$> cutn seps xs

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


--  ===================================================  tuple maps  ===================================================

map3 :: (a0 -> b0, a1 -> b1, a2 -> b2) -> (a0, a1, a2) -> (b0, b1, b2)
map3 (f0, f1, f2) (a0, a1, a2) = (f0 a0, f1 a1, f2 a2)
map4 :: (a0 -> b0, a1 -> b1, a2 -> b2, a3 -> b3) -> (a0, a1, a2, a3) -> (b0, b1, b2, b3)
map4 (f0, f1, f2, f3) (a0, a1, a2, a3) = (f0 a0, f1 a1, f2 a2, f3 a3)
map5 :: (a0 -> b0, a1 -> b1, a2 -> b2, a3 -> b3, a4 -> b4) -> (a0, a1, a2, a3, a4) -> (b0, b1, b2, b3, b4)
map5 (f0, f1, f2, f3, f4) (a0, a1, a2, a3, a4) = (f0 a0, f1 a1, f2 a2, f3 a3, f4 a4)
map6 :: (a0 -> b0, a1 -> b1, a2 -> b2, a3 -> b3, a4 -> b4, a5 -> b5) -> (a0, a1, a2, a3, a4, a5) -> (b0, b1, b2, b3, b4, b5)
map6 (f0, f1, f2, f3, f4, f5) (a0, a1, a2, a3, a4, a5) = (f0 a0, f1 a1, f2 a2, f3 a3, f4 a4, f5 a5)


--  ===================================================  misc list  ===================================================

firstLine :: [a] -> Maybe (a, [a])
firstLine = uncons

removeLastEmpty :: [[a]] -> [[a]]
removeLastEmpty [] = []
removeLastEmpty [[]] = []
removeLastEmpty (x:xs) = x : removeLastEmpty xs


--  ===================================================  parentheses  ===================================================

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


--  ===================================================  translates  ===================================================

translate :: (Eq a) => [(a, b)] -> [a] -> [Maybe b]
translate _ [] = []
translate t (x:xs) = lookup x t : translate t xs

translateDefualt :: (Eq a) => b -> [(a, b)] -> [a] -> [b]
translateDefualt d = (map (fromMaybe d) .) . translate


--  ===================================================  basic splits  ===================================================

splitc = removeLastEmpty . split ","
splitn = removeLastEmpty . split "\n"
splitnn = removeLastEmpty . split "\n\n"
splits = removeLastEmpty . split " "
splitns = removeLastEmpty . splitMulti [" ", "\n"]


 --  ===================================================  cuts without Maybe  ===================================================

cut2u :: (Eq a) => [a] -> [a] -> ([a], [a])
cut2u = (fromJust .) . cut2
cut3u :: (Eq a) => ([a], [a]) -> [a] -> ([a], [a], [a])
cut3u = (fromJust .) . cut3
cut4u :: (Eq a) => ([a], [a], [a]) -> [a] -> ([a], [a], [a], [a])
cut4u = (fromJust .) . cut4
cut5u :: (Eq a) => ([a], [a], [a], [a]) -> [a] -> ([a], [a], [a], [a], [a])
cut5u = (fromJust .) . cut5
cut6u :: (Eq a) => ([a], [a], [a], [a], [a]) -> [a] -> ([a], [a], [a], [a], [a], [a])
cut6u = (fromJust .) . cut6


--  ===================================================  basic maps  ===================================================

mapi :: [String] -> [Int]
mapi = map read


--  ===================================================  misc  ===================================================

count :: (a -> Bool) -> [a] -> Int
count = (length .) . filter

inRange :: Ord a => a -> a -> a -> Bool
inRange mi ma x = mi <= x && x <= ma

binDigitRead :: Char -> Int
binDigitRead '0' = 0
binDigitRead '1' = 1

binToInt :: [Int] -> Int
binToInt = foldl (\n c -> 2 * n + c) 0

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetUpper = map toUpper alphabet

digits = "0123456789"


loadInpFile :: String -> IO String
loadInpFile = readFile



--  ===================================================  Advent Of Code  ===================================================

type AOCResult = Int
type AOCInput = [[Int]]



main :: IO ()
main = do
    inp <- parseInput <$> loadInpFile "inp.txt"
    print $ solveA inp
    putStrLn "  -------------------------------  "
    print $ solveB inp


parseInput :: String -> AOCInput
parseInput = map (map digitToInt) . splitn

solveA :: AOCInput -> AOCResult
solveA inp = binToInt g * binToInt e
    where
        oneCounts = map (count (== 1)) $ transpose inp
        g = map (fromEnum . (> length inp `div` 2)) oneCounts
        e = map (1 -) g

filterB :: Bool -> [[Int]] -> [Int]
filterB _ [x] = x
filterB n xs = g : filterB n (map tail (filter ((== g) . head) xs))
    where
        g = fromEnum $ (2 * count (== 1) (map head xs) >= length xs) == n

solveB :: AOCInput -> AOCResult
solveB inp = binToInt (filterB True inp) * binToInt (filterB False inp)