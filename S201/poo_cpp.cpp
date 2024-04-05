#include <iostream>
#include <string>

using namespace std;

class Pessoa {
protected:
    string nome;
    int idade;

public:
    Pessoa(string nome, int idade) : nome(nome), idade(idade) {}

    void imprimirNome() {
        cout << "O nome é: " << nome << endl;
    }
};

class Professor : public Pessoa {
public:
    Professor(string nome, int idade) : Pessoa(nome, idade) {}

    void idade() {
        cout << "A idade do professor é: " << idade << " anos" << endl;
    }
};

class Aluno : public Pessoa {
private:
    string matricula;

public:
    Aluno(string nome, int idade, string matricula) : Pessoa(nome, idade), matricula(matricula) {}

    void idade() {
        cout << "A idade do aluno é: " << idade << " anos" << endl;
    }
};

int main() {
    Pessoa pessoa("Fulano", 30);
    Professor professor("Prof. Silva", 45);
    Aluno aluno("João", 20, "2024001");

    pessoa.imprimirNome();
    cout << endl;
    professor.imprimirNome();
    professor.idade();
    cout << endl;
    aluno.imprimirNome();
    aluno.idade();

    return 0;
}
