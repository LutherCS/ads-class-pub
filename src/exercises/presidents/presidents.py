'''
Incoming assessment
Find the year when the most US presidents were alive
Use pytest to test your implementation
'''

from datetime import datetime as dt


def build_dictionary(filename: str) -> dict:
    '''Build a dictionary of presidents from the input file'''
    current_year = dt.today().year
    people = set()
    the_dict = dict()

    with open(filename, 'r') as file_in:
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

    for year in range(born_first[1], died_last[2]):
        for name, born, died in people:
            if born <= year <= died:
                if year not in the_dict:
                    the_dict[year] = [name]
                else:
                    the_dict[year].append(name)

    return the_dict


def get_number_of_presidents_alive(presidents_dict: dict, year: int) -> int:
    '''Return the number of presidens alive that year'''
    pass


def get_names_of_presidents_alive(presidents_dict: dict, year: int) -> list:
    '''Return the names of presidens alive that year'''
    pass


def get_most_alive_year(presidents_dict: dict) -> int:
    '''Find the year when the most presidents were alive'''
    return max(presidents_dict, key=lambda x: len(set(presidents_dict[x])))


def get_most_alive_all_years(presidents_dict: dict) -> list:
    '''Return all years when the largest number of presidens were alive'''
    pass


def print_all_names(presidents_dict: dict, year: int) -> None:
    pass


def main():
    '''Main function'''
    the_dict = build_dictionary('data/presidents.txt')
    the_year = get_most_alive_year(the_dict)
    print(the_year)

if __name__ == '__main__':
    main()
