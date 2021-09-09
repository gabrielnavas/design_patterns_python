"""

Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.
    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).
    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory
Nessa aula:

Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID

"""
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: 
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Buscando com carro de luxo')



class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Buscando com carro popular')


class MotoRapida(Veiculo):
    def buscar_cliente(self) -> None:
        print('Buscando com moto rapida')



class VeiculoFactory:

    def __init__(self, tipo_carro: str):
        self.carro = self.get_carro(tipo_carro)

    @staticmethod
    def get_carro(tipo_carro: str) -> Veiculo:
        if tipo_carro == 'luxo':
            return CarroLuxo()
        elif tipo_carro == 'popular':
            return CarroPopular()  
        elif tipo_carro == 'moto_rapida':
            return MotoRapida()    
        assert 0, 'Veiculo não existe'  

    def buscar_cliente(self):
        self.carro.buscar_cliente()

if __name__ == '__main__':
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'moto_rapida']

    for _ in range(10):
        tipo_carro = choice(carros_disponiveis)
        carro = VeiculoFactory(tipo_carro)
        carro.buscar_cliente()