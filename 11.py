lst = [int(x) for x in input().split()]

command = input()

direction = command[0]
n = int(command[1:])

n = n % len(lst)

if direction == 'R':
    lst = lst[-n:] + lst[:-n]
elif direction == 'L':
    lst = lst[n:] + lst[:n]

print(lst)