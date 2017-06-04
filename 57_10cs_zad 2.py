S = ' 779091968 23 Sep 2009 system.zip\n 284164096 14 Aug 2013 to-do-list.xml\n 714080256 19 Jun 2013 blockbuster.mpeg\n       329 12 Dec 2010 notes.html\n 444596224 17 Jan 1950 delete-this.zip\n       641 24 May 1987 setup.png\n    245760 16 Jul 2005 archive.zip\n 839909376 31 Jan 1990 library.dll'
L = """        68 23 Sep 2009 system.zip"""
from datetime import datetime


def solution(S):
    counter = 0
    for line in S.splitlines():
        data = ([int(line[:10]),
                     datetime.strptime(line[11:22], '%d %b %Y')])
        if data[0] >= 240*(2**10) and data[1] > datetime(year=1990, month=1, day=31):
            counter += 1
    if counter > 0:
        return "%i" % counter
    else:
        return "NO FILES"

print(solution(S))

