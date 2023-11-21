"""
This module contains a unit test for the `optimal_order` function in the `govern` module.
The `TestOptimalOrder` class contains a single test case that checks 
if the function returns the expected result.
The test data is written to a file, the function is called with the input file and an output file,
and the result is compared to the expected output.
The input and output files are then deleted.
"""
import unittest
import os
import sys
sys.path.append('/Users/ledan404/projects/labs_algo/lab5') # past your path here to root of repo
from src.govern import optimal_order


class TestOptimalOrder(unittest.TestCase):
    def test_optimal_order(self):
        input_file = "test_input.in"
        output_file = "test_output.out"

        # Записати тестові дані в файл
        with open(input_file, "w", encoding="utf-8") as file:
            file.write(
                "visa foreignpassport\n"
                "visa hotel\n"
                "visa bankstatement\n"
                "bankstatement nationalpassport\n"
                "hotel creditcard\n"
                "creditcard nationalpassport\n"
                "nationalpassport birthcertificate\n"
                "foreignpassport nationalpassport\n"
                "foreignpassport militarycertificate\n"
                "militarycertificate nationalpassport\n"
            )

        # Викликати функцію, яку ви написали
        optimal_order(input_file, output_file)

        # Зчитати очікуваний результат
        with open(output_file, "r", encoding="utf-8") as file:
            expected_result = [line.strip() for line in file]

        # Перевірити, чи отриманий результат відповідає очікуваному
        self.assertEqual(
            expected_result,
            [
                "birthcertificate",
                "nationalpassport",
                "militarycertificate",
                "foreignpassport",
                "creditcard",
                "hotel",
                "bankstatement",
                "visa",
            ],
        )

        # Перевірити, чи вихідні файли були створені
        self.assertTrue(os.path.isfile(input_file))
        self.assertTrue(os.path.isfile(output_file))

        # Видалити тестові файли
        os.remove(input_file)
        os.remove(output_file)


class TestOptimalOrder2(unittest.TestCase):
    def test_optimal_order2(self):
        input_file = "test_input.in"
        output_file = "test_output.out"

        # Записати тестові дані в файл
        with open(input_file, "w", encoding="utf-8") as file:
            file.write("visa foreignpassport\n")

        # Викликати функцію, яку ви написали
        optimal_order(input_file, output_file)

        # Зчитати очікуваний результат
        with open(output_file, "r", encoding="utf-8") as file:
            expected_result = [line.strip() for line in file]

        # Перевірити, чи отриманий результат відповідає очікуваному
        self.assertEqual(expected_result, ["foreignpassport", "visa"])

        # Перевірити, чи вихідні файли були створені
        self.assertTrue(os.path.isfile(input_file))
        self.assertTrue(os.path.isfile(output_file))

        # Видалити тестові файли
        os.remove(input_file)
        os.remove(output_file)


if __name__ == "__main__":
    unittest.main()
