import re
from collections import Counter
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

def analyze_log(file_path, output_widget):
    log_levels = Counter()
    ip_addresses = set()

    log_level_pattern = re.compile(r'\b(INFO|WARNING|ERROR|DEBUG|CRITICAL)\b')
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = log_level_pattern.search(line)
                if match:
                    log_levels[match.group()] += 1

                ip_match = ip_pattern.findall(line)
                ip_addresses.update(ip_match)

        # Display results in the text box
        output_widget.delete('1.0', tk.END)
        output_widget.insert(tk.END, "=== Log Level Summary ===\n")
        for level, count in log_levels.items():
            output_widget.insert(tk.END, f"{level}: {count}\n")

        output_widget.insert(tk.END, "\n=== Unique IP Addresses ===\n")
        for ip in sorted(ip_addresses):
            output_widget.insert(tk.END, f"{ip}\n")

    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{file_path}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_file(output_widget):
    file_path = filedialog.askopenfilename(title="Select Log File", filetypes=[("Log files", "*.log *.txt"), ("All files", "*.*")])
    if file_path:
        analyze_log(file_path, output_widget)

def create_gui():
    window = tk.Tk()
    window.title("Log Analyzer")
    window.geometry("600x500")

    label = tk.Label(window, text="Log File Analyzer", font=("Arial", 16))
    label.pack(pady=10)

    browse_button = tk.Button(window, text="Browse Log File", command=lambda: browse_file(output_box))
    browse_button.pack(pady=5)

    output_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=25)
    output_box.pack(padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
