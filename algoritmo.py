from classes import *
import os

hotel = Hotel("Enchanted Echo Resort")

def descrição_hotel():
    print("Nosso hotel: \n \n Bem-vindo ao Enchanted Echo Resort, onde a magia encontra o conforto. \n Situado em um cenário deslumbrante, nosso resort oferece uma experiência encantadora que combina luxo com natureza. \n Cada detalhe do nosso espaço, desde a arquitetura até os jardins bem cuidados, é projetado para criar uma atmosfera mágica e relaxante. \n Nossos quartos e suítes foram concebidos para serem verdadeiros refúgios, com decoração elegante e conforto incomparável. \n As vistas panorâmicas da natureza exuberante que nos rodeia são um espetáculo à parte. \n O Enchanted Echo Resort é o lugar perfeito para se desconectar do mundo e se conectar com a serenidade da natureza.")

def listar_apartamentos():
    quartos_disponiveis = hotel.listar_quartos_disponiveis()
    for quarto in quartos_disponiveis:
        print(quarto.obter_detalhes_quarto())


for numero_quarto in range(1, 5):
    hotel.adicionar_quarto(ApartamentoSimples(numero_quarto))
    hotel.adicionar_quarto(ApartamentoSimplesCasal(numero_quarto))
    hotel.adicionar_quarto(ApartamentoDuplo(numero_quarto))
    hotel.adicionar_quarto(ApartamentoDuploCasal(numero_quarto))
    hotel.adicionar_quarto(ApartamentoLuxo(numero_quarto))
    hotel.adicionar_quarto(ApartamentoMaster(numero_quarto))

def reserva(Hotel):
    nome_cliente: input("Digite seu nome: ")
    quant_dias : int(input("Tempo de hospedagem: "))

    quarto_encontrado = hotel.adicionar_reserva(nome_cliente)
    if  quarto_encontrado:
        quarto_ocupado = remove.numero_quarto
        valor_quarto * quant_dias == valor_total
        print(f" Olá! {nome_cliente}! Você concluiu sua reserva por R${valor_total}, tenha uma boa estadia!!")
    else:
        print("Quartos indisponiveis")


def main():
    while True:
        try:
            print("+------------------------------------------+ \n | BEM VINDO(A) AO ENCHANTED ECHO RESORT! | \n+------------------------------------------+ \n [1] Descrição do Hotel \n [2] Apartamentos disponíveis \n [3] Realizar reserva \n [4] Cancelar reserva \n [5] Serviços disponíveis \n [6] Sair")

            escolha = int(input("> "))

            if escolha == 1:
                os.system("cls")
                descrição_hotel()
                os.system("pause")
                os.system("cls")

            elif escolha == 2:
                os.system("cls")
                listar_apartamentos()
                os.system("pause")
                os.system("cls")

        except ValueError:
            print('Problema: Digito não correspondente/ Opção Indisponível')
