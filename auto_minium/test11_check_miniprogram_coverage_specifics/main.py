import unittest, minium_tests.page_checker_log02

if __name__ == "__main__":
    loaded_suite = unittest.TestLoader().loadTestsFromTestCase(minium_tests.page_checker_log02.PageChecker)
    result = unittest.TextTestRunner().run(loaded_suite)
    