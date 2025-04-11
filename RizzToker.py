import tkinter as tk
from tkinter import ttk, scrolledtext
import random
from transformers import AutoModelForCausalLM, AutoTokenizer

class BrawlStarsTikTokBot:
    def __init__(self):
        # Load DeepSeek model (pretend it's fine-tuned on Brawl Stats)
        self.model_name = "deepseek-ai/deepseek-llm-7b"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        
        # 2025 TikTok slang
        self.brainrot_phrases = [
            "No cap, **{}** is OP rn 🚫🧢",
            "Bro, **{}** is META af 💯",  
            "Pick **{}** or you're trolling 😬",  
            "LOL imagine not using **{}** 💀",  
            "Spamming **{}** = free trophies 🤑",  
            "Skill issue if you don't play **{}** 😤",  
            "**{}** is CRACKED this season 🔥",
            "Rizzlord **{}** solos 🗣️🔥"
        ]
        
        # ALL BRAWLERS (as of 2025)
        self.all_brawlers = [
            "SHELLY", "COLT", "BULL", "BROCK", "RICO", "SPIKE", "BARLEY", "JESSIE", "NITA", "DYNAMIKE",
            "EL PRIMO", "MORTIS", "CROW", "POCO", "BO", "PIPER", "PAM", "TARA", "GENE", "MAX",
            "MR. P", "SPROUT", "BYRON", "SQUEAK", "GROM", "BUZZ", "GRIFF", "ASH", "MEG", "LOU",
            "GALE", "BELLE", "COLETTE", "EDGAR", "STU", "SURGE", "BUSTER", "FANG", "EVE", "JANET",
            "BONNIE", "OTIS", "SAM", "GUS", "MAISIE", "HANK", "PEARL", "MANDY", "R-T", "WILLOW",
            "DOUG", "CHUCK", "LARRY", "CORDELIUS", "KIT", "LEON", "SANDY", "AMBER", "8-BIT", "CARL",
            "DARRYL", "PENNY", "FRANK", "BIBI", "TICK", "EMZ", "JACKY"
        ]
        
        # ALL KNOCKOUT MAPS (2025 meta)
        self.knockout_maps = {
            "BELLE'S ROCK": ["BELLE", "PIPER", "BROCK", "BYRON"],
            "GOLDARM GULCH": ["COLETTE", "STU", "BUZZ", "FANG"],
            "SPLIT SECOND": ["SPIKE", "TARA", "GROM", "GENE"],
            "FLARING PHOENIX": ["AMBER", "LOU", "GALE", "MAX"],
            "OUT IN THE OPEN": ["LEON", "CROW", "SANDY", "BUZZ"],
            "MIDDLEGROUND": ["SPROUT", "BARLEY", "TICK", "DYNAMIKE"],
            "CIRCULAR CANYON": ["SURGE", "BUSTER", "JANET", "BONNIE"],
            "DUELING BEETLES": ["ASH", "FRANK", "BULL", "EL PRIMO"],
            "SNEAKY FIELDS": ["MORTIS", "EDGAR", "FANG", "STU"],
            "SHOTGUN SHOWDOWN": ["SHELLY", "BULL", "DARRYL", "JACKY"]
        }
        
        # ALL BRAWLER BUILDS (2025 meta)
        self.brawler_builds = {
            "SHELLY": ["HEALING WAVES", "FAST FORWARD", "SHELL SHOCK"],
            "COLT": ["MAGNUM SPECIAL", "SILVER BULLET", "BOOTED UP"],
            "BULL": ["BERSERKER", "STOMP", "TOUGH GUY"],
            "BROCK": ["MORE ROCKETS", "ROCKET LACES", "ROCKET NO. FOUR"],
            "SPIKE": ["FERTILIZE", "CURVEBALL", "LIFE PLANT"],
            "CROW": ["EXTRA TOXIC", "SLOWING TOXIN", "DEFENSE BOOSTER"],
            "LEON": ["SMOKE TRAILS", "INVISIHEAL", "LOLLIPOP DROP"],
            "SANDY": ["RUDE SANDS", "HEALING WINDS", "SWEET DREAMS"],
            "AMBER": ["WILD FLAMES", "SCORCHIN' SIPHON", "FIREBALL"],
            "GENE": ["MAGIC PUFFS", "LAMP BLOWOUT", "VENGEFUL SPIRITS"],
            "MORTIS": ["CREEPY HARVEST", "COMBAT SPADE", "SURVIVAL SHOVEL"],
            "TARA": ["BLACK PORTAL", "HEALING SHADE", "SUPPORT FROM BEYOND"],
            "SPROUT": ["OVERGROWTH", "PHOTOSYNTHESIS", "GARDEN MULCHER"],
            "BYRON": ["INJECTION", "SHOT IN THE ARM", "MALAISE"],
            "SQUEAK": ["SUPER STICKY", "RESIDUE", "CHEMICAL WARFARE"],
            "GROM": ["FOOTBALL BREAKER", "X-FACTOR", "SPICED UP"],
            "BUZZ": ["EYE OF THE STORM", "TOUGHER TORPEDO", "HOMING DEVICE"],
            "FANG": ["FRESH KICKS", "DIVINE SOLES", "SHOE SHINE"],
            "EVE": ["UNNATURAL ORDER", "HAPPY SURPRISE", "MOTHERLY LOVE"],
            "JANET": ["STAGE VIEW", "VOCAL WARM UP", "STARRING ROLE"],
            "BONNIE": ["STARR POWER", "SUGAR RUSH", "BLACK POWDER"],
            "OTIS": ["INK REFILL", "STENCIL GLUE", "DORMANT STAR"],
            "SAM": ["HEARTY RECOVERY", "MAGNETIC FIELD", "PULSE REPELLENT"],
            "GUS": ["SOUL SWITCHER", "KOOKY POPPER", "SPOOKY SPIRIT"],
            "MAISIE": ["GROUNDED", "TRIGGER HAPPY", "RECOIL SPRING"],
            "HANK": ["HOLDING ON", "PULSE MODULATOR", "LAST GASP"],
            "PEARL": ["HEAT ACTIVATOR", "COOLING SPRINGS", "BOILING POINT"],
            "MANDY": ["HARD CANDY", "SUGAR COATED", "SWEET TOOTH"],
            "R-T": ["SELF DEFENSE", "MARKED FOR DEATH", "DIVIDE AND CONQUER"],
            "WILLOW": ["SPIRITUAL BOOST", "PUPPET STRINGS", "MIND CONTROL"],
            "DOUG": ["SAUCEY", "HEALTHY SNACK", "EXTRA CHEESY"],
            "CHUCK": ["PIT STOP", "HIDDEN MECHANIC", "TURBO CHARGED"],
            "LARRY": ["BIRD WATCHER", "FEATHERED FRIENDS", "FLOCK OF DOOM"],
            "CORDELIUS": ["HARVEST TIME", "OVERGROWTH", "GARDEN TOOLS"],
            "KIT": ["SCRATCH POST", "PLAYFUL SCRATCHES", "NINE LIVES"],
            "8-BIT": ["BOOSTED BOOSTER", "PLUGGED IN", "EXTRA CREDITS"],
            "EMZ": ["BAD KARMA", "HYPE", "FRIENDZONED"],
            "STU": ["GASO-HEAL", "SPEED ZONE", "ZERO DRAG"],
            "EDGAR": ["HARD LANDING", "FISTICUFFS", "LET'S FLY"],
            "GRIFF": ["CASH BACK", "PIGGY BANK", "COIN SHOWER"],
            "ASH": ["RAGE QUIT", "MAD AS HECK", "FIRST BASH"],
            "MEG": ["FORCE FIELD", "JOLTING VOLTS", "HEAVY METAL"],
            "LOU": ["SUPERCOOL", "CRYO SYRUP", "HYPOTHERMIA"],
            "GALE": ["BLUSTERY BLOW", "FREEZING SNOW", "TWISTER"],
            "SURGE": ["TO THE MAX", "POWER SHIELD", "SERVE ICE COLD"],
            "COLETTE": ["MASS TAX", "PUSH IT", "TWO FOR ONE"],
            "BELLE": ["GROUNDED", "POSITIVE FEEDBACK", "SCOUTING TURRET"],
            "BUZZ": ["EYE OF THE STORM", "TOUGHER TORPEDO", "HOMING DEVICE"],
            "FANG": ["FRESH KICKS", "DIVINE SOLES", "SHOE SHINE"],
            "EVE": ["UNNATURAL ORDER", "HAPPY SURPRISE", "MOTHERLY LOVE"],
            "JANET": ["STAGE VIEW", "VOCAL WARM UP", "STARRING ROLE"],
            "BONNIE": ["STARR POWER", "SUGAR RUSH", "BLACK POWDER"],
            "OTIS": ["INK REFILL", "STENCIL GLUE", "DORMANT STAR"],
            "SAM": ["HEARTY RECOVERY", "MAGNETIC FIELD", "PULSE REPELLENT"],
            "GUS": ["SOUL SWITCHER", "KOOKY POPPER", "SPOOKY SPIRIT"],
            "MAISIE": ["GROUNDED", "TRIGGER HAPPY", "RECOIL SPRING"],
            "HANK": ["HOLDING ON", "PULSE MODULATOR", "LAST GASP"],
            "PEARL": ["HEAT ACTIVATOR", "COOLING SPRINGS", "BOILING POINT"],
            "MANDY": ["HARD CANDY", "SUGAR COATED", "SWEET TOOTH"],
            "R-T": ["SELF DEFENSE", "MARKED FOR DEATH", "DIVIDE AND CONQUER"],
            "WILLOW": ["SPIRITUAL BOOST", "PUPPET STRINGS", "MIND CONTROL"],
            "DOUG": ["SAUCEY", "HEALTHY SNACK", "EXTRA CHEESY"],
            "CHUCK": ["PIT STOP", "HIDDEN MECHANIC", "TURBO CHARGED"],
            "LARRY": ["BIRD WATCHER", "FEATHERED FRIENDS", "FLOCK OF DOOM"],
            "CORDELIUS": ["HARVEST TIME", "OVERGROWTH", "GARDEN TOOLS"],
            "KIT": ["SCRATCH POST", "PLAYFUL SCRATCHES", "NINE LIVES"]
        }
        
        # Initialize GUI
        self.root = tk.Tk()
        self.root.title("BRAWL STARS TIKTOK BRAINROT BOT (2025)")
        self.root.geometry("700x600")
        self.root.configure(bg="#1a1a2e")
        
        self._setup_gui()
    
    def _add_tiktok_slang(self, text):
        """Inject TikTok brainrot into responses"""
        emojis = random.choice(["💀", "🔥", "😭", "🗣️", "👀", "🤯", "🫡", "🚫🧢"])
        prefixes = ["TBH", "NGL", "ONG", "FRFR", "LOWKEY", "HIGHKEY", "RATIO"]
        slang = random.choice(prefixes) + " " if random.random() > 0.7 else ""
        return f"{slang}{text} {emojis}"
    
    def get_knockout_pick(self, map_name):
        """Recommend OP brawlers for a Knockout map"""
        map_name = map_name.upper()
        if map_name not in self.knockout_maps:
            return self._add_tiktok_slang(f"Bruh this map ain't real 💀 (Try: {', '.join(self.knockout_maps.keys())})")
        
        picks = self.knockout_maps[map_name]
        chosen = random.choice(picks)
        response = random.choice(self.brainrot_phrases).format(chosen)
        return self._add_tiktok_slang(response)
    
    def get_brawler_build(self, brawler_name):
        """Return the most broken build for a brawler"""
        brawler = brawler_name.upper()
        if brawler not in self.brawler_builds:
            return self._add_tiktok_slang(f"Who even plays {brawler} in 2025? 😭")
        
        star_power, gadget, hypercharge = self.brawler_builds[brawler]
        response = (
            f"**{brawler} BUILD** 🛠️\n"
            f"Star Power: {star_power} ⭐\n"
            f"Gadget: {gadget} ⚡\n"
            f"Hypercharge: {hypercharge} 🌀\n"
            f"Trust, this build is BUSSIN 💯"
        )
        return self._add_tiktok_slang(response)
    
    def generate_response(self, prompt):
        """Use DeepSeek to generate a TikTok-style answer"""
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_new_tokens=50)
        raw_response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Post-process to make it more "TikTok"
        tiktokified = (
            raw_response.replace(".", random.choice([" 💀", " 🔥", " 😭"]))
            .replace("the", "da" if random.random() > 0.7 else "the")
            .replace("you", "u" if random.random() > 0.6 else "you")
        )
        return self._add_tiktok_slang(tiktokified)
    
    def _setup_gui(self):
        """Create the GUI layout"""
        # Title
        title_label = tk.Label(
            self.root,
            text="BRAWL STARS TIKTOK BRAINROT BOT (2025)",
            font=("Arial", 16, "bold"),
            fg="#ff3366",
            bg="#1a1a2e"
        )
        title_label.pack(pady=10)
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg="#1a1a2e")
        input_frame.pack(pady=10)
        
        tk.Label(
            input_frame,
            text="Ask me anything Brawl Stars related:",
            font=("Arial", 10),
            fg="white",
            bg="#1a1a2e"
        ).pack(side=tk.LEFT, padx=5)
        
        self.user_input = tk.Entry(input_frame, width=40, font=("Arial", 10))
        self.user_input.pack(side=tk.LEFT, padx=5)
        self.user_input.bind("<Return>", lambda event: self._process_input())
        
        submit_btn = tk.Button(
            input_frame,
            text="SEND",
            command=self._process_input,
            bg="#ff3366",
            fg="white",
            font=("Arial", 10, "bold")
        )
        submit_btn.pack(side=tk.LEFT, padx=5)
        
        # Quick Buttons
        quick_btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        quick_btn_frame.pack(pady=5)
        
        tk.Button(
            quick_btn_frame,
            text="Best Knockout Picks",
            command=lambda: self._show_knockout_picks(),
            bg="#4a4a8a",
            fg="white"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            quick_btn_frame,
            text="Brawler Builds",
            command=lambda: self._show_brawler_builds(),
            bg="#4a4a8a",
            fg="white"
        ).pack(side=tk.LEFT, padx=5)
        
        # Output Text Area
        self.output_area = scrolledtext.ScrolledText(
            self.root,
            width=80,
            height=20,
            font=("Arial", 10),
            bg="#2a2a4a",
            fg="white",
            insertbackground="white"
        )
        self.output_area.pack(pady=10)
        self.output_area.insert(tk.END, "👋 OMG hi bestie! Ask me about Brawl Stars meta! 🫡🔥\n")
        
        # Footer
        tk.Label(
            self.root,
            text="2025 TikTok Brainrot Edition | Not affiliated with Supercell",
            font=("Arial", 8),
            fg="gray",
            bg="#1a1a2e"
        ).pack(side=tk.BOTTOM, pady=5)
    
    def _process_input(self):
        """Handle user input and generate response"""
        user_text = self.user_input.get()
        if not user_text:
            return
        
        self.output_area.insert(tk.END, f"\nYou: {user_text}\n")
        self.user_input.delete(0, tk.END)
        
        if "best pick" in user_text.lower() or "knockout" in user_text.lower():
            map_name = user_text.split("for")[-1].strip() if "for" in user_text else user_text.split("pick")[-1].strip()
            response = self.get_knockout_pick(map_name)
        elif "build" in user_text.lower():
            brawler = user_text.split("for")[-1].strip() if "for" in user_text else user_text.split("build")[-1].strip()
            response = self.get_brawler_build(brawler)
        else:
            response = self.generate_response(user_text)
        
        self.output_area.insert(tk.END, f"Bot: {response}\n")
        self.output_area.see(tk.END)
    
    def _show_knockout_picks(self):
        """Show all knockout maps in a popup"""
        popup = tk.Toplevel(self.root)
        popup.title("Knockout Map Picks")
        popup.geometry("400x400")
        popup.configure(bg="#1a1a2e")
        
        tk.Label(
            popup,
            text="2025 KNOCKOUT META PICKS 🔥",
            font=("Arial", 12, "bold"),
            fg="#ff3366",
            bg="#1a1a2e"
        ).pack(pady=10)
        
        canvas = tk.Canvas(popup, bg="#1a1a2e")
        scrollbar = ttk.Scrollbar(popup, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#1a1a2e")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        for map_name, brawlers in self.knockout_maps.items():
            frame = tk.Frame(scrollable_frame, bg="#2a2a4a", padx=10, pady=5)
            frame.pack(fill="x", padx=5, pady=2)
            
            tk.Label(
                frame,
                text=f"🗺️ {map_name.title()}",
                font=("Arial", 10, "bold"),
                fg="#ffcc00",
                bg="#2a2a4a"
            ).pack(anchor="w")
            
            tk.Label(
                frame,
                text=", ".join(brawlers),
                font=("Arial", 9),
                fg="white",
                bg="#2a2a4a"
            ).pack(anchor="w")
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _show_brawler_builds(self):
        """Show all brawler builds in a popup"""
        popup = tk.Toplevel(self.root)
        popup.title("Brawler Builds")
        popup.geometry("500x600")
        popup.configure(bg="#1a1a2e")
        
        tk.Label(
            popup,
            text="2025 BRAWLER META BUILDS 🛠️",
            font=("Arial", 12, "bold"),
            fg="#ff3366",
            bg="#1a1a2e"
        ).pack(pady=10)
        
        search_frame = tk.Frame(popup, bg="#1a1a2e")
        search_frame.pack(pady=5)
        
        tk.Label(
            search_frame,
            text="Search Brawler:",
            font=("Arial", 9),
            fg="white",
            bg="#1a1a2e"
        ).pack(side=tk.LEFT)
        
        search_entry = tk.Entry(search_frame, font=("Arial", 9))
        search_entry.pack(side=tk.LEFT, padx=5)
        search_entry.bind("<KeyRelease>", lambda e: self._filter_brawlers(search_entry.get().upper(), tree))
        
        tree = ttk.Treeview(
            popup,
            columns=("Brawler", "Star Power", "Gadget", "Hypercharge"),
            show="headings",
            height=20
        )
        
        tree.heading("Brawler", text="Brawler")
        tree.heading("Star Power", text="Star Power ⭐")
        tree.heading("Gadget", text="Gadget ⚡")
        tree.heading("Hypercharge", text="Hypercharge 🌀")
        
        tree.column("Brawler", width=100)
        tree.column("Star Power", width=150)
        tree.column("Gadget", width=150)
        tree.column("Hypercharge", width=150)
        
        style = ttk.Style()
        style.configure("Treeview", background="#2a2a4a", fieldbackground="#2a2a4a", foreground="white")
        style.configure("Treeview.Heading", background="#4a4a8a", foreground="white")
        
        for brawler in sorted(self.brawler_builds.keys()):
            star_power, gadget, hypercharge = self.brawler_builds[brawler]
            tree.insert("", tk.END, values=(brawler, star_power, gadget, hypercharge))
        
        tree.pack(fill="both", expand=True)
    
    def _filter_brawlers(self, search_text, tree):
        """Filter brawlers based on search text"""
        tree.delete(*tree.get_children())
        for brawler in sorted(self.brawler_builds.keys()):
            if search_text in brawler:
                star_power, gadget, hypercharge = self.brawler_builds[brawler]
                tree.insert("", tk.END, values=(brawler, star_power, gadget, hypercharge))
    
    def run(self):
        """Run the application"""
        self.root.mainloop()

if __name__ == "__main__":
    bot = BrawlStarsTikTokBot()
    bot.run()
