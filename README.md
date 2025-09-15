# 🤖 Awesome Telegram Bot

A feature-rich, interactive Telegram bot built with Python that provides entertainment, utilities, and smart responses!

## ✨ Features

- 🎯 **Interactive Commands** - `/start`, `/help`, `/about`, `/joke`, `/fact`, `/time`, `/calc`
- 🎨 **Inline Keyboards** - Beautiful button-based interactions
- 💬 **Smart Echo** - Intelligent message responses and echoing
- 📸 **Photo Analysis** - Handles and analyzes uploaded photos
- 📄 **Document Processing** - File upload handling with details
- 🧮 **Calculator** - Built-in math expression calculator
- 😂 **Entertainment** - Random jokes and interesting facts
- 🕒 **Time Info** - Current date and time display
- 🌤️ **Weather Info** - Weather information (demo implementation)

## 🚀 Quick Start

### 1. Create Your Bot

1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow instructions
3. Copy your bot token (looks like `123456789:ABCdefGhIjKlMnOpQrStUvWxYz`)

### 2. Local Setup

```bash
# Clone the repository
git clone https://github.com/FLASHANISH/telegram-bot.git
cd telegram-bot

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Edit .env and add your bot token
BOT_TOKEN=your_bot_token_here

# Run the bot
python bot.py
```

### 3. Test Your Bot

1. Start a chat with your bot on Telegram
2. Send `/start` to see the welcome message
3. Try various commands and features!

## 🌐 Live Deployment

### Option 1: Railway (Recommended)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/zUcpux?referralCode=alphasec)

1. Click the Railway button above
2. Connect your GitHub account
3. Set environment variable: `BOT_TOKEN=your_token_here`
4. Deploy! ✅

### Option 2: Heroku

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. Click the Heroku button above
2. Set `BOT_TOKEN` environment variable
3. Deploy as a worker dyno

### Option 3: Manual Docker Deployment

```bash
# Build Docker image
docker build -t telegram-bot .

# Run container
docker run -e BOT_TOKEN=your_token_here telegram-bot
```

## 📋 Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Welcome message with interactive buttons | `/start` |
| `/help` | Show all available commands | `/help` |
| `/about` | Information about the bot | `/about` |
| `/joke` | Get a random joke | `/joke` |
| `/fact` | Get an interesting fact | `/fact` |
| `/time` | Show current date and time | `/time` |
| `/calc` | Calculate math expressions | `/calc 2 + 2 * 3` |

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Your Telegram bot token from @BotFather | ✅ Yes |
| `DEBUG` | Enable debug mode (True/False) | ❌ No |
| `LOG_LEVEL` | Logging level (INFO, DEBUG, WARNING, ERROR) | ❌ No |
| `PORT` | Port for deployment platforms | ❌ No |

### File Structure

```
telegram-bot/
├── bot.py              # Main bot application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── Procfile          # Heroku configuration
├── railway.json      # Railway configuration
├── runtime.txt       # Python version specification
├── .env.example      # Environment variables template
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## 🛠️ Development

### Adding New Features

1. **New Commands**: Add handlers in `bot.py`
```python
async def my_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello from new command!")

# Register in setup_handlers()
self.app.add_handler(CommandHandler("mycommand", self.my_command))
```

2. **New Buttons**: Add to inline keyboard in `start_command()`
```python
InlineKeyboardButton("My Button", callback_data='my_action')
```

3. **Handle Button Clicks**: Add to `button_callback()`
```python
elif query.data == 'my_action':
    await self.my_command(update, context)
```

### Local Testing

```bash
# Install development dependencies
pip install -r requirements.txt

# Run with debug logging
export LOG_LEVEL=DEBUG
python bot.py
```

## 📊 Bot Statistics

- **Commands**: 8+ interactive commands
- **Handlers**: Text, Photo, Document, Callback handlers
- **Features**: 10+ unique features
- **Response Time**: < 1 second average
- **Uptime**: 24/7 when deployed

## 🔒 Security Features

- ✅ Environment-based token management
- ✅ Input validation for calculator
- ✅ Safe file handling
- ✅ Non-root Docker user
- ✅ Error handling and logging

## 📱 Mobile Optimization

- ✅ Responsive inline keyboards
- ✅ Emoji-rich interface
- ✅ Quick action buttons
- ✅ Touch-friendly interactions

## 🎯 Use Cases

- **Personal Assistant** - Quick calculations, time, facts
- **Entertainment Bot** - Jokes, facts, interactive features  
- **Learning Project** - Study Telegram bot development
- **Base Template** - Fork and customize for your needs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

- 📧 **Issues**: [GitHub Issues](https://github.com/FLASHANISH/telegram-bot/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/FLASHANISH/telegram-bot/discussions)
- 🐛 **Bug Reports**: Use the issue template

## 🌟 Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Excellent Telegram Bot API wrapper
- [Telegram Bot API](https://core.telegram.org/bots/api) - Official API documentation
- [Railway](https://railway.app) - Free hosting for bot deployment

---

**Made with ❤️ by [FLASHANISH](https://github.com/FLASHANISH)**

⭐ **Star this repository if you find it helpful!**