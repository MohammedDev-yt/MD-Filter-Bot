# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
ᴍʏ ɴᴀᴍᴇ ɪs <a href=https://t.me/{}>{}</a>, I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs, sᴇʀɪᴇs, ᴅʀᴀᴍᴀs, ᴀɴɪᴍᴇs..Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ sᴇᴇ ᴍʏ ᴍᴀɢɪᴄ 😍"""
    HELP_TXT = """ʜᴇʏ {}
ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs."""
    ABOUT_TXT = """• ᴍʏ ɴᴀᴍᴇ : {}
• ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Mr_Mohammed_29>ᴍᴏʜᴀᴍᴍᴇᴅ</a>
• ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ
• ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 𝟹
• ᴅᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ
• ʙᴏᴛ sᴇᴠᴇʀ : ʀᴇɴᴅᴇʀ
• ʙᴜɪʟᴅ sᴛᴀᴛᴜs: v1.0.1 [ ʙᴇᴛᴀ ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- MD Fɪʟᴛᴇʀ Bᴏᴛ ɪs ᴀ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ᴘʀᴏɪᴇᴄᴛ. 
- sᴏᴜʀᴄᴇ - https://github.com/MohammedDev-yt/MD-Filter-Bot

<b>ᴜᴘᴅᴀᴛᴇs :</b>
- <a href=https://t.me/Anime_UpdatesAU>ᴀɴɪᴍᴇ ᴜᴘᴅᴀᴛᴇs ᴀᴜ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- 𝖥𝗂𝗅𝗍𝖾𝗋 𝗂𝗌 𝗍𝗁𝖾 𝖿𝖾𝖺𝗍𝗎𝗋𝖾 𝗐𝖾𝗋𝖾 𝗎𝗌𝖾𝗋𝗌 𝖼𝖺𝗇 𝗌𝖾𝗍 𝖺𝗎𝗍𝗈𝗆𝖺𝗍𝖾𝖽 𝗋𝖾𝗉𝗅𝗂𝖾𝗌 𝖿𝗈𝗋 𝖺 𝗉𝖺𝗋𝗍𝗂𝖼𝗎𝗅𝖺𝗋 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝖺𝗇𝖽 𝖤𝗏𝖺𝖬𝖺𝗋𝗂𝖺 𝗐𝗂𝗅𝗅 𝗋𝖾𝗌𝗉𝗈𝗇𝖽 𝗐𝗁𝖾𝗇𝖾𝗏𝖾𝗋 𝖺 𝗄𝖾𝗒𝗐𝗈𝗋𝖽 𝗂𝗌 𝖿𝗈𝗎𝗇𝖽 𝗍𝗁𝖾 𝗆𝖾𝗌𝗌𝖺𝗀𝖾

<b>NOTE:</b>
1. MD-Fɪʟᴛᴇʀ-Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- MD-Filter-Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. MD-Filter-Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Mr_Mohammed_29)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #