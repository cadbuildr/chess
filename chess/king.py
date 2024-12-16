# %%
from cadbuildr.foundation import (
    Sketch,
    Lathe,
    PlaneFactory,
    Extrusion,
    CircularPattern,
    Point,
    show,
)
from chess.utils import ChessPiece


class King(ChessPiece):
    # King-specific dimensions
    CROWN_ARC_HEIGHT = 44.02
    CROWN_ARC_ANGLE = 85
    HEAD_WIDTH = 5
    HEAD_HEIGHT = 10
    TOP_WIDTH = 8
    CROSS_HEIGHT = 15
    CROSS_WIDTH = 2
    NUM_CROSS_CUTS = 6

    def __init__(self):
        super().__init__()
        # Build the King base
        shape, axis = self.get_sketch()
        self.add_operation(Lathe(shape, axis))

        # Cut the cross pattern
        cross_shapes = self.cut_sketch()
        for shape in cross_shapes:
            self.add_operation(Extrusion(shape, 5, cut=True))
        self.paint("plywood")

    def get_sketch(self, debug=False):
        sketch = Sketch(self.xz())

        # Create base
        self.create_base_sketch(sketch)

        # Head
        sketch.pencil.arc(0, self.CROWN_ARC_HEIGHT, self.CROWN_ARC_ANGLE)
        sketch.pencil.arc(1.625, 3.16, -2)
        sketch.pencil.arc(-0.625, 10.84, 10.16)
        sketch.pencil.line(4, 8)
        sketch.pencil.line(0, 2)

        # Top crown
        sketch.pencil.line(-self.HEAD_WIDTH, 0)
        sketch.pencil.line(0, -self.HEAD_HEIGHT)
        sketch.pencil.line(-self.TOP_WIDTH, 0)

        shape = sketch.pencil.get_closed_shape()
        axis = self.get_rotation_axis(sketch)

        if debug:
            return sketch

        return shape, axis

    def cut_sketch(self, debug=False):
        pf = PlaneFactory()
        plane = pf.get_parallel_plane(self.xy(), 80)
        sketch = Sketch(plane)

        sketch.pencil.move_to(1, 1)

        # Cross pattern
        sketch.pencil.line(0, self.CROSS_HEIGHT)
        sketch.pencil.line(-self.CROSS_WIDTH, 0)
        sketch.pencil.line(0, -self.CROSS_HEIGHT)

        shape = sketch.pencil.get_closed_shape()

        cp = CircularPattern(Point(sketch, 0, 0), self.NUM_CROSS_CUTS).run(shape)
        cp.insert(0, shape)

        if debug:
            return sketch

        return cp


# %%
if __name__ == "__main__":
    show(King())

# %%
