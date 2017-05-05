# funkcja pso, która szuka minimum globalnego podanej funkcji przy pomocy algorytmu PSO
# function - funkcja do optymalizacji
# particles - liczba czasteczek
# xmin - dolne ograniczenie
# xmax - gorne ograniczenie
# q - wagi przypisywane elementom ustalajacym velocity
# maxiter - liczba iteracji
# funkcja pso zwraca liste zawierajaca historie najlepszych znalezionych dotychczas rozwiazan

import math
import random

random.seed()


def schaffer2(x):
    # funkcja 2 zmiennych
    return 0.5 + (((math.sin(x[0] ** 2 + x[1] ** 2) ** 2) - 0.5) / (1 + (0.001 * (x[0] ** 2 + x[1] ** 2))) ** 2)
    # return x[0] + 7
    # return x[0]**2 - x[1]**3 - 2
    # return x[0]**2 - x[1]**3 - x[2]**2 - 2


def pso(function, particles, xmin, xmax, q, maxiter):
    class Particle:
        velocity = []
        position = []
        pers_best = []

        def __init__(self):
            first_pos = Particle.set_random_position()
            self.position = first_pos
            self.velocity = Particle.set_random_velocity()
            self.pers_best = first_pos

        @staticmethod
        def set_random_position():
            position = []
            for i in range(len(xmin)):
                p = random.uniform(xmin[i], xmax[i])
                position.append(p)
            return position

        @staticmethod
        def set_random_velocity():
            velocity = []
            for i in range(len(xmin)):
                v = random.uniform(xmin[i], xmax[i])
                velocity.append(v)
            return velocity

        def update_velocity(self, glob_best_pos):
            vel = []
            for i in range(len(xmin)):
                r1 = random.random()
                r2 = random.random()
                first = q[1] * r1 * (glob_best_pos[i] - self.position[i])
                second = q[2] * r2 * (self.pers_best[i] - self.position[i])
                vel.append(q[0] * self.velocity[i] + first + second)
            self.velocity = vel

        def update_position(self):
            new_pos = []
            for i in range(len(xmin)):
                temp_pos = self.position[i] + self.velocity[i]
                if xmin[i] <= temp_pos <= xmax[i]:
                    new_pos.append(temp_pos)
                elif temp_pos > xmax[i]:
                    new_pos.append(xmax[i])
                else:
                    new_pos.append(xmin[i])

            self.position = new_pos

    swarm = []  # rój
    solution = []  # historia rozwiązań w każdej z iteracji

    for i in range(particles):
        part = Particle()
        swarm.append(part)

    for i in range(maxiter):
        print("Iteracja {}".format(i))
        glob_best_pos = Particle.set_random_position()
        for j in range(particles):
            swarm[j].update_velocity(glob_best_pos)
            swarm[j].update_position()
            if function(swarm[j].position) < function(swarm[j].pers_best):
                swarm[j].pers_best = swarm[j].position
            if function(swarm[j].position) < function(glob_best_pos):
                glob_best_pos = swarm[j].position
        solution.append(glob_best_pos)

    return solution


result = pso(function=schaffer2, particles=100, xmin=[-20, -20], xmax=[20, 20], q=[0.3, 0.3, 0.4], maxiter=1000)
print(result)
print('\nMinimum to: ', schaffer2(result[-1]), 'dla argumentów: ', result[-1])
print('\nMinimum w przybliżeniu to: ', round(schaffer2(result[-1]), 5), 'dla argumentów: ', [round(i, 5) for i in result[-1]])
