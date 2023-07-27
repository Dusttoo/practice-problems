numbers_list = []

with open('lottotexas.csv') as lucky_numbers:
    numbers = lucky_numbers.readlines()
    for line in numbers:
        if line[0] == ',':
            for num in line[1:].split(','):
                numbers_list.append(num.strip())
        else:
            for num in line.split(','):
                numbers_list.append(num.strip())

most_common_nums = {}

for num in numbers_list:
    if num in most_common_nums.keys():
        most_common_nums[num] += 1
    else:
        most_common_nums[num] = 1

print(most_common_nums)

lucky_nums = []

for k, v in most_common_nums.items():
    lucky_nums.append(k)

print(
    f'Your lucky numbers are: {lucky_nums[0:5]} and {lucky_nums[5]}')
