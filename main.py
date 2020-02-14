from reader import reader
from writer import writer
from car import Car

if __name__ == "__main__":
    R,C,F,N,B,T,rides = reader("a_example.in")

    carList = []
    for i in range(0,F):
        carList.append(Car())
    while Car.step < T:
        isCarFunc = 0
        for car in carList:
            rides = car.update(rides)

    writer("result.in", carList)
