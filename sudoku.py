def red_zauzet(mat, red, x):
    for i in range(9):
        if (mat[red][i] == x):
            return False
    return True


def kolona_zauzeta(mat, kolona, x):
    for i in range(9):
        if (mat[i][kolona] == x):
            return False
    return True


def kvadrat_zauzet(mat, red, kolona, x):
    for i in range(3):
        for j in range(3):
            if (mat[i + red-red%3][j + kolona - kolona%3] == x):
                return False
    return True



def mjesto_ok(mat, red, kolona, x):
    return red_zauzet(mat, red, x) and kolona_zauzeta(mat, kolona, x) and kvadrat_zauzet(mat, red, kolona, x)

def ispisi(mat):
    for i in range(9):
        for j in range(9):
            print(mat[i][j], end=" "),
        print(" ")

def prazno(mat, red_i_kolona):
    for red in range(9):
        for kolona in range(9):
            if (mat[red][kolona] == 0):
                red_i_kolona[0] = red
                red_i_kolona[1] = kolona
                return True
    return False



def rijesi(mat):
    red_i_kolona = [0, 0]

    if (not prazno(mat, red_i_kolona)):
        return True

    red = red_i_kolona[0]
    kolona = red_i_kolona[1]

    for x in range(1, 10):

        if (mjesto_ok(mat, red, kolona, x)):
            mat[red][kolona] = x

            if (rijesi(mat)):
                return True
            mat[red][kolona] = 0
    return False


if __name__ == "__main__":

    sudoku = [[0 for x in range(9)] for y in range(9)]

    sudoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
              [5, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 3, 1],
              [0, 0, 3, 0, 1, 0, 0, 8, 0],
              [9, 0, 0, 8, 6, 3, 0, 0, 5],
              [0, 5, 0, 0, 9, 0, 6, 0, 0],
              [1, 3, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 4],
              [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    sudoku1 = [[0 for x in range(9)] for y in range(9)]

    sudoku1 = [[0, 8, 0, 0, 0, 9, 7, 4, 3],
              [0, 5, 0, 0, 0, 8, 0, 1, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0],
              [8, 0, 0, 0, 0, 5, 0, 0, 0],
              [0, 0, 0, 8, 0, 4, 0, 0, 0],
              [0, 0, 0, 3, 0, 0, 0, 0, 6],
              [0, 0, 0, 0, 0, 0, 0, 7, 0],
              [0, 3, 0, 5, 0, 0, 0, 8, 0],
              [9, 7, 2, 4, 0, 0, 0, 5, 0]]

    if (rijesi(sudoku)):
        ispisi(sudoku)
    else:
        print("Nema rjesenja")

    if(rijesi(sudoku1)):
        ispisi(sudoku1)
    else:
        print("Nema rjesenja")