
from enum import Enum


class HouseStatus(Enum):
    SOLD = 'VENDIDA'
    FOR_SALE = 'A_VENDA'
    FOR_RENT = 'PARA_ALUGAR'
    RENTED = 'ALUGADA'