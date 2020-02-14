class Car:
    nb_car = 0
    step = 0

    def __init__(self):
        self.id = Car.nb_car
        self.pos = (0, 0)
        self.rCompleted = []
        self.occupation = -1
        self.inRides = 0 #0 is not in ride, 1 is in ride
        self.target = (0,0)
        Car.nb_car += 1
    def assign(self,idRide, ride):
        self.occupation = idRide
        self.target = (ride(0), ride(1))
    def update(self, rides):
        if self.occupation != 1:
            self.move(self.target)
            if self.pos == self.target:
                if self.inRides == 0:
                    self.target = (rides[self.occupation][0],rides[self.occupation][1])
                elif self.inRides == 1:
                    self.rCompleted.append(self.occupation)
                    self.occupation = -1
                else:
                    print("error")
        if self.occupation == -1:
            closest = self.findClosestAcceptable()
            if closest != -1:
                self.assign(closest, rides(closest))
            else:
                print("stop")
        Car.step+=1
    def distance(self, a,b): #target is (x,y)
        return abs(self.pos[0]-a)+abs(self.pos[1]-b)
    def findClosestAcceptable(self, rides):
        for ride in rides:
            closest = (20001,-1) #distance, idRide
            timeneeded = abs(rides[ride][2]-rides[ride][0])+abs(rides[ride][3]-rides[ride][1])
            if rides[ride][6] == 0:
                if self.distance(rides[ride][0],rides[ride][1]) < closest[0]:
                    if self.distance(rides[ride][0],rides[ride][1])+timeneeded < rides[ride][5]:
                        closest = (self.distance(rides[ride][0],rides[ride][1]),ride)
        return closest[1]
    def move(self,a,b):
        while self.pos[0]!=a:
            if self.pos[0] < a:
                self.pos[0]+=1
            elif self.pos[0] > a:
                self.pos[0] -=1
        while self.pos[1]!=b:
            if self.pos[1] < b:
                self.pos[1]+=1
            elif self.pos[1] > b:
                self.pos[1]-=1

