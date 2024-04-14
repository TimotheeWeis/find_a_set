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

        self.shown_color = (int(self.color == 0) * 255, int(self.color == 1) * 255, int(self.color == 2) * 255)


    def draw(self, screen, x, y):
        pygame.draw.rect(screen, (200, 200, 200), (x, y, self.width, self.height))
        if self.shape == 0:
            self.draw_multiple_circles(screen, x + self.width/2, y + self.height/2, self.number)
        elif self.shape == 1:
            self.draw_multiple_diamonds(screen, x + self.width/2, y + self.height/2, self.number)
        else:
            self.draw_multiple_s(screen, x + self.width/2, y + self.height/2, self.number)


    def is_equal(self, other_card):
        return (self.color == other_card.color and self.shape == other_card.shape and self.shading == other_card.shading)
    
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

    def generate_board(self):

        while len(self.cards) != 12:
            color = random.randint(0, 2)
            shape = random.randint(0, 2)
            number = random.randint(0, 2)
            shading = random.randint(0, 2)

            new_card = Card(color, shape, number, shading)

            if not any(new_card.is_equal(card) for card in self.cards):
                self.cards.append(new_card)

    def check_if_solution(self):
        for i in range(len(self.cards)):
            for j in range(i + 1, len(self.cards)):
                for k in range(j + 1, len(self.cards)):
                    first_card = self.cards[i]
                    second_card = self.cards[j]
                    third_card = self.cards[k]

                    color_check = ((first_card.color == second_card.color and second_card.color == third_card.color) or (first_card.color != second_card.color and second_card.color != third_card.color and first_card.color != third_card.color))
                    shape_check = ((first_card.shape == second_card.shape and second_card.shape == third_card.shape) or (first_card.shape != second_card.shape and second_card.shape != third_card.shape and first_card.shape != third_card.shape))
                    number_check = ((first_card.number == second_card.number and second_card.number == third_card.number) or (first_card.number != second_card.number and second_card.number != third_card.number and first_card.number != third_card.number))
                    shading_check = ((first_card.shading == second_card.shading and second_card.shading == third_card.shading) or (first_card.shading != second_card.shading and second_card.shading != third_card.shading and first_card.shading != third_card.shading))

                    if color_check and shape_check and number_check and shading_check:
                        return True
        return False
    
    def draw(self, screen):
        base_x = 50
        base_y = 50
        x_space = 220
        y_space = 150

        for i in range(len(self.cards)):
            self.cards[i].draw(screen, base_x + (i%3)*x_space, base_y + (i//3)*y_space)
        
    
