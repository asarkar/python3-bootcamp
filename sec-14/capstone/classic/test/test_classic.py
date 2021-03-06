import capstone.classic.functions as classic


class TestClassic:
    def test_collatz(self):
        assert classic.collatz(12) == 10
        assert classic.collatz(19) == 21

    def test_closest_pair(self):
        p1 = classic.Point2D(2, 3)
        p2 = classic.Point2D(3, 4)
        closest = classic.closest_pair([
            p1,
            classic.Point2D(12, 30),
            classic.Point2D(40, 50),
            classic.Point2D(5, 1),
            classic.Point2D(12, 10),
            p2
        ])
        assert closest == (p1, p2)

    def test_sieve_of_eratosthenes(self):
        assert classic.sieve_of_eratosthenes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    def test_bubble_sort(self):
        nums = [10, 3, 5, 12, 9, 10]
        classic.bubble_sort(nums)
        assert nums == [3, 5, 9, 10, 10, 12]
