import time
from animation import *
from renderer import *

NUM_STRIPS = 5
NUM_STRIP_LEDS = 12


# main program
def main() -> None:
    print('- - - welcome at the led matrix controls - - -\n')
    viewport = Viewport((NUM_STRIP_LEDS, NUM_STRIPS))
    renderer = Renderer(viewport)

    dot_shape = [[1]]
    dot = RenderObject('dot', dot_shape, (0,0))

    heart_shape = [
        [0,1,0,1,0],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        ]
    heart = RenderObject('heart', heart_shape, (0,0))

    renderer.addRenderObject(Animation(dot))
    renderer.addRenderObject(Animation(heart))

    while True:
        renderer.render()
        time.sleep(1)


if __name__ == '__main__':
    main()
