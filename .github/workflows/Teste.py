from main import calcular_media

def test_media_normal():
    assert calcular_media(8, 6) == 7

def test_media_invalida():
    assert calcular_media(-1, 5) == "Notas inválidas"