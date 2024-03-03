from test_minium import Minium_Query
import unittest

if __name__ == "__main__":

    loaded_suite = unittest.TestLoader().loadTestsFromTestCase(Minium_Query)
    result = unittest.TextTestRunner().run(loaded_suite)
    print(result)
