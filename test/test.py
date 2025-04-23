from src.main import *
from unittest.mock import patch


def test_root():
    assert root() == {"message": "Hello World"}


def teste_funcao_teste():
    with patch('random.randint', return_value=12223):
        result = funcao_teste()
        assert  result == {"teste": True, "num_aleatorio": 12223}


 def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name="Wesley", curso="Analise e dev", ativo=False)
    assert estudante_teste == create_estudante(estudante_teste)
    ''


def teste_update_item_negativo():
    assert not update_estudante(-5) > 0

def test_update_item_positivo():
    assert update_estudante(15) > 0

def test_delete_estudante_negativo():
    assert not delete_estudante(-5)

def test_delete_estudante_positivo():
    assert delete_estudante(10)


