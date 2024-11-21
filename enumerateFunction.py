# 21.11.2024

# when you work with iterators, you need to know the value of iterator and index of iterator
# for this reason python build the function enumerate()

list_1 = ['python','java','PHP','C','C++']

# create enumerate object
programming_languages = enumerate(list_1)
next_programming_languages = next(programming_languages)
print(f'next programming language is : {next_programming_languages}')

print(list(enumerate(list_1)))

# change list to tuple
for ele in enumerate(list_1):
    print(ele)

# change index of list
for count, ele in enumerate(list_1,100):
    print(count,ele)