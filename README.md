# 📝 Log Analyzer GUI Tool

A simple Python GUI application for analyzing log files. This tool helps you extract log level statistics (INFO, ERROR, WARNING, etc.) and unique IP addresses from server or application logs, all through an easy-to-use interface built with **Tkinter**.

---

## 📸 Screenshots

![Tool](https://github.com/user-attachments/assets/5d9e5335-1ddd-4177-b98d-43475f3aa4b5)

---

## 🚀 Features

* ✅ Browse and select `.log` or `.txt` files
* ✅ Counts occurrences of log levels (INFO, ERROR, WARNING, etc.)
* ✅ Extracts and displays unique IP addresses
* ✅ Scrollable text box for viewing results
* ✅ Simple and beginner-friendly GUI using Tkinter

---

## 📦 Requirements

* Python 3.x

No external libraries are required — only built-in Python modules:

```bash
tkinter
re
collections
```

---

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/log-analyzer-gui.git
   cd log-analyzer-gui
   ```

2. **Run the tool**

   ```bash
   python log_analysis_gui.py
   ```

---

## 📂 Example Log Format

This tool works well with log files like:

```
127.0.0.1 - - [10/May/2025:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326 INFO
192.168.1.10 - - [10/May/2025:14:02:20 +0000] "POST /login HTTP/1.1" 401 564 WARNING
10.0.0.5 - - [10/May/2025:14:05:55 +0000] "GET /dashboard HTTP/1.1" 500 1024 ERROR
```

---

## 🛠️ Future Improvements

* Filter logs by date/time
* Export results to CSV or JSON
* Support for compressed `.log.gz` files
* Dark mode for the GUI
