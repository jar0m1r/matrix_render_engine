import time

NUM_STRIPS = 5
NUM_STRIP_LEDS = 12

# The actual matrix to output
class Viewport(object):

    def __init__(self, size):
        self.size = size

    def getZeroMatrix(self):
        x, y = self.size
        return [[ (0) for j in range(x)] for i in range(y)]

    def show(self, output_matrix):
        for row in output_matrix:
            for led in row:
                if led == 0:
                    print(f" {chr(11041)} ", end=" ")
                else:
                    print(f" {chr(11042)} ", end=" ")

            print('\n')
        print('\n\n')




# Renderer of RenderObjects to the Viewport
class Renderer(object):

    def __init__(self, viewport):
        self.viewport = viewport
        self.render_objects = []

    def addRenderObject(self, render_object):
        self.render_objects.append(render_object)

    def render(self):
        output_matrix = viewport.getZeroMatrix()

        for render_object in self.render_objects:

            # TODO RenderObject and Animation ABC
            if type(render_object) is Animation:
                render_object.animate()
                render_object = render_object.render_object

            # 
            offset_x, offset_y = render_object.position
            matrix = render_object.shape_matrix

            for i in range(len(matrix)):
                for j in range(len(matrix[0])): #fix when changing shape to set of offsets
                    if matrix[i][j] == 1:
                        x = i + offset_x
                        y = j + offset_y
                        if len(output_matrix) > x and len(output_matrix[0]) > y: output_matrix[x][y] = 1

        viewport.show(output_matrix)




# Renderable object
class RenderObject(object):

    def __init__(self, name, shape_matrix, position):
        self.name = name
        self.shape_matrix = shape_matrix
        self.position = position

    def draw(self):
        return (self.shape_matrix, self.position)
        




# Animation able to change position of RenderObject 
# later make Ankmation base class and different Animation subclasses 
# like Slide, blink, fade, rotate
# subclasses are chainable or pipeable
class Animation(object):

    def __init__(self, render_object):
        self.render_object = render_object

    def animate(self):
        y, x = self.render_object.position
        self.render_object.position = (y, x+1)




# main program
if __name__ == '__main__':
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

    dot_animation = Animation(dot)

    renderer.addRenderObject(Animation(dot))
    renderer.addRenderObject(Animation(heart))

    while True:
        renderer.render()
        time.sleep(1)
