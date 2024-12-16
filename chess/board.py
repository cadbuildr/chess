# %%
from cadbuildr.foundation import (
    Assembly,
    Material,
    Part,
    Point,
    Square,
    TFHelper,
    show,
    Sketch,
    Extrusion,
)
from chess.bishop import Bishop
from chess.king import King
from chess.knight import Knight
from chess.pawn import Pawn
from chess.queen import Queen
from chess.rook import Rook


class ChessBoard(Assembly):
    TILE_SIZE = 40  # Size of each square on the board
    BOARD_SIZE = 8  # Number of squares per dimension (8x8 for chess)

    def __init__(self):
        super().__init__()
        self.create_board()
        self.add_pieces()

    def create_board(self):
        # material_dark = Material()
        # material_dark.set_diffuse_colorRGB(0, 0, 0)  # Black squares

        # material_light = Material()
        # material_light.set_diffuse_colorRGB(255, 255, 255)  # White squares

        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                # Create a square for each tile
                square = Part()
                sketch = Sketch(square.xy())
                tile = Square.from_center_and_side(Point(sketch, 0, 0), self.TILE_SIZE)
                extrusion = Extrusion(tile, 5)  # Give some thickness to tiles
                square.add_operation(extrusion)

                # Apply material based on checkerboard pattern
                if (row + col) % 2 == 0:
                    square.paint("plywood")
                else:
                    square.paint("grey")

                # Translate the square to the proper position
                tf = TFHelper()
                tf.translate_x(
                    col * self.TILE_SIZE
                    - (self.BOARD_SIZE / 2) * self.TILE_SIZE
                    + self.TILE_SIZE / 2
                )
                tf.translate_y(
                    row * self.TILE_SIZE
                    - (self.BOARD_SIZE / 2) * self.TILE_SIZE
                    + self.TILE_SIZE / 2
                )
                self.add_component(square, tf.get_tf())

    def add_pieces(self):
        initial_positions = {
            "R": Rook,
            "N": Knight,
            "B": Bishop,
            "Q": Queen,
            "K": King,
            "P": Pawn,
        }

        # Standard chess starting positions
        setup = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]

        # Black pieces (rows 0 and 1)
        self.place_pieces(setup[:2], initial_positions, color="black", y_offset=0)

        # White pieces (rows 6 and 7)
        self.place_pieces(setup[6:], initial_positions, color="white", y_offset=6)

    def place_pieces(self, setup, initial_positions, color, y_offset):
        for i, row in enumerate(setup):
            for j, piece in enumerate(row):
                if piece is not None:
                    x_pos = (
                        j * self.TILE_SIZE
                        - (self.BOARD_SIZE / 2) * self.TILE_SIZE
                        + self.TILE_SIZE / 2
                    )
                    y_pos = (
                        (i + y_offset) * self.TILE_SIZE
                        - (self.BOARD_SIZE / 2) * self.TILE_SIZE
                        + self.TILE_SIZE / 2
                    )

                    piece_instance = initial_positions[piece]()  # Create the piece
                    if color == "white":
                        piece_instance.paint("plywood")
                    else:
                        piece_instance.paint("grey")

                    # Translate the piece to the correct position
                    tf = TFHelper()
                    tf.translate_x(x_pos)
                    tf.translate_y(y_pos)
                    tf.translate_z(5)  # Lift the piece slightly above the board
                    self.add_component(piece_instance, tf.get_tf())


# if __name__ == "__main__":
show(ChessBoard())

# %%
