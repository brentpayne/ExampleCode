import copy

def recursively_defined_generator(main_list, length=None, current_index=0, return_list=[]):
    if length is None:
        length = len(main_list)
    for item in main_list[current_index]:
        return_list.append(item)
        if current_index+1 < length:
            generator = recursively_defined_generator(main_list, length, current_index+1, return_list)
            for copy_of_return_list in generator:
                yield copy_of_return_list #value identical to return_list but is a copy
        else:
            yield copy.copy(return_list)
        return_list.pop()
        
def create_all_combinations_where_there_is_only_one_item_from_each_bucket(list_of_lists):
    full_set_of_walks = []
    a_generator = recursively_defined_generator(list_of_lists)
    for a_walk in a_generator:
        full_set_of_walks.append(a_walk)
    return full_set_of_walks

if __name__ == '__main__':
    print create_all_combinations_where_there_is_only_one_item_from_each_bucket([['1'],['2a','2b'],['3a','3b','3c'],['4'],['5']])
