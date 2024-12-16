# %%
from cadbuildr.foundation import Sketch, Lathe, PlaneFactory, Extrusion, show
from chess.utils import ChessPiece


class Rook(ChessPiece):
    # Rook-specific dimensions
    HEAD_ARC_HEIGHT = 34.2
    HEAD_ARC_ANGLE = 50
    BATTLEMENT_WIDTH = 8.5
    BATTLEMENT_HEIGHT = 8
    CROSS_SIZE = 7
    CROSS_WIDTH = 12

    def __init__(self):
        super().__init__()
        # Build the rook
        shape, axis = self.get_sketch()
        self.add_operation(Lathe(shape, axis))

        # Cut the top
        shape = self.cut_sketch()
        self.add_operation(Extrusion(shape, 20, cut=True))
        self.paint("plywood")

    def get_sketch(self, debug=False):
        sketch = Sketch(self.xz())

        # Base
        self.create_base_sketch(sketch)

        # Head
        sketch.pencil.arc(0.5, self.HEAD_ARC_HEIGHT, self.HEAD_ARC_ANGLE)
        sketch.pencil.arc(2, 3.32, -2)
        sketch.pencil.line(2.5, 2.5)
        sketch.pencil.line(0, 18)

        sketch.pencil.line_to(self.BATTLEMENT_WIDTH, self.TOTAL_HEIGHT)
        sketch.pencil.line(0, -self.BATTLEMENT_HEIGHT)
        sketch.pencil.line(-self.BATTLEMENT_WIDTH, 0)

        shape = sketch.pencil.get_closed_shape()
        axis = self.get_rotation_axis(sketch)

        if debug:
            return sketch

        return shape, axis

    def cut_sketch(self, debug=False):
        pf = PlaneFactory()
        plane = pf.get_parallel_plane(self.xy(), 70)
        sketch = Sketch(plane)

        # Make a cross to cut the top
        sketch.pencil.move_to(3.5, 3.5)

        # Top
        sketch.pencil.line(0, self.CROSS_WIDTH)
        sketch.pencil.line(-self.CROSS_SIZE, 0)
        sketch.pencil.line(0, -self.CROSS_WIDTH)

        # Left
        sketch.pencil.line(-self.CROSS_WIDTH, 0)
        sketch.pencil.line(0, -self.CROSS_SIZE)
        sketch.pencil.line(self.CROSS_WIDTH, 0)

        # Bottom
        sketch.pencil.line(0, -self.CROSS_WIDTH)
        sketch.pencil.line(self.CROSS_SIZE, 0)
        sketch.pencil.line(0, self.CROSS_WIDTH)

        # Right
        sketch.pencil.line(self.CROSS_WIDTH, 0)
        sketch.pencil.line(0, self.CROSS_SIZE)
        sketch.pencil.line(-self.CROSS_WIDTH, 0)

        shape = sketch.pencil.get_closed_shape()

        if debug:
            return sketch

        return shape


# %%
if __name__ == "__main__":
    show(Rook())

# %%
