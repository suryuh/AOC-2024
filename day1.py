with open("day1.in", "r") as f:
    data = [i for i in f.read().split("\n")]

left_nums = []
right_nums = []
smallest_left_num = 0
smallest_right_num = 0

for line in data:
    num_1, num_2 = line.split("   ")
    
    left_nums.append(int(num_1))
    right_nums.append(int(num_2))

left_nums.sort()
right_nums.sort()

distance = 0

for i in range(len(left_nums)):
    distance += abs(left_nums[i] - right_nums[i])

print(distance)


#part dosuno
ting1 = 0
tingtotal = 0
for i in range(len(left_nums)):
    ting1 += (left_nums[i] * (right_nums.count(left_nums[i])))
    tingtotal += ting1
    ting1 = 0
print(tingtotal)


    
    

    