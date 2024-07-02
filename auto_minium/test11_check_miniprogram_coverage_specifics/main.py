import unittest
# coverage
import minium_tests.miniprogram_checker_wx0bc8123197e70985 as test_script

if __name__ == "__main__":
    # cov = coverage.Coverage()
    # cov.start()
    loaded_suite = unittest.TestLoader().loadTestsFromTestCase(test_script.Miniprogram_Checker)
    result = unittest.TextTestRunner().run(loaded_suite)

    # cov.stop()
    # cov.save()

    # cov.html_report()
    