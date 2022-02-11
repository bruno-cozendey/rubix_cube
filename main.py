import sys 

file = []
for line in sys.stdin: 
    file.append(line.strip())
#num_testes = int(file[0])

#tests = []
#init = 1
#for i in range(1,num_testes+1):
#    tests.append(file[init:(10*i)+1])
#    init=+11
#print(tests)

tests = [file[x:x+10] for x in range(1, len(file), 10)]

rotation = []
for i in tests:
    rotation.append(i[9])
print(rotation)

faces = [
[["X","X","X"],["X","X","X"],["X","X","X"]],
[["","",""],["","",""],["","",""]],
[["","",""],["","",""],["","",""]],
[["","",""],["","",""],["","",""]],
[["","",""],["","",""],["","",""]],
[["","",""],["","",""],["","",""]],
[["","",""],["","",""],["","",""]]
]


def create_cube(test):
    faces[1][0][0] = test[3][0]
    faces[1][0][1] = test[3][2]
    faces[1][0][2] = test[3][4]
    faces[1][1][0] = test[4][0]
    faces[1][1][1] = test[4][2]
    faces[1][1][2] = test[4][4]
    faces[1][2][0] = test[5][0]
    faces[1][2][1] = test[5][2]
    faces[1][2][2] = test[5][4]

    faces[2][0][0] = test[3][6]
    faces[2][0][1] = test[3][8]
    faces[2][0][2] = test[3][10]
    faces[2][1][0] = test[4][6]
    faces[2][1][1] = test[4][8]
    faces[2][1][2] = test[4][10]
    faces[2][2][0] = test[5][6]
    faces[2][2][1] = test[5][8]
    faces[2][2][2] = test[5][10]

    faces[3][0][0] = test[3][12]
    faces[3][0][1] = test[3][14]
    faces[3][0][2] = test[3][16]
    faces[3][1][0] = test[4][12]
    faces[3][1][1] = test[4][14]
    faces[3][1][2] = test[4][16]
    faces[3][2][0] = test[5][12]
    faces[3][2][1] = test[5][14]
    faces[3][2][2] = test[5][16]

    faces[4][0][0] = test[3][18]
    faces[4][0][1] = test[3][20]
    faces[4][0][2] = test[3][22]
    faces[4][1][0] = test[4][18]
    faces[4][1][1] = test[4][20]
    faces[4][1][2] = test[4][22]
    faces[4][2][0] = test[5][18]
    faces[4][2][1] = test[5][20]
    faces[4][2][2] = test[5][22]

    faces[5][0][0] = test[0][0]
    faces[5][0][1] = test[0][2]
    faces[5][0][2] = test[0][4]
    faces[5][1][0] = test[1][0]
    faces[5][1][1] = test[1][2]
    faces[5][1][2] = test[1][4]
    faces[5][2][0] = test[2][0]
    faces[5][2][1] = test[2][2]
    faces[5][2][2] = test[2][4]

    faces[6][0][0] = test[6][0]
    faces[6][0][1] = test[6][2]
    faces[6][0][2] = test[6][4]
    faces[6][1][0] = test[7][0]
    faces[6][1][1] = test[7][2]
    faces[6][1][2] = test[7][4]
    faces[6][2][0] = test[8][0]
    faces[6][2][1] = test[8][2]
    faces[6][2][2] = test[8][4]
    print(faces)

faces_2 = [
[["X","X","X"],["X","X","X"],["X","X","X"]],
[["W","W","W"],["W","W","W"],["W","W","W"]],
[["Y","R","R"],["Y","R","R"],["Y","R","R"]],
[["M","M","M"],["M","M","M"],["M","M","M"]],
[["G","G","B"],["G","G","B"],["G","G","B"]],
[["G","Y","Y"],["G","Y","Y"],["G","Y","Y"]],
[["R","B","B"],["R","B","B"],["R","B","B"]]
]

# -> Clockwise <- Anticlockwise
def rotate_face_one(direction):
    if direction == "-":
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[2][i][0]
            faces[2][i][0] = faces[6][i][0]
            faces[6][i][0] = faces[4][i][2]
            faces[4][i][2] = faces[5][i][0]
            faces[5][i][0] = aux[i]
    else:
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[5][i][0] 
            faces[5][i][0] = faces[4][i][2] 
            faces[4][i][2] = faces[6][i][0]
            faces[6][i][0] = faces[2][i][0]
            faces[2][i][0] = aux[i]

def rotate_face_two(direction):
    if direction == "-":
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[3][i][0]
            faces[3][i][0] = faces[6][0][i]
            faces[6][0][i] = faces[1][i][2]
            faces[1][i][2] = faces[5][2][i]
            faces[5][2][i] = aux[i]
    else:
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[5][2][i] 
            faces[5][2][i] = faces[1][i][2] 
            faces[1][i][2] = faces[6][0][i]
            faces[6][0][i] = faces[3][i][0]
            faces[3][i][0] = aux[i]

def rotate_face_three(direction):
    if direction == "-":
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[2][i][2]
            faces[2][i][2] = faces[6][i][2]
            faces[6][i][2] = faces[4][i][0]
            faces[4][i][0] = faces[5][i][2]
            faces[5][i][2] = aux[i]
    else:
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[5][i][2] 
            faces[5][i][2] = faces[4][i][0] 
            faces[4][i][0] = faces[6][i][2]
            faces[6][i][2] = faces[2][i][2]
            faces[2][i][2] = aux[i]

def rotate_face_four(direction):
    if direction == "-":
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[3][i][2]
            faces[3][i][2] = faces[6][2][i]
            faces[6][2][i] = faces[1][i][0]
            faces[1][i][0] = faces[5][0][i]
            faces[5][0][i] = aux[i]
    else:
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[5][0][i] 
            faces[5][0][i] = faces[1][i][0] 
            faces[1][i][0] = faces[6][2][i]
            faces[6][2][i] = faces[3][i][2]
            faces[3][i][2] = aux[i]

def rotate_face_five(direction):
    if direction == "-":
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[4][0][i]
            faces[4][0][i] = faces[1][0][i]
            faces[1][0][i] = faces[2][0][i]
            faces[2][0][i] = faces[3][0][i]
            faces[3][0][i] = aux[i]
    else:
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[3][0][i] 
            faces[3][0][i] = faces[2][0][i] 
            faces[2][0][i] = faces[1][0][i]
            faces[1][0][i] = faces[4][0][i]
            faces[4][0][i] = aux[i]

def rotate_face_six(direction):
    if direction == "-":
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[2][2][i]
            faces[2][2][i] = faces[3][i][2]
            faces[3][i][2] = faces[4][i][2]
            faces[4][i][2] = faces[1][i][2]
            faces[1][i][2] = aux[i]
    else:
        aux = ["","",""]
        for i in range(0,3):
            aux[i] = faces[1][i][2] 
            faces[1][i][2] = faces[4][i][2] 
            faces[4][i][2] = faces[3][i][2]
            faces[3][i][2] = faces[2][2][i]
            faces[2][2][i] = aux[i]

def rotate(rotation):
    rotations = rotation.split(" ")
    for r in rotations:
        if r == "0":
            break
        if r[1] == "1":
            rotate_face_one(r[0])
        if r[1] == "2":
            rotate_face_two(r[0])
        if r[1] == "3":
            rotate_face_three(r[0])
        if r[1] == "4":
            rotate_face_four(r[0])
        if r[1] == "5":
            rotate_face_five(r[0])
        if r[1] == "6":
            rotate_face_six(r[0])







for test in tests:
    create_cube(test)
    rotate(test[9])
    print(faces)
    #check_rotation()
    pass
