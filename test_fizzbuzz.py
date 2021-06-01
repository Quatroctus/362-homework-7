import unittest
from fizzbuzz import fizzbuzz

def test_number(capsys):
    fizzbuzz()

    output_lines = capsys.readouterr().out.split('\n')[:-1]

    assert output_lines[0] == "1"
    assert output_lines[1] == "2"
    assert output_lines[3] == "4"

