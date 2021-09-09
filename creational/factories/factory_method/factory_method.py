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


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Buscando com moto')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Buscando com moto rapida')



class VeiculoFactory(ABC):
    def __init__(self, tipo_veiculo: str):
        self.carro = self.get_carro(tipo_veiculo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo_veiculo: str) -> Veiculo:
      pass 

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZoneNorteVeiculosFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo_veiculo: str) -> Veiculo:
        if tipo_veiculo == 'luxo':
            return CarroLuxo()
        elif tipo_veiculo == 'moto':
            return Moto() 
        elif tipo_veiculo == 'moto_luxo':
            return MotoLuxo()  
        elif tipo_veiculo == 'popular':
            return CarroPopular()  

        msg_error = f'Veiculo {tipo_veiculo} não existe' 
        assert 0, msg_error
        

class ZoneSulVeiculosFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo_veiculo: str) -> Veiculo:
        if tipo_veiculo == 'popular':
            return CarroPopular()

        msg_error = f'Veiculo {tipo_veiculo} não existe' 
        assert 0, msg_error



if __name__ == '__main__':
    from random import choice

    def exemple_test_zone_sul():
        veiculos_disponiveis_zona_sul = ['popular']
        zona_norte_carro = ZoneSulVeiculosFactory(choice(veiculos_disponiveis_zona_sul))
        zona_norte_carro.buscar_cliente()

    def exemple_test_zone_north():
        veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto', 'moto_luxo']
        for _ in range(10):
            zona_norte_carro = ZoneNorteVeiculosFactory(choice(veiculos_disponiveis_zona_norte))
            zona_norte_carro.buscar_cliente()


    exemple_test_zone_sul()
    exemple_test_zone_north()