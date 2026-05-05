
class Particle:
    def __init__(self, x=0, y=0, vx=0, vy=0, g=0):
        self.x  = x #x position [m]
        self.y  = y #y position [m]
        self.vx = vx #x velocity [m/s]
        self.vy = vy #y velocity [m/s]
        self.g = 0.0 # m/s^2
        self.box = [[0,5],[0,5]] # define bounds of the box
        self.hitwall = False # check if we hit a wall

    def setposition(self,x,y):
        self.x = x
        self.y = y
        self.__selfcheck()

    def setvelocity(self,vx,vy):
        self.vx = vx
        self.vy = vy

    def setgravity(self,a):
        self.g = a

    def update(self, dt):

        #Advance position by one time step.
        newx = self.x + self.vx * dt
        newy = self.y + self.vy * dt #+ (0.5 * self.g * dt*dt)
        if (self.__check(newx,newy)):
            self.x = newx
            self.y = newy
        else:
            print("OUT-OF-BOUNDS!")

        # update velocity from acceleration
        self.vy += self.g * dt

    def speed(self):
        #Scalar speed (magnitude of velocity).
        return (self.vx**2 + self.vy**2) ** 0.5

    def inbox(self):
        if (self.hitwall == True): return False
        return True

    def __repr__(self):
        return "particle position [%.02f,%.02f] and velocity [%.02f,%.02f]"%(self.x,self.y,self.vx,self.vy)

    def __selfcheck(self):
        
        if ((self.x > self.box[0][1]) or (self.x < self.box[0][0]) or (self.y > self.box[1][1]) or (self.y < self.box[1][0]) ):
            self.hitwall = True
            return False
        self.hitwall = False
        return True

    def __check(self,x,y):
        #are we moving to a point outside of the "box"?
        if ((x > self.box[0][1]) or (x < self.box[0][0]) or (y > self.box[1][1]) or (y < self.box[1][0]) ):
            self.hitwall = True
            return False
        self.hitwall = False
        return True
