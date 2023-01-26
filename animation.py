import time

# Animation able to change position of RenderObject 
# later make Ankmation base class and different Animation subclasses 
# like Slide, blink, fade, rotate
# subclasses are chainable or pipeable
class Animation:

    def __init__(self, render_object) -> None:
        self.render_object = render_object

    def animate(self) -> None:
        y, x = self.render_object.position
        self.render_object.position = (y, x+1)

# linear from -> to animation in x or y
class LinearAnimation:
    pass 

# color and intensity animation
class FadeAnimation:
    pass
