# 🚀 WhatsApp Message Scheduler

Schedule WhatsApp messages to anyone, at any time — automatically!  
Never forget to send an important message again.

---

## ✨ Features

- **⏰ Schedule Messages:** Set a time and recipient, and your message will be sent automatically.
- **🗣️ Personal Touch:** Send to any WhatsApp contact — choose the message, the timing, and the recipient.
- **🖥️ Easy to Use:** Simple command-line interface, no coding skills needed.
- **🔒 Secure:** Runs locally on your machine, keeping your data private.

---

## 📦 Requirements

- **Python 3.7+**
- **Google Chrome browser** (for WhatsApp Web automation)
- **WhatsApp account**

### 🛠️ Required Python Libraries

| Library      | Purpose                                | Install Command              |
|--------------|----------------------------------------|------------------------------|
| `pywhatkit`  | WhatsApp message scheduling & sending  | `pip install pywhatkit`      |
| `datetime`   | Handling date and time (built-in)      | -                            |
| `time`       | Time-related functions (built-in)      | -                            |

> **Note:** `pywhatkit` will open WhatsApp Web in your default browser. The first time you use it, you may need to scan the QR code.

---

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/whatsapp.git
   cd whatsapp
   ```

2. **Install dependencies:**
   ```bash
   pip install pywhatkit
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```
   *(Replace `main.py` with your actual startup file if different.)*

4. **Follow on-screen prompts:**
   - Enter the recipient’s phone number (with country code, e.g. +919876543210).
   - Type your message.
   - Set the scheduled time (in 24-hour format).

---

## 📝 Example Usage

```python
import pywhatkit

# Send "Hello!" to +919876543210 at 14:30 (2:30 PM)
pywhatkit.sendwhatmsg("+919876543210", "Hello!", 14, 30)
```

---

## 💡 Tips & Notes

- Ensure your computer and browser stay active at the scheduled time.
- Keep your WhatsApp Web logged in.
- You can schedule messages minutes or hours ahead.
- For advanced usage, refer to [pywhatkit documentation](https://github.com/Ankit404butfound/PyWhatKit).

---

## 🧑‍💻 Technologies Used

- **Python**
- **pywhatkit**
- **WhatsApp Web**

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, open an issue first to discuss what you’d like to change.

---

## ⚠️ Disclaimer

This project is for educational purposes only.  
Please use responsibly and comply with [WhatsApp’s Terms of Service](https://www.whatsapp.com/legal/).

---

## 📄 License

[MIT](LICENSE)

---
