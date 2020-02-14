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
            closest = (0,-1) #distance, idRide
            if rides[ride][6] == 0:
                if self.distance(rides[ride][0],rides[ride][1]) < closest[0]:
                    closest = (self.distance(rides[ride][0],rides[ride][1]),ride)
        return closest[1]



