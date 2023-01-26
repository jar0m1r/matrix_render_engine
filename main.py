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
    dot = RenderObject('dot', dot_shape, (-5,2))

    heart_shape = [
        [0,1,0,1,0],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        ]
    heart = RenderObject('heart', heart_shape, (0,0))

    # renderer.addRenderObject(heart) 
    # #TODO Fix this, position missing, animation should get startposition from RenderObject not other way around
    
    renderer.addRenderObject(dot, [LinearAnimation(dot.position, viewport.size[1], 2)])
    renderer.addRenderObject(heart, [LinearAnimation(heart.position, viewport.size[1] + len(heart_shape))])

    while True:
        renderer.render()
        time.sleep(0.5)


if __name__ == '__main__':
    main()