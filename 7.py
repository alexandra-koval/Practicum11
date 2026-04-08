numbers = list(map(int, input().split()))

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(sum(even_numbers), sum(odd_numbers))
