

def get_int():
    while True:
        try: n = int(input("Num: "))
        except: print("Bad num.")
        else:
            if n >= 0: return n
            print(">= 0 please.")

def fact(n):
    f = 1
    for i in range(1, n + 1): f *= i
    return f if n else 1

def main():
    n = get_int()
    print(f"Fact: {fact(n)}")

class TestFact(unittest.TestCase):
    def test_0(self): self.assertEqual(fact(0), 1)
    def test_5(self): self.assertEqual(fact(5), 120)
    def test_in(self):
        with unittest.mock.patch('builtins.input', return_value='3'): self.assertEqual(get_int(), 3)
    def test_in_bad(self):
        with unittest.mock.patch('builtins.input', side_effect=['a', '4']): self.assertEqual(get_int(), 4)
    def test_in_neg(self):
        with unittest.mock.patch('builtins.input', side_effect=['-1', '5']): self.assertEqual(get_int(), 5)

if __name__ == "__main__":
    unittest.main(argv=['ignored'], exit=False)
    main()
