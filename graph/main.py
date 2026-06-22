from orange_rot import orangeRot01, orangeRot02
from number_of_islands import countIslands, countIslands01
from flood_fill import floodFill
from min_word_transform import wordLadder, wordLadder01
from detect_cycle_directed import isCycle_directed

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

    def testeMinWordTransform(self):
        arr = ["poon", "plee", "same", "poie", "plie", "poin", "plea"]
        start = "toon"
        target = "plea"
        
        # start = "abcv"
        # target = "ebad"
        # arr = ["abcd", "ebad", "ebcd", "xyza"]

        print(wordLadder01(start, target, arr))

    def test_detect_cycle_directed(self):
        # adj = [[1], [2], [0,3], []]
        adj = [[2], [0], []]
        for i in adj:
            print(i)

        print("True" if isCycle_directed(adj) else "False")

    def test_detect_cycle_undirected(self):
        pass

if __name__ == '__main__':

    teste = Teste()
    # teste.testeOrangeRot()
    # teste.testeNumberIslands()
    # teste.testeFloodFill()
    # teste.testeMinWordTransform()
    # teste.test_detect_cycle_directed()
    teste.test_detect_cycle_undirected()


