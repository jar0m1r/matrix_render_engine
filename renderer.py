from __future__ import annotations
from typing import NamedTuple
from animation import *
from shape import Shape

Offset = NamedTuple('Offset', [('x',int), ('y',int)])
Size = NamedTuple('Size', [('h',int), ('w',int)])

# The actual matrix to output
class Viewport:
    _size:Size

    def __init__(self, size:Size) -> None:
        self._size = size

    @property
    def size(self):
        return self._size

    @property
    def zero_matrix(self) -> list[list[int]]:
        x, y = self._size
        return [[ (0) for j in range(x)] for i in range(y)]

    def show(self, output_matrix) -> None:
        pass

class Ledmatrix(Viewport):
    pass

class Terminal(Viewport):
    def show(self, output_matrix) -> None:
        for row in output_matrix:
            for led in row:
                if led == 0:
                    print(f" {chr(11041)} ", end=" ")
                else:
                    group, color = led
                    r,g,b = color
                    if group == 1:
                        if r > g and r > b:
                            print(f" {chr(11042)} ", end=" ")
                        elif g > r and g > b:
                            print(f" {chr(11045)} ", end=" ")
                        elif b > r and b > g:
                            print(f" {chr(11054)} ", end=" ")
                        else:
                            print(f" {chr(11053)} ", end=" ")
                    else:
                        pass
            print('\n')
        print('\n\n')


# Renders RenderObjects to Viewport
class Renderer:
    renderables:list[Renderable] = []

    def __init__(self, viewport) -> None:
        self.viewport = viewport

    def add_renderable(self, renderable) -> None:
        self.renderables.append(renderable)

    def render(self) -> None:
        output_matrix = self.viewport.zero_matrix

        for renderable in self.renderables:
            render_object = renderable.render()
            offset_x, offset_y = render_object.position
            
            for (x, y), group, color in render_object.shape.shape_items:
                    if group != 0:
                        _x = x + offset_x
                        _y = y + offset_y
                        if len(output_matrix) > _x and len(output_matrix[0]) > _y: 
                            output_matrix[_x][_y] = (group, color)

        self.viewport.show(output_matrix)


class Renderable:
    def render() -> RenderObject:
        pass

class RenderObject(Renderable):

    def __init__(self, name:str, shape:Shape, position:Offset) -> None:
        self.name = name
        self.shape = shape
        self.position = position
        self.color = (0,0,255) 

    def render(self) -> RenderObject:
        return self
