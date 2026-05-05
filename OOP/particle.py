
class Particle:
    def __init__(self, x, y, vx, vy, g=0):
        self.x  = x #x position [m]
        self.y  = y #y position [m]
        self.vx = vx #x velocity [m/s]
        self.vy = vy #y velocity [m/s]
        self.g = 0.0 # m/s^2

    def setposition(self,x,y):
        self.x = x
        self.y = y

    def setvelocity(self,vx,vy):
        self.vx = vx
        self.vy = vy

    def update(self, dt):
        #Advance position by one time step.
        self.x += self.vx * dt
        self.y += self.vy * dt - (0.5 * self.g * dt*dt)

    def speed(self):
        #Scalar speed (magnitude of velocity).
        return (self.vx**2 + self.vy**2) ** 0.5

    def __repr__(self):
        return "particle position [%.02f,%.02f] and velocity [%.02f,%.02f]"%(self.x,self.y,self.vx,self.vy)


