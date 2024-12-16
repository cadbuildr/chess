# %%
from cadbuildr.foundation import Sketch, Lathe, show
from chess.utils import ChessPiece


class Pawn(ChessPiece):
    # Pawn-specific dimensions
    BODY_ARC_HEIGHT = 24.06
    BODY_ARC_ANGLE = 50
    HEAD_RADIUS = 9

    def __init__(self):
        super().__init__()
        axis, shape = self.get_sketch()
        self.add_operation(Lathe(shape, axis))
        self.paint("plywood")

    def get_sketch(self, debug=False):
        sketch = Sketch(self.xz())

        # Base
        self.create_base_sketch(sketch)

        # Body
        sketch.pencil.arc(-3, self.BODY_ARC_HEIGHT, self.BODY_ARC_ANGLE)
        sketch.pencil.arc(1, 3.26, -2)
        sketch.pencil.arc_to(0, 60, -self.HEAD_RADIUS)

        shape = sketch.pencil.get_closed_shape()
        axis = self.get_rotation_axis(sketch)

        if debug:
            return sketch

        return axis, shape


# %%
if __name__ == "__main__":
    show(Pawn())

# %%
