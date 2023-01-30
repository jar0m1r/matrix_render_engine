
# immutable?
class Shape:
    _shape_items: list[tuple[tuple[int,int],int, tuple[int,int,int]]]
    dimension = (0,0)

    def __init__(self):
        self._shape_items = []

    @property
    def shape_items(self):
        return self._shape_items
    
    # group 1 always outline
    def add_shape_item(self, offset:tuple[int,int], group:int, color:tuple[int,int]):
        self._shape_items.append((offset, group, color))
    
    # translate matrix to coordinate tuples, return new object
    @classmethod
    def fromMatrix(cls, matrix: list[list[int]]): # how to declare return value of Shape instance
        shape = cls()
        shape.dimension = (len(matrix), len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    shape.add_shape_item((i, j), matrix[i][j], (0,0,0))
        return shape

# [0,1,0,1,0],
# [1,2,1,2,1],
# [1,2,3,2,1],
# [0,1,2,1,0],
# [0,0,1,0,0]