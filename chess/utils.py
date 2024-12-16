# %%
from cadbuildr.foundation import Part, Sketch, Axis, Line, Point


class ChessPiece(Part):
    """Base class for all chess pieces"""

    # Common dimensions
    BASE_DIAMETER = 30  # Width of base
    BASE_HEIGHT = 3  # Height of first vertical section
    STEM_HEIGHT = 2  # Height of stem connection
    TOTAL_HEIGHT = 75  # Standard height for pieces

    def __init__(self):
        super().__init__()

    def create_base_sketch(self, sketch):
        """Creates the common base shape used by all pieces"""
        # Base
        sketch.pencil.line_to(self.BASE_DIAMETER / 2, 0)
        sketch.pencil.line(0, self.BASE_HEIGHT)
        sketch.pencil.line(-2, self.STEM_HEIGHT)
        sketch.pencil.arc(-3, 8.97, -6)
        sketch.pencil.line(0, 1)
        sketch.pencil.arc(-2, 2, -2)

        return sketch

    def get_rotation_axis(self, sketch):
        """Creates the standard rotation axis for lathe operations"""
        return Axis(Line(Point(sketch, 0, 0), Point(sketch, 0, 10)))
