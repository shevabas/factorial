number = int(input("What number do you want to find the factorial of?: "))
y=1

for x in range(number, 0, -1):
  y = y * x

print(f'{y:,}')
