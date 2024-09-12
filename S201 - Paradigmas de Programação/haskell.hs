-- 1
multiplicar :: Int -> [Int] -> [Int]
multiplicar n lista = map (*n) lista

main :: IO ()
main = do
    let lista = [30, 29..1]
        listaMultiplicada = multiplicar 3 lista
        listaInversa = reverse listaMultiplicada
    print (last listaInversa)

-- 2
fatorialOuDobro :: Int -> Int
fatorialOuDobro n
  | n > 0 = fatorial n
  | otherwise = n * 2
  where
    fatorial 0 = 1
    fatorial m = m * fatorial (m - 1)

main :: IO ()
main = do
  let numero = 5
      resultado = fatorialOuDobro numero
  print resultado
