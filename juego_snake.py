import os
import random

# Tamaño del tablero
n = 10  # Tamaño del tablero (n x n)

# Símbolos del juego
EMPTY_CELL = '.'
SNAKE_CELL = '<'
FOOD_CELL = 'Ó'
OBSTACLE_CELL = '*'

# Direcciones de movimiento (arriba, abajo, izquierda, derecha)
DIRECTIONS = {
    'w': (-1, 0),  # Arriba
    's': (1, 0),   # Abajo
    'a': (0, -1),  # Izquierda
    'd': (0, 1)    # Derecha
}

# Función para inicializar el tablero
def create_board(size):
    return [[EMPTY_CELL for _ in range(size)] for _ in range(size)]

# Función para imprimir el tablero
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print(' '.join(row))

# Función para generar posiciones aleatorias asegurando que no estén muy cerca de otros obstáculos
def generate_random_position(board, size):
    while True:
        row = random.randint(0, size - 2)
        col = random.randint(0, size - 2)
        if can_place_obstacle(board, row, col, size):
            return row, col

# Función para verificar si se puede colocar un obstáculo de 2x2 en una posición
def can_place_obstacle(board, row, col, size):
    if row + 1 >= size or col + 1 >= size:
        return False
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            if board[r][c] != EMPTY_CELL:
                return False
    return True

# Función para colocar obstáculos de 2x2 en posiciones aleatorias
def place_obstacles(board, size, num_obstacles):
    obstacles_placed = 0
    while obstacles_placed < num_obstacles:
        row, col = generate_random_position(board, size)
        board[row][col] = OBSTACLE_CELL
        board[row][col + 1] = OBSTACLE_CELL
        board[row + 1][col] = OBSTACLE_CELL
        board[row + 1][col + 1] = OBSTACLE_CELL
        obstacles_placed += 1

# Función para colocar una manzana en una posición aleatoria
def place_food(board, size):
    while True:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        if board[row][col] == EMPTY_CELL:
            board[row][col] = FOOD_CELL
            break

# Función principal del juego
def main():
    board = create_board(n)
    
    # Generar obstáculos aleatorios
    num_obstacles = 2  # Número de obstáculos de 2x2
    place_obstacles(board, n, num_obstacles)
    
    # Colocar la manzana
    place_food(board, n)
    
    # Imprimir el tablero inicial
    print_board(board)

if __name__ == "__main__":
    main()