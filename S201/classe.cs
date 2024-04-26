using System;

class Cachorro {
    public string Nome { get; set; }
    public int Idade { get; set; }

    public Cachorro(string nome, int idade) {
        Nome = nome;
        Idade = idade;
    }

    public void MostrarNome() {
        Console.WriteLine("O nome do cachorro é: " + Nome);
    }

    public virtual void MostrarIdade() {
        Console.WriteLine("A idade do cachorro é: " + Idade);
    }
}

class CachorroGrande : Cachorro {
    private string tamanho;

    public CachorroGrande(string nome, int idade, string tamanho) : base(nome, idade) {
        this.tamanho = tamanho;
    }

    public override void MostrarIdade() {
        Console.WriteLine("A idade do cachorro grande é: " + Idade);
    }
}

class CachorroPequeno : Cachorro
{
    public CachorroPequeno(string nome, int idade) : base(nome, idade) {
    }

    public override void MostrarIdade() {
        Console.WriteLine("A idade do cachorro pequeno é: " + Idade);
    }
}

class Program {
    static void Main(string[] args) {
        Cachorro cachorro = new Cachorro("Bob", 3);
        CachorroGrande cachorroGrande = new CachorroGrande("Rex", 5, "Grande");
        CachorroPequeno cachorroPequeno = new CachorroPequeno("Luna", 2);

        cachorro.MostrarNome();
        cachorro.MostrarIdade();

        cachorroGrande.MostrarNome();
        cachorroGrande.MostrarIdade();

        cachorroPequeno.MostrarNome();
        cachorroPequeno.MostrarIdade();
    }
}
