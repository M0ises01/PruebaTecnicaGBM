import unittest
import solucion

class TestProcesarCampeonatos(unittest.TestCase):

    def test_case_0(self):
        input_data = [
            "1 3",
            "3 2 1",
            "3",
            "3 5 3 2", 
            "3 5 3 1",
            "3 1 1 1",
            "3 10",
            "1 2 3 4 5 6 7 8 9 10",
            "10 1 2 3 4 5 6 7 8 9",
            "9 10 1 2 3 4 5 6 7 8",
            "2",
            "5 5 4 3 2 1",
            "3 10 5 1",
            "2 4",
            "1 3 4 2",
            "4 1 3 2",
            "2 ",
            "3 3 2 1",
            "3 5 4 2",
            "0 0"
        ]
        input_data = "\n".join(input_data)
        expected_output = ["3", "3", "1 2 3", "3", "3", "2 4", "4"]
        expected_output = "\n".join(expected_output)
        result = solucion.procesar_campeonatos(input_data)
        self.assertEqual(result, expected_output)

    def test_case_1(self):
        input_data = [
            "1 3",
            "3 2 1",
            "3",
            "3 5 3 2",
            "3 5 3 1",
            "3 1 1 1",
            "0 0"
        ]
        input_data = "\n".join(input_data)
        expected_output = ["3", "3", "1 2 3"]
        expected_output = "\n".join(expected_output)
        result = solucion.procesar_campeonatos(input_data)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        input_data = [
            "3 10",
            "1 2 3 4 5 6 7 8 9 10",
            "10 1 2 3 4 5 6 7 8 9",
            "9 10 1 2 3 4 5 6 7 8",
            "2",
            "5 5 4 3 2 1",
            "3 10 5 1",
            "0 0"
        ]
        input_data = "\n".join(input_data)
        expected_output = ["3", "3"]
        expected_output = "\n".join(expected_output)
        result = solucion.procesar_campeonatos(input_data)
        self.assertEqual(result, expected_output)

    def test_case_3(self):
        input_data = [
            "2 4",
            "1 3 4 2",
            "4 1 3 2",
            "2",
            "3 3 2 1",
            "3 5 4 2",
            "0 0"
        ]
        input_data = "\n".join(input_data)
        expected_output = ["2 4", "4"]
        expected_output = "\n".join(expected_output)
        result = solucion.procesar_campeonatos(input_data)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()

