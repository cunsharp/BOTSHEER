# 🚀 Railway Deployment Guide

## ✅ Your Configuration is Ready!

Your `.env` file has been created with your credentials:
- ✅ Bot Token: `8451354612:AAH...Pf70`
- ✅ Admin User ID: `844983156`
- ✅ MySQL Database: Connected to Railway

---

## 📋 Next Steps to Deploy

### Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. Repository name: `tgbot-verify`
3. Keep it **Private** (to protect your bot)
4. **Don't** initialize with README
5. Click **"Create repository"**

### Step 2: Push Code to GitHub

Copy and run these commands in VS Code Terminal (one at a time):

```bash
# Set branch to main
git branch -M main

# Add your GitHub repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/tgbot-verify.git

# Push code to GitHub
git push -u origin main
```

**Note**: Replace `YOUR_USERNAME` with your actual GitHub username!

If you don't have Git configured, run these first:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

### Step 3: Deploy on Railway

1. **Go to**: https://railway.app/dashboard

2. **Click**: "New Project" → "Deploy from GitHub repo"

3. **Select**: Your `tgbot-verify` repository

4. **Click**: "Deploy Now"

5. **Wait** for initial deployment (will fail - that's OK!)

---

### Step 4: Add Environment Variables

1. In Railway, click on your **bot service**

2. Click **"Variables"** tab

3. Click **"RAW Editor"** button

4. **Copy and paste** this EXACTLY:

```env
BOT_TOKEN=8451354612:AAHzSwtgw7Qn5Hspr94_ejIi8ofgLLDPf70
ADMIN_USER_ID=844983156
CHANNEL_USERNAME=pk_oa
CHANNEL_URL=https://t.me/pk_oa
MYSQL_HOST=${{MYSQLHOST}}
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=jojDoCDHRtStMgwzazaTSNuAlMhonHJZ
MYSQL_DATABASE=railway
```

5. Press **Ctrl+S** or click **"Update Variables"**

---

### Step 5: Configure Build Settings

Railway needs to install Playwright browser:

1. Click on your bot service
2. Go to **"Settings"** tab
3. Find **"Build Command"** section
4. Click **"Configure"**
5. Enter:
```bash
pip install -r requirements.txt && playwright install chromium && playwright install-deps chromium
```
6. Save

---

### Step 6: Verify Deployment

1. **Check Logs**:
   - Click **"View Logs"** in Railway
   - Look for these success messages:
     ```
     机器人启动中...
     数据库连接成功
     机器人已启动！
     ```

2. **If you see errors**, common fixes:
   
   **Error: "MySQL Connection Failed"**
   - Update `MYSQL_HOST` to use: `${{RAILWAY_PRIVATE_DOMAIN}}`
   - Or manually copy the value from MySQL service → Variables → `RAILWAY_PRIVATE_DOMAIN`

   **Error: "Playwright not found"**
   - Make sure build command includes `playwright install chromium`

---

### Step 7: Test Your Bot! 🎉

1. Open Telegram
2. Search for your bot: Search by the username you gave it
3. Send `/start`
4. You should see welcome message!

---

## 🎮 Using Your Bot

### Give Yourself Points (Admin Command)

```
/addbalance 844983156 100
```

This gives you 100 points to test verifications.

### Available Commands

**Admin Commands** (only you can use):
```
/addbalance <user_id> <amount>  - Add points to user
/genkey <amount>                - Generate redemption key
/listkeys                       - List all keys
/broadcast <message>            - Send message to all users
/block <user_id>                - Block a user
/white <user_id>                - Whitelist a user
/blacklist                      - View blocked users
```

**User Commands**:
```
/start      - Register and start
/help       - Show help menu
/about      - About the bot
/balance    - Check points balance
/checkin    - Daily check-in (get 1 point)
/invite     - Get invite link (refer friends for 2 points)
/use <code> - Redeem key code

/verify <link>   - Gemini One Pro (Teacher)
/verify2 <link>  - ChatGPT K12 (Teacher)
/verify3 <link>  - Spotify (Student)
/verify4 <link>  - Bolt.new (Teacher)
/verify5 <link>  - YouTube Premium (Student)
```

---

## 🔧 Troubleshooting

### Bot deployed but not responding?

**Check 1**: Verify bot token is correct
```
Go to @BotFather → /mybots → select your bot → API Token
```

**Check 2**: Check Railway logs
```
Railway Dashboard → Your Service → View Logs
Look for errors in red
```

**Check 3**: Verify MySQL connection
```
In Railway Variables, make sure:
MYSQL_HOST=${{MYSQLHOST}}
```

### MySQL connection issues?

**Option 1**: Use internal Railway domain
```
MYSQL_HOST=${{RAILWAY_PRIVATE_DOMAIN}}
```

**Option 2**: Get exact value
```
Railway → MySQL service → Variables → Copy RAILWAY_PRIVATE_DOMAIN
Then use that value in bot's MYSQL_HOST
```

---

## 📊 Free Tier Limits

Railway Free Tier:
- ✅ $5 credit/month (usually enough for 24/7)
- ✅ Unlimited builds
- ✅ 1GB RAM per service
- ⏰ ~500 hours of runtime

**Tip**: Monitor usage at: Railway Dashboard → Usage

---

## 🎉 Success Checklist

- [ ] Created GitHub repository
- [ ] Pushed code to GitHub
- [ ] Deployed on Railway
- [ ] Added environment variables
- [ ] Configured build command
- [ ] Verified logs show "机器人已启动"
- [ ] Tested `/start` command in Telegram
- [ ] Gave yourself points with `/addbalance`

---

## 🆘 Need Help?

**Your Bot Details:**
- Bot Token: `8451...Pf70` (keep secret!)
- Your Telegram ID: `844983156`
- MySQL Password: `jojD...nHJZ` (keep secret!)

**Telegram Support:**
- Channel: https://t.me/pk_oa
- Original Author: [@auto_sheerid_bot](https://t.me/auto_sheerid_bot)

**GitHub Issues:**
- https://github.com/PastKing/tgbot-verify/issues

---

🚀 **Happy Verifying!**
