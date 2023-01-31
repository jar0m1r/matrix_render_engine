import time
from renderer import Renderable, RenderObject
from color import colorwheel

# Animation ABC implementing Renderable 
class Animation(Renderable):
    _renderable:Renderable = None

    def __init__(self, renderable:Renderable):
        self._renderable = renderable

    def render(self) -> RenderObject:
        return self._renderable.render()

# linear from -> to animation in x or y
class LinearAnimation(Animation):
    
    def __init__(self, start_position:tuple[int, int], num_steps, velocity, renderable:Renderable):
        super().__init__(renderable)
        self.start_position = start_position
        self.num_steps = num_steps
        self.step = 0
        self.velocity = velocity
    
    def render(self) -> RenderObject:
        render_object = super().render() # check
        if self.step < self.num_steps:
            self.step += 1
            y, x = render_object.position
            render_object.position = (y, x+self.velocity)
        else:
            render_object.position = self.start_position
            self.step = 0
        return render_object

# color and intensity animation
class FadeAnimation(Animation):
    isOn = True

    def __init__(self, renderable:Renderable):
        super().__init__(renderable)

    def render(self) -> RenderObject:
        render_object = super().render()
        if self.isOn: render_object.color = (255,0,0)
        else: render_object.color = (0,0,255)
        self.isOn = not self.isOn
        return render_object


class RainbowAnimation(Animation):

    def __init__(self, direction:str, width:int, speed:int, renderable:Renderable): # change direction to class or enum / width for now, refactor decorator
        super().__init__(renderable)
        self.color_value = 0
        self.direction = direction
        self.width = width
        self.speed = speed
        self.color_columns = [(0,0,0) for i in range(width)]

    def render(self) -> RenderObject:
        render_object = super().render()
        color = colorwheel(self.color_value)

        self.color_columns.pop()
        self.color_columns.insert(0, (color))

        if self.direction == 'LR':
            for i in range(len(render_object.shape.shape_items)):
                render_object.shape.shape_items[i] = (render_object.shape.shape_items[i][0], 
                                                      render_object.shape.shape_items[i][1], 
                                                      self.color_columns[render_object.shape.shape_items[i][0][1]])
                
        if self.color_value + self.speed > 255: 
            self.color_value = 0
        else:
            self.color_value += self.speed

        return render_object

# tickertape
class LoopAnimation(Animation):
    pass

# maybe better as PatternShape(Shape) vs Single Shape
class PatternAnimation(Animation):
    pass

# Normal (Shape on/off) and Inverted (shape on <-> Inverted shape off)
class BlinkAnimation(Animation):
    pass

# SlideIn / SlideOut
class SlideAnimation(Animation):
    pass