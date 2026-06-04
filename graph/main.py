from orange_rot import orangeRot01, orangeRot02

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
        pass

if __name__ == '__main__':

    teste = Teste()
    teste.testeOrangeRot()


