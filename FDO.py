from manim import *

class FDO(Scene):
    
    def construct(self):
        axis = Axes(
            x_range=[0, 200, 10],     # Adjusted x-range for better visualization
            y_range=[-50, 50, 10],  # Adjusted y-range for better visualization
            axis_config={"color": BLUE},
        )

        axis_labels = axis.get_axis_labels(x_label="t", y_label="A(t)")

        
        A = 10
        F = 100                     # Reduced external force for less dominance
        omega = 3        # Increased angular frequency for faster oscillation
        b = 1                      # Increased damping coefficient for more pronounced damping
        m = 1
        k = 1

        def Ao():
                return F / np.sqrt((k - m * omega**2)**2 + (b * omega)**2)

        def delta():
                return np.arctan((m*omega*omega - k)/b*omega)

        def oss(t):
                return Ao() * np.cos(omega * t - delta())

        graph1 = axis.plot(oss, color=GREEN)

        self.add(axis, axis_labels)
        self.play(Create(graph1), run_time=10)  # Increased run_time for better observation
