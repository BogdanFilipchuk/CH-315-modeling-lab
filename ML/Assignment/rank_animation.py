from manim import *


class RankInterpretation(LinearTransformationScene):
    def __init__(self, **kwargs):
        super().__init__(show_coordinates=False, **kwargs)

    def apply_function(self, function, **kwargs):
        self.moving_mobjects = []
        super().apply_function(function, **kwargs)

    def set_caption(self, text):
        new_caption = Text(text, font_size=30).to_edge(UP).add_background_rectangle()
        self.play(FadeOut(self.caption), FadeIn(new_caption))
        self.caption = new_caption
        self.add_foreground_mobject(new_caption)
        self.wait(1.5)

    def construct(self):
        self.caption = Text("rank = number of independent columns", font_size=30)
        self.caption.to_edge(UP).add_background_rectangle()
        self.add_foreground_mobject(self.caption)
        self.wait(1.5)

        # rank 2: the columns (2, 1) and (1, 1.5) are independent
        A = [[2, 1], [1, 1.5]]
        self.set_caption("rank 2: columns (2, 1) and (1, 1.5)")
        self.apply_matrix(A)
        self.set_caption("the plane is mapped onto the whole plane")
        self.apply_inverse(A)
        self.set_caption("nothing is lost, so we can go back (invertible)")

        # rank 1: the second column (2, 1) is 2 x the first column (1, 0.5)
        B = [[1, 2], [0.5, 1]]
        null_space = Line([-6, 3, 0], [6, -3, 0], color=YELLOW, stroke_width=6)
        self.add_transformable_mobject(null_space)
        self.play(Create(null_space))
        self.set_caption("rank 1: columns (1, 0.5) and (2, 1) = 2 x (1, 0.5)")
        self.apply_matrix(B)
        self.set_caption("the plane is squashed onto a line, yellow line (null space) -> 0")

        y = Dot([-1, 2, 0], radius=0.12, color=PINK)
        y_label = Text("y", font_size=30, color=PINK).next_to(y, RIGHT, buff=0.15)
        self.add_foreground_mobject(y, y_label)
        self.play(FadeIn(y), FadeIn(y_label))
        self.set_caption("y is not on the line, so Xw = y has no solution")
        self.wait(1)
