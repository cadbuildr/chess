# %%
from cadbuildr.foundation import Sketch, Lathe, show
from chess.utils import ChessPiece


class Queen(ChessPiece):
    # Queen-specific dimensions
    CROWN_HEIGHT = 42.43
    CROWN_ANGLE = 90
    SPIKE_HEIGHT = 15
    SPIKE_WIDTH = 5

    def __init__(self):
        super().__init__()
        shape, axis = self.get_sketch()
        self.add_operation(Lathe(shape, axis))
        self.paint("plywood")

    def get_sketch(self, debug=False):
        sketch = Sketch(self.xz())

        # Base
        self.create_base_sketch(sketch)

        # Head
        sketch.pencil.arc(-2, self.CROWN_HEIGHT, self.CROWN_ANGLE)
        sketch.pencil.arc(1.5, 3.32, -2)
        sketch.pencil.line(0, 1)
        sketch.pencil.line(self.SPIKE_WIDTH, self.SPIKE_HEIGHT)
        sketch.pencil.line(0, 1)
        sketch.pencil.arc(-10.5, 3.27, -25)
        sketch.pencil.arc(-2, 2, -2)

        shape = sketch.pencil.get_closed_shape()
        axis = self.get_rotation_axis(sketch)

        if debug:
            return sketch

        return shape, axis


# %%
if __name__ == "__main__":
    show(Queen())

# %%
