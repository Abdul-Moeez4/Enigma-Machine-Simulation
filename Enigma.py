import tkinter as tk
from tkinter import messagebox, ttk
import string

# --- Enigma Logic ---

ROTORS = {
    "I":     "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "II":    "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "III":   "BDFHJLCPRTXVZNYEIWGAKMUSQO",
}

REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

ROTOR_NOTCHES = {
    "I": 'Q',
    "II": 'E',
    "III": 'V',
}

def char_to_index(c):
    return ord(c) - ord('A')

def index_to_char(i):
    return chr((i % 26) + ord('A'))

def rotate_forward(c, rotor, offset):
    idx = (char_to_index(c) + offset) % 26
    return index_to_char((char_to_index(rotor[idx]) - offset) % 26)

def rotate_backward(c, rotor, offset):
    idx = (char_to_index(c) + offset) % 26
    return index_to_char((rotor.index(index_to_char(idx)) - offset) % 26)

def plug_swap(c, plugboard):
    return plugboard.get(c, c)

class Enigma:
    def __init__(self, rotor_order, rotor_positions, plugboard_pairs):
        self.rotors = [ROTORS[r] for r in rotor_order]
        self.positions = [char_to_index(p) for p in rotor_positions]
        self.notches = [ROTOR_NOTCHES[r] for r in rotor_order]
        self.plugboard = self.create_plugboard(plugboard_pairs)
        self.initial_positions = self.positions.copy()

    def create_plugboard(self, pairs):
        plugboard = {}
        for pair in pairs:
            if len(pair) == 2:
                a, b = pair[0], pair[1]
                plugboard[a] = b
                plugboard[b] = a
        return plugboard

    def step_rotors(self):
        self.positions[2] = (self.positions[2] + 1) % 26
        if index_to_char(self.positions[2]) == self.notches[2]:
            self.positions[1] = (self.positions[1] + 1) % 26
        if index_to_char(self.positions[1]) == self.notches[1]:
            self.positions[0] = (self.positions[0] + 1) % 26

    def encrypt_char(self, c):
        if c not in string.ascii_uppercase:
            return c
        self.step_rotors()
        c = plug_swap(c, self.plugboard)
        for i in reversed(range(3)):
            c = rotate_forward(c, self.rotors[i], self.positions[i])
        c = REFLECTOR_B[char_to_index(c)]
        for i in range(3):
            c = rotate_backward(c, self.rotors[i], self.positions[i])
        c = plug_swap(c, self.plugboard)
        return c

    def encrypt(self, message):
        result = ''
        for c in message:
            if c in string.ascii_uppercase:
                result += self.encrypt_char(c)
        return result

    def reset(self):
        self.positions = self.initial_positions.copy()

# --- GUI Code ---

def run_enigma():
    rotor_order = [rotor1_var.get(), rotor2_var.get(), rotor3_var.get()]
    rotor_pos = [pos1_var.get(), pos2_var.get(), pos3_var.get()]
    plugboard_input = plugboard_var.get().upper().split()
    message = msg_var.get().upper()

    if not all(r in ROTORS for r in rotor_order) or not all(p in string.ascii_uppercase for p in rotor_pos):
        messagebox.showerror("Invalid Input", "Please check rotor order and positions.")
        return

    enigma = Enigma(rotor_order, rotor_pos, plugboard_input)
    enigma.reset()
    result = enigma.encrypt(''.join(c for c in message if c in string.ascii_uppercase))
    result_var.set(result)

def show_help():
    help_text = (
        "How to use the Enigma Simulator:\n\n"
        "1. Select rotor order (I, II, III).\n"
        "2. Set starting positions (A-Z).\n"
        "3. Define plugboard swaps like 'AB CD EF'.\n"
        "4. Enter a message using A-Z only.\n"
        "5. Click 'Encrypt / Decrypt' to get the result.\n\n"
        "Note: The same setup is required to decrypt the message."
    )
    messagebox.showinfo("Help - Enigma Simulator", help_text)

root = tk.Tk()
root.title("Enigma Machine Simulator")
root.geometry("550x500")
root.configure(bg="#f0f4f7")

# Menu Bar
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="How to Use", command=show_help)
menubar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menubar)

# Title
tk.Label(root, text="Enigma Simulator", font=("Helvetica", 22, "bold"), bg="#f0f4f7").pack(pady=15)

frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

# Rotor Order
tk.Label(frame, text="Rotor Order:", bg="#f0f4f7").grid(row=0, column=0, padx=5, sticky="e")
rotor1_var = tk.StringVar(value="I")
rotor2_var = tk.StringVar(value="II")
rotor3_var = tk.StringVar(value="III")
tk.Entry(frame, textvariable=rotor1_var, width=5).grid(row=0, column=1)
tk.Entry(frame, textvariable=rotor2_var, width=5).grid(row=0, column=2)
tk.Entry(frame, textvariable=rotor3_var, width=5).grid(row=0, column=3)

# Start Positions
tk.Label(frame, text="Start Positions:", bg="#f0f4f7").grid(row=1, column=0, padx=5, pady=5, sticky="e")
pos1_var = tk.StringVar(value="A")
pos2_var = tk.StringVar(value="A")
pos3_var = tk.StringVar(value="A")
tk.Entry(frame, textvariable=pos1_var, width=5).grid(row=1, column=1)
tk.Entry(frame, textvariable=pos2_var, width=5).grid(row=1, column=2)
tk.Entry(frame, textvariable=pos3_var, width=5).grid(row=1, column=3)

# Plugboard
tk.Label(root, text="Plugboard Pairs (e.g., AB CD):", bg="#f0f4f7").pack()
plugboard_var = tk.StringVar()
tk.Entry(root, textvariable=plugboard_var, width=30).pack(pady=5)

# Message
tk.Label(root, text="Message:", bg="#f0f4f7").pack()
msg_var = tk.StringVar()
tk.Entry(root, textvariable=msg_var, width=40).pack(pady=5)

# Encrypt / Decrypt Button
style = ttk.Style()
style.configure("Green.TButton",
                font=("Helvetica", 12),
                padding=6,
                foreground="green",
                background="#27ae60")  # Green color

style.map("Green.TButton",
          background=[("active", "#219150")])  # Darker green on hover

ttbutton = ttk.Button(root, text="Encrypt / Decrypt", style="Green.TButton", command=run_enigma)
ttbutton.pack(pady=15)


# Result
result_var = tk.StringVar()
tk.Label(root, text="Result:", bg="#f0f4f7").pack()
tk.Entry(root, textvariable=result_var, width=40, state="readonly").pack(pady=5)

root.mainloop()
