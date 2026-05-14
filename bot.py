from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8744055485:AAG9_EyB26rKSyMCkweX6TdPDhzW1zzh83w"
OWNER_ID = 5519575890

pots = {}
finals = {}

# ================= WELCOME =================
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):

    for member in update.message.new_chat_members:

        username = (
            f"@{member.username}"
            if member.username
            else member.first_name
        )

        await update.message.reply_text(
            f"""

Halo {username} selamat datang di ftcs GOZEXX 🚀
🧾 TESTIMONI :
https://t.me/+lBK1UOUQTmVkODc9
"""
        )


# ================= MAIN =================
async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    text = update.message.text

    if not text:
        return

    text = text.lower().replace("/", "").strip()

    # ================= OWNER ONLY =================
    if update.message.from_user.id != OWNER_ID:
        return

    # ================= PAY =================
    if text == "pay":

        await update.message.reply_text(
            """
💸 GOZEXX PAYMENT 💸
━━━━━━━━━━━━━━
📜 RULES PAYMENT :
https://t.me/+X5CN3IQrholjNGVl
🧾 TESTIMONI :
https://t.me/+lBK1UOUQTmVkODc9
━━━━━━━━━━━━━━
"""
        )

        return

    # ================= DEPOSIT =================
    if text == "d":

        await update.message.reply_text(
            """
✨ SALDO TELAH MASUK ✨

Terima kasih telah FT di GOZEXX 🚀
Saldo berhasil ditransfer ke nomor anda ✅
"""
        )

        return

    # HARUS REPLY
    if not update.message.reply_to_message:
        return

    user = update.message.reply_to_message.from_user

    username = (
        f"@{user.username}"
        if user.username
        else user.first_name
    )

    # ================= D1-D4 =================
    if text in ["d1", "d2", "d3", "d4"]:

        pots[text] = username

        nomor = text.replace("d", "")

        await update.message.reply_text(
            f"POT {nomor} : {username}"
        )

    # ================= MATCH 1 =================
    if "d1" in pots and "d2" in pots:

        await update.message.reply_text(
            f"""
🔥 MATCH 1 🔥

{pots['d1']} VS {pots['d2']}
"""
        )

        del pots["d1"]
        del pots["d2"]

    # ================= MATCH 2 =================
    if "d3" in pots and "d4" in pots:

        await update.message.reply_text(
            f"""
🔥 MATCH 2 🔥

{pots['d3']} VS {pots['d4']}
"""
        )

        del pots["d3"]
        del pots["d4"]

    # ================= FINAL =================
    if text == "f1":

        finals["f1"] = username

        await update.message.reply_text(
            f"FINAL SET : {username}"
        )

    if text == "f2":

        finals["f2"] = username

        if "f1" in finals:

            await update.message.reply_text(
                f"""
🏆 FINAL MATCH 🏆

{finals['f1']} VS {finals['f2']}
"""
            )

            del finals["f1"]
            del finals["f2"]


# ================= BOT =================
app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
)

app.add_handler(
    MessageHandler(filters.TEXT, handler)
)

print("GOZEXX BOT ACTIVE 🚀")

app.run_polling(
    timeout=30,
    drop_pending_updates=True
)