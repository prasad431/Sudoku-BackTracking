import pygame
import random
class Attributes:
    __boards = [[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ],
        [
        [4, 0, 0, 0, 0, 0, 8, 0, 5],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 8, 0, 4, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 3, 0, 7, 0],
        [5, 0, 0, 2, 0, 0, 0, 0, 0],
        [1, 0, 4, 0, 0, 0, 0, 0, 0]
        ],
        [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ],
        [
        [0, 0, 6, 4, 8, 1, 3, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 4, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 9],
        [8, 0, 0, 0, 9, 0, 0, 0, 4],
        [6, 0, 0, 3, 4, 2, 0, 0, 1],
        [5, 0, 0, 0, 6, 0, 0, 0, 2],
        [3, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 9, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 5, 7, 1, 6, 2, 0, 0]
        ],
        [
        [3, 0, 0, 8, 0, 1, 0, 0, 2],
        [2, 0, 1, 0, 3, 0, 6, 0, 4],
        [0, 0, 0, 2, 0, 4, 0, 0, 0],
        [8, 0, 9, 0, 0, 0, 1, 0, 6],
        [0, 6, 0, 0, 0, 0, 0, 5, 0],
        [7, 0, 2, 0, 0, 0, 4, 0, 9],
        [0, 0, 0, 5, 0, 9, 0, 0, 0],
        [9, 0, 4, 0, 8, 0, 7, 0, 5],
        [6, 0, 0, 1, 0, 7, 0, 0, 3]
        ],
        [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
        ],
        [
        [4, 0, 0, 8, 1, 5, 6, 0, 0],
        [0, 0, 7, 0, 0, 3, 0, 1, 0],
        [8, 0, 0, 4, 7, 0, 0, 0, 0],
        [2, 0, 0, 1, 0, 0, 7, 9, 8],
        [1, 7, 5, 0, 0, 0, 2, 4, 6],
        [6, 8, 9, 0, 0, 7, 0, 0, 1],
        [0, 0, 0, 0, 8, 1, 0, 0, 2],
        [0, 2, 0, 9, 0, 0, 1, 0, 0],
        [0, 0, 4, 5, 6, 2, 0, 0, 3]
        ]
        ]
    fonts = ['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath', 'cambria', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'inkfree', 'erasmediumitc', 'erasitc', 'erasdemiitc', 'engravers', 'elephant', 'blackadderitc']
    def randomcolor_generator(self):
            codes = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
            hexcolor = self.__random_hex_code(codes)
            while hexcolor == 'ffffff' or hexcolor == 'eeeeee' or hexcolor == 'dddddd':
                hexcolor = self.__random_hex_code(codes)
            rgb_color = tuple(int(hexcolor[i:i+2], 16) for i in (0, 2, 4))
            return rgb_color

    def __random_hex_code(self, codes):
        hexcolor = ''
        for i in range(6):
            hexcolor = hexcolor + random.choice(codes)
        return hexcolor

    def randomfont_selection(self):
        #all_fonts = pygame.font.get_fonts()
        return random.choice(self.fonts)

    def random_board(self):
        return random.choice(self.__boards)
