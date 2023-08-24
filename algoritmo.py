from classes import *

hotel = Hotel("Enchanted Echo Resort")

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
            print("+------------------------------+ \n | BEM VINDO(A) AO ENCHANTED ECHO RESORT! | \n +------------------------------+ \n [1] Descrição do Hotel \n [2] Apartamentos disponíveis \n [3] Realizar reserva \n [4] Cancelar reserva \n [5] Serviços disponíveis \n [6] Sair")

        except ValueError:
            print('Problema: Digito não correspondente/ Opção Indisponível')
