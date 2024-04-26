### 1
1. F - Código feito em Lua
2. V
3. V
4. V
5. F - a saida será [2 1 6 16 18 1]
---
### 2
1. V
2. F - Gato é a classe mãe de Persa
3. F - o metódo pode sim ser usado nas classes filhas
4. V
5. F - contém a variavel privada de idade e nome ja que foi herdado de gato
---
### 3
```lua
function multiplicar_vetor(valor, multiplicador)
  for i = 0, #valor do
    valor[i] = valor[i] * multiplicador
    print(valor[i] .. " ")
  end
end

local valor = {}
local i = 30
local j = 0

while j <= 30 do
  valor[j] = i
  i = i - 1
  j = j + 1
end
print("Digite um numero: ")
local multiplicador = tonumber(io.read())

multiplicar_vetor(valor, multiplicador)
```
---
### 4
```cpp
#include <iostream>
#include <string>
using namespace std;

class AnimalCorrida {
    protected:
        string nome;
        string cor;
        double velocidade;

    public:
        AnimalCorrida(string nome, string cor, double velocidade) : nome(nome), cor(cor), velocidade(velocidade) {}
};

class Cavalo : public AnimalCorrida {
    private:
        int posicao_atual = 0;

    public:
        Cavalo(string nome, string cor, double velocidade) : AnimalCorrida(nome, cor, velocidade) {}

        void mover() {
            if(posicao_atual < 200)
                posicao_atual += velocidade * 4;
            else
                cout << nome << " terminou a corrida!" << endl;
        }
};

int main() {
    Cavalo cavalo1("Cavalo 1", "Preto", 10);
    Cavalo cavalo2("Cavalo 2", "Branco", 11);
    Cavalo cavalo3("Cavalo 3", "Marrom", 12);

    for(int i = 0; i < 6; i++) {
    cavalo1.mover();
    cavalo2.mover();
    cavalo3.mover();
    }
}
```
