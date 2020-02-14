def writer(name, cars):
    with open(name, "w") as f:
        for car in cars:
            f.write(str(len(car.rCompleted)))
            for ride in car.rCompleted:
                f.write(" " + str(ride))
            f.write("\n")