import pytest
from unittest.mock import patch
from main import hello_world, personalized_greeting


def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out


@patch('rich.console.Console.input', return_value='World')
def test_personalized_greeting(mock_input, capsys):
    personalized_greeting()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out

