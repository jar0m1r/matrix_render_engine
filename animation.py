import time
from renderer import RenderObject
from color import colorwheel

# Animation able to change properties of RenderObject 

class Animation:

    def __init__(self) -> None:
        pass

    def animate(self) -> None:
        pass

# linear from -> to animation in x or y
class LinearAnimation(Animation):
    
    def __init__(self, start_position:tuple[int, int], num_steps, velocity=1):
        self.start_position = start_position
        self.num_steps = num_steps
        self.step = 0
        self.velocity = velocity
    
    def animate(self, render_object:RenderObject) -> None:
        if self.step < self.num_steps:
            self.step += 1
            y, x = render_object.position
            render_object.position = (y, x+self.velocity)
        else:
            render_object.position = self.start_position
            self.step = 0

# color and intensity animation
class FadeAnimation(Animation):
    isOn = True

    def animate(self, render_object:RenderObject) -> None:
        if self.isOn: render_object.color = (255,0,0)
        else: render_object.color = (0,0,255)
        self.isOn = not self.isOn


class RainbowAnimation(Animation):

    def __init__(self, direction:str, width:int, speed:int = 1): # change direction to class or enum / width for now, refactor decorator
        self.color_value = 0
        self.direction = direction
        self.width = width
        self.speed = speed
        self.color_columns = [(0,0,0) for i in range(width)]

    def animate(self, render_object:RenderObject) -> None:
        if self.color_value + self.speed > 255: 
            self.color_value = 0
        else:
            self.color_value += self.speed

        color = colorwheel(self.color_value)

        self.color_columns.pop()
        self.color_columns.insert(0, (color))

        print(f'these are the color columns: {self.color_columns}')

        if self.direction == 'LR':
            for item in render_object.shape.shape_items:
                item = (item[0], item[1], self.color_columns[item[0][0]])