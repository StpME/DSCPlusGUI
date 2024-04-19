import tkinter as tk
class Setup:
    def setup_gui(self, gui_name):
        # GUI main headers
        self.label = tk.Label(self.root, text=("Select " + gui_name + " theme CSS file"), font=("Arial", 12))
        self.label.pack()
        self.sub_label = tk.Label(self.root, text="Default Location: C:\\Users\\"+str(self.username)+"\\AppData\\Roaming\\Vencord\\themes", 
                            font=("Arial", 10))
        self.sub_label.pack()

        # Text shown for main window
        self.text = tk.Text(self.root, wrap="word")
        self.text.pack(expand=True, fill="both")
        
        # Dropdown menu
        self.backdrop_options = tk.StringVar(value="Select Backdrop")
        self.backdrop_menu = tk.OptionMenu(self.root, 
                                                self.backdrop_options,
                                                "Select Below"
                                            )
        self.backdrop_menu.pack(side=tk.LEFT,
                                    padx=5,
                                    pady=2,
                                    )

        self.backdrop_menu_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.backdrop_menu_label.pack(side=tk.LEFT)

        self.backdrop_entry = tk.Entry(self.root, width=50)
        self.backdrop_entry.pack(side=tk.RIGHT, padx=5, pady=5)

        # Add backdrop button
        self.add_backdrop_btn = tk.Button(self.root, text="Add Backdrop", 
                                        command=self.add_backdrop_to_css,
                                        bd=3 # Border width
                                    )
        self.add_backdrop_btn.pack(side=tk.RIGHT,
                                padx=5,
                                pady=5,
                            )