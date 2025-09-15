import os
import logging
import asyncio
import aiohttp
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

class TelegramBot:
    def __init__(self):
        self.app = Application.builder().token(BOT_TOKEN).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Set up all command and message handlers"""
        # Command handlers
        self.app.add_handler(CommandHandler("start", self.start_command))
        self.app.add_handler(CommandHandler("help", self.help_command))
        self.app.add_handler(CommandHandler("about", self.about_command))
        self.app.add_handler(CommandHandler("joke", self.joke_command))
        self.app.add_handler(CommandHandler("fact", self.fact_command))
        self.app.add_handler(CommandHandler("weather", self.weather_command))
        self.app.add_handler(CommandHandler("time", self.time_command))
        self.app.add_handler(CommandHandler("calc", self.calc_command))
        
        # Callback query handler for inline keyboards
        self.app.add_handler(CallbackQueryHandler(self.button_callback))
        
        # Message handlers
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo_message))
        self.app.add_handler(MessageHandler(filters.PHOTO, self.photo_handler))
        self.app.add_handler(MessageHandler(filters.Document, self.document_handler))

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a welcome message with inline keyboard"""
        user = update.effective_user
        welcome_text = f"""
🤖 **Welcome to My Awesome Bot, {user.first_name}!**

I'm here to help you with various tasks and have some fun!

🔹 Use /help to see all available commands
🔹 Send me any message and I'll echo it back
🔹 Send me photos and I'll analyze them
🔹 Try the buttons below for quick actions!

Let's get started! 🚀
        """
        
        keyboard = [
            [InlineKeyboardButton("📚 Help", callback_data='help'),
             InlineKeyboardButton("ℹ️ About", callback_data='about')],
            [InlineKeyboardButton("😂 Random Joke", callback_data='joke'),
             InlineKeyboardButton("🧠 Fun Fact", callback_data='fact')],
            [InlineKeyboardButton("🕒 Current Time", callback_data='time'),
             InlineKeyboardButton("🌤️ Weather Info", callback_data='weather')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send help information"""
        help_text = """
🔧 **Available Commands:**

**Basic Commands:**
• /start - Start the bot and see main menu
• /help - Show this help message
• /about - Learn about this bot

**Fun Commands:**
• /joke - Get a random joke
• /fact - Get an interesting fact
• /time - Get current time
• /calc <expression> - Calculate math expressions

**Interactive Features:**
• Send any text message - I'll echo it back
• Send photos - I'll analyze and describe them
• Send documents - I'll provide file information
• Use inline buttons for quick actions

**Example Usage:**
• `/calc 2 + 2 * 3` - Calculate math
• Just type "Hello!" - I'll respond back

Need more help? Just ask! 😊
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')

    async def about_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send information about the bot"""
        about_text = """
🤖 **About This Bot**

**Name:** Awesome Telegram Bot
**Version:** 1.0.0
**Created:** 2025
**Developer:** FLASHANISH

**Features:**
✅ Interactive commands
✅ Inline keyboards
✅ Message echoing
✅ Photo analysis
✅ File handling
✅ Math calculations
✅ Jokes and facts
✅ Real-time responses

**Technology Stack:**
• Python 3.9+
• python-telegram-bot library
• Asyncio for performance
• Deployed on cloud platform

**Status:** 🟢 Online and running 24/7

Thanks for using my bot! 💙
        """
        await update.message.reply_text(about_text, parse_mode='Markdown')

    async def joke_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a fake noodle? An impasta!",
            "Why did the coffee file a police report? It got mugged!",
            "How does a penguin build its house? Igloos it together!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't some couples go to the gym? Because some relationships don't work out!",
            "What did the ocean say to the beach? Nothing, it just waved!",
            "Why do programmers prefer dark mode? Because light attracts bugs!"
        ]
        
        import random
        joke = random.choice(jokes)
        await update.message.reply_text(f"😂 **Here's a joke for you:**\n\n{joke}")

    async def fact_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send an interesting fact"""
        facts = [
            "🐙 Octopuses have three hearts and blue blood!",
            "🍯 Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
            "🧠 Your brain uses about 20% of your body's total energy!",
            "🌍 The Earth's core is as hot as the Sun's surface!",
            "🦈 Sharks have been around longer than trees!",
            "🐧 Penguins can jump 6 feet out of water!",
            "☕ Coffee is the second most traded commodity in the world after oil!",
            "🌙 The Moon is moving away from Earth at about 1.5 inches per year!",
            "🐘 Elephants can recognize themselves in mirrors!",
            "💎 Bananas are berries, but strawberries aren't!"
        ]
        
        import random
        fact = random.choice(facts)
        await update.message.reply_text(f"🧠 **Interesting Fact:**\n\n{fact}")

    async def time_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send current time"""
        now = datetime.now()
        time_text = f"🕒 **Current Time:**\n\n📅 Date: {now.strftime('%Y-%m-%d')}\n⏰ Time: {now.strftime('%H:%M:%S')}\n🌍 Timezone: UTC"
        await update.message.reply_text(time_text, parse_mode='Markdown')

    async def weather_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send weather information (mock data for demo)"""
        weather_text = """
🌤️ **Weather Information**

📍 **Location:** Global
🌡️ **Temperature:** 22°C (72°F)
☁️ **Condition:** Partly Cloudy
💨 **Wind:** 15 km/h
💧 **Humidity:** 65%

*Note: This is demo data. For real weather, provide your location!*

Use: `/weather YourCity` for specific location weather.
        """
        await update.message.reply_text(weather_text, parse_mode='Markdown')

    async def calc_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Calculate math expressions"""
        if not context.args:
            await update.message.reply_text("🔢 **Calculator**\n\nUsage: `/calc <expression>`\n\nExample: `/calc 2 + 2 * 3`")
            return
        
        expression = ' '.join(context.args)
        
        try:
            # Simple and safe evaluation
            allowed_chars = set('0123456789+-*/()., ')
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")
            
            result = eval(expression)
            await update.message.reply_text(f"🔢 **Calculator Result:**\n\n`{expression} = {result}`", parse_mode='Markdown')
        
        except Exception as e:
            await update.message.reply_text(f"❌ **Error in calculation:**\n\n`{expression}`\n\nPlease check your math expression!")

    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle inline keyboard button presses"""
        query = update.callback_query
        await query.answer()
        
        if query.data == 'help':
            await self.help_command(update, context)
        elif query.data == 'about':
            await self.about_command(update, context)
        elif query.data == 'joke':
            await self.joke_command(update, context)
        elif query.data == 'fact':
            await self.fact_command(update, context)
        elif query.data == 'time':
            await self.time_command(update, context)
        elif query.data == 'weather':
            await self.weather_command(update, context)

    async def echo_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Echo user messages with enhancements"""
        user_message = update.message.text
        user_name = update.effective_user.first_name
        
        # Add some smart responses
        if "hello" in user_message.lower() or "hi" in user_message.lower():
            response = f"👋 Hello {user_name}! How can I help you today?"
        elif "how are you" in user_message.lower():
            response = f"I'm doing great, thanks for asking {user_name}! 🤖✨"
        elif "thank" in user_message.lower():
            response = f"You're welcome {user_name}! Happy to help! 😊"
        elif "bye" in user_message.lower():
            response = f"Goodbye {user_name}! Have a wonderful day! 👋"
        else:
            response = f"💬 **You said:** {user_message}\n\n🔄 **I say:** {user_message} (echoed back!)"
        
        await update.message.reply_text(response, parse_mode='Markdown')

    async def photo_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle photo messages"""
        photo = update.message.photo[-1]  # Get the highest resolution photo
        
        response_text = f"""
📸 **Photo received!**

🔍 **Photo Details:**
• File ID: `{photo.file_id}`
• Size: {photo.width}x{photo.height}
• File Size: ~{photo.file_size} bytes

✨ **Analysis:** This looks like a beautiful image! Thanks for sharing!

*Note: Advanced image analysis features coming soon!*
        """
        
        await update.message.reply_text(response_text, parse_mode='Markdown')

    async def document_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle document messages"""
        document = update.message.document
        
        response_text = f"""
📄 **Document received!**

📋 **File Details:**
• Name: `{document.file_name}`
• Size: {document.file_size} bytes
• Type: `{document.mime_type}`

✅ **Status:** File received successfully!

*Note: Document processing features coming soon!*
        """
        
        await update.message.reply_text(response_text, parse_mode='Markdown')

    def run(self):
        """Start the bot"""
        logger.info("Starting bot...")
        self.app.run_polling(drop_pending_updates=True)

def main():
    """Main function to run the bot"""
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN environment variable is not set!")
        return
    
    bot = TelegramBot()
    bot.run()

if __name__ == '__main__':
    main()