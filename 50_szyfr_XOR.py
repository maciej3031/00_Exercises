def encryption(text, key):
    try:
        assert isinstance(key, int)
        assert 5 <= key <= 255
    except AssertionError:      # wyłapujemy błędne dane
        print("Błędny klucz. Klucz musi być liczbą całkowitą z przedziału [5,255]")
    else:
        bin_text_list = ["{0:b}".format(ord(x)) for x in text]  # tworzymy listę binarnych, stringowych odpowiedników każej litery
        bin_key = "{0:09b}".format(key)     # tworzymy binarny, stringowy odpowiednik klucza
        result_list = []
        for i in bin_text_list:     # dla każdej litery zapisanej binarnie
            char_list = []
            for j, k in enumerate(i):   # dla każdej 1 lub 0 w binarnym zapisie litery
                if int(k) != int(bin_key[j]):   # sprawdzamy czy ta 1 lub 0 jest równe 1 lub 0 na odpowiadającym im miejscu w binarnie zapisanym kluczu
                    char_list.append("1")       # jeżeli nie sąrówne zwracamy 1
                else:
                    char_list.append("0")       # jeżeli są równe zwracamy 0
            result_list.append("".join(char_list))  # łączymy ciąg 1 i 0 stringową liczbę binarną
        return "".join([chr(int(x, 2)) for x in result_list])   #zamieniamy liczbę na int, potem na odpowiedni znak, a potem łączymy znaki w zaszyfrowane zdanie

print(encryption("Maciek", 8))