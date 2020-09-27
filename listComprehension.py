nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
my_list = []

for n in nums:
    my_list.append(n)

# list comprehension style the above for loop
my_list = [n for n in nums]
print my_list

my_list_2 = []

for n in nums:
    my_list_2.append(n*n)
print my_list_2

my_list_2 = [n*n for n in nums]
print my_list_2