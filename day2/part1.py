import os
import sys

class Draw:
    red = 0
    green = 0
    blue = 0

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class Configuration:
    draws = []
    id = None

    def __init__(self, id):
        self.id = id
        self.draws = []

    def add_draw(self, draw):
        self.draws.append(draw)

    @staticmethod
    def from_config_line(config_line):
        parts = config_line.split(':')
        id = parts[0].replace('Game ', '')
        configuration = Configuration(id)

        draws = parts[1].split(';')

        for draw in draws:
            cubes = draw.split(',')
            red = 0
            green = 0
            blue = 0
            
            for cube in cubes:
                cube = cube.strip()
                number, color = cube.split(' ')

                if color == 'blue':
                    blue = int(number)
                elif color == 'green':
                    green = int(number)
                elif color == 'red':
                    red = int(number)
                
            configuration.add_draw(Draw(red, green, blue))


        return configuration

    def is_valid(self):
        for draw in self.draws:
            valid = draw.red <= 12 and draw.green <= 13 and draw.blue <= 14
            if not valid:
                return False
        
        return True



def load_input():
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    f = open(f"{script_directory}/input.txt", "r")
    return f.read().split('\n')


def execute():
    sum = 0

    for line in load_input():
        configuration = Configuration.from_config_line(line)
        if (configuration.is_valid()):
            sum += int(configuration.id) 

    print(f"Sum={sum}")

if __name__ == "__main__":
    execute()