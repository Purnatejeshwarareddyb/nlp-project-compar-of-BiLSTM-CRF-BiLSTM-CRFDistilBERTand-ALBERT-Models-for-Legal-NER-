"""
Animation utilities for Legal NER System Hub
Author: B. Purna Tejeshwara Reddy
"""

import customtkinter as ctk


class AnimatedButton(ctk.CTkButton):
    """Custom button with hover animations"""

    def __init__(self, master, hover_color=None, **kwargs):
        super().__init__(master, **kwargs)

        self.default_color = self.cget("fg_color")
        self.hover_color = hover_color or self.default_color
        self.default_height = kwargs.get("height", 50)

        # Bind hover events
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        """Handle mouse hover"""
        self.configure(
            fg_color=self.hover_color,
            height=self.default_height + 5
        )

    def on_leave(self, event):
        """Handle mouse leave"""
        self.configure(
            fg_color=self.default_color,
            height=self.default_height
        )


class PulsingLabel(ctk.CTkLabel):
    """Label with pulsing animation"""

    def __init__(self, master, pulse_colors=None, **kwargs):
        super().__init__(master, **kwargs)

        self.pulse_colors = pulse_colors or ["#00ffaa", "#00ff88"]
        self.current_color_index = 0
        self.pulse_animation()

    def pulse_animation(self):
        """Animate color pulsing"""
        self.configure(text_color=self.pulse_colors[self.current_color_index])
        self.current_color_index = (self.current_color_index + 1) % len(self.pulse_colors)
        self.after(1000, self.pulse_animation)


def glow_effect(widget, color, intensity=0.3):
    """Apply glow effect to a widget"""
    try:
        # This is a placeholder - actual glow would require custom drawing
        widget.configure(border_color=color, border_width=2)
    except:
        pass


def fade_in(widget, duration=500):
    """Fade in animation"""
    steps = 20
    delay = duration // steps

    def step(alpha):
        if alpha <= 1.0:
            # CustomTkinter doesn't support alpha, so we'll just show the widget
            widget.after(delay, lambda: step(alpha + 0.05))
        else:
            widget.update()

    step(0.0)