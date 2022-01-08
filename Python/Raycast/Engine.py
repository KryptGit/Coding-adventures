loop = True
def generate_Board(columns, rows):
    area = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append("1")
        area.append(row)
    return area

def project(arr):
	for row in arr:
		print("")
		for col in row:
			print("|"+col, end = "|"),
	