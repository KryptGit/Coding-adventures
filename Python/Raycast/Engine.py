loop = True
def generate_Board(columns, rows):
    area = [columns]
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(" ")
        area.append(row)
    print(area)

def project(arr):
    print(arr[0][0],"|",arr[0][1],"|",arr[0][2])
    print("------------")
    print(arr[1][0],"|",arr[1][1],"|",arr[1][2])
    print("------------")
    print(arr[2][0],"|",arr[2][1],"|",arr[2][2])
