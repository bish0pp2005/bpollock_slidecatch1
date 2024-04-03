import pygame, simpleGE, random

class Ram(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ram.png")
        self.setSize(30, 30)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class DVD(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("dvd.png")
        self.setSize(60, 60)
        self.position = (320, 400)
        self.moveSpeed = 5
    
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_d):
            self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_s):
            self.y += self.moveSpeed
        if self.isKeyPressed(pygame.K_w):
            self.y -= self.moveSpeed
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("smogcity.png")
        
        self.sndRam = simpleGE.Sound("connection.wav")
        self.dvd = DVD(self)
        self.ram = Ram(self)
        
        self.sprites = [self.dvd,
                        self.ram]
    def process(self):
        if self.dvd.collidesWith(self.ram):
            self.sndRam.play()
            self.ram.reset()
            
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()