from PPlay.window import *
from PPlay.sprite import *


def criar(janela):
    lista_chao = []

    chao = Sprite("images/fase2/chao_azul_pequeno.png")
    chao.set_position(0,janela.height - chao.height+15)
    lista_chao.append(chao)

    chao = Sprite("images/fase2/chao_azul_pequeno.png")
    chao.set_position(108,janela.height - chao.height+15)
    lista_chao.append(chao)

    chao = Sprite("images/fase2/chao_azul_pequeno.png")
    chao.set_position(216,janela.height - chao.height+15)
    lista_chao.append(chao)

    chao = Sprite("images/fase2/chao_azul_pequeno.png")
    chao.set_position(324,janela.height - chao.height+15)
    lista_chao.append(chao)
    
    chao = Sprite("images/fase2/chao_azul_medio.png")
    chao.set_position(432,janela.height - chao.height+15)
    lista_chao.append(chao)

    chao = Sprite("images/fase2/chao_azul_grande.png")
    chao.set_position(587,janela.height - chao.height+15)
    lista_chao.append(chao)
    
    return lista_chao