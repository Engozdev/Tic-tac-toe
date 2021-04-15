import pygame
import sys


class Board:
    # создание поля
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 40
        self.top = 28
        self.cell_size = cell_size

    def show_letters(self, screen):
        font = pygame.font.Font(None, 30)
        # lets = 'abcdefghijklnopqrstuvwxyz'
        lets = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        fx, fy = 50, 5
        for i in range(self.width):
            text = font.render(lets[i], True, (51, 247, 255))
            screen.blit(text, (fx + 30 * i, fy))
        sx, sy = 10, 35
        for j in range(1, self.height + 1):
            text = font.render(str(j), True, (51, 247, 255))
            screen.blit(text, (sx, sy + 30 * (j - 1)))

    def render(self, screen):
        global order
        global sze
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 2:
                    pygame.draw.circle(screen, (255, 242, 51),
                                       (j * self.cell_size + self.left + self.cell_size // 2,
                                        i * self.cell_size + self.top + self.cell_size // 2), self.cell_size // 2 - 2,
                                       3)
                elif self.board[i][j] == 1:
                    pygame.draw.line(screen, pygame.Color('red'), (j * self.cell_size + self.left + 2,
                                                                   i * self.cell_size + self.top + 2),
                                     (j * self.cell_size + self.left + self.cell_size - 2,
                                      i * self.cell_size + self.top + self.cell_size - 2), 5)
                    pygame.draw.line(screen, pygame.Color('red'), (j * self.cell_size + self.left + self.cell_size - 2,
                                                                   i * self.cell_size + self.top + 2),
                                     (j * self.cell_size + self.left + 2,
                                      i * self.cell_size + self.top + self.cell_size - 2), 5)

                pygame.draw.rect(screen, pygame.Color('white'), (j * self.cell_size + self.left,
                                                                 i * self.cell_size + self.top,
                                                                 self.cell_size, self.cell_size), 1)
        y = sze[1] - int(self.cell_size * 1.2)
        x = sze[0] // 2
        if order % 2 == 0:
            pygame.draw.line(screen, pygame.Color('red'), (x - 25, y - 25), (x + 25, y + 25), 5)
            pygame.draw.line(screen, pygame.Color('red'), (x + 25, y - 25), (x - 25, y + 25), 5)
        else:
            pygame.draw.circle(screen, (255, 242, 51), (x, y), 25, 3)
        self.show_letters(screen)

    def get_cell(self, mouse_pos, player_order):
        global order
        if mouse_pos[0] < self.left or mouse_pos[0] > self.width * self.cell_size + self.left or \
                mouse_pos[1] < self.top or mouse_pos[1] > self.height * self.cell_size + self.top:
            return None
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        x //= self.cell_size
        y //= self.cell_size
        if self.board[y][x] == 0:
            order += 1
            if player_order % 2 == 0:
                self.board[y][x] = 1
            else:
                self.board[y][x] = 2


def main(w, h, size, cell):
    global order
    pygame.init()
    pygame.display.set_caption('Крестики-нолики')
    screen = pygame.display.set_mode(size)
    board = Board(w, h, cell)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_cell(event.pos, order)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    try:
        a = int(input('Enter the width of the board: '))
        b = int(input('Enter the height of the board: '))
        if a < 1 or b < 1 or a > 35 or b > 35:
            raise ValueError
    except ValueError:
        print('Recheck your input values')
        sys.exit()
    order = 0
    cll = 30
    sze = a * cll + 56, b * cll + 100
    main(a, b, sze, cll)
# создать голосовое управление
# сделать функцию распознающую речь, и передавать ее вывод сюда
