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

        for renderObject in self.render_objects:
            row_num = 0
            col_num = 0
            if type(renderObject) is Animation:
                renderObject.animate()
                row_num = renderObject.render_object.position[0]
                col_num = renderObject.render_object.position[1]
            elif type(renderObject) is RenderObject:
                row_num = renderObject.position[0]
                col_num = renderObject.position[1]
            else:
              continue

            if self.elementExists(row_num, col_num, output_matrix): output_matrix[row_num][col_num] = 1

        viewport.show(output_matrix)

    def elementExists(self, row_num, col_num, output_matrix): 
        if len(output_matrix) < row_num - 1:
            return False
        elif len(output_matrix[row_num]) < col_num - 1:
            return False
        else:
            return True





# Renderable object
class RenderObject(object):

    def __init__(self, name, shape, position):
        self.name = name
        self.shape = shape
        self.position = position

    def draw(self):
        return (self.shape, self.position)
        




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

    renderer.addRenderObject(dot_animation)

    while True:
        renderer.render()
        time.sleep(2)
