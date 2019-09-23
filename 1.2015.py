A, B, C = [int(i) for i in input().split()]

if 0 <= A <= 1000 and 0 <= B <= 1000 and 0 <= C <= 1000:
    print(A+B+C)
else:
    print('Sorry')

# print(sum([int(i) for i in input().split()]))