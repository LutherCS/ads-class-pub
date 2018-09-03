'''
Incoming assessment
'''

from datetime import datetime as dt

current_year = dt.today().year
people = set()

with open('data/presidents.txt', 'r') as file_in:
    for line in file_in:
        name = ''
        born = None
        died = None

        line_lst = line.split()
        for item in line_lst:
            if not str.isdigit(item):
                name = name + item + ' '
            elif not born:
                born = int(item)
            else:
                died = int(item)
        if not died:
            died = current_year + 1
        people.add((name.strip(), born, died))

died_last = max(people, key=lambda x: x[2])
born_first = min(people, key=lambda x: x[1])

the_dict = dict()

for year in range(born_first[1], died_last[2]):
    for name, born, died in people:
        if born <= year <= died:
            if year not in the_dict:
                the_dict[year] = [name]
            else:
                the_dict[year].append(name)

# for k, v in the_dict.items():
#     print('{}: {}'.format(k, v))

the_year = max(the_dict, key=lambda x : len(the_dict[x]))
print(the_year)
