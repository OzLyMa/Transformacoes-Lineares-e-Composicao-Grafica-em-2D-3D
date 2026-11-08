import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


# ==========================================
# FUNÇÕES 2D (Figuras Geométricas Preenchidas)
# ==========================================
def criar_objeto_2d_padrao():
  # Modelo de um polígono geométrico 2D em coordenadas homogêneas [x, y, 1] (3xN)
  vertices = np.array(
      [[0, 0, 1], [2, 0, 1], [2, 1, 1], [3, 1, 1], [1, 3, 1], [-1, 1, 1], [0, 1, 1]]
  ).T
  return vertices


def matriz_rotacao_2d(theta_graus):
  theta = np.radians(theta_graus)
  c, s = np.cos(theta), np.sin(theta)
  return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def matriz_escala_2d(sx, sy):
  return np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])


def matriz_cisalhamento_2d(shx, shy):
  return np.array([[1, shx, 0], [shy, 1, 0], [0, 0, 1]])


# ==========================================
# FUNÇÕES 3D (Objetos Sólidos Preenchidos)
# ==========================================
def criar_cubo_3d():
  # 8 vértices de um cubo em coordenadas homogêneas [x, y, z, 1] (4x8)
  vertices = np.array([
      [0, 0, 0, 1],
      [1, 0, 0, 1],
      [1, 1, 0, 1],
      [0, 1, 0, 1],
      [0, 0, 1, 1],
      [1, 0, 1, 1],
      [1, 1, 1, 1],
      [0, 1, 1, 1],
  ]).T

  # Definição das 6 faces do cubo por índices de vértices
  faces = [
      [0, 1, 2, 3],  # Base inferior
      [4, 5, 6, 7],  # Base superior
      [0, 1, 5, 4],  # Face frontal
      [2, 3, 7, 6],  # Face traseira
      [1, 2, 6, 5],  # Face lateral direita
      [0, 3, 7, 4],  # Face lateral esquerda
  ]
  return vertices, faces


def matriz_rotacao_3d(eixo, theta_graus):
  theta = np.radians(theta_graus)
  c, s = np.cos(theta), np.sin(theta)
  if eixo == 'x':
    return np.array([[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]])
  elif eixo == 'y':
    return np.array([[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]])
  elif eixo == 'z':
    return np.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
  return np.eye(4)


def matriz_escala_3d(sx, sy, sz):
  return np.array([[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]])


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================
def main():
  print('==================================================')
  print(' TEMA 4: Transformações e Composição (2D/3D)')
  print(' Figuras 2D Preenchidas & Objetos Sólidos 3D')
  print('==================================================')

  dimensao = input(
      'Deseja trabalhar em ambiente 2D ou 3D? (Digite 2 ou 3): '
  ).strip()

  if dimensao == '2':
    # --- FLUXO 2D ---
    objeto_inicial = criar_objeto_2d_padrao()
    m_composta = np.eye(3)
    relatorio = []

    while True:
      print('\n--- Menu de Transformações 2D ---')
      print('1. Rotação')
      print('2. Escala')
      print('3. Cisalhamento')
      print('4. Finalizar e Renderizar Figura 2D')
      opcao = input('Escolha uma opção (1-4): ').strip()

      if opcao == '1':
        ang = float(input('Ângulo de rotação (graus): '))
        m_trans = matriz_rotacao_2d(ang)
        relatorio.append(f'Rotação 2D de {ang}°')
        m_composta = m_trans @ m_composta
      elif opcao == '2':
        sx = float(input('Fator escala X (sx): '))
        sy = float(input('Fator escala Y (sy): '))
        m_trans = matriz_escala_2d(sx, sy)
        relatorio.append(f'Escala 2D (sx={sx}, sy={sy})')
        m_composta = m_trans @ m_composta
      elif opcao == '3':
        shx = float(input('Cisalhamento X (shx): '))
        shy = float(input('Cisalhamento Y (shy): '))
        m_trans = matriz_cisalhamento_2d(shx, shy)
        relatorio.append(f'Cisalhamento 2D (shx={shx}, shy={shy})')
        m_composta = m_trans @ m_composta
      elif opcao == '4':
        break
      else:
        print('Opção inválida!')

    objeto_final = m_composta @ objeto_inicial

    # Relatório 2D
    print('\n--- RELATÓRIO DO AMBIENTE 2D ---')
    for idx, t in enumerate(relatorio, 1):
      print(f'  {idx}. {t}')
    print('\nMatriz Composta Final (3x3):\n', m_composta)
    print('\nCoordenadas Finais dos Vértices:\n', objeto_final)

    # Plotagem 2D com Figuras Geométricas Preenchidas
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    pts_ini = objeto_inicial[:2, :].T
    pts_fin = objeto_final[:2, :].T

    poly_ini = Polygon(
        pts_ini, closed=True, facecolor='skyblue', edgecolor='blue', alpha=0.7
    )
    poly_fin = Polygon(
        pts_fin, closed=True, facecolor='salmon', edgecolor='red', alpha=0.7
    )

    ax1.add_patch(poly_ini)
    ax1.set_xlim([-4, 4])
    ax1.set_ylim([-4, 4])
    ax1.axhline(0, color='black', linewidth=0.8, linestyle='--')
    ax1.axvline(0, color='black', linewidth=0.8, linestyle='--')
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.set_aspect('equal')
    ax1.set_title('Estado Inicial (Figura 2D Preenchida)')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')

    ax2.add_patch(poly_fin)
    ax2.set_xlim([-6, 6])
    ax2.set_ylim([-6, 6])
    ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')
    ax2.axvline(0, color='black', linewidth=0.8, linestyle='--')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.set_aspect('equal')
    ax2.set_title('Estado Final Transformado (Figura 2D Preenchida)')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')

    plt.suptitle(
        'Transformações Lineares e Composição em 2D (Figuras Geométricas'
        ' Preenchidas)'
    )
    plt.tight_layout()
    plt.show()

  elif dimensao == '3':
    # --- FLUXO 3D ---
    objeto_inicial, faces = criar_cubo_3d()
    m_composta = np.eye(4)
    relatorio = []

    while True:
      print('\n--- Menu de Transformações 3D ---')
      print('1. Rotação (Eixo X, Y ou Z)')
      print('2. Escala (sx, sy, sz)')
      print('3. Finalizar e Renderizar Objeto Sólido 3D')
      opcao = input('Escolha uma opção (1-3): ').strip()

      if opcao == '1':
        eixo = input('Eixo de rotação (x, y ou z): ').lower()
        ang = float(input('Ângulo de rotação (graus): '))
        m_trans = matriz_rotacao_3d(eixo, ang)
        relatorio.append(f'Rotação 3D no eixo {eixo.upper()} de {ang}°')
        m_composta = m_trans @ m_composta
      elif opcao == '2':
        sx = float(input('Escala X (sx): '))
        sy = float(input('Escala Y (sy): '))
        sz = float(input('Escala Z (sz): '))
        m_trans = matriz_escala_3d(sx, sy, sz)
        relatorio.append(f'Escala 3D (sx={sx}, sy={sy}, sz={sz})')
        m_composta = m_trans @ m_composta
      elif opcao == '3':
        break
      else:
        print('Opção inválida!')

    objeto_final = m_composta @ objeto_inicial

    # Relatório 3D
    print('\n--- RELATÓRIO DO AMBIENTE 3D SÓLIDO ---')
    for idx, t in enumerate(relatorio, 1):
      print(f'  {idx}. {t}')
    print('\nMatriz Composta Final (4x4):\n', m_composta)

    # Plotagem 3D Sólida
    fig = plt.figure(figsize=(12, 6))

    # Estado Inicial Sólido
    ax1 = fig.add_subplot(121, projection='3d')
    poly_verts_ini = [
        [objeto_inicial[:3, idx] for idx in face] for face in faces
    ]
    collection_ini = Poly3DCollection(
        poly_verts_ini,
        alpha=0.6,
        facecolors='cyan',
        edgecolors='black',
        linewidths=1.2,
    )
    ax1.add_collection3d(collection_ini)
    ax1.set_xlim([-2, 2])
    ax1.set_ylim([-2, 2])
    ax1.set_zlim([-2, 2])
    ax1.set_title('Estado Inicial (Objeto Sólido 3D)')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')

    # Estado Final Sólido
    ax2 = fig.add_subplot(122, projection='3d')
    poly_verts_fin = [
        [objeto_final[:3, idx] for idx in face] for face in faces
    ]
    collection_fin = Poly3DCollection(
        poly_verts_fin,
        alpha=0.6,
        facecolors='tomato',
        edgecolors='black',
        linewidths=1.2,
    )
    ax2.add_collection3d(collection_fin)
    ax2.set_xlim([-3, 3])
    ax2.set_ylim([-3, 3])
    ax2.set_zlim([-3, 3])
    ax2.set_title('Estado Final Transformado (Objeto Sólido 3D)')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')

    plt.suptitle(
        'Transformações Lineares e Composição em 3D (Objetos Sólidos)'
    )
    plt.tight_layout()
    plt.show()

  else:
    print('Opção inválida! Execute novamente e digite 2 ou 3.')


if __name__ == '__main__':
  main()