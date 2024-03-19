from enum import Enum


class PaymentStatus(Enum):
    PAYED = 'PAGO'
    NOT_PAYED = 'AGUARDANDO_PAGAMENTO'
