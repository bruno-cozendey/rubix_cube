import sys 

file = []
for line in sys.stdin: 
    file.append(line.rstrip())
    num_testes = int(file[0])
# for i in range(1,(num_testes+1)*10):
#     pass

faces_2 = [
[["X","X","X"],["X","X","X"],["X","X","X"]],
[["","",""],["","",""],["","",""]],
[["","",""],["","",""],["","",""]],
[["","",""],["","",""],["","",""]],
[["","",""],["","",""],["","",""]],
[["","",""],["","",""],["","",""]],
[["","",""],["","",""],["","",""]]
]

faces = [
[["X","X","X"],["X","X","X"],["X","X","X"]],
[["W","W","W"],["W","W","W"],["W","W","W"]],
[["Y","R","R"],["Y","R","R"],["Y","R","R"]],
[["M","M","M"],["M","M","M"],["M","M","M"]],
[["G","G","B"],["G","G","B"],["G","G","B"]],
[["G","Y","Y"],["G","Y","Y"],["G","Y","Y"]],
[["R","B","B"],["R","B","B"],["R","B","B"]]
]
      
face_one = [["","",""],["","",""],["","",""]]
face_two = [["","",""],["","",""],["","",""]]
face_three = [["","",""],["","",""],["","",""]]
face_four = [["","",""],["","",""],["","",""]]
face_five = [["","",""],["","",""],["","",""]]
face_six = [["","",""],["","",""],["","",""]]

# -> Clockwise <- Anticlockwise
faces_rotate_one = [(2,0),(6,0),(4,4),(5,0)]
faces_rotate_two = [3,6,1,5]
faces_rotate_three = [2,6,4,5]
faces_rotate_four = [4,6,2,5]
faces_rotate_five = [4,1,2,3]
faces_rotate_six = [2,3,4,1]
#[face,columns]
faces_rotation_order = [
    [0,0,0,0],
    [[2,0],[6,0],[4,2],[5,0]],
    [3,6,1,5],
    [2,6,4,5],
    [4,6,2,5],
    [4,1,2,3],
    [2,3,4,1]
]

def rotate_face(face, direction):
    if direction == "+":
        aux = faces[faces_rotation_order[face][0][0]]
        for i in range(0,3):
            faces[faces_rotation_order[face][i][0]][faces_rotation_order[face][i][1]] = faces[faces_rotation_order[face][i+1][0]][faces_rotation_order[face][i+1][1]]
        faces[faces_rotation_order[face][-1][0]] = aux
    else:
        faces_rotation_order_inverted = faces_rotation_order[face].reverse()
        aux = faces_rotation_order_inverted
        for i in faces_rotation_order_inverted:
            faces[0][i] = faces[0][i+1]
        faces[faces_rotation_order_inverted[-1]] = aux


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


rotate_face_one("-")
print(faces)
