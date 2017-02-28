print("podaj liczbe")

a = input()

try:
    int(a)
    print("Całkowita")

except ValueError as e:
    try:
        float(a)
        print("Niecałkowita")

    except Exception as e:
        print("Błędna wartość, użyj kropki zamiast przecinka")