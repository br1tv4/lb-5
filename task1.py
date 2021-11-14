import random
list1 = ['Hello ', 'Good morning ', 'Good afternoon ', 'Good evening ']
list2 = ['Vlad ', 'Dima ', 'Nikita ', 'Sasha ']
list3 = ['Whats up?', 'How are you doing?', 'How are things going?', 'How are you getting on?']

string_list = [list1, list2, list3]

def random_phrase():
    result_string = ''
    for i in range(0, 3):
        random_index = random.randrange(0, 7)
        random_phrase = result_string + string_list[i][random_index] + ''

    return result_string

print(random_phrase())