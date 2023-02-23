from typing import NamedTuple
from .color import Color

ShapeItem = NamedTuple('ShapeItem', [('offset', tuple[int,int]), ('group', int), ('color',Color)])

# immutable?
class Shape:
    _shape_items:list[ShapeItem]
    dimension = (0,0)

    def __init__(self):
        self._shape_items = []

    @property
    def shape_items(self) -> list[ShapeItem]:
        return self._shape_items
    
    # group 1 always outline
    def add_shape_item(self, shape_item:ShapeItem):
        self._shape_items.append(shape_item)
    
    # translate matrix to coordinate tuples, return new object
    @classmethod
    def from_matrix(cls, matrix: list[list[int]]): # how to declare return value of Shape instance
        shape = cls()
        shape.dimension = (len(matrix), len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    shape.add_shape_item(ShapeItem((i, j), matrix[i][j], Color(0,0,0)))
        return shape




# [0,1,0,1,0],
# [1,2,1,2,1],
# [1,2,3,2,1],
# [0,1,2,1,0],
# [0,0,1,0,0]

# Override + operator to add shapes together as one 