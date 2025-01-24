# 2. During a marathon, the system tracks distances covered by runners every hour for 5 hours. Write 
# a program to calculate the total distance run by each of 3 participants

print("Enter distances covered by 3 participants for 5 hours:")

distances = []
for i in range(3):
    print(f"Enter distances for Participant {i + 1} (space-separated for 5 hours):")
    hours = list(map(float, input().split()))
    distances.append(sum(hours))

for i in range(3):
    print(f"Total distance run by Participant {i + 1}: {distances[i]} units")
