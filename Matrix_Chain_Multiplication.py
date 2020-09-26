import numpy as np
class Matrix_Chain_Mul():

    def __init__(self, list_Of_Dim):
        self.dict_dim_m = np.zeros(shape=(len(list_Of_Dim), len(list_Of_Dim)))
        self.dict_dim_s = np.zeros(shape=(len(list_Of_Dim), len(list_Of_Dim)))
    def calc(self, i, j):
        lista = []
        if i == j and self.dict_dim_m[i][j] != 0:
            return self.dict_dim_m[i][j]
        else:
            try:
                for k in range(i, j):
                    lista.append(self.calc(i, k) + self.calc(k+1, j) \
                                 + list_Of_Dim[i][0]*list_Of_Dim[k][1] \
                                 *list_Of_Dim[j][1])
                self.dict_dim_m[i, j] = min(lista)
                self.dict_dim_s[i, j] = lista.index(self.dict_dim_m[i, j])+1
            except ValueError:
                self.calc(i, j+1)

    def control_mul(self):
        for i in range(1, len(list_Of_Dim)+1):
            for j in range(i, len(list_Of_Dim)+1):
                self.calc(i, j)
        return self.dict_dim_m

if __name__ == "__main__":
    list_Of_Dim = [(3, 2), (2, 4), (4, 2),(2, 5)]
    test = Matrix_Chain_Mul(list_Of_Dim)
    x = test.control_mul()
    print(x)
    # dict_dim_m = {i:j for i in range(len(list_Of_Dim)) for j in list_Of_Dim}
    # # dict_dim_s =
    # dict_dim_s = np.zeros(shape=(len(list_Of_Dim), len(list_Of_Dim)))
    # dict_dim_m = np.zeros(shape=(3,3))
    # print(dict_dim_m)

