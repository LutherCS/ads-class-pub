"""
Testing the Max Binary Heap module
Roman Yasinovskyy, 2018
"""

import pytest
from exercises.heaps import BinaryHeapMax


class TestBinaryHeapMethods:
    """Testing the Max Binary Heap module"""

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        """Setting up"""
        self.b_movie_heap = BinaryHeapMax()
        self.b_movie_heap.insert("Alfred")
        self.b_movie_heap.insert("Batman")
        self.b_movie_heap.insert("Catwoman")
        self.b_movie_heap.insert("Dent")
        self.b_movie_heap.insert("Elfo")
        self.b_movie_heap.insert("Frodo")
        self.b_movie_heap.insert("Gordon")
        self.b_movie_heap.insert("Pavel")
        self.b_movie_heap.insert("Robin")

        self.b_movie_heap_5 = BinaryHeapMax(5)
        self.b_movie_heap_5.insert("Alfred")
        self.b_movie_heap_5.insert("Batman")
        self.b_movie_heap_5.insert("Catwoman")
        self.b_movie_heap_5.insert("Dent")
        self.b_movie_heap_5.insert("Elfo")
        self.b_movie_heap_5.insert("Frodo")
        self.b_movie_heap_5.insert("Gordon")
        self.b_movie_heap_5.insert("Pavel")
        self.b_movie_heap_5.insert("Robin")

    def test_len(self):
        """Testing __len__ method"""
        assert len(self.b_movie_heap) == 9
        assert len(self.b_movie_heap_5) == 5

    def test_str(self):
        """Testing __str__ method"""
        assert (
            str(self.b_movie_heap)
            == "['Robin', 'Pavel', 'Frodo', 'Gordon', 'Catwoman', 'Batman', 'Elfo', 'Alfred', 'Dent']"
        )
        assert (
            str(self.b_movie_heap_5) == "['Robin', 'Pavel', 'Elfo', 'Frodo', 'Gordon']"
        )


if __name__ == "__main__":
    pytest.main(["test_heaps.py"])
