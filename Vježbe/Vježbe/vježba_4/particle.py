class Particle:
    def __init__(self,v,fi,x):
        self.počv=0
        self.v=v
        self.počfi=0
        self.fi=fi
        self.počx=0
        self.x=x

    def reset(self):
        self.v=self.počv
        self.fi=self.počfi
        self.x=self.počx
    def __move(self,dt):
       
        


