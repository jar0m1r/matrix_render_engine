import time
from ...engine.animation import *
from ...engine.renderer import *
from ...engine.viewports.terminal import Terminal
from ...engine.shape import Shape

NUM_STRIPS = 5
NUM_STRIP_LEDS = 12


# main program
def main() -> None:
    print('- - - welcome at the led matrix controls - - -\n')
    viewport = Terminal((NUM_STRIP_LEDS, NUM_STRIPS))
    renderer = Renderer(viewport)

    # dot_shape = Shape.from_matrix([[1]])
    # dot = RenderObject('dot', dot_shape, (0,-2))
    # renderer.add_renderable(LinearAnimation(dot.position, viewport.size[1] + dot_shape.dimension[0], 1, BlinkAnimation(dot)))

    # outline_matrix = [[1] * NUM_STRIP_LEDS for j in range(NUM_STRIPS)]
    # outline_shape = Shape.from_matrix(outline_matrix)   
    # outline = RenderObject('outline', outline_shape, (0,0))
    # renderer.add_renderable(RainbowAnimation('LR', outline.shape.dimension[1], 10, outline))

    heart_shape = Shape.from_matrix([
        [0,1,0,1,0],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        ])
    heart = RenderObject('heart', heart_shape, (0,-5))
    renderer.add_renderable(LinearAnimation(heart.position, viewport.size[1], 2, RainbowAnimation('LR', heart.shape.dimension[1], 10, heart)))


    while True:
        renderer.render()
        time.sleep(0.5)


if __name__ == '__main__':
    main()