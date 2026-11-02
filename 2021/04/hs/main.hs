{-# LANGUAGE TupleSections #-}

import Data.List (findIndices, tails, isPrefixOf, uncons, singleton, lookup, findIndex, elemIndex, transpose)
import Data.Bifunctor (Bifunctor(), first, second, bimap)
import Data.Maybe (fromMaybe, fromJust, isNothing, isJust, catMaybes)
import Data.Char (toUpper, toLower)
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


digitToInt :: Char -> Int
digitToInt = fromJust . flip elemIndex (digits ++ alphabet) . toLower

binToInt :: [Int] -> Int
binToInt = foldl (\n c -> 2 * n + c) 0

binToIntStr :: String -> Int
binToIntStr = binToInt . map digitToInt

stringToDigits :: String -> [Int]
stringToDigits = map digitToInt

digitsToInt :: Int -> [Int] -> Int
digitsToInt base = foldl (\n c -> base * n + c) 0

intToDigits :: Int -> Int -> [Int]
intToDigits base = reverse . intToDigitsRev
    where
        intToDigitsRev n = let (d, m) = n `divMod` base in d : intToDigitsRev m

digitsToString :: [Int] -> String
digitsToString = concatMap show

-- intToDigits :: Int -> Int -> 


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetUpper = map toUpper alphabet

digits = "0123456789"


loadInpFile :: String -> IO String
loadInpFile = readFile



--  ===================================================  Advent Of Code  ===================================================

type AOCResult = Int
type AOCInput = ([Int], [[[Int]]])



main :: IO ()
main = do
    inp <- parseInput <$> loadInpFile "inp.txt"
    print $ solveA inp
    putStrLn "  -------------------------------  "
    print $ solveB inp


parseInput :: String -> AOCInput
parseInput = bimap (mapi . splitc) (map (map (mapi . filter (not . null) . splits) . splitn)) . fromJust . firstLine . splitnn

loop_ :: Int -> [Int] -> [([[Maybe Int]], Bool)] -> Int
loop_ endCount [] boards = traceShow boards $ error ""
loop_ endCount (n : ns) boards = if count snd newBoards >= endCount then score * n else loop_ endCount ns newBoards
    where
        checkBoard board = checkBoard_ board || checkBoard_ (transpose board)
        checkBoard_ :: [[Maybe Int]] -> Bool
        checkBoard_ = any (all isNothing)

        updateBoard (board, True) = (board, True)
        updateBoard (board, False) = let newBoard = updateBoard_ board in (newBoard, checkBoard newBoard)
        updateBoard_ = map (map updateEl)
        updateEl Nothing = Nothing
        updateEl (Just x) = if x == n then Nothing else Just x

        newBoards = map updateBoard boards

        score = calculateScore $ snd $ head $ filter (uncurry (/=) . bimap snd snd) $ zip boards newBoards
        calculateScore = sum . map (sum . catMaybes) . fst

loop :: Int -> [Int] -> [[[Int]]] -> Int
loop e ns boards = loop_ e ns $ map ((, False) . map (map Just)) boards

solveA :: AOCInput -> AOCResult
solveA = uncurry $ loop 1

solveB :: AOCInput -> AOCResult
solveB (ns, boards) = loop (length boards) ns boards