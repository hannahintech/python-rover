import re
import fileinput

class Rover:
    def __init__(self, x, y, orientation, grid_size, is_lost):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.grid_size = grid_size
        self.is_lost = is_lost

    def move(self, char):
        if self.is_lost:
            return
        if char == 'F':
            if self.check_boundary():
                self.is_lost = True
            else: 
                self.move_forward()
        if char == 'R':
            self.rotate_right()
        if char == 'L':
            self.rotate_left()

    def move_forward(self): 
        if (self.orientation == 'N'):
            self.y = self.y + 1
        elif (self.orientation == 'S'):
            self.y = self.y - 1
        elif (self.orientation == 'E'):
            self.x = self.x + 1
        elif (self.orientation == 'W'):
            self.x = self.x - 1
    
    def check_boundary(self):   
        if (self.orientation == 'N' and self.y == self.grid_size['height']):
            return True
        elif (self.orientation == 'S' and self.y == 0):
            return True
        elif (self.orientation == 'E' and self.x == self.grid_size['width']):
            return True
        elif (self.orientation == 'W' and self.x == 0):
            return True  

    def rotate_left(self):
        if (self.orientation == 'N'):
            self.orientation = 'W'
        elif (self.orientation == 'W'):
            self.orientation = 'S'
        elif (self.orientation == 'S'):
            self.orientation = 'E'
        elif (self.orientation == 'E'):
            self.orientation = 'N'
 

    def rotate_right(self):
        if (self.orientation == 'N'):
            self.orientation = 'E'
        elif (self.orientation == 'E'):
            self.orientation = 'S'
        elif (self.orientation == 'S'):
            self.orientation = 'W'
        elif (self.orientation == 'W'):
            self.orientation = 'N'

    def get_output(self):
        if self.check_boundary():
            return f'({self.x}, {self.y}, {self.orientation}) LOST'
        else:
            return f'({self.x}, {self.y}, {self.orientation})'

print('Please enter the rover data') 

def rover_data_input():
    rover_dict = dict()
    grid_size = dict()
    for line in fileinput.input(encoding="utf-8"):
        if line != '':
            clean_line = line.strip() and re.sub(r'[^A-Za-z0-9]', '', line)
            if fileinput.isfirstline():
                grid_size['height'] = int(clean_line[0])+1
                grid_size['width'] =int(clean_line[1])+1
            else:
                rover_dict[fileinput.lineno()-1] = dict(
                    x = int(clean_line[0]), 
                    y = int(clean_line[1]),
                    orientation = clean_line[2:3],
                    movements = clean_line[3:]
                )
        else:
            ('There is an error in your input, please try again')
    return grid_size, rover_dict

           
def main():
    grid_size, rover_dict = rover_data_input()
    rover_output = []
    for _, rover_data in rover_dict.items():
        rover = (Rover(rover_data['x'], rover_data['y'], rover_data['orientation'], grid_size, False))
        
        for direction in rover_data['movements']:
            rover.move(direction)

        rover_output.append(rover.get_output())

    for item in rover_output:
        print(item)

if __name__ == '__main__':
    main()

'''
Test input:
4 8
(2, 3, E) LFRFF
(0, 2, N) FFLFRFF
(2, 3, N) FLLFR
(1, 0, S) FFRLF
The output would be:
(4, 4, E)
(0, 4, W) LOST
(2, 3, W)
(1, 0, S) LOST
'''