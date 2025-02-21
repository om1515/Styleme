from manim import *

class StudentIntro(ThreeDScene):
    def construct(self):
        # Set up 3D camera with adjusted orientation to avoid flipping
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Start with some abstract, energetic animations
        intro_text = Text("Welcome to the Future of Technology", font_size=60, color=YELLOW)
        intro_text.scale(1.5)
        intro_text.shift(UP * 3)
        self.play(Write(intro_text), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(intro_text), run_time=1)

        # Transition into AI and ML Theme with a cool animation
        ai_circle = Circle(radius=1.5, color=BLUE).shift(LEFT * 2)
        ai_text = Text("Where Artificial Intelligence meets Creativity", font_size=40, color=WHITE)
        ai_text.move_to(ai_circle.get_center())
        self.play(Create(ai_circle), Write(ai_text), run_time=2)
        self.wait(1)

        # Zoom out and transition into code and software world
        self.play(ai_circle.animate.shift(RIGHT * 3), ai_text.animate.shift(RIGHT * 3), run_time=1)
        code_lines = VGroup(
            Text("def machine_learning_model():", font_size=30, color=WHITE).shift(UP),
            Text("    # Neural Networks, Deep Learning", font_size=30, color=WHITE).shift(UP * 0.5),
            Text("    return 'Intelligence!'", font_size=30, color=WHITE)
        )
        self.play(FadeIn(code_lines), run_time=1.5)
        self.wait(1)

        # Add 3D elements to represent 3D modelling
        model_cube = Cube(side_length=2).shift(DOWN * 2)
        model_text = Text("Transforming Ideas into Reality", font_size=50, color=ORANGE)
        model_text.move_to(model_cube.get_center())
        self.play(FadeIn(model_text), Create(model_cube), run_time=2)
        self.wait(1)

        # Transition into a fast-paced 3D world of creativity
        self.play(model_cube.animate.rotate(PI / 2, axis=UP), model_text.animate.scale(1.2), run_time=1.5)

        # Final cinematic: Mix all themes in one fluid 3D motion
        final_scene = VGroup(ai_circle, ai_text, model_cube, model_text)
        self.play(
            final_scene.animate.scale(0.8).shift(UP * 2),
            run_time=2
        )

        # End with a powerful message that ties it all together
        final_text = Text("Empowering the Future through Code, AI & 3D", font_size=60, color=PURPLE)
        final_text.scale(1.5)
        self.play(Write(final_text), run_time=1.5)

        # Add a 3D spin for dramatic flair
        self.play(Rotate(final_text, angle=360 * DEGREES, axis=UP), run_time=2)
        
        self.wait(1)
