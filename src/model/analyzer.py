from collections import Counter
import re
import math
from typing import Dict


class TextAnalyzer:




    def __init__(self):


        self.log_probs: Dict[str, float] = {}
        self.min_log_prob = -20.0


    def _clean_text(self, text: str) -> str:


        """
        ------------------------------------------------------------------------
        Czyści tekst, pozostawiając tylko małe litery alfabetu polskiego.

        Args:
            text (str): Tekst do oczyszczenia.
        
        Returns:
            str: Oczyszczony tekst.
        ----------------------------------------------------------------------- 
        """


        text = text.lower()
        text = re.sub(r'[^a-ząćęłńóśźż]', '', text)
        
        return text 
    

    def train(self, text: str) -> None:


        """
        ------------------------------------------------------------------------
        Trenuje analizator na podstawie dostarczonego tekstu, obliczając 
        logarytmy prawdopodobieństw bigramów.

        Args:
            text (str): Tekst treningowy.
        
        Raises:
            ValueError: Jeśli tekst treningowy zawiera mniej niż dwa znaki.
        -----------------------------------------------------------------------
        """


        clean_text = self._clean_text(text)

        if len(clean_text) < 2:
            raise ValueError("Tekst treningowy musi zawierać co najmniej dwa znaki.")
        
        bigrams = [clean_text[i:i+2] for i in range(len(clean_text) - 1)]
        bigram_counts = Counter(bigrams)
        total_bigrams = sum(bigram_counts.values())
        unique_bigrams = len(bigram_counts)

        self.log_probs = {}

        for bg, count in bigram_counts.items():
            
            prob = count / total_bigrams
            self.log_probs[bg] = math.log(prob)

        
        if self.log_probs:
            self.min_log_prob = min(self.log_probs.values()) - 2.0


    def score(self, text: str) -> float:


        """
        ------------------------------------------------------------------------
        Ocena tekstu na podstawie średniego logarytmu prawdopodobieństwa 
        bigramów.

        Args:
            text (str): Tekst do oceny.

        Returns:
            float: Średni logarytm prawdopodobieństwa bigramów w tekście.
        -----------------------------------------------------------------------
        """


        clean_text = self._clean_text(text)

        if len(clean_text) < 2:
            return -float('inf')
        

        score = 0.0
        bigrams = [clean_text[i:i+2] for i in range(len(clean_text) - 1)]

        for bg in bigrams:

            score += self.log_probs.get(bg, self.min_log_prob)

        return score / len(bigrams) if bigrams else -float('inf')