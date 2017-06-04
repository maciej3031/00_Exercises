def solution(file_object):
    content = file_object.readlines()
    for line in [x.strip() for x in content]:
        try:
            if line in ('0', '+0', '-0') or not line.startswith(('0', '+0', '-0')):
                line = int(line)
                if -1000000000 <= line <= 1000000000:
                    yield line
        except ValueError:
            pass

file = open('test.txt')

for i in solution(file):
    print(i)

file.close()