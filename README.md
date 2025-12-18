
# Decoder

Narzędzie do łamania szyfru metodą brute-force z automatyczną detekcją poprawnej wiadomości w języku polskim. Program testuje wszystkie przesunięcia alfabetu, analizuje wyniki i wyodrębnia prawidłowy tekst.



## Zakres zadania

Celem projektu jest:
- przetestowanie wszystkich możliwych przesunięć alfabetu (26),
- wygenerowanie kompletu odszyfrowanych wersji tekstu,
- automatyczne wykrycie poprawnej wiadomości w języku polskim,
- wyodrębnienie adresu e-mail z poprawnie odszyfrowanego komunikatu.

## Założenia i ograniczenia

- Obsługiwany alfabet: łaciński (A–Z, a–z).
- Znaki specjalne (spacje, przecinki, kropki, dwukropki, @) nie podlegają szyfrowaniu.

## Architektura projektu

```text
├── data
│   └── input.txt
├── docs
├── LICENSE
├── README.md
├── requirements.txt
├── src
│   ├── model
│   └── utils
│       └── io.py
└── tests
 ```

Projekt został podzielony na logiczne moduły:

- `data` – dane wejściowe,
- `docs/` – dokumentacja projektowa,
- `src/` – kod źródłowy aplikacji,
- `tests/` – testy jednostkowe.

## Autor

Nazywam się Mateusz Urbańczyk, jestem studentem IV roku Automatyki i Robotyki na Akademi Górniczo-Hutniczej w Krakowie. Obszarem moich zainteresowań są algorytmy, badania operacyjne oraz modele uczenia maszynowego.

Kontakt: mateusz.u.779@icloud.com