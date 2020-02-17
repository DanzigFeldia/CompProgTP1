class Car:
    nb_car = 0
    step = 0
    maxStep = 0
    score = 0
    bonus = 0
    bonusMultiplier = 1 #the lower it is, the more important bonuses are (0<x<=1)

    def __init__(self, B, T):
        self.id = Car.nb_car
        self.pos = (0, 0)
        self.rCompleted = []
        self.occupation = -1
        self.inRides = 0 #0 is not in ride, 1 is in ride
        self.target = (0,0)
        self.stopped = 0 #1 when there's no rides anymore
        Car.maxStep = T
        Car.bonus = B
        Car.nb_car += 1

    def assign(self,idRide, ride):
        self.occupation = idRide
        self.target = (ride[0], ride[1])
        Car.score+=abs(ride[2]-ride[0])+abs(ride[3]-ride[1])
        ride[6] = 1
        if (Car.step+self.distance(ride[0],ride[1])) <= ride[4]:
            Car.score += Car.bonus
    def update(self, rides):
        if self.occupation != -1:
            if Car.step >= rides[self.occupation][4]:
                self.move(self.target[0],self.target[1])
                if self.pos == self.target:
                    if self.inRides == 0:
                        self.target = (rides[self.occupation][2],rides[self.occupation][3])
                        self.inRides = 1
                    elif self.inRides == 1:
                        self.inRides =0
                        self.rCompleted.append(self.occupation)
                        self.occupation = -1
                    else:
                        print("error")
        if self.occupation == -1 and self.stopped == 0:
            closest = self.findMostProfitable(rides)
            if closest != -1:
                self.assign(closest, rides[closest])

            elif closest == -1:
                self.stopped = 1


        #return rides

    def distance(self, a,b): #target is (x,y)
        return abs(self.pos[0]-a)+abs(self.pos[1]-b)

    def findClosestAcceptable(self, rides):
        closest = (999999999999999999, -1)  # distance, idRide
        for ride in rides:
            if rides[ride][6] == 0:
                distance = self.distance(rides[ride][0],rides[ride][1])
                if (self.distance(rides[ride][0],rides[ride][1])+Car.step) <= rides[ride][4]:
                    distance *= Car.bonusMultiplier
                timeNeeded = (self.distance(rides[ride][0],rides[ride][1])+abs(rides[ride][2] - rides[ride][0]) + abs(rides[ride][3] - rides[ride][1])+Car.step)
                if distance < closest[0] and timeNeeded <= rides[ride][5] and timeNeeded <= Car.maxStep:
                    closest = (self.distance(rides[ride][0],rides[ride][1]),ride)

        return closest[1]

    def findMostProfitable(self, rides):
        mostProfitables = (0, -1)
        for ride in rides:
            if rides[ride][6] == 0:
                score = 0
                distance = self.distance(rides[ride][0], rides[ride][1])
                timeNeeded = (distance + abs(rides[ride][2] - rides[ride][0]) + abs(rides[ride][3] - rides[ride][1]))+Car.step
                if timeNeeded <= rides[ride][5] and timeNeeded <= Car.maxStep:
                    score += abs(rides[ride][2] - rides[ride][0]) + abs(rides[ride][3] - rides[ride][1])
                    if distance + Car.step <= rides[ride][4]:
                        score += Car.bonus
                    if (score/timeNeeded) > mostProfitables[0]:
                        mostProfitables =((score/timeNeeded),ride)
        return mostProfitables[1]


    def move(self,a,b):
        x = self.pos[0]
        y = self.pos[1]
        if x!=a:
            if x < a:
                x += 1
            elif x > a:
                x -=1
        elif y!=b:
            if y < b:
                y+=1
            elif y > b:
                y-=1
        self.pos = (x,y)
