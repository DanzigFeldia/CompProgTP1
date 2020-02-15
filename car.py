class Car:
    nb_car = 0
    step = 0
    score = 0
    bonus = 0

    def __init__(self, B):
        self.id = Car.nb_car
        self.pos = (0, 0)
        self.rCompleted = []
        self.occupation = -1
        self.inRides = 0 #0 is not in ride, 1 is in ride
        self.target = (0,0)
        Car.bonus = B
        Car.nb_car += 1

    def assign(self,idRide, ride):
        self.occupation = idRide
        self.target = (ride[0], ride[1])
        Car.score+=abs(ride[2]-ride[0])+abs(ride[3]-ride[1])
        if (Car.step+self.distance(ride[0],ride[1])) <= ride[4]:
            Car.score += Car.bonus
    def update(self, rides):
        if self.occupation != -1:
            self.move(self.target[0],self.target[1])
            if self.pos == self.target:
                if self.inRides == 0:
                    self.target = (rides[self.occupation][0],rides[self.occupation][1])
                    self.inRides = 1
                elif self.inRides == 1:
                    self.inRides =0
                    self.rCompleted.append(self.occupation)
                    self.occupation = -1
                else:
                    print("error")
        if self.occupation == -1:
            closest = self.findClosestAcceptable(rides)
            if closest != -1:
                self.assign(closest, rides[closest])
                rides[closest][6] = 1

        return rides

    def distance(self, a,b): #target is (x,y)
        return abs(self.pos[0]-a)+abs(self.pos[1]-b)

    def findClosestAcceptable(self, rides):
        closest = (20001, -1)  # distance, idRide
        for ride in rides:

            timeneeded = abs(rides[ride][2]-rides[ride][0])+abs(rides[ride][3]-rides[ride][1])
            if rides[ride][6] == 0:
                if self.distance(rides[ride][0],rides[ride][1]) < closest[0]:
                    if ((self.distance(rides[ride][0],rides[ride][1])+timeneeded+Car.step) <= rides[ride][5]):
                        closest = (self.distance(rides[ride][0],rides[ride][1]),ride)

        return closest[1]

    def move(self,a,b):
        x = self.pos[0]
        y = self.pos[1]
        if x!=a:
            if x < a:
                x += 1
            elif x > a:
                x -=1
        if y!=b:
            if y < b:
                y+=1
            elif y > b:
                y-=1
        self.pos = (x,y)
