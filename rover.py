import re
import fileinput

class Rover:
    def __init__(self, x, y, orientation, grid_size):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.grid_size = grid_size

    def move(self, char):
        if char == 'F':
            self.move_forward()
        if char == 'R':
            self.rotate_left()
        if char == 'L':
            self.rotate_right()

    def move_forward(self):
        if (self.orientation == 'N'):
            self.y = self.y - 1
        elif (self.orientation == 'S'):
            self.y = self.y + 1
        elif (self.orientation == 'E'):
            self.x = self.x + 1
        elif (self.orientation == 'W'):
            self.x = self.x - 1

    def rotate_left(self):
        self.orientation = 'W'

    def rotate_right(self):
        self.orientation = 'E'

    def is_lost(self):
        if self.x < 1:
            return True
        if self.y < 1:
            return True
        if self.x > self.grid_size[0]:
            return True
        if self.y > self.grid_size[1]:
            return True
        return False

    def get_output(self):
        st = f'({self.x}, {self.y}, {self.orientation})'
        if self.is_lost():
            st = st + ' LOST'
        return st

print('Please enter the rover data') 

def rover_data_input():
    rover_dict = dict()
    grid_size = list()
    for line in fileinput.input(encoding="utf-8"):
        if line != '':
            clean_line = line.strip() and re.sub(r'[^A-Za-z0-9]', '', line)
            if fileinput.isfirstline():
                grid_size.extend([int(clean_line[0]), int(clean_line[1])])
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
    for id, rover_data in rover_dict.items():
        # print('rover data', rover_data)
        rover = (Rover(rover_data['x'], rover_data['y'], rover_data['orientation'], grid_size))
        
        for direction in rover_data['movements']:
            rover.move(direction)

        rover_output.append(rover)

    for rover in rover_output:
        print(rover.get_output())

if __name__ == '__main__':
    main()

'''
4 8
(2, 3, N) FLFRR
(2, 3, E) LFRF
(1, 2, E) FFLF
(1, 2, E) LLLF
(2, 3, N) FFF
'''