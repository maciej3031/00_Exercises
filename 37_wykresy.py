import pylab

a = 2

x = pylab.arange(-10,11,0.1)

y1 = [i/(-3) + a for i in x if i <= 0]
y2 = [(i*i)/3 + a for i in x if i > 0]

pylab.plot(x[:len(y1)],y1,x[-len(y2):],y2,)
pylab.title("Wykres f(x)")
pylab.grid(True)
pylab.show()