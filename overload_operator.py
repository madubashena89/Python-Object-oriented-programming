class Square:
    def __init__(self, side):
        self.side = side

    def __add__(sq1, sq2):
        return ((4*sq1.side )+(4*sq1.side))

sq1 = Square(40) # 40*4 = 160
sq2 = Square(30) # 30*4 = 120
print("This is the total perimeter of two squares", sq1 + sq2)