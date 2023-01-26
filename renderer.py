from animation import *

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

    def addRenderObject(self, render_object, animations=[]) -> None:
        self.render_objects.append((render_object, animations))

    def render(self) -> None:
        output_matrix = self.viewport.getZeroMatrix()

        for render_object, animations in self.render_objects:
            for animation in animations:
                animation.animate(render_object)
            render_object.render()
            offset_x, offset_y = render_object.position
            matrix = render_object.shape_matrix

            for i in range(len(matrix)):
                for j in range(len(matrix[0])): # TODO fix when changing shape to set of offsets
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

        # color will be in tuple on matrix item, for now ..
        self.color = 'R' # 'R' 'G' 'B' 

    def render(self) -> None:
        pass