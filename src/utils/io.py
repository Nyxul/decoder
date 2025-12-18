from pathlib import Path
from typing import Union


def read_file(file_path: Union[str, Path]) -> str:


    """
    ------------------------------------------------------------------------
    Wczytuje zawartość pliku tekstowego z podanej ścieżki.

    Args:
        file_path (Union[str, Path]): Ścieżka do pliku tekstowego.

    Returns:
        str: Zawartość pliku jako łańcuch znaków.

    Raises:
        FileNotFoundError: Jeśli plik nie istnieje.
    -----------------------------------------------------------------------
    """


    path = Path(file_path)

    if not path.exists():

        raise FileNotFoundError(f"Plik {file_path} nie istnieje.")
    
    return path.read_text(encoding='utf-8')


def write_file(file_path: Union[str, Path], content: str) -> None:


    """
    ------------------------------------------------------------------------
    Zapisuje zawartość do pliku tekstowego pod podaną ścieżką.

    Args:
        file_path (Union[str, Path]): Ścieżka do pliku tekstowego.
        content (str): Zawartość do zapisania w pliku.

    Returns:
        None
    -----------------------------------------------------------------------
    """


    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')