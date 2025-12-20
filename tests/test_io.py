import pytest
from src.utils.io import read_file, write_file


def test_read_and_write_file(tmp_path):


    """Testuje funkcje read_file i write_file."""


    test_file = tmp_path / "test_message.txt"
    content = "Przybyłem, zobaczyłem, zwyciężyłem!"

    write_file(test_file, content)
    assert test_file.exists()

    read_content = read_file(test_file)
    assert read_content == content


def test_read_file_nonexistent():


    """Testuje odczyt z nieistniejącego pliku."""


    with pytest.raises(FileNotFoundError):
        read_file("nonexistent.txt")



