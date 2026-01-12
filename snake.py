from turtle import Turtle
move_distance = 20
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)



    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        segment = self.segments[0]
        if self.head.heading() != down:
            segment.setheading(up)

    def down(self):
        segment = self.segments[0]
        if self.head.heading() != up:
            segment.setheading(down)

    def left(self):
        segment = self.segments[0]
        if self.head.heading() != right:
            segment.setheading(left)

    def right(self):
        segment = self.segments[0]
        if self.head.heading() != left:
            segment.setheading(right)
