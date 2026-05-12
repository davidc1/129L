
class Planet:
    def __init__(self, x=0, y=0, z=0, vx=0, vy=0, vz=0, m=0, r=0, G=0, idx=0):
        self.x  = x # x position [m]
        self.y  = y # y position [m]
        self.z  = z # z position [m]
        self.r  = r # radius [m]
        self.m  = m # mass [Kg]
        self.vx = vx # x velocity [m/s]
        self.vy = vy # y velocity [m/s]
        self.vz = vz # y velocity [m/s]
        self.ax = 0 # x acceleration [m/s]
        self.ay = 0 # y acceleration [m/s]
        self.az = 0 # z acceleration [m/s]
        self.f = 0.0 # force [Kg * m / s**2]
        self.G = G # gravitational constant
        self.idx = idx

    def setposition(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def setvelocity(self,vx,vy,vz):
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def setgravity(self,a):
        self.g = a

    def reset_force(self):
        self.f = 0
        self.ax = 0
        self.ay = 0
        self.az = 0

    def calculate_distance(self,planet):

        xp = planet.x
        yp = planet.y
        zp = planet.z

        d = ((xp-self.x)**2 + (yp-self.y)**2 + (zp-self.z)**2)**(0.5)

        return d

    def update_force(self,planet):

        d = self.calculate_distance(planet)

        F = (self.G * self.m * planet.m) / (d**2)

        #print("Force magnitude is %g"%F)

        # direction aligned with distance between two objects
        dirx = planet.x - self.x
        diry = planet.y - self.y
        dirz = planet.z - self.z

        Fx = F * (dirx / d)
        Fy = F * (diry / d)
        Fz = F * (dirz / d)

        self.f += F

        self.ax += Fx/self.m
        self.ay += Fy/self.m
        self.az += Fz/self.m


    def update(self, dt, planets):

        # reset force
        self.reset_force()

        # simulate the force between planets
        for planet in planets:
            if (planet.idx != self.idx):
                self.update_force(planet)

        # now that we have calculated forces and updated the acceleration
        # let's update the velocities / positions

        # Euler
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.z += self.vz * dt

        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.vz += self.az * dt

        # Leapfrog
        #self.x += self.vx * dt
        #self.y += self.vy * dt
        #self.z += self.vz * dt

    def __repr__(self):
        return "Planet idx %i with mass %g has position [%g, %g, %g]"%(self.idx,self.m,self.x,self.y,self.z)
