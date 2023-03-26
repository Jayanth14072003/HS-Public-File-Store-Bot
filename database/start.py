from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram import filters
from WebStreamer.utils.Translation import Language, BUTTON
from pyrogram.enums.parse_mode import ParseMode

@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    lang = Language(m)
    await m.reply_photo(
        photo="https://te.legra.ph/file/403a8223288699d50ecf1.jpg",
        caption=lang.START_TEXT.format(m.from_user.mention),
        parse_mode=ParseMode.HTML,
        reply_markup=BUTTON.START_BUTTONS
    )


@StreamBot.on_message(filters.private & filters.command(["about"]))
async def aboutcmd(bot, update):
    lang = Language(update)
    await update.reply_text(
        photo="https://te.legra.ph/file/403a8223288699d50ecf1.jpg",
        caption=lang.ABOUT_TEXT.format(update.from_user.mention),
        reply_markup=BUTTON.ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    lang = Language(message)
    await message.reply_text(
        photo="https://te.legra.ph/file/403a8223288699d50ecf1.jpg",
        caption=lang.HELP_TEXT.format(Var.UPDATES_CHANNEL),
        parse_mode=ParseMode.HTML,
        reply_markup=BUTTON.HELP_BUTTONS
    )
