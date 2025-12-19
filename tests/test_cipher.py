import pytest
from src.cipher.cracker import CipherCracker


class TestCipherCracker:
    
    
    @pytest.fixture
    def cracker(self):
        return CipherCracker()
    

    @pytest.mark.parametrize("char, shift, expected", [
        ('a', 1, 'b'),
        ('z', 1, 'a'),      # Przejście przez koniec alfabetu
        ('A', 1, 'B'),      # Wielka litera
        ('Z', 1, 'A'),      # Wielka litera z przejściem
        ('a', 26, 'a'),     # Pełny obrót
        ('!', 5, '!'),      # Znak specjalny
        (' ', 10, ' '),     # Spacja
        ('5', 3, '5'),      # Cyfra
    ])


    def test_shift_char(self, cracker, char, shift, expected):


        """Testuje przesuwanie pojedynczych znaków."""


        assert cracker._shift_char(char, shift) == expected


    def test_decrypt(self, cracker):
    

        """Testuje odszyfrowanie całego zdania."""


        encrypted_text = "bcdef"
        shift = 1

        assert cracker.decrypt(encrypted_text, shift) == "abcde"


    def test_brute_force_decrypt(self, cracker):
        

        """Sprawdza, czy brute force zwraca dokładnie 25 wariantów."""


        results = cracker.brute_force_decrypt("test")

        assert len(results) == cracker.alphabet_len - 1

        shifts = [r[0] for r in results]
        assert 1 in shifts
        assert 25 in shifts