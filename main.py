import time
import animation

NUM_STRIPS = 5
NUM_STRIP_LEDS = 12

# The actual matrix to output
class Viewport:

    def __init__(self, size) -> None:
        self.size = size

    def getZeroMatrix(self) -> list[list[int]]:
        x, y = self.size
        return [[ (0) for j in range(x)] for i in range(y)]

    def show(self, output_matrix) -> None:
        for row in output_matrix:
            for led in row:
                if led == 0:
                    print(f" {chr(11041)} ", end=" ")
                else:
                    print(f" {chr(11042)} ", end=" ")
            print('\n')
        print('\n\n')



# Renders RenderObjects to Viewport
class Renderer:

    def __init__(self, viewport) -> None:
        self.viewport = viewport
        self.render_objects = []

    def addRenderObject(self, render_object) -> None:
        self.render_objects.append(render_object)

    def render(self) -> None:
        output_matrix = self.viewport.getZeroMatrix()

        for render_object in self.render_objects:

            # TODO RenderObject and Animation ABC
            if type(render_object) is animation.Animation:
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

        self.viewport.show(output_matrix)




# Renderable object
class RenderObject:

    def __init__(self, name, shape_matrix, position) -> None:
        self.name = name
        self.shape_matrix = shape_matrix
        self.position = position

    def draw(self) -> tuple[int, int]:
        return (self.shape_matrix, self.position)
        



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

    renderer.addRenderObject(animation.Animation(dot))
    renderer.addRenderObject(animation.Animation(heart))

    while True:
        renderer.render()
        time.sleep(1)


if __name__ == '__main__':
    main()
