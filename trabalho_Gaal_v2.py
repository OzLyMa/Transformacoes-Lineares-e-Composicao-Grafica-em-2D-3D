import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

def cisalhamento_horizontal(vertices, k):
    m_composta = np.array([
        [1, k],
        [0, 1]
    ])
    vertices_trans = m_composta @ vertices
    return vertices_trans

def cisalhamento_vertical(vertices, k):
    m_composta = np.array([
        [1, 0],
        [k, 1]
    ])
    vertices_trans = m_composta @ vertices
    return vertices_trans


def main():
    print('Digite as Coordenadas da seu quadrilátero:')
    x_one = float(input('X1: '))
    y_one = float(input('Y1: '))
    x_two = float(input('X2: '))
    y_two = float(input('Y2: '))
    x_three = float(input('X3: '))
    y_three = float(input('Y3: '))
    x_four = float(input('X4: '))
    y_four = float(input('Y4: '))

    vertices = np.array([[x_one, y_one], [x_two, y_two], [x_three, y_three], [x_four, y_four]]).T

    print('Você deseja fazer qual operação?\n1.Cisalhamento Horizontal\n2.Cisalhamento Vertical')
    cod = int(input())
    match cod:
        case 1:
            k = float(input('Digite o fator de cisalhamento (em porcentagem): '))
            matriz_transformada = cisalhamento_horizontal(vertices, (k / 100))
        case 2:
            k = float(input('Digite o fator de cisalhamento (em porcentagem): '))
            matriz_transformada = cisalhamento_vertical(vertices, (k / 100))
        case _:
            print('Valor invalido')


    figura_trans = matriz_transformada[:2, :].T
    figura_inicial = vertices[:2, :].T

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(6, 6))

    poligono_transformado = Polygon(
        figura_trans, closed=True, facecolor='skyblue', edgecolor='black', alpha=0.7
    )
    poligono_inicial = Polygon(
        figura_inicial, closed=True, facecolor='red', edgecolor='black', alpha=0.7
    )

    ax1.add_patch(poligono_transformado)
    ax1.set_xlim([-5, 5])
    ax1.set_ylim([-5, 5])
    ax1.axhline(0, color='black', linewidth=0.8, linestyle='--')
    ax1.axvline(0, color='black', linewidth=0.8, linestyle='--')
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.set_aspect('equal')
    ax1.set_title('Figura pós transformação linear')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')

    ax2.add_patch(poligono_inicial)
    ax2.set_xlim([-5, 5])
    ax2.set_ylim([-5, 5])
    ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')
    ax2.axvline(0, color='black', linewidth=0.8, linestyle='--')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.set_aspect('equal')
    ax2.set_title('Figura pré transformação linear')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')

    plt.suptitle(
        'Transformações lineares 2D'
    )
    plt.tight_layout()
    plt.show()


# Executa a função principal
if __name__ == '__main__':
    main()