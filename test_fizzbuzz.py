import unittest
from fizzbuzz import fizzbuzz

def test_number(capsys):
    fizzbuzz()

    output_lines = capsys.readouterr().out.split('\n')[:-1]

    assert output_lines[0] == "1"
    assert output_lines[1] == "2"
    assert output_lines[3] == "4"


def test_fizz(capsys):
    fizzbuzz()

    output_lines = capsys.readouterr().out.split()[:-1]

    assert output_lines[2] == "Fizz"
    assert output_lines[5] == "Fizz"
    assert output_lines[8] == "Fizz"


def test_buzz(capsys):
    fizzbuzz()

    output_lines = capsys.readouterr().out.split()[:-1]

    assert output_lines[4] == "Buzz"
    assert output_lines[9] == "Buzz"
    assert output_lines[19] == "Buzz"
