from classes import *

hotel = Hotel("Enchanted Echo Resort")

for numero_quarto in range(1, 5):
    hotel.adicionar_quarto(ApartamentoSimples(numero_quarto))
    hotel.adicionar_quarto(ApartamentoSimplesCasal(numero_quarto))
    hotel.adicionar_quarto(ApartamentoDuplo(numero_quarto))
    hotel.adicionar_quarto(ApartamentoDuploCasal(numero_quarto))
    hotel.adicionar_quarto(ApartamentoLuxo(numero_quarto))
    hotel.adicionar_quarto(ApartamentoMaster(numero_quarto))
