x = 'AC/DC' == 'Michael Jackson'
print(x)

x1 = 'AC/DC' != 'Michael Jackson'
print(x1)

y = 15
if (y > 18):
    print('You can enter Reggae Concert')
else:
    print("You cannot enter.Move on Nigga")

album_year = 1984
if (album_year < 1980) or (album_year > 1989):
    print("The album was released in the 70's, 90's or new millenium")
else:
    print("The album was released in the 1980's")

squares = ["red,yellow,green,purple,blue"]
for i, square in enumerate(squares):
    print(square)

album_ratings = [10, 20, 5, -0.25, -1, 40, 50, 200, -250]
album_ratings.sort();
print(album_ratings)


def student(a):
    print(student)
    return


class Circle(object):
    def __init__(self,radius,color):
        self.radius=radius;
        self.color=color;

    def add_radius(self,r):
        self.radius=self.radius+r
        return (self.radius)


