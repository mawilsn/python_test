import pytest

import main


def test_main():
    assert main.thing() == "hello_world"
