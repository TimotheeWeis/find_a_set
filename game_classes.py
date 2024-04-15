import pygame
import random
import math

class Card:
    def __init__(self, color, shape, number, shading, width=200, height=100):
        self.color = color
        self.shape = shape
        self.number = number
        self.shading = shading
        self.width = width
        self.height = height

        self.shown_color = (int(self.color == 0) * 255, int(self.color == 1) * 150, int(self.color == 2) * 255)


    def draw(self, screen, x, y, cursor_is_in, is_selected, solution=False):
        pygame.draw.rect(screen, (200, 200, 200), (x, y, self.width, self.height))
        if cursor_is_in and not is_selected:
            pygame.draw.rect(screen, (255, 255, 0), (x, y, self.width, self.height), 2)
        
        if solution and not is_selected:
            pygame.draw.rect(screen, (0, 255, 0), (x, y, self.width, self.height), 2)

        if is_selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, self.width, self.height), 2)

        if self.shape == 0:
            self.draw_multiple_circles(screen, x + self.width/2, y + self.height/2, self.number)
        elif self.shape == 1:
            self.draw_multiple_diamonds(screen, x + self.width/2, y + self.height/2, self.number)
        else:
            self.draw_multiple_s(screen, x + self.width/2, y + self.height/2, self.number)

    def cursor_is_in(self, x, y, cursor_pos):
        cursor_x = cursor_pos[0]
        cursor_y = cursor_pos[1]
        return (cursor_x >= x and cursor_x <= x + self.width and cursor_y >= y and cursor_y <= y + self.height)


    def is_equal(self, other_card):
        return (self.color == other_card.color and self.shape == other_card.shape and self.shading == other_card.shading and self.number == other_card.number)
    
    def draw_s(self, screen, x, y):
        s_points = [(x, y - self.height/4), (x + self.width/12, y - self.height/4), (x, y - self.height/12),
                        (x + self.width/12, y + self.height/12), (x, y + self.height/4), (x - self.width/12, y + self.height/4),
                        (x, y + self.height/12), (x - self.width/12, y - self.height/12)]
        if self.shading == 0:
            pygame.draw.polygon(screen, self.shown_color, s_points)

        elif self.shading == 1:
            pygame.draw.polygon(screen, self.shown_color, s_points, 1)

        else:
            pygame.draw.polygon(screen, self.shown_color, s_points, 1)

            for i in range(1, 4):
                pygame.draw.line(screen, self.shown_color, (x + self.width*i/36, y + self.height*(9 - 2*i)/36), (x + self.width*(i - 3)/36, y + self.height*(9 - 2*i)/36))

            for i in range(1, 4):
                pygame.draw.line(screen, self.shown_color, (x - self.width*i/36, y + self.height*(3 - 2*i)/36), (x + self.width*(3 - i)/36, y + self.height*(3 - 2*i)/36))

            for i in range(1, 4):
                pygame.draw.line(screen, self.shown_color, (x + self.width*i/36, y + self.height*(-3 - 2*i)/36), (x + self.width*(i - 3)/36, y + self.height*(-3 - 2*i)/36))


    def draw_multiple_s(self, screen, x, y, number_of_shapes):
        if number_of_shapes == 0:
            self.draw_s(screen, x, y)
        
        elif number_of_shapes == 1:
            self.draw_s(screen, x - self.width/6, y)
            self.draw_s(screen, x + self.width/6, y)
        
        elif number_of_shapes == 2:
            self.draw_s(screen, x - self.width/3, y)
            self.draw_s(screen, x, y)
            self.draw_s(screen, x + self.width/3, y)
    
    def draw_diamond(self, screen, x, y):
        diamond_points = [(x, y - self.height/4), (x + self.width/12, y), (x, y + self.height/4), (x - self.width/12, y)]

        if self.shading == 0:
            pygame.draw.polygon(screen, self.shown_color, diamond_points)

        elif self.shading == 1:
            pygame.draw.polygon(screen, self.shown_color, diamond_points, 1)

        else:
            pygame.draw.polygon(screen, self.shown_color, diamond_points, 1)
        
            for i in range(1, 5):
                pygame.draw.line(screen, self.shown_color, (x + self.width/12 - self.width*i/48, y + self.height*i/16), (x - self.width/12 + self.width*i/48, y + self.height*i/16))
            
            for i in range(1, 5):
                pygame.draw.line(screen, self.shown_color, (x - self.width/12 + self.width*i/48, y - self.height*i/16), (x + self.width/12 - self.width*i/48, y - self.height*i/16))
            
            pygame.draw.line(screen, self.shown_color, (x - self.width/12, y), (x + self.width/12, y))

    def draw_multiple_diamonds(self, screen, x, y, number_of_shapes):
        if number_of_shapes == 0:
            self.draw_diamond(screen, x, y)
        
        elif number_of_shapes == 1:
            self.draw_diamond(screen, x - self.width/6, y)
            self.draw_diamond(screen, x + self.width/6, y)
        
        elif number_of_shapes == 2:
            self.draw_diamond(screen, x - self.width/3, y)
            self.draw_diamond(screen, x, y)
            self.draw_diamond(screen, x + self.width/3, y)

    def draw_circle(self, screen, x, y):
        radius = self.height/4

        if self.shading == 0:
            pygame.draw.circle(screen, self.shown_color, (x, y), radius)
        
        elif self.shading == 1:
            pygame.draw.circle(screen, self.shown_color, (x, y), radius, 1)
        
        else:
            pygame.draw.circle(screen, self.shown_color, (x, y), radius, 1)
            for i in range(11):
                pi = math.pi
                pygame.draw.line(screen, self.shown_color, (x + radius*math.cos((5 - i)*pi/10), y + radius*math.sin((5-i)*pi/10)), (x - radius*math.cos((5 - i)*pi/10), y + radius*math.sin((5 - i)*pi/10)))


    def draw_multiple_circles(self, screen, x, y, number_of_shapes):
        if number_of_shapes == 0:
            self.draw_circle(screen, x, y)
        
        elif number_of_shapes == 1:
            self.draw_circle(screen, x - self.width/6, y)
            self.draw_circle(screen, x + self.width/6, y)
        
        elif number_of_shapes == 2:
            self.draw_circle(screen, x - self.width/3, y)
            self.draw_circle(screen, x, y)
            self.draw_circle(screen, x + self.width/3, y)

class GameBoard:
    def __init__(self):
        self.cards = []
        self.selected = []

        self.base_x = 50
        self.base_y = 50
        self.x_space = 220
        self.y_space = 150
        self.show_solution = False
        self.solution = []

        self.sol_button_x_offset = 50
        self.sol_button_y_offset = 50
        self.sol_button_x = 200
        self.sol_button_y = 100

        self.hint_image = pygame.transform.scale(pygame.image.load("images/hint.png"), (self.sol_button_y, self.sol_button_y))


    def check_if_global_solution(self):
        for i in range(len(self.cards)):
            for j in range(i + 1, len(self.cards)):
                for k in range(j + 1, len(self.cards)):
                    first_card = self.cards[i]
                    second_card = self.cards[j]
                    third_card = self.cards[k]
                    is_solution = self.check_if_solution(first_card, second_card, third_card)
                    if is_solution:
                        self.solution = [i, j, k]
                        return True
        return False
    
    def check_if_solution(self, first_card, second_card, third_card):
        color_check = ((first_card.color == second_card.color and second_card.color == third_card.color) or (first_card.color != second_card.color and second_card.color != third_card.color and first_card.color != third_card.color))
        shape_check = ((first_card.shape == second_card.shape and second_card.shape == third_card.shape) or (first_card.shape != second_card.shape and second_card.shape != third_card.shape and first_card.shape != third_card.shape))
        number_check = ((first_card.number == second_card.number and second_card.number == third_card.number) or (first_card.number != second_card.number and second_card.number != third_card.number and first_card.number != third_card.number))
        shading_check = ((first_card.shading == second_card.shading and second_card.shading == third_card.shading) or (first_card.shading != second_card.shading and second_card.shading != third_card.shading and first_card.shading != third_card.shading))
        if color_check and shape_check and number_check and shading_check:
            return True
        return False
    
    def draw(self, screen, cursor_pos, is_clicked):

        self.draw_solution_button(screen, cursor_pos)
    
        if is_clicked:
            self.process_click(cursor_pos, screen)

        for i in range(len(self.cards)):
            x = self.base_x + (i%3)*self.x_space
            y = self.base_y + (i//3)*self.y_space
            self.cards[i].draw(screen, x, y, self.cards[i].cursor_is_in(x, y, cursor_pos), i in self.selected, solution=(i in self.solution and self.show_solution))

    def draw_solution_button(self, screen, cursor_pos):
        screen_width, screen_height = screen.get_size()
        cursor_x, cursor_y = cursor_pos
        pygame.draw.rect(screen, (200, 200, 200), (self.sol_button_x_offset, screen_height - self.sol_button_y_offset - self.sol_button_y, self.sol_button_x, self.sol_button_y))
        if (cursor_x >= self.sol_button_x_offset and
            cursor_x <= self.sol_button_x_offset + self.sol_button_x and
            cursor_y >= screen_height - self.sol_button_y_offset - self.sol_button_y and
            cursor_y <=screen_height - self.sol_button_y_offset):

            pygame.draw.rect(screen, (255, 255, 0), (self.sol_button_x_offset, screen_height - self.sol_button_y_offset - self.sol_button_y, self.sol_button_x, self.sol_button_y), 2)
        
        screen.blit(self.hint_image, (self.sol_button_x_offset + (self.sol_button_x - self.sol_button_y)//2, screen_height - self.sol_button_y_offset - self.sol_button_y))



    def process_click(self, cursor_pos, screen):
        for i in range(len(self.cards)):
            x = self.base_x + (i%3)*self.x_space
            y = self.base_y + (i//3)*self.y_space
            if self.cards[i].cursor_is_in(x, y, cursor_pos):
                if i in self.selected:
                    self.selected.remove(i)
                elif len(self.selected) < 3:
                    self.selected.append(i)
                else:
                    self.selected = self.selected[1:] + [i]
                break

        screen_width, screen_height = screen.get_size()
        cursor_x, cursor_y = cursor_pos
        if (cursor_x >= self.sol_button_x_offset and
            cursor_x <= self.sol_button_x_offset + self.sol_button_x and
            cursor_y >= screen_height - self.sol_button_y_offset - self.sol_button_y and
            cursor_y <=screen_height - self.sol_button_y_offset):

            self.show_solution = True
            self.selected = []


    def update(self):
        if len(self.selected) == 3:
            first_card = self.cards[self.selected[0]]
            second_card = self.cards[self.selected[1]]
            third_card = self.cards[self.selected[2]]
            if self.check_if_solution(first_card, second_card, third_card):
                self.selected = sorted(self.selected, reverse=True)
                for i in self.selected:
                    self.cards.pop(i)
                self.show_solution = False
                self.selected = []

        self.fill_board()

    def fill_board(self):
        while(len(self.cards) < 12):
            self.add_card()
        
        while not self.check_if_global_solution():
            for _ in range(3):
                self.add_card()
        

    def add_card(self):
        color = random.randint(0, 2)
        shape = random.randint(0, 2)
        number = random.randint(0, 2)
        shading = random.randint(0, 2)

        new_card = Card(color, shape, number, shading)
        sentinelle = True
        while sentinelle:
            color = random.randint(0, 2)
            shape = random.randint(0, 2)
            number = random.randint(0, 2)
            shading = random.randint(0, 2)
            new_card = Card(color, shape, number, shading)
            if not any(new_card.is_equal(card) for card in self.cards) or len(self.cards) == 0:
                self.cards.append(new_card)
                sentinelle = False






        
    