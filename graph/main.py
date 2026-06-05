from orange_rot import orangeRot01, orangeRot02
from number_of_islands import countIslands, countIslands01

class Teste():

    def testeOrangeRot(self):
        mat1 = [[2, 1, 0, 2, 1],
                [1, 0, 1, 2, 1],
                [1, 0, 0, 2, 1]]

        mat2 = [[2, 1, 0, 2, 1],
                [0, 0, 1, 2, 1], 
                [1, 0, 0, 2, 1]]

        print(orangeRot02(mat1))
        print(orangeRot02(mat2))

    def testeNumberIslands(self):
        grid01 = [
        ['L', 'W', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'L'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'W', 'W', 'W', 'W'],
        ['L', 'W', 'L', 'L', 'W']
        ]

        grid02 = [['W', 'L', 'L', 'L', 'W', 'W', 'W'],
                  ['W', 'W', 'L', 'L', 'W', 'L', 'W']] 

        mats = [grid01, grid02]
        
        for grid in mats:
            print(countIslands01(grid)) 

        # print(countIslands01(grid02))

    def testeFloodFill(self):
        img = [
        [1, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1]
        ]
        
        sr, sc = 1, 2
        newColor = 2
    
        result = floodFill(img, sr, sc, newColor)
        
        for row in result:
            print(*row)

if __name__ == '__main__':

    teste = Teste()
    # teste.testeOrangeRot()
    # teste.testeNumberIslands()
    teste.testeFloodFill()


