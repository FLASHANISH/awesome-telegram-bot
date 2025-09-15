# Telegram Bot Live Deployment Helper
Write-Host "🤖 Telegram Bot Deployment Helper" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Green
Write-Host ""

Write-Host "📋 Pre-deployment Checklist:" -ForegroundColor Yellow
Write-Host "1. ✅ Bot created with @BotFather on Telegram"
Write-Host "2. ✅ Bot token copied"
Write-Host "3. ✅ Code uploaded to GitHub"
Write-Host "4. 🔄 Now ready to deploy to live platform"
Write-Host ""

Write-Host "🌐 Choose your deployment platform:" -ForegroundColor Cyan
Write-Host "1. Railway (Recommended - Free and Easy)" -ForegroundColor Green
Write-Host "2. Heroku (Popular - Free tier available)" -ForegroundColor Blue  
Write-Host "3. Render (Alternative - Free tier)" -ForegroundColor Magenta
Write-Host ""

$choice = Read-Host "Enter your choice (1, 2, or 3)"

if ($choice -eq "1") {
    Write-Host "🚄 Railway Deployment Instructions:" -ForegroundColor Green
    Write-Host ""
    Write-Host "📝 Steps:"
    Write-Host "1. Go to: https://railway.app"
    Write-Host "2. Sign up with GitHub"
    Write-Host "3. Click New Project -> Deploy from GitHub repo"
    Write-Host "4. Select: FLASHANISH/awesome-telegram-bot"
    Write-Host "5. Add environment variable:"
    Write-Host "   Name: BOT_TOKEN"
    Write-Host "   Value: [Your bot token from @BotFather]"
    Write-Host "6. Click Deploy!"
    Write-Host ""
    Write-Host "🔗 GitHub Repository: https://github.com/FLASHANISH/awesome-telegram-bot" -ForegroundColor Yellow
}
elseif ($choice -eq "2") {
    Write-Host "🟣 Heroku Deployment Instructions:" -ForegroundColor Blue
    Write-Host ""
    Write-Host "📝 Steps:"
    Write-Host "1. Go to: https://heroku.com"
    Write-Host "2. Sign up for account"
    Write-Host "3. Use the deploy button in the README"
    Write-Host "4. Set BOT_TOKEN environment variable"
    Write-Host "5. Choose worker dyno type (not web)"
    Write-Host "6. Deploy!"
    Write-Host ""
    Write-Host "⚠️ Important: Use worker process type, not web" -ForegroundColor Yellow
}
elseif ($choice -eq "3") {
    Write-Host "🎨 Render Deployment Instructions:" -ForegroundColor Magenta
    Write-Host ""
    Write-Host "📝 Steps:"
    Write-Host "1. Go to: https://render.com"
    Write-Host "2. Sign up with GitHub"
    Write-Host "3. Create new Web Service"
    Write-Host "4. Connect repository: FLASHANISH/awesome-telegram-bot"
    Write-Host "5. Set start command: python bot.py"
    Write-Host "6. Add environment variable: BOT_TOKEN"
    Write-Host "7. Deploy!"
}
else {
    Write-Host "❌ Invalid choice. Please run the script again." -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "🔧 Important Notes:" -ForegroundColor Yellow
Write-Host "• Keep your bot token secret and secure"
Write-Host "• Your bot will be live 24/7 once deployed"
Write-Host "• Test the bot after deployment"
Write-Host "• Monitor logs for any issues"
Write-Host ""

Write-Host "✅ Repository: https://github.com/FLASHANISH/awesome-telegram-bot" -ForegroundColor Green
Write-Host "🎉 Once deployed, your bot will be live!" -ForegroundColor Green
Write-Host ""

$openRepo = Read-Host "Open GitHub repository in browser? (y/n)"
if ($openRepo -eq "y" -or $openRepo -eq "Y") {
    Start-Process "https://github.com/FLASHANISH/awesome-telegram-bot"
}