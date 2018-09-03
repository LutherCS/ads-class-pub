'''presidents import statement'''
__name__ = "presidents"

from .presidents import get_most_alive_year
from .presidents import get_most_alive_all_years
from .presidents import get_number_of_presidents_alive
from .presidents import get_names_of_presidents_alive
from .presidents import print_all_names

__all__ = [
    'get_most_alive_year',
    'get_most_alive_all_years',
    'get_number_of_presidents_alive',
    'get_names_of_presidents_alive',
    'print_all_names'
    ]
