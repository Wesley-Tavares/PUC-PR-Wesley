from src.main import *
from unittest.mock import patch


def test_root():
    result = read_root()
    yield result
    assert result == {"message": "Hello World"}


def teste_funcao_teste():
    with patch('random.randint', return_value=12223):
        result = funcao_teste()
        yield result
    assert  result == {"teste": True, "num_aleatorio": 12223}


 def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name="Wesley", curso="Analise e dev", ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result



def teste_update_estudante_negativo():
    result = update_estudante(-5)
    yield result
    assert not result

def test_update_estudante_positivo():
    result =  update_estudante(15) > 0
    yield result
    assert not result

def test_delete_estudante_negativo():
    result =  delete_estudante(-5)
    yield result
    assert not result

def test_delete_estudante_positivo():
    result = delete_estudante(10)
    yield result
    assert not result



