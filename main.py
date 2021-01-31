import pygame


class Board:
    # создание поля
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 28
        self.top = 28
        self.cell_size = cell_size

    def show_letters(self, screen):
        font = pygame.font.Font(None, 30)
        lets = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
        x, y = 40, 5
        for i in range(self.width):
            text = font.render(lets[i], True, (0, 255, 0))
            screen.blit(text, (x + 30 * i, y))

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 2:
                    pygame.draw.circle(screen, pygame.Color('red'),
                                       (j * self.cell_size + self.left + self.cell_size // 2,
                                        i * self.cell_size + self.top + self.cell_size // 2), self.cell_size // 2 - 2,
                                       1)
                elif self.board[i][j] == 1:
                    pygame.draw.line(screen, pygame.Color('blue'), (j * self.cell_size + self.left + 2,
                                                                    i * self.cell_size + self.top + 2),
                                     (j * self.cell_size + self.left + self.cell_size - 2,
                                      i * self.cell_size + self.top + self.cell_size - 2), 3)
                    pygame.draw.line(screen, pygame.Color('blue'), (j * self.cell_size + self.left + self.cell_size - 2,
                                                                    i * self.cell_size + self.top + 2),
                                     (j * self.cell_size + self.left + 2,
                                      i * self.cell_size + self.top + self.cell_size - 2), 3)

                pygame.draw.rect(screen, pygame.Color('white'), (j * self.cell_size + self.left,
                                                                 i * self.cell_size + self.top,
                                                                 self.cell_size, self.cell_size), 1)
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


def main():
    global order
    a = int(input('Введите ширину поля: '))
    b = int(input('Введите высоту поля: '))
    pygame.init()
    pygame.display.set_caption('Крестики-нолики')
    cell = 30
    size = a * cell + 56, b * cell + 56
    screen = pygame.display.set_mode(size)
    board = Board(a, b, cell)
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


if __name__ == '__main__':
    order = 0
    main()
