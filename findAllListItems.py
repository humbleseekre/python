'''
write a python function to index all items in a list
Input: List to search, value to search for
Output: list of indices

example = [[[1,2,3], 2, [1,3]], [1,2,3]]

output = [[0,0,1], [0,1], [1,1]]
'''

example = [[[1,2,3], 2, [1,3]], [1,2,3]]

def index_all(search_list, item):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], item):
                indices.append([i]+index)
    return indices


print(index_all(example, 2))