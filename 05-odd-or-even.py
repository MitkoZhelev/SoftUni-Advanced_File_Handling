command = input()
num = [int(word) for word in input().split()]

filtered = []
if command == "Even":
    filtered = filter(lambda x: x % 2 == 0, num)
elif command == "Odd":
    filtered = filter(lambda x: x % 2 != 0, num)

result = sum(filtered) * len(num)

print(result)
