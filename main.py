import time
from animation import *
from renderer import *
from shape import Shape

NUM_STRIPS = 5
NUM_STRIP_LEDS = 12


# main program
def main() -> None:
    print('- - - welcome at the led matrix controls - - -\n')
    viewport = Terminal((NUM_STRIP_LEDS, NUM_STRIPS))
    renderer = Renderer(viewport)

    dot_shape = Shape.fromMatrix([[1]])
    dot = RenderObject('dot', dot_shape, (-5,2))

    heart_shape = Shape.fromMatrix([
        [0,1,0,1,0],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        ])
    heart = RenderObject('heart', heart_shape, (0,0))

    smiley_shape = Shape.fromMatrix([
        [0,0,1,1,0,0],
        [0,1,0,0,1,0],
        [1,0,1,1,0,1],
        [0,1,0,0,1,0],
        [0,0,1,1,0,0]
        ])
    smiley = RenderObject('smiley', smiley_shape, (-5,0))

    renderer.add_render_object(smiley, [LinearAnimation(smiley.position, viewport.size[1], 2), FadeAnimation()])
    # renderer.add_render_object(heart, [LinearAnimation(heart.position, viewport.size[1] + heart_shape.dimension[0]), FadeAnimation()])

    while True:
        renderer.render()
        time.sleep(0.5)


if __name__ == '__main__':
    main()