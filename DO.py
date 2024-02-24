from manim import *

class DO(Scene):
    
    def construct(self):
        axis = Axes(
            x_range=[-30, 30, 3],  
            y_range=[-50, 50],      
            axis_config={"color": BLUE},
        )

        axis_labels = axis.get_axis_labels(x_label="t", y_label="A(t)")

        A = 50
        omega = 2 * np.pi * 0.2   
        b = 0.1
        m = 1

        def oss(t):
            return A * np.exp(-b * t / (2 * m)) * np.cos(omega * t)
        
        graph1 = axis.plot(oss, color=GREEN)

        self.add(axis, axis_labels)
        self.play(Create(graph1), run_time=10)  # Increased run_time for better observation
