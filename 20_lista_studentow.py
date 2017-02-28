class Student():
    name = ""
    surname = ""
    album = ""
    grade = ""

studenci = []
nr = 0
s = 0
while True:
    na = input("give a surname of a student number {}".format(nr+1))
    if not na: break
    studenci.append(Student())      #tworzy nowy obiekt w liście i przypisuje mu klasę Student
    studenci[nr].surname = na
    studenci[nr].name = input("give a name of a student number {}".format(nr+1))
    studenci[nr].album = int(input("give a album number of a student number {}".format(nr+1)))
    studenci[nr].grade = float(input("give a grade of a student number {}".format(nr+1)))
    s = s + studenci[nr].grade
    nr += 1

print("\n%-4s %-14s %-10s %-14s %-7s" % ("L.p.","Surname","Name","Number","Grade"))
for i in studenci:
    print("%3i. %-14s %-10s %-14i %-7.1f" % (studenci.index(i)+1 , i.surname, i.name, i.album, i.grade))    #- wyrównuje do lewej

print("\nAverage grade of students: {}".format(s/len(studenci)))
