people, area = map(int, input().split())
data = list(map(int, input().split()))
result = []
for i in data:
    result.append(i - (people * area))
print(*result)