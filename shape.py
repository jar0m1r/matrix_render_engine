
# immutable?
class Shape:
    _shape_items: list[tuple[tuple[int, int], int]]  = []
    dimension = (0,0)

    # group 1 always outline
    def addShapeItem(self, offset, group):
        self._shape_items.append((offset, group))

    def getShapeItems(self):
        return self._shape_items
    
    # translate matrix to coordinate tuples, return new object
    @staticmethod
    def fromMatrix(matrix: list[list[int]]): # how to declare return value of Shape instance
        shape = Shape()
        shape.dimension = (len(matrix), len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    shape.addShapeItem((i, j), matrix[i][j])
        return shape

# [0,1,0,1,0],
# [1,2,1,2,1],
# [1,2,3,2,1],
# [0,1,2,1,0],
# [0,0,1,0,0]