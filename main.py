from reader import reader
from writer import writer
from car import Car

if __name__ == "__main__":
    with open("log.in", "w") as log:
        R,C,F,N,B,T,rides = reader("e_high_bonus.in")

        carList = []
        for i in range(0,F):
            carList.append(Car(B, T))
        while Car.step < T:
            isCarFunc = 0
            for car in carList:
                car.update(rides)
                log.write("Car : " + str(car.id) + " - rides : " + str(car.occupation) + " - position : " + str(car.pos) + " - target : " + str(car.target) + "\n")
                if car.stopped != 1:
                    isCarFunc +=1
            if isCarFunc == 0:
                break
            Car.step +=1
        writer("result.in", carList)
        print(Car.score)
