import re

phonePattern = re.compile(r'''
                # nie dopasowuj początku łańcucha, numer może się zacząć gdziekolwiek
    (\d{3})     # numer kierunkowy - 3 cyfry (np. '800')
    \D*         # opcjonalny nienumeryczny separator
    (\d{3})     # pierwsza część numeru - 3 cyfry (np. '555')
    \D*         # opcjonalny separator
    (\d{4})     # druga część numeru (np. '1212')
    \D*         # opcjonalny separator
    (\d*)       # numer wewnętrzny jest opcjonalny i może mieć dowolną długość
    $           # koniec łańcucha
    ''', re.VERBOSE)

#phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') #<-- znaczy to sam oco powyżej

phone = re.search(phonePattern, 'work 1-(800) 555.1212 #1234').groups()

print(phone)

