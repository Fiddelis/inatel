class Carro
  def initialize(marca)
    @marca = marca
  end

  def descrever
    puts "O marca do carro é #{@marca}"
  end
end

class CarroEsportivo < Carro
  def initialize(marca, potencia)
    super(marca)
    @potencia = potencia
  end

  def descrever
    puts "O carro esportivo é da marca #{@marca} e tem uma potência de #{@potencia}"
  end
end

class CarroSedan < Carro
  def initialize(marca, potencia)
    super(marca)
    @potencia = potencia
  end

  def descrever
    puts "O carro esportivo é da marca #{@marca} e tem uma potência de #{@potencia}"
  end
end

carro = Carro.new('Ford')
carroEsportivo = CarroEsportivo.new('Ferrari', '1000')
carroSedan = CarroSedan.new('Honda', '2000')

carro.descrever()
carroEsportivo.descrever()
carroSedan.descrever()