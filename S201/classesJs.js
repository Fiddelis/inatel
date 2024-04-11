class Animal {
    constructor(nome, idade, especie) {
        this.nome = nome
        this.idade = idade
        this.especie = especie
    }
    printInfo() {
        console.log(`${this.nome} tem ${this.idade} e é um ${this.especie}`)
    }
}

class Cachorro extends Animal {
    #raca
    constructor(nome, idade, especie, raca) {
        super(nome, idade, especie)
        this.#raca = raca
    } 
    printInfo() {
        console.log(`${this.nome} tem ${this.idade} e é um ${this.especie} da raça ${this.#raca}`)
    }
}

class Gato extends Animal {
    constructor(nome, idade, especie, cores) {
        super(nome, idade, especie)
        this.cores = cores
    }
    printInfo() {
        console.log(`${this.nome} tem ${this.idade} e é um ${this.especie} com as cores: ${this.cores.join(", ")}`)
    }
}

let cachorro = new Cachorro("Lupi", 8, "vira-lata", "nao sei")
let gato = new Gato("gato", 1, "teste", ["laranja", "verde"])
let animal = new Animal("Animal", 1, "testee")

cachorro.printInfo()
gato.printInfo()
animal.printInfo()