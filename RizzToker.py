import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
from deepseek import DeepSeek  # Make sure to install: pip install deepseek-ai

class BrawlStarsTikTokBot:
    def __init__(self):
        # Initialize DeepSeek AI 
        self.ai = DeepSeek(api_key=sk-0957d2ee373c4f25b873749db4f8435a)
        
        # TikTok brainrot phrases
        self.brainrot_phrases = [
            "No cap, **{}** is OP rn 🚫🧢",
            "Bro, **{}** is META af 💯",  
            "Pick **{}** or you're trolling 😬",  
            "LOL imagine not using **{}** 💀",  
            "Spamming **{}** = free trophies 🤑",  
            "Skill issue if you don't play **{}** 😤",  
            "**{}** is CRACKED this season 🔥"
        ]
        
        # (Previous brawler/map data remains the same...)
        
        # GUI Setup
        self.root = tk.Tk()
        self.root.title("BRAWL STARS TIKTOK BRAINROT BOT (2025)")
        self.root.geometry("750x650")
        self.root.configure(bg="#1a1a2e")
        self._setup_gui()
        self._create_menu()
    
    def _create_menu(self):
        """Create professional menu bar with credits"""
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Credits menu
        credits_menu = tk.Menu(menubar, tearoff=0)
        credits_menu.add_command(label="Developer Info", command=self._show_credits)
        credits_menu.add_separator()
        credits_menu.add_command(label="About", command=self._show_about)
        menubar.add_cascade(label="Credits", menu=credits_menu)
        
        self.root.config(menu=menubar)
    
    def _show_credits(self):
        """Show professional credits dialog"""
        credits_text = """
        Developer Information:
        
        TikTok: @T...bby
        Discord: tyabby
        YouTube: @TabbyEh
        
        This application uses:
        - DeepSeek AI for dynamic responses
        - Tkinter for GUI
        - Brawl Stars 2025 meta data
        """
        messagebox.showinfo("Credits", credits_text)
    
    def _show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About", 
            "Brawl Stars TikTok Brainrot Advisor\n"
            "Version 1.0 (2025)\n\n"
            "Provides meta advice with 2025 TikTok slang humor"
        )
    
    # (All previous methods remain the same...)

    def _setup_gui(self):
        """Create the GUI layout with professional touches"""
        # Main container
        main_frame = tk.Frame(self.root, bg="#1a1a2e", padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title with subtle border
        title_frame = tk.Frame(main_frame, bg="#2a2a4a", bd=2, relief=tk.GROOVE)
        title_frame.pack(fill=tk.X, pady=(0,10))
        
        title_label = tk.Label(
            title_frame,
            text="BRAWL STARS TIKTOK BRAINROT BOT",
            font=("Arial", 16, "bold"),
            fg="#ff3366",
            bg="#2a2a4a",
            padx=10,
            pady=5
        )
        title_label.pack()
        
        # Input frame with modern look
        input_frame = tk.Frame(main_frame, bg="#1a1a2e")
        input_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            input_frame,
            text="Ask about brawlers, maps, or meta:",
            font=("Arial", 9),
            fg="white",
            bg="#1a1a2e"
        ).pack(side=tk.LEFT, padx=(0,5))
        
        self.user_input = tk.Entry(
            input_frame,
            width=45,
            font=("Arial", 10),
            bd=2,
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground="#4a4a8a",
            highlightcolor="#ff3366"
        )
        self.user_input.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        submit_btn = tk.Button(
            input_frame,
            text="Send",
            command=self._process_input,
            bg="#ff3366",
            fg="white",
            font=("Arial", 10, "bold"),
            bd=0,
            padx=15,
            activebackground="#ff0044"
        )
        submit_btn.pack(side=tk.LEFT, padx=(5,0))
        
        # Output area with modern styling
        output_frame = tk.Frame(main_frame, bg="#2a2a4a", bd=2, relief=tk.GROOVE)
        output_frame.pack(fill=tk.BOTH, expand=True)
        
        self.output_area = scrolledtext.ScrolledText(
            output_frame,
            width=80,
            height=20,
            font=("Consolas", 10),
            bg="#2a2a4a",
            fg="white",
            insertbackground="white",
            padx=10,
            pady=10,
            bd=0,
            highlightthickness=0
        )
        self.output_area.pack(fill=tk.BOTH, expand=True)
        self.output_area.insert(tk.END, "👋 OMG hi bestie! Ask me about Brawl Stars! 🫡🔥\n")

    # (Rest of your existing methods remain unchanged...)

if __name__ == "__main__":
    bot = BrawlStarsTikTokBot()
    bot.run()