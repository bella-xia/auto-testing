import unittest
from minium_test import TestInput

if __name__ == "__main__":
    loaded_suite = unittest.TestLoader().loadTestsFromTestCase(TestInput)
    result = unittest.TextTestRunner().run(loaded_suite)
    print(result)
