function tabuada(valor)
    print ("Tabuada do numero: " .. valor)
    for i = 1, 10 do
      local resultado = valor * i
      print(valor .. " x " .. i .. ": " .. resultado)
    end
end

print("Digite um numero: ")
local numero = tonumber(io.read())

tabuada(numero)
