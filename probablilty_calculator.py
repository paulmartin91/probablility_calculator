import math
import random
import copy
from copy import deepcopy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for ball_colour, quantity in kwargs.items():
            self.contents += [ball_colour] * quantity

    def draw(self, number_to_draw):
        drawn_list = []
        if number_to_draw >= len(self.contents):
            drawn_list = self.contents
            self.contents = []
            return drawn_list
        else:
            for draw_instance in range(0, number_to_draw):
                random_number = random.randint(0, len(self.contents)-1)
                drawn_list.append(self.contents[random_number])
                self.contents.remove(self.contents[random_number])
            return drawn_list
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    test_case = []
    passed_cases = 0

    for ball_colour, quantity in expected_balls.items():
        test_case += [ball_colour] * quantity

    for test_number in range(num_experiments):
        temp_hat = deepcopy(hat)
        drawn_balls = temp_hat.draw(num_balls_drawn)
        flag = True

        for ball_colour in test_case:
            if ball_colour in drawn_balls:
                drawn_balls.remove(ball_colour)

            else:
                flag = False
        
        if flag == True: passed_cases = passed_cases + 1


    return passed_cases / num_experiments


# TEST CASES
# 
# hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# print(experiment(
#     hat=hat, 
#     expected_balls={"yellow":2,"blue":3,"test":1},
#     num_balls_drawn=20,
#     num_experiments=100
#     ))