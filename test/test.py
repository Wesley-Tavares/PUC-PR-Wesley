from src.main import *
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_root():
    result = await read_root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def teste_funcao_teste():
    with patch('random.randint', return_value=12223):
        result = await funcao_teste()
    assert  result == {"Verdadeiro": True, "numero_aleatório": 12223}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(name="Wesley", curso="Analise e dev", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def teste_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result
@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(15)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(10)
    assert result

@pytest.mark.asyncio
async def test_validacao_reservista_reprovado():
    result = await validacao_idade_reservista(16)
    assert result == {"mensagem": "Reprovado"}

@pytest.mark.asyncio
async def test_validacao_reservista_aprovado():
    result = await validacao_idade_reservista(19)
    assert result == {"mensagem": "Aprovado"}

@pytest.mark.asyncio
async def test_validacao_reservista():
    result = validacao_reservista()
    assert result == {"mensagem" : "Aprovado"}

@pytest.mark.asyncio
async def test_validacao_peso():
    result = await validacao_peso(140)
    assert result == {"mensagem": "Avaliação necessária"}

@pytest.mark.asyncio
async def test_impar():
    result = await impar(12)
    assert result == {"mensagem": "par"}

@pytest.mark.asyncio
async def test_avaliacao():
    result = await avaliacao(6)
    assert result == {"mensagem": "reprovado"}

