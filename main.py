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
