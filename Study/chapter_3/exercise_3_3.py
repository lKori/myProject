def print_absolute(x):
    """정수를 입력받아 그 수의 절댓값을 반환한다."""
    print(x, '의 절댓값:', abs(x))

print('정수를 입력하세요.')
number = int(input())

print_absolute(number)