# ⚡ Quick Start Guide - GOD v1.0.0

Get up and running in **5 minutes**!

---

## 🎯 Choose Your Setup

### Option 1: GitHub Pages (Recommended - No Install!)

**Time:** 2 minutes  
**Best for:** Easy deployment, sharing with others

```
1. Fork this repository on GitHub
2. Go to Settings → Pages
3. Source: main branch
4. Done! Visit: https://YOUR-USERNAME.github.io/GOD-v1.0.0/
```

---

### Option 2: Run Locally

**Time:** 3 minutes  
**Best for:** Development, testing, offline use

**Windows:**
```
Double-click: start.bat
```

**Mac/Linux:**
```bash
chmod +x start.sh
./start.sh
```

**Any OS:**
```bash
python server.py
# Then visit: http://localhost:8000
```

---

## 🔧 First Time Configuration

### For Cloud Mode (Anthropic Claude):

1. Get API key from [console.anthropic.com](https://console.anthropic.com/)
2. Open GOD v1.0.0
3. Click Settings ⚙️
4. Select "Cloud (Anthropic Claude)"
5. Paste your API key
6. Click "Save Settings"
7. Start chatting! 🎉

### For Local Mode (Ollama):

**Step 1: Install Ollama**
```bash
# On Mac/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# On Windows
# Download from: https://ollama.ai/download
```

**Step 2: Start Ollama**
```bash
ollama serve
# Keep this running!
```

**Step 3: Pull a Model**
```bash
# Open new terminal
ollama pull llama3.2
# or
ollama pull llama3.2:1b  # Smaller, faster
```

**Step 4: Configure GOD**
1. Open GOD v1.0.0
2. Click Settings ⚙️
3. Select "Local (Ollama)"
4. Ollama URL: `http://localhost:11434`
5. Model: `llama3.2`
6. Click "Save Settings"
7. Start chatting! 🎉

---

## ✅ Quick Test

Try these prompts to test your setup:

```
1. "Hello! Can you hear me?"
2. "Explain AI in one sentence"
3. "Write a haiku about technology"
```

If you get responses, **you're all set!** ✨

---

## 🎤 Enable Voice Features

1. Click Settings ⚙️
2. Scroll to "Voice" section
3. ✅ Enable voice features
4. Set voice speed (1.0x recommended)
5. Click "Save Settings"

**Test Voice:**
- Click microphone icon (🎤) in input area
- Speak: "Hello GOD"
- Should convert to text!

---

## 📱 Install as App (PWA)

### On Desktop:
1. Look for install icon in browser address bar
2. Click "Install"
3. App opens in own window!

### On Mobile:
1. Open in Chrome (Android) or Safari (iOS)
2. Menu → "Install app" or "Add to Home Screen"
3. App appears on your home screen!

---

## 🚨 Troubleshooting

### "Cannot connect to API"
```
✅ Check API key is correct
✅ Verify internet connection
✅ Check Anthropic console for credits
```

### "Cannot connect to Ollama"
```
✅ Make sure `ollama serve` is running
✅ Check URL: http://localhost:11434
✅ Test: curl http://localhost:11434/api/tags
✅ Verify model downloaded: ollama list
```

### "Voice not working"
```
✅ Use Chrome or Edge browser
✅ Grant microphone permissions
✅ Check mic is working in other apps
```

---

## 🎓 Next Steps

### Explore Features:
- [ ] Try different AI modes
- [ ] Test voice input/output
- [ ] Customize theme (dark/light)
- [ ] Save and resume chats
- [ ] Export important conversations

### Learn More:
- Read full [README.md](README.md)
- Check [Documentation](#) (coming soon)
- Join [Discussions](https://github.com/yourusername/GOD-v1.0.0/discussions)

---

## 💡 Pro Tips

1. **Keyboard Shortcuts:**
   - `Enter` = Send message
   - `Shift + Enter` = New line

2. **Better Responses:**
   - Be specific in your questions
   - Provide context when needed
   - Ask follow-up questions

3. **Voice Mode:**
   - Click 🎤 in top nav (turns blue)
   - Perfect for hands-free use
   - Adjustable speed in settings

4. **Save Important Chats:**
   - Auto-saves by default
   - Find in sidebar by date
   - Click to resume anytime

---

## 📞 Need Help?

- 🐛 [Report Issues](https://github.com/yourusername/GOD-v1.0.0/issues)
- 💬 [Ask Questions](https://github.com/yourusername/GOD-v1.0.0/discussions)
- 📖 [Full Documentation](README.md)

---

## 🎉 You're Ready!

**Your GOD v1.0.0 is now running!**

Start with: *"Hello! What can you help me with?"*

---

<div align="center">

**Enjoy using GOD v1.0.0!** ✨

Made with ❤️ for the AI community

</div>
