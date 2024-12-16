# %%
from cadbuildr.foundation import Sketch, Lathe, Extrusion, show
from chess.utils import ChessPiece


class Knight(ChessPiece):
    # Knight-specific dimensions
    NECK_HEIGHT = 16.97
    HEAD_WIDTH = 13.05
    HEAD_EXTRUSION = 5

    def __init__(self):
        super().__init__()
        # Build the base of the knight with a Lathe operation
        shape, axis = self.get_base_sketch()
        self.add_operation(Lathe(shape, axis))

        # Build the top of the knight with a Extrusion operation
        shape = self.get_knight_sketch()
        self.add_operation(Extrusion(shape, -self.HEAD_EXTRUSION, self.HEAD_EXTRUSION))
        self.paint("plywood")

    def get_base_sketch(self, debug=False):
        sketch = Sketch(self.xz())
        # Base
        self.create_base_sketch(sketch)
        sketch.pencil.line_to(0, self.NECK_HEIGHT)

        shape = sketch.pencil.get_closed_shape()
        axis = self.get_rotation_axis(sketch)

        if debug:
            return sketch

        return shape, axis

    def get_knight_sketch(self, debug=False):
        sketch = Sketch(self.xz())

        # Move to the top of the base
        sketch.pencil.move_to(self.HEAD_WIDTH / 2, self.NECK_HEIGHT)

        # Draw the knight head profile
        sketch.pencil.arc(8.67 - self.HEAD_WIDTH / 2, 7.06, 16.08)
        sketch.pencil.arc(-(8.67 - 7.12), 21.71 - 7.06, -12.68)
        sketch.pencil.line(-7.12, 29.37 - 21.71)
        sketch.pencil.line(-1, 33.34 - 29.37)
        sketch.pencil.line(1.78, 35.83 - 33.34)
        sketch.pencil.line(12.3 - 0.78, 34.89 - 35.83)
        sketch.pencil.line(14.14 - 12.3, 38.64 - 34.89)
        sketch.pencil.line(-(14.14 - 3.08), 45.91 - 38.64)
        sketch.pencil.line(4.18 - 3.08, 47.58 - 45.91)
        sketch.pencil.line(-4.18, 50.31 - 47.58)
        sketch.pencil.line(-1.33, (self.TOTAL_HEIGHT - self.NECK_HEIGHT) - 50.31)

        # Left side
        sketch.pencil.arc(
            -(8.67 - 1.33), 7.06 - (self.TOTAL_HEIGHT - self.NECK_HEIGHT), -42.07
        )
        sketch.pencil.arc(8.67 - self.HEAD_WIDTH / 2, -7.06, 16.08)

        shape = sketch.pencil.get_closed_shape()

        if debug:
            return sketch

        return shape


# %%
if __name__ == "__main__":
    show(Knight())

# %%
