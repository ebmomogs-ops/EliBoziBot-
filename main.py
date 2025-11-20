import os
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)

# =========================
# Konfiguration
# =========================

AFFILIATE_LINK = "https://app.trustyfy.com?by=101ddm"
KONTAKT_INFO = "Du erreichst Eli direkt auf Telegram: @Eli_Bozinovska3"
BOT_NAME = "EliBoziBot"

# Callback-Konstanten
CB_WHAT_IS_TRUSTYFY = "what_is_trustyfy"
CB_CONTACT_ELI = "contact_eli"
CB_ROLE_PRIVATE = "role_private"
CB_ROLE_BUSINESS = "role_business"
CB_PRIVATE_KRYPTO_YES = "private_krypto_yes"
CB_PRIVATE_KRYPTO_NO = "private_krypto_no"
CB_BUSINESS_CLASSIC = "business_classic"
CB_BUSINESS_WEB3 = "business_web3"
# =========================
# Hilfsfunktionen: Keyboards
# =========================

def main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🔍 Was ist Trustyfy?", callback_data=CB_WHAT_IS_TRUSTYFY)],
        [InlineKeyboardButton("📩 Kontakt zu Eli", callback_data=CB_CONTACT_ELI)],
    ]
    return InlineKeyboardMarkup(keyboard)


def role_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("👤 Privatperson", callback_data=CB_ROLE_PRIVATE)],
        [InlineKeyboardButton("🏢 Unternehmen", callback_data=CB_ROLE_BUSINESS)],
    ]
    return InlineKeyboardMarkup(keyboard)


def private_experience_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("💰 Ja, ich habe Krypto-Erfahrung", callback_data=CB_PRIVATE_KRYPTO_YES)],
        [InlineKeyboardButton("✨ Nein, ich bin neu im Bereich", callback_data=CB_PRIVATE_KRYPTO_NO)],
    ]
    return InlineKeyboardMarkup(keyboard)


def business_type_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🧩 Klassisches Unternehmen / Dienstleister", callback_data=CB_BUSINESS_CLASSIC)],
        [InlineKeyboardButton("🪙 Web3 / Blockchain-Unternehmen", callback_data=CB_BUSINESS_WEB3)],
    ]
    return InlineKeyboardMarkup(keyboard)


def free_account_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🔗 Kostenfreien Account erstellen", url=AFFILIATE_LINK)],
        [InlineKeyboardButton("📩 Kontakt zu Eli", callback_data=CB_CONTACT_ELI)],
    ]
    return InlineKeyboardMarkup(keyboard)


def business_pricing_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🔗 Kostenfreien Business-Account erstellen", url=AFFILIATE_LINK)],
        [InlineKeyboardButton("📩 Kontakt zu Eli", callback_data=CB_CONTACT_ELI)],
    ]
    return InlineKeyboardMarkup(keyboard) 
# =========================
# Text-Bausteine
# =========================

def get_start_text() -> str:
    return (
        f"Hey! 👋\n\n"
        f"Mein Briefkasten ist aktuell ziemlich voll – und bevor du lange auf eine Antwort warten musst, "
        f"übernimmt hier mein kleiner digitaler Assistent **{BOT_NAME}**. 🤖\n\n"
        "Er hilft dir, in Ruhe herauszufinden, ob **Trustyfy** für dich oder dein Business spannend ist.\n\n"
        "Und wenn du später Fragen hast oder persönliche Unterstützung möchtest:\n"
        "👉 Ich bin natürlich trotzdem persönlich für dich da. 💬"
    )


def get_trustyfy_intro_text() -> str:
    return (
        "Trustyfy ist deine **Brücke in echte finanzielle Freiheit** – schnell, sicher und vollständig unter deiner Kontrolle.\n\n"
        "Wir leben in einer Welt, in der Banken, Plattformen und Staaten entscheiden können, "
        "wer Zugriff auf sein Geld hat – und wer nicht.\n\n"
        "🔹 Trustyfy dreht dieses Machtverhältnis um.\n\n"
        "✨ **Was macht Trustyfy besonders?**\n"
        "• Die Brücke zwischen **Fiat und Krypto** – ohne Hürden\n"
        "• **Schnell, sicher & dezentral**\n"
        "• Du holst dir die **Verantwortung für dein Geld** zurück\n"
        "• **Niemand außer dir** hat Zugriff auf dein Geld\n"
        "• **Visa Karte**, um Krypto im Alltag auszugeben\n"
        "• Volle Kontrolle – volle Freiheit\n\n"
        "Damit ich dir die richtigen Infos geben kann:\n"
        "👉 **Bist du Privatperson oder Unternehmer?**"
    )
    def get_private_experience_text() -> str:
    return (
        "Super, lass uns herausfinden, welcher Weg am besten zu dir passt. ✨\n\n"
        "Darf ich kurz fragen:\n"
        "👉 **Hast du bereits Erfahrung mit Krypto?**"
    )


def get_private_krypto_yes_text() -> str:
    return (
        "Perfekt! 💰\n\n"
        "Dann kennst du ja die typischen Pain Points:\n"
        "Mehrere Wallets, Börsen, KYC-Prozesse, Transfers, Wartezeiten…\n\n"
        "Genau hier setzt Trustyfy an:\n\n"
        "✅ **Kaufen**\n"
        "✅ **Halten**\n"
        "✅ **Tauschen**\n"
        "✅ **Ausgeben**\n\n"
        "…und das **alles auf EINER Plattform**.\n\n"
        "Keine weiteren Wallets, keine zusätzlichen Börsen, keine Umwege.\n\n"
        "Das ist die Fiat–Krypto-Brücke, wie sie sein sollte:\n"
        "**einfach, schnell, sicher. 🔐**"
    )


def get_private_krypto_no_text() -> str:
    return (
        "Kein Problem – dann ist Trustyfy für dich der **ideale Start**, um dein Geld sicherer aufzustellen. 🤍\n\n"
        "Du kannst ganz einfach:\n\n"
        "💶 **Euro schicken**\n"
        "🔄 **in Stablecoins tauschen**\n"
        "🔐 **sicher halten**\n\n"
        "Damit entkoppelst du dein Geld ein Stück weit vom klassischen Bankensystem – "
        "ohne komplizierte Technik und ohne, dass jemand von außen eingreifen kann.\n\n"
        "Du gehst den ersten Schritt in Richtung **echter, eigener finanzieller Sicherheit**."
    )def get_free_account_text() -> str:
    return (
        "🔐 **Kostenfreier, dezentraler Account – so einfach ist der Start**\n\n"
        "Der Einstieg in Trustyfy ist superleicht und dauert meistens weniger als 20 Sekunden.\n\n"
        "So funktioniert es:\n"
        "1️⃣ Gib einfach deine **E-Mail-Adresse** ein.\n"
        "2️⃣ Du erhältst einen **6-stelligen One-Time Passcode** an diese Adresse.\n"
        "3️⃣ Diesen Code gibst du im zweiten Schritt ein – **fertig**.\n\n"
        "➡ Du bist direkt auf der **Blockchain**.\n"
        "➡ Du hast deine **eigene, native Wallet**.\n"
        "➡ **Niemand außer dir** hat Zugriff.\n\n"
        "Ab hier kannst du sofort loslegen: kaufen, halten, tauschen, ausgeben. 🚀\n\n"
        "💰 **Preise für Privatpersonen:**\n"
        "• Kostenfreier Start-Account\n"
        "• **15 $ Lifetime** (einmal zahlen – für immer nutzen)\n"
        "• **60 $ pro Jahr** (wenn du flexibel bleiben möchtest)"
    )def get_business_intro_text() -> str:
    return (
        "Alles klar, du bist ein Unternehmen. 🏢\n\n"
        "Damit ich dir das passende Modell zeigen kann, sag mir bitte:\n\n"
        "👉 **Welche Art von Unternehmen bist du?**"
    )


def get_business_classic_text() -> str:
    return (
        "Perfekt. 🙌\n\n"
        "Für **Dienstleister, Agenturen, Selbstständige und klassische Unternehmen** bietet Trustyfy "
        "eine einfache, sichere dezentrale Identitäts- und Verifizierungsstruktur.\n\n"
        "Ideal für:\n"
        "• Mitarbeiterzugänge & Rollen\n"
        "• Verifizierungen & Berechtigungen\n"
        "• Digitale Nachweise & Zertifikate\n"
        "• Sicheres Identitäts-Management\n"
    )


def get_business_web3_text() -> str:
    return (
        "Sehr spannend! 🪙\n\n"
        "Für **Web3- & Blockchain-Unternehmen** bietet Trustyfy tiefere Integrationen, APIs und "
        "dezentrale Unternehmensstrukturen.\n\n"
        "Ideal für Projekte, die:\n"
        "• Automatisierung brauchen\n"
        "• Token-Prozesse integrieren\n"
        "• sichere Identitätslayer einbauen\n"
    )


def get_business_pricing_text() -> str:
    return (
        "💼 **B2B-Angebote bei Trustyfy**\n\n"
        "⭐ **B2B Start – kostenfrei**\n"
        "⭐ **600 $ pro Jahr – Unternehmen**\n"
        "⭐ **3000 $ pro Jahr – Web3 Unternehmen**\n\n"
        "Alles beginnt mit der kostenfreien Version – und du buchst nur, was du brauchst."
    )


def get_contact_text() -> str:
    return (
        "Wenn du Fragen hast oder eine persönliche Empfehlung möchtest:\n\n"
        f"👉 {KONTAKT_INFO}\n\n"
        "Ich freue mich, von dir zu hören! – Eli 🤍"
    )# =========================
# Handler
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        get_start_text(),
        reply_markup=main_menu_keyboard(),
        parse_mode="Markdown",
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == CB_WHAT_IS_TRUSTYFY:
        await query.message.reply_text(
            get_trustyfy_intro_text(),
            reply_markup=role_keyboard(),
            parse_mode="Markdown",
        )

    elif data == CB_CONTACT_ELI:
        await query.message.reply_text(
            get_contact_text(),
            parse_mode="Markdown",
        )

    elif data == CB_ROLE_PRIVATE:
        await query.message.reply_text(
            get_private_experience_text(),
            reply_markup=private_experience_keyboard(),
            parse_mode="Markdown",
        )

    elif data == CB_ROLE_BUSINESS:
        await query.message.reply_text(
            get_business_intro_text(),
            reply_markup=business_type_keyboard(),
            parse_mode="Markdown",
        )

    elif data == CB_PRIVATE_KRYPTO_YES:
        await query.message.reply_text(
            get_private_krypto_yes_text(),
            parse_mode="Markdown",
        )
        await query.message.reply_text(
            get_free_account_text(),
            reply_markup=free_account_keyboard(),
            parse_mode="Markdown",
        )

    elif data == CB_PRIVATE_KRYPTO_NO:
        await query.message.reply_text(
            get_private_krypto_no_text(),
            parse_mode="Markdown",
        )
        await query.message.reply_text(
            get_free_account_text(),
            reply_markup=free_account_keyboard(),
            parse_mode="Markdown",
        )

    elif data == CB_BUSINESS_CLASSIC:
        await query.message.reply_text(
            get_business_classic_text(),
            parse_mode="Markdown",
        )
        await query.message.reply_text(
            get_business_pricing_text(),
            reply_markup=business_pricing_keyboard(),
            parse_mode="Markdown",
        )

    elif data == CB_BUSINESS_WEB3:
        await query.message.reply_text(
            get_business_web3_text(),
            parse_mode="Markdown",
        )
        await query.message.reply_text(
            get_business_pricing_text(),
            reply_markup=business_pricing_keyboard(),
            parse_mode="Markdown",
        )# =========================
# main() – Einstiegspunkt
# =========================

def main() -> None:
    # Token wird in Railway als Variable TELEGRAM_BOT_TOKEN gespeichert
    token = os.environ["TELEGRAM_BOT_TOKEN"]

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    application.run_polling()


if __name__ == "__main__":
    main()
  
