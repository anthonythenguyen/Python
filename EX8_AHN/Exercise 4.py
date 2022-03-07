from graphics import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    fileName = askopenfilename();
    win = GraphWin("Picture", 1000, 1000)

    image = Image(Point(500, 500), fileName)
    image.draw(win)

    print("Converting image to grayscale. This can take some time...")

    for row in range(0, image.getWidth()):
        for column in range (0, image.getHeight()):
            red, green, blue = image.getPixel(row, column)
            brightness = int(round((0.299 * red) + (0.587 * green) + (0.114 * blue)))
            image.setPixel(row, column, color_rgb(brightness, brightness, brightness))
        update()

    print("Save gray scale image as a .gif")
    grayImage = asksaveasfilename();
    image.save(grayImage);

    print("Click on image to close");

    win.getMouse()
    win.close()

    
main()
