from typing import Dict, List, Union

from pyrogram import Client, filters

from Hero import BOT_USERNAME, MUSIC_BOT_NAME, app, db
from Hero.Database import _get_theme, get_theme, save_theme

themes = [
    "blue",
    "black",
    "red",
    "green",
    "grey",
    "orange",
    "pink",
    "yellow",
    "Random",
]

themes2 = [
    "blue",
    "black",
    "red",
    "green",
    "grey",
    "orange",
    "pink",
    "yellow",
]

__MODULE__ = "ᴛʜᴇᴍᴇ"
__HELP__ = """


`/settheme`
- sᴇᴛ ᴀ ᴛʜᴇᴍᴇ ғᴏʀ ᴛʜᴜᴍʙɴᴀɪʟs.

`/theme`
- ᴄʜᴇᴄᴋ ᴛʜᴇᴍᴇ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ.
"""


@app.on_message(
    filters.command(["settheme", f"settheme@{BOT_USERNAME}"]) & filters.group
)
async def settheme(_, message):
    usage = f"ᴛʜɪs ɪsɴ'ᴛ ᴀ ᴛʜᴇᴍᴇ...\n\nsᴇʟᴇᴄᴛ ғʀᴏᴍ ᴛʜᴇᴍ\n{' | '.join(themes)}\n\nᴜsᴇ 'Random' ᴛᴏ ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴄʜᴏɪᴄᴇ ᴏғ ᴛʜᴇᴍᴇs"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    theme = message.text.split(None, 1)[1].strip()
    if theme not in themes:
        return await message.reply_text(usage)
    note = {
        "theme": theme,
    }
    await save_theme(message.chat.id, "theme", note)
    await message.reply_text(f"ᴄʜᴀɴɢᴇᴅ ᴛʜᴜᴍʙɴᴀɪʟ ᴛʜᴇᴍᴇ ᴛᴏ {theme}")


@app.on_message(filters.command("theme"))
async def theme_func(_, message):
    await message.delete()
    _note = await get_theme(message.chat.id, "theme")
    if not _note:
        theme = "Random"
    else:
        theme = _note["theme"]
    await message.reply_text(
        f"**{MUSIC_BOT_NAME} ᴛʜᴜᴍʙɴᴀɪʟs ᴛʜᴇᴍᴇ**\n\n**ᴄᴜʀʀᴇɴᴛ ᴛʜᴇᴍᴇ:-** {theme}\n\n**ᴀᴠᴀɪʟᴀʙʟᴇ ᴛʜᴇᴍᴇs:-** {' | '.join(themes2)} \n\nᴜsᴇ /settheme ᴛᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇᴍᴇ..."
    )
