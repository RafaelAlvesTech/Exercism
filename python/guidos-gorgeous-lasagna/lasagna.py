""" Módulo controle de tempo para assar lasanha."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(tempo_de_preparo_minutos: int):
    '''
       Retorna o tempo restante para assar a lasanha.
    '''
    return EXPECTED_BAKE_TIME - tempo_de_preparo_minutos

def preparation_time_in_minutes(number_of_layers: int):
    '''
    Retorna o tempo necessário para preparar a lasanha dada a quantidade de camadas.
    '''
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    '''
    Retorna o tempo total necessário.
    '''
    return preparation_time_in_minutes(number_of_layers) + (EXPECTED_BAKE_TIME - bake_time_remaining(elapsed_bake_time))
