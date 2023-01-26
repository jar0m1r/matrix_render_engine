import time
from renderer import RenderObject

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
    pass
