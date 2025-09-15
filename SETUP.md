# 🚀 Telegram Bot Setup & Deployment Guide

## Step-by-Step Setup

### 1. Get Your Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/start` to begin
3. Send `/newbot` to create a new bot
4. Follow the prompts:
   - Choose a name for your bot (e.g., "My Awesome Bot")
   - Choose a username (must end in 'bot', e.g., "myawesomebot")
5. Copy the token that looks like: `123456789:ABCdefGhIjKlMnOpQrStUvWxYz`

### 2. Local Testing (Optional)

```bash
# Clone or download the project
git clone https://github.com/FLASHANISH/telegram-bot.git
cd telegram-bot

# Install Python dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Edit .env file and add your token:
# BOT_TOKEN=your_token_here

# Run the bot locally
python bot.py
```

### 3. Deploy to Railway (Recommended - Free!)

**Option A: One-Click Deploy**
1. Click here: [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/zUcpux)
2. Connect your GitHub account
3. Set `BOT_TOKEN` environment variable
4. Click Deploy!

**Option B: Manual Deploy**
1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select this repository
5. Add environment variable: `BOT_TOKEN` = your token
6. Deploy!

### 4. Deploy to Heroku (Alternative)

1. Create a [Heroku account](https://heroku.com)
2. Click: [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
3. Set `BOT_TOKEN` environment variable
4. Choose "worker" dyno type (not web)
5. Deploy!

### 5. Deploy to Render (Alternative)

1. Go to [Render.com](https://render.com)
2. Connect your GitHub account
3. Create new "Web Service"
4. Connect this repository
5. Set environment: `BOT_TOKEN` = your token
6. Set start command: `python bot.py`
7. Deploy!

## 🔧 Configuration

### Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `BOT_TOKEN` | Your bot token from @BotFather | `123456789:ABC...` |

### Optional Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DEBUG` | `False` | Enable debug logging |
| `LOG_LEVEL` | `INFO` | Logging level (DEBUG/INFO/WARNING/ERROR) |
| `PORT` | `8080` | Port for deployment platforms |

## ✅ Verification Steps

After deployment:

1. **Check Deployment Status**
   - Railway: Check deployment logs in dashboard
   - Heroku: Check app logs with `heroku logs --tail`
   - Render: Check build and deploy logs

2. **Test Your Bot**
   - Open Telegram
   - Search for your bot username
   - Send `/start` to test
   - Try other commands like `/help`, `/joke`

3. **Monitor Performance**
   - Check platform dashboard for resource usage
   - Monitor bot response times in Telegram

## 🐛 Troubleshooting

### Common Issues

**Bot doesn't respond:**
- ✅ Check if `BOT_TOKEN` is set correctly
- ✅ Verify deployment is running (not sleeping)
- ✅ Check application logs for errors

**Deployment fails:**
- ✅ Ensure all files are committed to GitHub
- ✅ Check `requirements.txt` syntax
- ✅ Verify Dockerfile syntax if using Docker

**Bot stops working after some time:**
- ✅ Check if free tier limits are reached
- ✅ Verify deployment hasn't crashed
- ✅ Check logs for error messages

### Getting Help

1. **Check Logs First**
   - Railway: Dashboard → Deployments → Logs
   - Heroku: `heroku logs --tail --app your-app-name`
   - Render: Dashboard → Logs tab

2. **Common Solutions**
   - Restart the deployment
   - Check environment variables
   - Verify bot token is correct
   - Ensure sufficient resources

3. **Get Support**
   - Create GitHub Issue with logs
   - Check platform documentation
   - Join community forums

## 💡 Tips for Success

1. **Keep It Simple**
   - Start with basic deployment
   - Add features gradually
   - Test each change

2. **Monitor Usage**
   - Check platform resource limits
   - Monitor bot usage patterns
   - Plan for scaling if needed

3. **Backup & Version Control**
   - Keep code in GitHub
   - Use environment variables for secrets
   - Document changes in commits

4. **Security Best Practices**
   - Never commit bot tokens to code
   - Use environment variables
   - Regularly rotate tokens if needed

## 🎉 Next Steps

Once your bot is live:

1. **Customize Features**
   - Add new commands
   - Modify responses
   - Add database integration

2. **Share Your Bot**
   - Share with friends
   - Add to group chats
   - Promote on social media

3. **Scale & Improve**
   - Monitor performance
   - Add analytics
   - Upgrade hosting if needed

---

**Need help? Create an issue on GitHub!** 🚀