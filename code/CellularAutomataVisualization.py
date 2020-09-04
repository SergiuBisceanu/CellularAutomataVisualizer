# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:38:54 2020

@author: spiku
"""

import pygame 
import numpy as np
import tkinter as tk
import math
import RuleGUI as gui

gui.root.mainloop()
RULES = list(gui.rules[0])
RULES = [int(x) for x in RULES[0:8]]

def f(a, center, left, right, rules = RULES):
    if left == 1 and right == 1 and center == 1:
        return rules[0]
    elif left == 1 and right == 0 and center == 1:
        return rules[1]
    elif left == 1 and right == 1 and center == 0:
        return rules[2]
    elif left == 1 and right == 0 and center == 0:
        return rules[3]
    elif left == 0 and right == 1 and center == 1:
        return rules[4]
    elif left == 0 and right == 0 and center == 1:
        return rules[5]
    elif left == 0 and right == 1 and center == 0:
        return rules[6]
    elif left == 0 and right == 0 and center == 0:
        return rules[7]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

WIN_DIM = 1000
ROWS = 250
COLS = 2 * ROWS + 1
NSTATE = 1
DIM = WIN_DIM/2 // ROWS
WIN = pygame.display.set_mode((WIN_DIM, WIN_DIM//2))
pygame.display.set_caption("Cellular Automata Visualization")

class Cell(object):
    def __init__(self, row, col, cell_dim, total_rows, state):
        self.row = row
        self.col = col
        self.x = row * cell_dim
        self.y = col * cell_dim
        self.state = state
        self.cell_dim = cell_dim
        self.total_rows = total_rows
    
    def get_pos(self):
        return (self.row, self.col)
    
    def draw(self, win):
        pygame.draw.rect(win, self.state, (self.x, self.y, self.cell_dim, self.cell_dim))

# n is the number of rows
def solve_matrix(n, m, num_state):   
    MATRIX = np.zeros((n, m))
    if m%2 == 1:
        index = math.floor(m/2) 
    elif m%2 == 0:
        index = math.floor(m/2) - 1
    MATRIX[0, index] = num_state
    cnt = 1
    for i in range(1, n, +1):
        for j in range(0, cnt+1):
             MATRIX[i, index+j] = f(MATRIX, MATRIX[i-1, index+j], MATRIX[i-1, index+j-1], MATRIX[i-1, index+j+1])
             MATRIX[i, index-j] = f(MATRIX, MATRIX[i-1, index-j], MATRIX[i-1, index-j-1], MATRIX[i-1, index-j+1])
        cnt += 1
    return MATRIX

def interpret_matrix(matrix):
    MATRIX = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            if matrix[j, i] == 0:
                row.append(Cell(i, j, DIM, COLS, WHITE))
            if matrix[j, i] == 1:
                row.append(Cell(i, j, DIM, COLS, BLACK))
        MATRIX.append(row)     
    return MATRIX

def draw_matrix(window, cols, win_dim):
    for i in range(ROWS):
        pygame.draw.line(window, GRAY, (0, i * DIM), (win_dim, i * DIM))
        for j in range(cols):
            pygame.draw.line(window, GRAY, (j*DIM, 0), (j*DIM, win_dim//2))
            pass
            
def draw(window, matrix, cols, win_dim):
    window.fill(WHITE)
    
    for row in matrix:
        for cell in row:
            cell.draw(window)

    draw_matrix(window, cols, win_dim)
    pygame.display.update()

def main():
    M = interpret_matrix(solve_matrix(ROWS, COLS, NSTATE))
    status = True
    while status:            
        draw(WIN, M, COLS, WIN_DIM)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
                pygame.quit()
                           
main()
