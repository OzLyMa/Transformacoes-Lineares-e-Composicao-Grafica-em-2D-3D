import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
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

def rotacao(vertices, theta_graus):
    theta = np.radians(theta_graus)
    c, s = np.cos(theta), np.sin(theta)

    matriz = np.array([
        [c, -s],
        [s,  c]
    ])
    return matriz @ vertices

def escala(vertices, sx, sy):
    matriz = np.array([
        [sx, 0],
        [0, sy]
    ])
    return matriz @ vertices

def translacao(vertices, tx, ty):
    matriz = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0,  1]
    ])
    vertices_h = np.vstack((
        vertices,
        np.ones((1, vertices.shape[1]))
    ))
    return (matriz @ vertices_h)[:2, :]

def cisalhamento_3d(vertices, kxy=0, kxz=0, kyx=0, kyz=0, kzx=0, kzy=0):
    matriz = np.array([
        [1,   kxy, kxz],
        [kyx, 1,   kyz],
        [kzx, kzy, 1]
    ])
    return matriz @ vertices

def rotacao_3d(vertices, theta_graus, eixo='z'):
    theta = np.radians(theta_graus)
    c, s = np.cos(theta), np.sin(theta)

    if eixo.lower() == 'x':
        matriz = np.array([
            [1, 0,  0],
            [0, c, -s],
            [0, s,  c]
        ])
    elif eixo.lower() == 'y':
        matriz = np.array([
            [ c, 0, s],
            [ 0, 1, 0],
            [-s, 0, c]
        ])
    else:
        matriz = np.array([
            [c, -s, 0],
            [s,  c, 0],
            [0,  0, 1]
        ])
    return matriz @ vertices

def escala_3d(vertices, sx, sy, sz):
    matriz = np.array([
        [sx, 0,  0],
        [0,  sy, 0],
        [0,  0,  sz]
    ])
    return matriz @ vertices

def translacao_3d(vertices, tx, ty, tz):
    matriz = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0,  1]
    ])
    vertices_h = np.vstack((
        vertices,
        np.ones((1, vertices.shape[1]))
    ))
    return (matriz @ vertices_h)[:3, :]

def _faces_cubo(pts):
    return [
        [pts[0], pts[1], pts[2], pts[3]],
        [pts[4], pts[5], pts[6], pts[7]],
        [pts[0], pts[1], pts[5], pts[4]],
        [pts[2], pts[3], pts[7], pts[6]],
        [pts[1], pts[2], pts[6], pts[5]],
        [pts[0], pts[3], pts[7], pts[4]]
    ]

def executar_3d():
    print('Digite as Coordenadas do seu paralelepípedo/cubo (8 vértices):')
    x_one = float(input('X1: '))
    y_one = float(input('Y1: '))
    z_one = float(input('Z1: '))
    x_two = float(input('X2: '))
    y_two = float(input('Y2: '))
    z_two = float(input('Z2: '))
    x_three = float(input('X3: '))
    y_three = float(input('Y3: '))
    z_three = float(input('Z3: '))
    x_four = float(input('X4: '))
    y_four = float(input('Y4: '))
    z_four = float(input('Z4: '))
    x_five = float(input('X5: '))
    y_five = float(input('Y5: '))
    z_five = float(input('Z5: '))
    x_six = float(input('X6: '))
    y_six = float(input('Y6: '))
    z_six = float(input('Z6: '))
    x_seven = float(input('X7: '))
    y_seven = float(input('Y7: '))
    z_seven = float(input('Z7: '))
    x_eight = float(input('X8: '))
    y_eight = float(input('Y8: '))
    z_eight = float(input('Z8: '))

    vertices = np.array([
        [x_one, y_one, z_one],
        [x_two, y_two, z_two],
        [x_three, y_three, z_three],
        [x_four, y_four, z_four],
        [x_five, y_five, z_five],
        [x_six, y_six, z_six],
        [x_seven, y_seven, z_seven],
        [x_eight, y_eight, z_eight]
    ]).T
    matriz_transformada = vertices.copy()

    while True:
        print('Qual operação 3D você deseja fazer?\n1.Cisalhamento\n2.Rotação\n3.Escala\n4.Translação\n0.Finalizar')
        cod_3d = int(input())

        match cod_3d:
            case 0:
                break

            case 1:
                kxy = float(input('Digite o fator de cisalhamento X em Y (em porcentagem): ')) / 100
                kxz = float(input('Digite o fator de cisalhamento X em Z (em porcentagem): ')) / 100
                kyx = float(input('Digite o fator de cisalhamento Y em X (em porcentagem): ')) / 100
                kyz = float(input('Digite o fator de cisalhamento Y em Z (em porcentagem): ')) / 100
                kzx = float(input('Digite o fator de cisalhamento Z em X (em porcentagem): ')) / 100
                kzy = float(input('Digite o fator de cisalhamento Z em Y (em porcentagem): ')) / 100
                matriz_transformada = cisalhamento_3d(matriz_transformada, kxy, kxz, kyx, kyz, kzx, kzy)

            case 2:
                eixo = input('Digite o eixo de rotação (x, y ou z): ').strip()
                angulo = float(input('Digite o ângulo de rotação em graus: '))
                matriz_transformada = rotacao_3d(matriz_transformada, angulo, eixo)

            case 3:
                sx = float(input('Digite a escala no eixo X (em porcentagem): '))
                sy = float(input('Digite a escala no eixo Y (em porcentagem): '))
                sz = float(input('Digite a escala no eixo Z (em porcentagem): '))
                matriz_transformada = escala_3d(matriz_transformada, sx / 100, sy / 100, sz / 100)

            case 4:
                tx = float(input('Digite o deslocamento em X: '))
                ty = float(input('Digite o deslocamento em Y: '))
                tz = float(input('Digite o deslocamento em Z: '))
                matriz_transformada = translacao_3d(matriz_transformada, tx, ty, tz)

            case _:
                print('Valor invalido')
                continue
                
    figura_trans = matriz_transformada[:3, :].T
    figura_inicial = vertices[:3, :].T

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')

    cubo_transformado = Poly3DCollection(
        _faces_cubo(figura_trans), facecolors='skyblue', edgecolors='black', linewidths=0.8, alpha=0.7
    )
    cubo_inicial = Poly3DCollection(
        _faces_cubo(figura_inicial), facecolors='red', edgecolors='black', linewidths=0.8, alpha=0.7
    )

    ax1.add_collection3d(cubo_transformado)
    ax1.set_xlim([-5, 5])
    ax1.set_ylim([-5, 5])
    ax1.set_zlim([-5, 5])
    ax1.set_title('Figura pós transformação linear 3D')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')

    ax2.add_collection3d(cubo_inicial)
    ax2.set_xlim([-5, 5])
    ax2.set_ylim([-5, 5])
    ax2.set_zlim([-5, 5])
    ax2.set_title('Figura pré transformação linear 3D')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')

    plt.suptitle(
        'Transformações lineares 3D'
    )
    plt.tight_layout()
    plt.show()

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
    
    matriz_transformada = vertices.copy()

    while True:
        print('Você deseja fazer qual operação?\n1.Cisalhamento Horizontal\n2.Cisalhamento Vertical\n3.Rotação\n4.Escala\n5.Translação\n6.Operações em 3D\n0.Finalizar')        
        
        cod = int(input())

        match cod:
            case 0:
                break

            case 1:
                k = float(input('Digite o fator de cisalhamento (em porcentagem): '))
                matriz_transformada = cisalhamento_horizontal(matriz_transformada, (k / 100))

            case 2:
                k = float(input('Digite o fator de cisalhamento (em porcentagem): '))
                matriz_transformada = cisalhamento_vertical(matriz_transformada, (k / 100))

            case 3:
                angulo = float(input('Digite o ângulo de rotação em graus: '))
                matriz_transformada = rotacao(matriz_transformada, angulo)

            case 4:
                sx = float(input('Digite a escala no eixo X (em porcentagem): '))
                sy = float(input('Digite a escala no eixo Y (em porcentagem): '))
                matriz_transformada = escala(matriz_transformada, sx / 100, sy / 100)

            case 5:
                tx = float(input('Digite o deslocamento em X: '))
                ty = float(input('Digite o deslocamento em Y: '))
                matriz_transformada = translacao(matriz_transformada, tx, ty)

            case 6:
                executar_3d()
                return
        
            case _:
                print('Valor invalido')
                continue
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

if __name__ == '__main__':
    main()
