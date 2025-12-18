"""
Theme configuration for Legal NER System Hub
Author: B. Purna Tejeshwara Reddy
"""

# Color Palette
BACKGROUND = "#0a0e27"
SECONDARY_BG = "#1a1f3a"
CARD_BG = "#252d4a"
ACCENT = "#00ffaa"
ACCENT_HOVER = "#00ff88"
TEXT_PRIMARY = "#ffffff"
TEXT_SECONDARY = "#a0aec0"
TEXT_MUTED = "#64748b"

# Model Colors
MODEL_COLORS = {
    "CRF": "#00ffaa",
    "BiLSTM": "#00d4ff",
    "BiLSTM+CRF": "#ff00ff",
    "ALBERT": "#ffaa00",
    "DistilBERT": "#ff4444"
}

# Fonts
FONT_TITLE = ("Helvetica", 28, "bold")
FONT_SUBTITLE = ("Helvetica", 16)
FONT_BUTTON = ("Helvetica", 14, "bold")
FONT_SMALL = ("Helvetica", 10)

# Dimensions
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 80
BUTTON_PADDING = 20

# Animation Settings
HOVER_DURATION = 200  # milliseconds
GLOW_INTENSITY = 0.3