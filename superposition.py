from manim import *

class test(Scene):
    def construct(self):
        axis=Axes(
            x_range=[-5,5],
            y_range=[-5,5],
            axis_config={"color": BLUE},
        )

        axis_label=axis.get_axis_labels(x_label="t",y_label="A(t)")

        A1=1
        A2=1
        omega1 = 2 * np.pi * 2.1  # Slightly higher frequency
        omega2 = 2 * np.pi * 2.0  # Lower frequency

        phi1=0
        phi2=0

        def shm1(t):
            return A1*np.sin(omega1*t+phi1)
        
        def shm2(t):
            return A2*np.sin(omega2*t+phi2)
        
        def superposition(t):
            return shm1(t)+shm2(t)
        
        graph1=axis.plot(lambda x: shm1(x), color=GREEN)
        graph2=axis.plot(lambda x: shm2(x), color=RED)
        graph3=axis.plot(lambda x: superposition(x), color=WHITE)

        self.add(axis,axis_label)
        self.play(Create(graph1),run_time=2)
        self.play(Create(graph2),run_time=2)
        self.play(Create(graph3),run_time=4)
        self.play(FadeOut(graph1),FadeOut(graph2),run_time=2)
        self.wait(1)

