# %%
from cadbuildr.foundation import Sketch, Lathe, show
from chess.utils import ChessPiece


class Bishop(ChessPiece):
    # Bishop-specific dimensions
    HEAD_HEIGHT = 45
    HEAD_ANGLE = 45

    def __init__(self):
        super().__init__()
        axis, shape = self.get_sketch()
        self.add_operation(Lathe(shape, axis))
        self.paint("plywood")

    def get_sketch(self, debug=False):
        sketch = Sketch(self.xz())
        # Create base
        self.create_base_sketch(sketch)

        # Head
        sketch.pencil.arc(-0.5, 31.02, self.HEAD_ANGLE)
        sketch.pencil.arc(1, 3.94, -2.05)
        sketch.pencil.arc(-4.5, 19.06, -20)
        sketch.pencil.arc_to(0, self.TOTAL_HEIGHT, -3.1)

        shape = sketch.pencil.get_closed_shape()
        axis = self.get_rotation_axis(sketch)

        if debug:
            return sketch

        return axis, shape


# %%
if __name__ == "__main__":
    show(Bishop())

# %%
