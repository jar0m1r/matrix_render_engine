import time
from animation import *
from renderer import *
from shape import Shape

NUM_STRIPS = 5
NUM_STRIP_LEDS = 12


# main program
def main() -> None:
    print('- - - welcome at the led matrix controls - - -\n')
    viewport = Viewport((NUM_STRIP_LEDS, NUM_STRIPS))
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

    renderer.addRenderObject(dot, [LinearAnimation(dot.position, viewport.size[1], 2)])
    renderer.addRenderObject(heart, [LinearAnimation(heart.position, viewport.size[1] + heart_shape.dimension[0])])

    while True:
        renderer.render()
        time.sleep(0.5)


if __name__ == '__main__':
    main()