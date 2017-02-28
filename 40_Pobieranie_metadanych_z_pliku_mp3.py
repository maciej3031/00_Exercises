u"""Framework do pobierania matedanych specyficznych dla danego typu pliku.

Można utworzyć instancję odpowiedniej klasy podając jej nazwę pliku w konstruktorze.
Zwrócony obiekt zachowuje się jak słownik posiadający parę klucz-wartość
dla każdego fragmentu metadanych.

Framework może być roszerzony poprzez dodanie klas dla poszczególnych typów plików, np.:
HTMLFileInfo, MPGFileInfo, DOCFileInfo.  Każda klasa jest całkowicie odpowiedzialna
za właściwe sparsowanie swojego pliku; zobacz przykład MP3FileInfo."""

import sys, os

def stripnulls(data):
    u"usuwa białe znaki i nulle"
    return data.replace(b"\00", b" ").strip()

class FileInfo(dict):
    u"Przechowuje metadane pliku"
    def __init__(self, filename = None):
        dict.__init__(self)
        self["plik"] = filename

class MP3FileInfo(FileInfo):
    u"przechowuje znaczniki ID3v1.0 MP3"
    tagDataMap = {"tytuł"  : (3, 33, stripnulls),
                  "artysta" : (33, 63, stripnulls),
                  "album"   : (63, 93, stripnulls),
                  "rok"     : (93, 97, stripnulls),
                  "komentarz": (97,126, stripnulls),
                  "gatunek" : (127, 128, ord)}

    def __parse(self, filename):
        u"parsuje znaczniki ID3v1.0 z pliku MP3"
        try:
            fsock = open(filename, "rb", 0)
            try:
                fsock.seek(-128,2)
                tagdata = fsock.read(128)
            finally:
                fsock.close()
            if tagdata[:3] == b'TAG':
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])
        except IOError:
            print("Blad")

    def __setitem__(self, key, value):
        if key == "plik" and value:
            self.__parse(value)
        FileInfo.__setitem__(self, key, value)

def listDirectory(directory, fileExtList):
    u"zwraca listę obiektów zawierających metadane dla plików o podanych rozszerzeniach"
    fileList = [os.path.normcase(f) for f in os.listdir(directory)]
    fileList = [os.path.join(directory, f) for f in fileList if os.path.splitext(f)[1] in fileExtList ]

    def getFileInfoClass(filename, module = sys.modules[FileInfo.__module__]):
        u"zwraca klasę metadanych pliku na podstawie podanego rozszerzenia"
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
    return [getFileInfoClass(f)(f) for f in fileList]

if __name__ == "__main__":
    for info in listDirectory(r"C:\Users\Krysia\Dropbox\Praca\Programowanie\01_Python\02_Python_files\01_Training_files\music", [".mp3"]):
        print("\n".join(["%s = %s" % (k, v) for k, v in info.items()]))
        print()