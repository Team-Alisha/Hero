import asyncio
import os
import shutil
from asyncio import QueueEmpty

from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types.messages_and_media import message

from config import get_queue
from Hero import BOT_USERNAME, db_mem
from Hero.Core.PyTgCalls import Queues
from Hero.Core.PyTgCalls.Hero import (join_live_stream, join_video_stream,
                                        stop_stream)
from Hero.Database import (add_active_chat, add_active_video_chat,
                            is_active_chat, music_off, music_on,
                            remove_active_chat)
from Hero.Inline import (audio_markup, audio_markup2, primary_markup,
                          secondary_markup, secondary_markup2)
from Hero.Utilities.timer import start_timer

loop = asyncio.get_event_loop()


async def start_stream_video(message, file, title, mystic):
    global get_queue
    if message.chat.id not in db_mem:
        db_mem[message.chat.id] = {}
    wtfbro = db_mem[message.chat.id]
    wtfbro["live_check"] = False
    if message.chat.username:
        link = f"https://t.me/{message.chat.username}/{message.reply_to_message.message_id}"
    else:
        xf = str((message.chat.id))[4:]
        link = f"https://t.me/c/{xf}/{message.reply_to_message.message_id}"
    if await is_active_chat(message.chat.id):
        file = f"s1s_1080_+_{file}"
        position = await Queues.put(message.chat.id, file=file)
        if file not in db_mem:
            db_mem[file] = {}
        wtfbro = db_mem[file]
        wtfbro["chat_title"] = message.chat.title
        wtfbro["duration"] = 0
        wtfbro["username"] = message.from_user.mention
        wtfbro["videoid"] = "videoid"
        wtfbro["user_id"] = message.from_user.id
        got_queue = get_queue.get(message.chat.id)
        title = title
        user = message.from_user.first_name
        duration = 0
        to_append = [title, user, duration]
        got_queue.append(to_append)
        final_output = await message.reply_photo(
            photo="Utils/Telegram.JPEG",
            caption=(
                f"🎬<b>__ᴠɪᴅᴇᴏ:__ </b> [ɢɪᴠᴇɴ ᴠɪᴅᴇᴏ ᴠɪᴀ ᴛᴇʟᴇɢʀᴀᴍ]({link})\n\n👤<b>__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__ </b>{message.from_user.mention} \n⃣<b>__ǫᴜᴇᴜᴇᴅ ᴀᴛ:__</b> <b>#{position}!</b>"
            ),
            reply_markup=audio_markup2,
        )
        await mystic.delete()
        return
    else:
        if not await join_video_stream(message.chat.id, file, 720):
            return await mystic.edit(
                "ᴇʀʀᴏʀ ᴊᴏɪɴɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.../nᴍᴀᴋᴇ sᴜʀᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪs ᴇɴᴀʙʟᴇᴅ..."
            )
        get_queue[message.chat.id] = []
        got_queue = get_queue.get(message.chat.id)
        title = title
        user = message.from_user.first_name
        duration = 0
        to_append = [title, user, duration]
        got_queue.append(to_append)
        await music_on(message.chat.id)
        await add_active_chat(message.chat.id)
        await add_active_video_chat(message.chat.id)
        buttons = secondary_markup2("Smex1", message.from_user.id)
        await mystic.delete()
        cap = f"🎥<b>__ᴘʟᴀʏɪɴɢ:__ </b>[ɢɪᴠᴇɴ ᴠɪᴅᴇᴏ ᴠɪᴀ ᴛᴇʟᴇɢʀᴀᴍ]({link})\n👤**__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__** {message.from_user.mention}"
        final_output = await message.reply_photo(
            photo="Utils/Telegram.JPEG",
            reply_markup=InlineKeyboardMarkup(buttons),
            caption=cap,
        )


async def start_live_stream(
    CallbackQuery,
    quality,
    link,
    thumb,
    title,
    duration_min,
    duration_sec,
    videoid,
):
    global get_queue
    if CallbackQuery.message.chat.id not in db_mem:
        db_mem[CallbackQuery.message.chat.id] = {}
    wtfbro = db_mem[CallbackQuery.message.chat.id]
    wtfbro["live_check"] = True
    if await is_active_chat(CallbackQuery.message.chat.id):
        try:
            Queues.clear(CallbackQuery.message.chat.id)
        except QueueEmpty:
            pass
        await remove_active_chat(CallbackQuery.message.chat.id)
        try:
            await stop_stream(CallbackQuery.message.chat.id)
        except:
            pass
    if not await join_live_stream(
        CallbackQuery.message.chat.id, link, quality
    ):
        return await CallbackQuery.message.reply_text(
            f"ᴇʀʀᴏʀ ᴊᴏɪɴɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ..."
        )
    await music_on(CallbackQuery.message.chat.id)
    await add_active_chat(CallbackQuery.message.chat.id)
    await add_active_video_chat(CallbackQuery.message.chat.id)
    buttons = secondary_markup2(videoid, CallbackQuery.from_user.id)
    cap = f"**ʟɪᴠᴇ sᴛʀᴇᴀᴍɪɴɢ**\n\n🎥<b>__ᴘʟᴀʏɪɴɢ:__ </b>[{title[:25]}](https://www.youtube.com/watch?v={videoid}) \n💡<b>__ɪɴғᴏ:__</b> [ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n👤**__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__** {CallbackQuery.from_user.mention}"
    final_output = await CallbackQuery.message.reply_photo(
        photo=thumb,
        reply_markup=InlineKeyboardMarkup(buttons),
        caption=cap,
    )
    os.remove(thumb)
    await CallbackQuery.message.delete()


async def start_video_stream(
    CallbackQuery,
    quality,
    link,
    thumb,
    title,
    duration_min,
    duration_sec,
    videoid,
):
    global get_queue
    if CallbackQuery.message.chat.id not in db_mem:
        db_mem[CallbackQuery.message.chat.id] = {}
    wtfbro = db_mem[CallbackQuery.message.chat.id]
    wtfbro["live_check"] = False
    if await is_active_chat(CallbackQuery.message.chat.id):
        file = f"s1s_{quality}_+_{videoid}"
        position = await Queues.put(CallbackQuery.message.chat.id, file=file)
        _path_ = (
            (str(file))
            .replace("_", "", 1)
            .replace("/", "", 1)
            .replace(".", "", 1)
        )
        buttons = secondary_markup(videoid, CallbackQuery.from_user.id)
        if file not in db_mem:
            db_mem[file] = {}
        cpl = f"cache/{_path_}final.png"
        shutil.copyfile(thumb, cpl)
        wtfbro = db_mem[file]
        wtfbro["chat_title"] = CallbackQuery.message.chat.title
        wtfbro["duration"] = duration_min
        wtfbro["username"] = CallbackQuery.from_user.mention
        wtfbro["videoid"] = videoid
        wtfbro["user_id"] = CallbackQuery.from_user.id
        got_queue = get_queue.get(CallbackQuery.message.chat.id)
        title = title
        user = CallbackQuery.from_user.first_name
        duration = duration_min
        to_append = [title, user, duration]
        got_queue.append(to_append)
        final_output = await CallbackQuery.message.reply_photo(
            photo=thumb,
            caption=(
                f"🎬<b>ᴠɪᴅᴇᴏ:__ </b>[{title[:25]}](https://www.youtube.com/watch?v={videoid}) \n⏳<b>__ᴅᴜʀᴀᴛɪᴏɴ:__</b> {duration_min} \n💡<b>__ɪɴғᴏ:__</b> [ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n👤<b>__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__ </b>{CallbackQuery.from_user.mention} \n⃣<b>__ᴠɪᴅᴇᴏ ǫᴜᴇᴜᴇᴅ ᴀᴛ:__</b> <b>#{position}</b>"
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        await CallbackQuery.message.delete()
        os.remove(thumb)
        return
    else:
        if not await join_video_stream(
            CallbackQuery.message.chat.id, link, quality
        ):
            return await CallbackQuery.message.reply_text(
                f"ᴇʀʀᴏʀ ᴊᴏɪɴɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ..."
            )
        get_queue[CallbackQuery.message.chat.id] = []
        got_queue = get_queue.get(CallbackQuery.message.chat.id)
        title = title
        user = CallbackQuery.from_user.first_name
        duration = duration_min
        to_append = [title, user, duration]
        got_queue.append(to_append)
        await music_on(CallbackQuery.message.chat.id)
        await add_active_video_chat(CallbackQuery.message.chat.id)
        await add_active_chat(CallbackQuery.message.chat.id)

        buttons = primary_markup(
            videoid, CallbackQuery.from_user.id, duration_min, duration_min
        )
        cap = f"**ᴠɪᴅᴇᴏ sᴛʀᴇᴀᴍɪɴɢ**\n\n🎥<b>__ᴘʟᴀʏɪɴɢ:__ </b>[{title[:25]}](https://www.youtube.com/watch?v={videoid}) \n💡<b>__ɪɴғᴏ:__</b> [ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n👤**__ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:__** {CallbackQuery.from_user.mention}"
        final_output = await CallbackQuery.message.reply_photo(
            photo=thumb,
            reply_markup=InlineKeyboardMarkup(buttons),
            caption=cap,
        )
        os.remove(thumb)
        await CallbackQuery.message.delete()
        await start_timer(
            videoid,
            duration_min,
            duration_sec,
            final_output,
            CallbackQuery.message.chat.id,
            CallbackQuery.from_user.id,
            0,
        )
