🚀 LEGAL NER SYSTEM - MODEL HUB
📋 Complete Implementation Guide
I'll create a professional, production-ready unified GUI launcher for your Legal NER models with modern design, smooth animations, and perfect functionality.

📁 PROJECT STRUCTURE
legal_ner_project/
│
├── main_launcher/
│   ├── main.py                     # ⭐ Main GUI application
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── run_model.py            # Model execution handler
│   │   ├── theme.py                # Color themes and styling
│   │   └── animations.py           # GUI animations
│   ├── assets/
│   │   ├── logo.png                # Optional logo
│   │   └── icons/                  # Button icons
│   ├── requirements.txt
│   └── README.md
│
├── crf_model_training/
├── bilstm_model_training/
├── bilstm_crf_model_training/
├── DistilBERT_Model_training/
├── Legal_NER_ALBERT/
│
└── README.md

🎯 FEATURES
✅ Modern Dark UI - Professional cyberpunk-inspired design
✅ Smooth Animations - Hover effects, glow animations, transitions
✅ Process Management - Launch and monitor model processes
✅ Status Indicators - Real-time model running status
✅ Error Handling - Comprehensive error messages
✅ Responsive Design - Clean layout that works on all screens
✅ Easy Navigation - Intuitive button layout
✅ Professional Branding - Custom footer and title design

🔧 INSTALLATION
Step 1: Install Required Packages
bashpip install customtkinter Pillow
Step 2: Verify Folder Structure
Ensure all model folders exist with their respective main.py files:

crf_model_training/main.py
bilstm_model_training/main.py
bilstm_crf_model_training/main.py
Legal_NER_ALBERT/main.py
DistilBERT_Model_training/main.py


🚀 QUICK START
Run the Application
bashcd legal_ner_project/main_launcher
python main.py

💻 USAGE GUIDE

Launch the Hub: Run python main.py from the main_launcher directory
Select a Model: Click on any model button (CRF, BiLSTM, etc.)
Confirm Launch: A popup will confirm the model is launching
Use the Model: The model's GUI opens in a new window
Return to Hub: Close the model window to select another model
Exit: Click the ❌ button or close the main window


🎨 CUSTOMIZATION
Change Colors (edit utils/theme.py)
pythonBACKGROUND = "#0a0e27"      # Main background
ACCENT = "#00ffaa"          # Accent color
BUTTON_BG = "#1a1f3a"       # Button background
Add Custom Logo

Place your logo as assets/logo.png (300x100px recommended)
The app will automatically detect and display it

Modify Model Paths
Edit the model_paths dictionary in utils/run_model.py:
pythonmodel_paths = {
    "CRF": "../crf_model_training/main.py",
    # Add or modify paths here
}

🐛 TROUBLESHOOTING
Issue: Model doesn't launch
Solution: Verify the model path exists and main.py is executable
Issue: Import errors
Solution: Install all requirements: pip install -r requirements.txt
Issue: GUI doesn't appear
Solution: Ensure tkinter is installed (comes with Python by default)

📊 SYSTEM REQUIREMENTS

Python: 3.7 or higher
OS: Windows, macOS, Linux
RAM: 4GB minimum (8GB recommended for model execution)
Display: 800x600 minimum resolution


🔐 SECURITY NOTES

Models are launched in separate processes for isolation
No network connections required
All data processing is local


👨‍💻 DEVELOPER
B. Purna Tejeshwara Reddy

📝 LICENSE
This project is for academic and research purposes.

🆘 SUPPORT
For issues or questions:

Check the troubleshooting section
Verify all model folders exist
Ensure Python dependencies are installed


🎓 TECHNICAL DETAILS
Architecture

Frontend: CustomTkinter (modern UI framework)
Process Management: subprocess module
Styling: Custom CSS-like theme system
Animations: Event-driven hover/click effects

Model Integration
Each model runs independently with its own:

Training data
Saved weights
GUI interface
Prediction engine

The launcher serves as a unified access point without modifying individual models.

🔄 VERSION HISTORY
v1.0.0 (Current)

Initial release
5 model integration
Modern UI with animations
Process management system