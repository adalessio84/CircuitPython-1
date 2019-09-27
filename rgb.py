import pulseio
import time
class RGB():
    print("colors")

    full = 65535

    def __init__(self, r, g, b):
        print(str(r))
        self.r = pulseio.PWMOut(r, frequency=5000, duty_cycle=65)
        self.g = pulseio.PWMOut(g, frequency=5000, duty_cycle=65)
        self.b = pulseio.PWMOut(b, frequency=5000, duty_cycle=65)

    def red(self):
        print("red")
        self.r.duty_cycle = 0
        self.b.duty_cycle = self.full
        self.g.duty_cycle = self.full

    def green(self):
        print("green")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 0
        self.b.duty_cycle = self.full

    def blue(self):
        print("blue")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = self.full
        self.b.duty_cycle = 0

    def cyan(self):
        print("cyan")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 0
        self.b.duty_cycle = 0

    def magenta(self):
        print("magenta")
        self.r.duty_cycle = 0
        self.g.duty_cycle = self.full
        self.b.duty_cycle = 0

    def yellow(self):
        print("yellow")
        self.r.duty_cycle = 0
        self.g.duty_cycle = 0
        self.b.duty_cycle = self.full

    def rainbow(self, x):
        print("rainbow")
        if x == "rate1":
            self.r.duty_cycle = 0
            self.b.duty_cycle = (self.full)
            self.g.duty_cycle = (self.full)
            for i in range(5, 65535, 5):
                self.r.duty_cycle = i
                self.b.duty_cycle = (self.full)
                self.g.duty_cycle = (self.full)-i
                time.sleep(.000001)
            for i in range (5, 65535, 5):
                self.r.duty_cycle = (self.full)
                self.b.duty_cycle = (self.full)-i
                self.g.duty_cycle = i
                time.sleep(.000001)
            for i in range(5, 65535, 5):
                self.r.duty_cycle = (self.full)-i
                self.b.duty_cycle = i
                self.g.duty_cycle = (self.full)
                time.sleep(.000001)

        elif x == "rate2":
            self.r.duty_cycle = 0
            self.b.duty_cycle = (self.full)
            self.g.duty_cycle = (self.full)
            for i in range(1, 21845):
                self.r.duty_cycle += 11
                self.b.duty_cycle -= 9
            self.r.duty_cycle = (self.full)
            self.b.duty_cycle = 0
            self.g.duty_cycle = (self.full)
            for i in range(21845, 43690):
                self.b.duty_cycle += 11
                self.g.duty_cycle -= 9
            self.r.duty_cycle = (self.full)
            self.b.duty_cycle = (self.full)
            self.g.duty_cycle = 0
            for i in range(43690, 65535):
                self.g.duty_cycle += 11
                self.r.duty_cycle -= 9