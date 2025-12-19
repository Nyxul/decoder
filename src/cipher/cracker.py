import string
from typing import List, Tuple

class CipherCracker:


    def __init__ (self):


        self.alphabet = string.ascii_lowercase
        self.alphabet_len = len(self.alphabet)


    def _shift_char(self, char: str, shift: int) -> str:
        

        """
        ------------------------------------------------------------------------
        Przesuwa pojedynczy znak o określoną liczbę miejsc w alfabecie.

        Args:
            char (str): Pojedynczy znak do przesunięcia.
            shift (int): Liczba miejsc do przesunięcia znaku.

        Returns:
            str: Przesunięty znak.
        -----------------------------------------------------------------------
        """


        if char.lower() not in self.alphabet:
            return char
        
        is_upper = char.isupper()
        char_lower = char.islower()

        idx = self.alphabet.index(char_lower)

        new_idx = (idx + shift) % self.alphabet_len
        new_char = self.alphabet[new_idx]

        return new_char.upper() if is_upper else new_char
    
    
    def decrypt(self, text: str, shift: int) -> str:
        

        """
        ------------------------------------------------------------------------
        Odszyfrowuje tekst poprzez przesunięcie o określoną liczbę miejsc w 
        alfabecie.

        Args:
            text (str): Tekst do odszyfrowania.
            shift (int): Liczba miejsc do przesunięcia znaków w tekście.

        Returns:
            str: Odszyfrowany tekst.        
        -----------------------------------------------------------------------
        """


        return ''.join(self._shift_char(char, shift) for char in text)
    

    def brute_force_decrypt(self, text: str) -> List[Tuple[int, str]]:
        

        """
        ------------------------------------------------------------------------
        Uzywa brute-force, próbując wszystkich możliwych przesunięć.

        Args:
            text (str): Tekst do odszyfrowania. 

        Returns:
            List[Tuple[int, str]]: Lista krotek zawierających przesunięcie 
            i odpowiadający odszyfrowany tekst.
        -----------------------------------------------------------------------
        """

        
        results = []

        for shift in range(1, self.alphabet_len):

            decrypted_text = self.decrypt(text, shift)
            results.append((shift, decrypted_text))
        
        return results
