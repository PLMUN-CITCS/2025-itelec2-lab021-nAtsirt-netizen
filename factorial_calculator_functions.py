import unittest, unittest.mock

def get_int():
    while True:
        try:
            n = int(input("Enter non-negative int: "))
            if n >= 0: return n
            print("Invalid: non-negative.")
        except ValueError: print("Invalid: integer.")

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def main():
    n = get_int()
    print(f"Factorial of {n} is: {factorial(n)}")

class TestFactorial(unittest.TestCase):
    def test_zero(self): self.assertEqual(factorial(0), 1)
    def test_positive(self): self.assertEqual(factorial(5), 120)
    def test_input_valid(self):
        with unittest.mock.patch('builtins.input', return_value='3'): self.assertEqual(get_int(), 3)
    def test_input_invalid_text(self):
        with unittest.mock.patch('builtins.input', side_effect=['a', '4']): self.assertEqual(get_int(), 4)
    def test_input_invalid_negative(self):
        with unittest.mock.patch('builtins.input', side_effect=['-1', '5']): self.assertEqual(get_int(), 5)

if __name__ == "__main__":
    unittest.main(argv=['ignored'], exit=False)
    main()
