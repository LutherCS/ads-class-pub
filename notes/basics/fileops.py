filename = 'sample.in'

people = []

with open(filename, 'r') as foo:
    foo.readline()
#     people = foo.read().split('\n')
    for line in foo:
        # print(line.strip())
        people.append(line.strip())
print(people)
print(sorted(people))
print(sorted(people, key=lambda x: len(x)))