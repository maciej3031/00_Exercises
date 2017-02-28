print("\tPodaj stan początkowy konta")
SPK = input()
SPK = float(SPK)

print("\tpodaj liczbę lat")
N = input()
N = int(N)

print("\tpodaj stopę procentową w %")
P = input()
P = float(P)

SKK = SPK * (1 + P/(100*12))**(N*12)
SKK = round(SKK,2)
print("\tPrzy miesięcznej kapitalizacji odsetek, za {} lat będziesz mieć na koncie {} zł".format(N,SKK))

print("\tNaciśnij dowolny klawisz aby kontynuować")
a = input()