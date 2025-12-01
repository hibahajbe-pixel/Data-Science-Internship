# Client Project: Average temperature calculator

n = int(input("How many temperature readings? "))
temps = []

for i in range(n):
    val = float(input(f"Enter reading {i+1}: "))
    temps.append(val)

avg = sum(temps) / n

print("Average Temperature:", avg)
