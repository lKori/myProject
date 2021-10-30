def cal_triangle(length, height):
    """밑변과 높이를 입력받아 삼각형의 넓이를 계산한다."""
    print((length * height) / 2)

print('밑변을 입력하세요.')
length = int(input())

print('높이을 입력하세요.')
height = int(input())

cal_triangle(length, height)