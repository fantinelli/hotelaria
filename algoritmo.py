from classes import *

hotel = Hotel("Enchanted Echo Resort")

def descrição_hotel():
    print("Nosso hotel: \n \n Bem-vindo ao Enchanted Echo Resort, onde a magia encontra o conforto. \n Situado em um cenário deslumbrante, nosso resort oferece uma experiência encantadora que combina luxo com natureza. \n Cada detalhe do nosso espaço, desde a arquitetura até os jardins bem cuidados, é projetado para criar uma atmosfera mágica e relaxante. \n Nossos quartos e suítes foram concebidos para serem verdadeiros refúgios, com decoração elegante e conforto incomparável. \n As vistas panorâmicas da natureza exuberante que nos rodeia são um espetáculo à parte. \n O Enchanted Echo Resort é o lugar perfeito para se desconectar do mundo e se conectar com a serenidade da natureza.")

for numero_quarto in range(1, 5):
    hotel.adicionar_quarto(ApartamentoSimples(numero_quarto))
    hotel.adicionar_quarto(ApartamentoSimplesCasal(numero_quarto))
    hotel.adicionar_quarto(ApartamentoDuplo(numero_quarto))
    hotel.adicionar_quarto(ApartamentoDuploCasal(numero_quarto))
    hotel.adicionar_quarto(ApartamentoLuxo(numero_quarto))
    hotel.adicionar_quarto(ApartamentoMaster(numero_quarto))

def main():
    while True:
        try:
            print("+------------------------------------------+ \n | BEM VINDO(A) AO ENCHANTED ECHO RESORT! | \n+------------------------------------------+ \n [1] Descrição do Hotel \n [2] Apartamentos disponíveis \n [3] Realizar reserva \n [4] Cancelar reserva \n [5] Serviços disponíveis \n [6] Sair")

            escolha = int(input("> "))

            if escolha == 1:
                descrição_hotel()

        except ValueError:
            print('Problema: Digito não correspondente/ Opção Indisponível')
