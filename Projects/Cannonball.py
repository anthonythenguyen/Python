from graphics import *

class Button:
    """
    A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns True if the button is active and p is inside it.
    """
    
    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """

        w, h = width/2, height/2
        x, y = center.getX(), center.getY()

        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns True if button is active and p is inside"
        return (self.active and
                #type(p) == Point and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of the button"
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False
        
class InputDialog:
    """ A custom window for getting simulation values
    (angle, velocity, and height) from the user."""

    def __init__(self, angle, vel, height):
        """Build and display the input window"""

        self.win = win = GraphWin("Initial Values", 200, 300)
        win.setCoords(0, 4.5, 4, .5)

        Text(Point(1,1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1,2), "Velocity").draw(win)
        self.vel = Entry(Point(3,2), 5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1,3), "Height").draw(win)
        self.height = Entry(Point(3,3), 5).draw(win)
        self.height.setText(str(height))

        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire")
        self.fire.activate()

        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()

    def interact(self):
        """wait for user to click Quit or Fire button
        Returns a string indicating which button was clicked
        """

        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    def getValues(self):
        """return input values"""

        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())
        return a,v,h

    def close(self):
        """close the input window"""
        self.win.close()
class Launcher():
    def adjAngle(self, amt):
        """Change launch angle by amt degrees"""
        self.angle = self.angle + radians(amt)
        self.redraw()

    def adjVel(self, amt):
        """Change launch velocity by amt"""
        self.vel = self.vel + amt
        self.redraw()

    def redraw(self):
        """Redraw the arrow to show current angle and velocity"""

        self.arrow.undraw()
        pt2 = Point(self.vel*cos(self.angle),
                    self.vel*sin(self.angle))
        self.arrow = Line(Point(0,0), pt2).draw(self.win)
        self.arrow.setWidth(3)

    def fire(self):
        return ShotTracker(self.win, degrees(self.angle), self.vel, 0.0)
    def __init__(self, win):
        #draw the base shot of the launcher
        base = Circle(Point(0,0), 3)
        base.setFill("red")
        base.draw(win)

        #save the window and create initial angle and velocity
        self.win = win
        self.angle = radians(45.0)
        self.vel = 40.0

        #Create initial "dummy" arrow *needed by redraw)
        self.arrow = Line(Point(0,0), Point(0,0)).draw(win)
        #replace it with the correct arrow
        self.redraw()
        
class ProjectileApp:

    def __init__(self):
        self.win = GraphWin("Projectile Animation", 640, 480)
        self.win.setCoords(-10,-10,210,155)
        Line(Point(-10,0), Point(210,0)).draw(self.win)
        for x in range(0,210,50):
            Text(Point(x,-7), str(x)).draw(self.win)
            Line(Point(x,0), Point(x,2)).draw(self.win)

        self.launcher =Launcher(self.win)

        self.shots = []
    def run(self):
        while True:
            self.updateShots(1/30)

            key = self.win.checkKey()
            if key in ["q", "Q"]:
                break

            if key == "Up":
                self.launcher.adjAngle(5)
            elif key == "Down":
                self.launcher.adjAngle(-5)
            elif key == "Right":
                self.launcher.adjVel(5)
            elif ley == "Left":
                self.launcher.adjVel(5)
            elif key in ["f", "F"]:
                self.shots.append(self.launcher.fire())
            update(30)

        self.win.close()
    def updateShots(self, dt):
        alive = []
        for shot in self.shots:
            shot.update(dt)
            if shot.getY() >= 0 and -10 < shot.getX() <210:
                alive.append(shot)
            else:
                shot.undraw()
        self.shots = alive


dialog = InputDialog(45, 40, 2)
choice = dialog.interact()
if choice == "Fire!":
    angle, vel, height = dialog.getValues()


def main():

    #create animation window
    win = GraphWin("Projectile Animeation", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)
    Line(Point(-10, 0), Point(210,0)).draw(win)
    for x in range(0,210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x,0), Point(x,2)).draw(win)

    def __init__(self, win, angle, velocity, height):
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self, dt):
        """Move the shot dt seconds farther along its flight"""

        #Update the projectile
        self.proj,update(dt)

        #move the circle to the new projectile location
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)

    def getX(self):
        """return the current x coordinate of the shot's center"""
        return self.proj.getX()

    def getY(self):
        """return the current y coordinate of the shot's center"""
        return self.proj.getY()

    def undraw(self):
        """undraw the shot"""
        self.marker.undraw()

    #event loop, each time through fires a single shot
        angle, vel, height = 45.0, 40.0, 2.0
        while True:
            #Interact with the user
            inputwin = InputDialog(angle, vel, height)
            choice = inputwin.interact()
            inputwin.close()

            if choice == "Quit": #Loop exit
                break

            #Create a shot and track until it hits ground of leaves window
            angle, vel, height = inputwin.getValues()
            shot = ShotTracker(win, angle, vel, height)
            while 0 <= shot.getY() and -10 < shot.getX() <= 210:
                shot.update(1/50)
                update(50)

            win.close()
main()
