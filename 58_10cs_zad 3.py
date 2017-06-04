S = "1A 1B 1E 1J"
import itertools


def solution(N, S):
    def get_list_of_rows_with_seats_as_only_chars(N, S):
        res = []
        for row in range(1, N + 1):
            temp = []
            for seat in S:
                try:
                    seat_nr = int("".join(itertools.takewhile(str.isdigit, seat)))
                    seat_char = "".join(itertools.dropwhile(str.isdigit, seat))
                    if seat_nr == row:
                        temp.append(seat_char)
                    else:
                        continue
                except ValueError:
                    continue
            res.append(temp)
        return res

    def count_occurrences(array):
        counter = 0
        for row in array:
            if 'A' not in row and 'B' not in row and 'C' not in row:
                counter += 1
            if 'E' not in row and 'F' not in row and ('D' not in row or 'G' not in row):
                counter += 1
            if 'H' not in row and 'J' not in row and 'K' not in row:
                counter += 1
        return counter

    S = S.split(' ')
    array = get_list_of_rows_with_seats_as_only_chars(N, S)
    print(array)
    number = count_occurrences(array)
    return number


print(solution(3, S))


