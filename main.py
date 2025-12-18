"""
⚖️ LEGAL NER SYSTEM - MODEL HUB
Unified GUI Launcher for Legal Named Entity Recognition Models

Author: B. Purna Tejeshwara Reddy
Version: 1.0.0
"""

import customtkinter as ctk
from tkinter import messagebox
import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent))

from utils.run_model import run_model, is_model_running, stop_all_models
from utils.theme import *
from utils.animations import AnimatedButton, PulsingLabel

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class LegalNERHub(ctk.CTk):
    """Main application class for Legal NER Model Hub"""

    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("⚖️ Legal NER System - Model Hub")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)

        # Center window on screen
        self.center_window()

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Create UI elements
        self.create_header()
        self.create_subtitle()
        self.create_model_buttons()
        self.create_status_bar()
        self.create_footer()

        # Handle window close
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def center_window(self):
        """Center the window on screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_header(self):
        """Create the header section"""
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, pady=(30, 10), sticky="ew")

        # Main title
        title_label = PulsingLabel(
            header_frame,
            text="⚖️ LEGAL NER SYSTEM",
            font=FONT_TITLE,
            text_color=ACCENT,
            pulse_colors=[ACCENT, ACCENT_HOVER]
        )
        title_label.pack()

        # Subtitle
        subtitle = ctk.CTkLabel(
            header_frame,
            text="Model Hub & Launcher",
            font=("Helvetica", 18),
            text_color=TEXT_SECONDARY
        )
        subtitle.pack(pady=(5, 0))

        # Decorative line
        line = ctk.CTkFrame(header_frame, height=3, fg_color=ACCENT)
        line.pack(pady=10, padx=300)

    def create_subtitle(self):
        """Create subtitle section"""
        subtitle_label = ctk.CTkLabel(
            self,
            text="Select a Named Entity Recognition model to launch",
            font=FONT_SUBTITLE,
            text_color=TEXT_MUTED
        )
        subtitle_label.grid(row=1, column=0, pady=(0, 20))

    def create_model_buttons(self):
        """Create model selection buttons"""
        # Container frame
        models_frame = ctk.CTkFrame(self, fg_color="transparent")
        models_frame.grid(row=2, column=0, pady=20, sticky="n")

        # Model definitions
        models = [
            ("CRF", "Conditional Random Fields", MODEL_COLORS["CRF"]),
            ("BiLSTM", "Bidirectional LSTM", MODEL_COLORS["BiLSTM"]),
            ("BiLSTM+CRF", "BiLSTM with CRF Layer", MODEL_COLORS["BiLSTM+CRF"]),
            ("ALBERT", "A Lite BERT", MODEL_COLORS["ALBERT"]),
            ("DistilBERT", "Distilled BERT", MODEL_COLORS["DistilBERT"])
        ]

        # Create buttons in grid layout (3 columns)
        for idx, (name, description, color) in enumerate(models):
            row = idx // 3
            col = idx % 3

            # Button container with custom styling
            btn_container = ctk.CTkFrame(
                models_frame,
                fg_color=CARD_BG,
                corner_radius=15,
                border_width=2,
                border_color=SECONDARY_BG
            )
            btn_container.grid(row=row, column=col, padx=15, pady=15)

            # Model name
            name_label = ctk.CTkLabel(
                btn_container,
                text=name,
                font=("Helvetica", 20, "bold"),
                text_color=color
            )
            name_label.pack(pady=(20, 5), padx=20)

            # Model description
            desc_label = ctk.CTkLabel(
                btn_container,
                text=description,
                font=("Helvetica", 11),
                text_color=TEXT_SECONDARY
            )
            desc_label.pack(pady=(0, 15), padx=20)

            # Launch button
            launch_btn = AnimatedButton(
                btn_container,
                text="🚀 Launch Model",
                command=lambda m=name: self.launch_model(m),
                fg_color=color,
                hover_color=self.lighten_color(color),
                text_color=BACKGROUND,
                font=FONT_BUTTON,
                corner_radius=10,
                height=45,
                width=200
            )
            launch_btn.pack(pady=(0, 20), padx=20)

            # Bind hover effects to container
            btn_container.bind("<Enter>", lambda e, c=btn_container, col=color:
            c.configure(border_color=col))
            btn_container.bind("<Leave>", lambda e, c=btn_container:
            c.configure(border_color=SECONDARY_BG))

    def create_status_bar(self):
        """Create status bar"""
        status_frame = ctk.CTkFrame(self, fg_color=CARD_BG, corner_radius=10)
        status_frame.grid(row=3, column=0, pady=20, padx=50, sticky="ew")

        # Status indicator
        status_dot = ctk.CTkLabel(
            status_frame,
            text="●",
            font=("Helvetica", 20),
            text_color=ACCENT
        )
        status_dot.pack(side="left", padx=(20, 5))

        # Status text
        status_text = ctk.CTkLabel(
            status_frame,
            text="System Ready | 5 Models Available",
            font=FONT_SMALL,
            text_color=TEXT_SECONDARY
        )
        status_text.pack(side="left", padx=5)

    def create_footer(self):
        """Create footer section"""
        footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        footer_frame.grid(row=4, column=0, pady=(10, 20))

        # Developer credit
        dev_label = ctk.CTkLabel(
            footer_frame,
            text="Developed by B. Purna Tejeshwara Reddy",
            font=("Helvetica", 11),
            text_color=TEXT_SECONDARY
        )
        dev_label.pack()

        # Version info
        version_label = ctk.CTkLabel(
            footer_frame,
            text="Legal NER System v1.0.0 | Advanced NLP",
            font=("Helvetica", 9),
            text_color=TEXT_MUTED
        )
        version_label.pack(pady=(2, 0))

    def launch_model(self, model_name):
        """Launch selected model"""
        try:
            # Check if model is already running
            if is_model_running(model_name):
                messagebox.showinfo(
                    "Model Running",
                    f"{model_name} model is already running!"
                )
                return

            # Show launching message
            messagebox.showinfo(
                "Launching Model",
                f"🚀 Launching {model_name} Model...\n\n"
                f"The model GUI will open in a separate window."
            )

            # Launch the model
            process = run_model(model_name)

            if process is None:
                messagebox.showerror(
                    "Launch Error",
                    f"Failed to launch {model_name} model.\n\n"
                    f"Please check that the model folder exists."
                )
            else:
                print(f"✓ {model_name} launched successfully (PID: {process.pid})")

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred while launching {model_name}:\n\n{str(e)}"
            )

    def lighten_color(self, hex_color, factor=0.2):
        """Lighten a hex color"""
        # Remove # if present
        hex_color = hex_color.lstrip('#')

        # Convert to RGB
        r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

        # Lighten
        r = min(255, int(r + (255 - r) * factor))
        g = min(255, int(g + (255 - g) * factor))
        b = min(255, int(b + (255 - b) * factor))

        # Convert back to hex
        return f"#{r:02x}{g:02x}{b:02x}"

    def on_closing(self):
        """Handle window close event"""
        if messagebox.askokcancel("Quit", "Do you want to quit?\n\nAll running models will be stopped."):
            stop_all_models()
            self.destroy()


def main():
    """Main entry point"""
    print("=" * 60)
    print("⚖️  LEGAL NER SYSTEM - MODEL HUB")
    print("=" * 60)
    print("Starting application...")
    print()

    app = LegalNERHub()
    app.mainloop()

    print()
    print("Application closed.")
    print("=" * 60)


if __name__ == "__main__":
    main()

