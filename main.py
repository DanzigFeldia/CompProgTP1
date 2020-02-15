from reader import reader
from writer import writer
from car import Car

if __name__ == "__main__":
    R,C,F,N,B,T,rides = reader("c_no_hurry.in")

    carList = []
    for i in range(0,F):
        carList.append(Car(B))
    while Car.step < T:
        isCarFunc = 0
        for car in carList:
            rides = car.update(rides)
            if car.occupation != -1:
                isCarFunc +=1
        if isCarFunc == 0:
            break
        Car.step +=1
    writer("result.in", carList)
    print(Car.score)
