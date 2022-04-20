class Script(object):
    START_TXT = """Hᴇʟʟᴏ {},

𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 Tom , 𝙰 𝚂𝙼𝙰𝚁𝚃 𝚁𝙾𝙱𝙾𝚃 𝚆𝙸𝚃𝙷 𝙼𝙰𝙽𝚈 𝙰𝙼𝙰𝚉𝙸𝙽𝙶 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂. 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂 & 𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙼𝙰𝙽𝙰𝙶𝙴 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""

 
    E_TXT = """𝙷𝙴𝚈 {},𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄 𝙵𝙾𝚁 𝚈𝙾𝚄:"""
 
    ROG_TXT = """𝙷𝙴𝚈 {},𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄 𝙵𝙾𝚁 𝚈𝙾𝚄:"""

    D_TXT = """𝙷𝙴𝚈 {},𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄 𝙵𝙾𝚁 𝚈𝙾𝚄:"""

    C_TXT = """𝙷𝙴𝚈 {},𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄 𝙵𝙾𝚁 𝚈𝙾𝚄:"""

    B_TXT = """hey"""

    A_TXT = """𝙷𝙴𝚈 {},𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄 𝙵𝙾𝚁 𝚈𝙾𝚄:"""

    HELP_TXT = """𝙷𝙴𝚈 {},𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄 𝙵𝙾𝚁 𝚈𝙾𝚄:"""

    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
➢ 𝐌𝐲 𝐂𝐫𝐞𝐚𝐭𝐨𝐫: <a href='https://t.me/sarbudeen786'>💔Lᴏɴᴇʟʏᴋiɴɢ💔</a>
➢ 𝐌𝐲 𝐒𝐨𝐮𝐫𝐜𝐞: 𝖤𝗏𝖺 𝖬𝖺𝗋𝗂𝖺
➢ 𝐌𝐲 𝐋𝐢𝐛𝐫𝐚𝐫𝐲: <a href='https://docs.pyrogram.org'>𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆</a>
➢ 𝐌𝐲 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: <a herf='https://www.python.org'>𝖯𝗒𝗍𝗁𝗈𝗇3 </a>
➢ 𝐌𝐲 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞: <a href='https://cloud.mongodb.com'>𝖬𝗈𝗇𝗀𝗈 𝖣𝖡</a>
➢ 𝐌𝐲 𝐒𝐞𝐫𝐯𝐞𝐫: <a href='https://www.heroku.com'>𝖧𝖾𝗋𝗈𝗄𝗎</a>
➢ 𝐌𝐲 𝐔𝐩𝐝𝐚𝐭𝐞𝐬: <a href='https://t.me/thanimaibots'>Tᕼᴀɴʜᴍᴀʜ𝖡𝗈𝗍s</a>
➢ 𝐌𝐲 𝐒𝐮𝐩𝐩𝐨𝐫𝐭: <a href='https://t.me/thanimaisupport'>Tᕼᴀɴʜᴍᴀʜ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍</a>
➤ 𝙸𝚏 𝚢𝚘𝚞 𝚕𝚒𝚔𝚎 𝚝𝚑𝚒𝚜 𝚋𝚘𝚝 𝚙𝚕𝚎𝚊𝚜𝚎 𝚜𝚑𝚊𝚛𝚎 𝚊𝚗𝚍 𝚜𝚞𝚙𝚙𝚘𝚛𝚝 𝚞𝚜 ⚡
"""
    RAJ_TXT = """4th MODULES
"""
    SOURCE_TXT = """<b>Source:</b>
- 𝐌𝐲 𝐬𝐨𝐮𝐫𝐜𝐞  𝐢𝐬 𝐚  𝐂𝐋𝐎𝐒𝐄𝐝 𝐩𝐫𝐨𝐣𝐞𝐜𝐭. 
 <a href=https://t.me/thanimaisupport>𝐑𝐞𝐩𝐨𝐫𝐭 & 𝐛𝐮𝐠𝐬 </a>
𝐎𝐰𝐧𝐞𝐫 : 💔𝐋𝐨𝐧𝐞𝐥𝐲 𝐤𝐢𝐧𝐠 💔."""

    S_TXT = """5TH Modules"""

    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Fɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ Cʀᴀᴄᴋᴇʀ  ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ

<b>NOTE:</b>
1. Cʀᴀᴄᴋᴇʀ  sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. Oɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. Aʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs.

<b>Commands and Usage:</b>
• /filter - ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ.
• /filters - ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ.
• /del - ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ.
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)."""
    
    RPE_TXT = """
 ❍ /report <ʀᴇᴀsᴏɴ>*:* ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴀᴅᴍɪɴs.
 ❍ @admins*:* ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴀᴅᴍɪɴs.
*NOTE:* Nᴇɪᴛʜᴇʀ ᴏғ ᴛʜᴇsᴇ ᴡɪʟʟ ɢᴇᴛ ᴛʀɪɢɢᴇʀᴇᴅ ɪғ ᴜsᴇᴅ ʙʏ ᴀᴅᴍɪɴs.
*Aᴅᴍɪɴs ᴏɴʟʏ:*
 ❍ /reports <ᴏɴ/ᴏғғ>*:* ᴄʜᴀɴɢᴇ ʀᴇᴘᴏʀᴛ sᴇᴛᴛɪɴɢ, ᴏʀ ᴠɪᴇᴡ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs.
   • Iғ ᴅᴏɴᴇ ɪɴ ᴘᴍ, ᴛᴏɢɢʟᴇs ʏᴏᴜʀ sᴛᴀᴛᴜs.
   • Iғ ɪɴ ɢʀᴏᴜᴘ, ᴛᴏɢɢʟᴇs ᴛʜᴀᴛ ɢʀᴏᴜᴘs's sᴛᴀᴛᴜs.
"""
    POK_TXT = """
/pokedex Pᴏᴋᴇᴍᴏɴ Nᴀᴍᴇ 🦫
"""
    IN_TXT = """
*Away from group*
 ❍ /afk <ʀᴇᴀsᴏɴ>*:* ᴍᴀʀᴋ ʏᴏᴜʀsᴇʟғ ᴀs AFK(ᴀᴡᴀʏ ғʀᴏᴍ ᴋᴇʏʙᴏᴀʀᴅ).
 ❍ /brb <ʀᴇᴀsᴏɴ>*:* sᴀᴍᴇ ᴀs ᴛʜᴇ ᴀғᴋ ᴄᴏᴍᴍᴀɴᴅ - ʙᴜᴛ ɴᴏᴛ ᴀ ᴄᴏᴍᴍᴀɴᴅ.
Wʜᴇɴ ᴍᴀʀᴋᴇᴅ ᴀs AFK, ᴀɴʏ ᴍᴇɴᴛɪᴏɴs ᴡɪʟʟ ʙᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴡɪᴛʜ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴀʏ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ!
*ID:*
 ❍ /id*:* ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ɢʀᴏᴜᴘ ɪᴅ. Iғ ᴜsᴇᴅ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ, ɢᴇᴛs ᴛʜᴀᴛ ᴜsᴇʀ's ɪᴅ.
 ❍ /gifid*:* ʀᴇᴘʟʏ ᴛᴏ ᴀ ɢɪғ ᴛᴏ ᴍᴇ ᴛᴏ ᴛᴇʟʟ ʏᴏᴜ ɪᴛs ғɪʟᴇ ID.
*Sᴇʟғ ᴀᴅᴅᴅᴇᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ:* 
 ❍ /setme <ᴛᴇxᴛ>*:* ᴡɪʟʟ sᴇᴛ ʏᴏᴜʀ ɪɴғᴏ
 ❍ /mw*:* ᴡɪʟʟ ɢᴇᴛ ʏᴏᴜʀ ᴏʀ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ's ɪɴғᴏ.
*Exᴀᴍᴘʟᴇs:* 💡
 ➩ /setme I ᴀᴍ ᴀ ᴡᴏʟғ.
 ➩ /me @ᴜsᴇʀɴᴀᴍᴇ(ᴅᴇғᴀᴜʟᴛs ᴛᴏ ʏᴏᴜʀs ɪғ ɴᴏ ᴜsᴇʀ sᴘᴇᴄɪғɪᴇᴅ)
*Iɴғᴏʀᴍᴀᴛɪᴏɴ ᴏᴛʜᴇʀs ᴀᴅᴅ ᴏɴ ʏᴏᴜ:* 
 ❍ /bio*:* ᴡɪʟʟ ɢᴇᴛ ʏᴏᴜʀ ᴏʀ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ's ʙɪᴏ. Tʜɪs ᴄᴀɴɴᴏᴛ ʙᴇ sᴇᴛ ʙʏ ʏᴏᴜʀsᴇʟғ.
 ❍ /setbio <ᴛᴇxᴛ>*:* ᴡʜɪʟᴇ ʀᴇᴘʟʏɪɴɢ, ᴡɪʟʟ sᴀᴠᴇ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ's ʙɪᴏ 
*Exᴀᴍᴘʟᴇs:* 💡
 ➩ /bio @ᴜsᴇʀɴᴀᴍᴇ(ᴅᴇғᴀᴜʟᴛs ᴛᴏ ʏᴏᴜʀs ɪғ ɴᴏᴛ sᴘᴇᴄɪғɪᴇᴅ).`
 ➩ /setbio Tʜɪs ᴜsᴇʀ ɪs ᴀ ᴡᴏʟғ` (ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ)
*Oᴠᴇʀᴀʟʟ Iɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ʏᴏᴜ:*
 ❍ /info*:* ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ. 
 
*Wʜᴀᴛ ɪs ᴛʜᴀᴛ ʜᴇᴀʟᴛʜ ᴛʜɪɴɢʏ?*
 Cᴏᴍᴇ ᴀɴᴅ sᴇᴇ [HP Sʏsᴛᴇᴍ ᴇxᴘʟᴀɪɴᴇᴅ](ʜᴛᴛᴘs://ᴛ.ᴍᴇ/OɴᴇPᴜɴᴄʜUᴘᴅᴀᴛᴇs/192)
"""
    STI_TXT = """
❍ /stickerid*:* ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴛᴏ ᴍᴇ ᴛᴏ ᴛᴇʟʟ ʏᴏᴜ ɪᴛs ғɪʟᴇ ID.
 ❍ /getsticker*:* ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴛᴏ ᴍᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛs ʀᴀᴡ PNG ғɪʟᴇ.
 ❍ /kang*:* ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴛᴏ ᴀᴅᴅ ɪᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴀᴄᴋ.
 ❍ /stickers*:* Fɪɴᴅ sᴛɪᴄᴋᴇʀs ғᴏʀ ɢɪᴠᴇɴ ᴛᴇʀᴍ ᴏɴ ᴄᴏᴍʙᴏᴛ sᴛɪᴄᴋᴇʀ ᴄᴀᴛᴀʟᴏɢᴜᴇ
"""
    FED_TXT = """
Everything is fun, until a spammer starts entering your group, and you have to block it. Then you need to start banning more, and more, and it hurts.
But then you have many groups, and you don't want this spammer to be in one of your groups - how can you deal? Do you have to manually block it, in all your groups?\n
*No longer!* With Federation, you can make a ban in one chat overlap with all other chats.\n
You can even designate federation admins, so your trusted admin can ban all the spammers from chats you want to protect.\n
*Commands:*\n
Feds are now divided into 3 sections for your ease. 
✪ /fedownerhelp*:* Provides help for fed creation and owner only commands
✪ /fedadminhelp*:* Provides help for fed administration commands
✪ /feduserhelp*:* Provides help for commands anyone can use

🔱 Fed Admins:*
✪  fban <user> <reason>*:* Fed bans a user
✪  /unfban <user> <reason>*:* Removes a user from a fed ban
✪  /fedinfo <fed_id>*:* Information about the specified Federation
✪  /joinfed <fed_id>*:* Join the current chat to the Federation. Only chat owners can do this. Every chat can only be in one Federation
✪  /leavefed <fed_id>*:* Leave the Federation given. Only chat owners can do this
✪  /setfrules <rules>*:* Arrange Federation rules
✪  /fedadmins*:* Show Federation admin
✪  /fbanlist*:* Displays all users who are victimized at the Federation at this time
✪  /fedchats*:* Get all the chats that are connected in the Federation
✪  /chatfed *:* See the Federation in the current chat

💫Fed Owner Only:*
✪  /newfed <fed_name>*:* Creates a Federation, One allowed per user
✪  /renamefed <fed_id> <new_fed_name>*:* Renames the fed id to a new name
✪  /delfed <fed_id`*:* Delete a Federation, and any information related to it. Will not cancel blocked users
✪  /fpromote <user>*:* Assigns the user as a federation admin. Enables all commands for the user under `Fed Admins`
✪  /fdemote <user>*:* Drops the User from the admin Federation to a normal User
✪  /subfed <fed_id>*:* Subscribes to a given fed ID, bans from that subscribed fed will also happen in your fed
✪  /unsubfed <fed_id>*:* Unsubscribes to a given fed ID
✪  /setfedlog <fed_id>*:* Sets the group as a fed log report base for the federation
✪  /unsetfedlog <fed_id>*:* Removed the group as a fed log report base for the federation
✪  /fbroadcast <message>*:* Broadcasts a messages to all groups that have joined your fed
✪  /fedsubs*:* Shows the feds your group is subscribed to
"""

    REP_TXT = """
❍ /report <ʀᴇᴀsᴏɴ>*:* ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴀᴅᴍɪɴs.
 ❍ @admins*:* ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴀᴅᴍɪɴs.
*NOTE:* Nᴇɪᴛʜᴇʀ ᴏғ ᴛʜᴇsᴇ ᴡɪʟʟ ɢᴇᴛ ᴛʀɪɢɢᴇʀᴇᴅ ɪғ ᴜsᴇᴅ ʙʏ ᴀᴅᴍɪɴs.
*Aᴅᴍɪɴs ᴏɴʟʏ:*
 ❍ /reports <ᴏɴ/ᴏғғ>*:* ᴄʜᴀɴɢᴇ ʀᴇᴘᴏʀᴛ sᴇᴛᴛɪɴɢ, ᴏʀ ᴠɪᴇᴡ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs.
   • Iғ ᴅᴏɴᴇ ɪɴ ᴘᴍ, ᴛᴏɢɢʟᴇs ʏᴏᴜʀ sᴛᴀᴛᴜs.
   • Iғ ɪɴ ɢʀᴏᴜᴘ, ᴛᴏɢɢʟᴇs ᴛʜᴀᴛ ɢʀᴏᴜᴘs's sᴛᴀᴛᴜs.
"""
    INS_TXT = """
- Reply to a text with /insult for insults.
"""
    NEXT_TXT = """
𝖆 4𝖙𝖍 𝖒𝖔𝖉𝖚𝖑𝖊𝖘"""
    TAL_TXT = """
- /tagall : Tᴀɢ ᴇᴠᴇʀʏᴏɴᴇ ɪɴ ᴀ ᴄʜᴀᴛ
"""
    ST_TXT = """
❍ `/text1`*:* ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴛᴇxᴛ.
 ❍ `/text2`*:* ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴛᴇxᴛ.
 ❍ `/text3`*:* ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴛᴇxᴛ.
 ❍ `/text4`*:* ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴛᴇxᴛ.
 ❍ `/text5`*:* ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴛᴇxᴛ.
"""
    DISB_TXT = """
    ❍ /cmds*:* ᴄʜᴇᴄᴋ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs ᴏғ ᴅɪsᴀʙʟᴇᴅ ᴄᴏᴍᴍᴀɴᴅs
    *Aᴅᴍɪɴs ᴏɴʟʏ:*
    ❍ /enable <ᴄᴍᴅ ɴᴀᴍᴇ>*:* ᴇɴᴀʙʟᴇ ᴛʜᴀᴛ ᴄᴏᴍᴍᴀɴᴅ
    ❍ /disable <ᴄᴍᴅ ɴᴀᴍᴇ>*:* ᴅɪsᴀʙʟᴇ ᴛʜᴀᴛ ᴄᴏᴍᴍᴀɴᴅ
    ❍ /enablemodule <ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ>*:* ᴇɴᴀʙʟᴇ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴀᴛ ᴍᴏᴅᴜʟᴇ
    ❍ /disablemodule <ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ>*:* ᴅɪsᴀʙʟᴇ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴀᴛ ᴍᴏᴅᴜʟᴇ
    ❍ /listcmds*:* ʟɪsᴛ ᴀʟʟ ᴘᴏssɪʙʟᴇ ᴛᴏɢɢʟᴇᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs
    """
    APR_TXT = """
Sᴏᴍᴇᴛɪᴍᴇs, ʏᴏᴜ ᴍɪɢʜᴛ ᴛʀᴜsᴛ ᴀ ᴜsᴇʀ ɴᴏᴛ ᴛᴏ sᴇɴᴅ ᴜɴᴡᴀɴᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ.
Mᴀʏʙᴇ ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇᴍ ᴀᴅᴍɪɴ, ʙᴜᴛ ʏᴏᴜ ᴍɪɢʜᴛ ʙᴇ ᴏᴋ ᴡɪᴛʜ ʟᴏᴄᴋs, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ɴᴏᴛ ᴀᴘᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇᴍ.
Tʜᴀᴛ's ᴡʜᴀᴛ ᴀᴘᴘʀᴏᴠᴀʟs ᴀʀᴇ ғᴏʀ - ᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴛʀᴜsᴛᴡᴏʀᴛʜʏ ᴜsᴇʀs ᴛᴏ ᴀʟʟᴏᴡ ᴛʜᴇᴍ ᴛᴏ sᴇɴᴅ 
*Aᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:*
❍ /approval*:* Cʜᴇᴄᴋ ᴀ ᴜsᴇʀ's ᴀᴘᴘʀᴏᴠᴀʟ sᴛᴀᴛᴜs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.
❍ /approve*:* Aᴘᴘʀᴏᴠᴇ ᴏғ ᴀ ᴜsᴇʀ. Lᴏᴄᴋs, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ᴡᴏɴ'ᴛ ᴀᴘᴘʟʏ ᴛᴏ ᴛʜᴇᴍ ᴀɴʏᴍᴏʀᴇ.
❍ /unapprove*:* Uɴᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴀ ᴜsᴇʀ. Tʜᴇʏ ᴡɪʟʟ ɴᴏᴡ ʙᴇ sᴜʙᴊᴇᴄᴛ ᴛᴏ ʟᴏᴄᴋs, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ᴀɢᴀɪɴ.
❍ /approved*:* Lɪsᴛ ᴀʟʟ ᴀᴘᴘʀᴏᴠᴇᴅ ᴜsᴇʀs.
❍ /unapporveall*:* Uɴᴀᴘᴘʀᴏᴠᴇ *ALL* ᴜsᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ. Tʜɪs ᴄᴀɴɴᴏᴛ ʙᴇ ᴜɴᴅᴏɴᴇ.
"""
    FLOOD_TXT = """
Aɴᴛɪғʟᴏᴏᴅ* ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴛᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏɴ ᴜsᴇʀs ᴛʜᴀᴛ sᴇɴᴅ ᴍᴏʀᴇ ᴛʜᴀɴ x ᴍᴇssᴀɢᴇs ɪɴ ᴀ ʀᴏᴡ. Exᴄᴇᴇᴅɪɴɢ ᴛʜᴇ sᴇᴛ ғʟᴏᴏᴅ \
ᴡɪʟʟ ʀᴇsᴜʟᴛ ɪɴ ʀᴇsᴛʀɪᴄᴛɪɴɢ ᴛʜᴀᴛ ᴜsᴇʀ.
 Tʜɪs ᴡɪʟʟ ᴍᴜᴛᴇ ᴜsᴇʀs ɪғ ᴛʜᴇʏ sᴇɴᴅ ᴍᴏʀᴇ ᴛʜᴀɴ 10 ᴍᴇssᴀɢᴇs ɪɴ ᴀ ʀᴏᴡ, ʙᴏᴛs ᴀʀᴇ ɪɢɴᴏʀᴇᴅ.
 ❍ /flood*:* Gᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ғʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ sᴇᴛᴛɪɴɢ
• *Aᴅᴍɪɴs ᴏɴʟʏ:*
 ❍ /setflood <ɪɴᴛ/'ɴᴏ'/'ᴏғғ'>*:* ᴇɴᴀʙʟᴇs ᴏʀ ᴅɪsᴀʙʟᴇs ғʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ
 *Exᴀᴍᴘʟᴇ:* `/setflood 10`
 ❍ /setfloodmode <ʙᴀɴ/ᴋɪᴄᴋ/ᴍᴜᴛᴇ/ᴛʙᴀɴ/ᴛᴍᴜᴛᴇ> <ᴠᴀʟᴜᴇ>*:* Aᴄᴛɪᴏɴ ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴡʜᴇɴ ᴜsᴇʀ ʜᴀᴠᴇ ᴇxᴄᴇᴇᴅᴇᴅ ғʟᴏᴏᴅ ʟɪᴍɪᴛ. ʙᴀɴ/ᴋɪᴄᴋ/ᴍᴜᴛᴇ/ᴛᴍᴜᴛᴇ/ᴛʙᴀɴ
• *Nᴏᴛᴇ:*
 • Vᴀʟᴜᴇ ᴍᴜsᴛ ʙᴇ ғɪʟʟᴇᴅ ғᴏʀ ᴛʙᴀɴ ᴀɴᴅ ᴛᴍᴜᴛᴇ!!
 Iᴛ ᴄᴀɴ ʙᴇ:
 `5ᴍ` = 5 ᴍɪɴᴜᴛᴇs
 `6ʜ` = 6 ʜᴏᴜʀs
 `3ᴅ` = 3 ᴅᴀʏs
 `1ᴡ` = 1 ᴡᴇᴇᴋ
 """

    AD_TXT = """
 ❍ /admins*:* ʟɪsᴛ ᴏғ ᴀᴅᴍɪɴs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ
*Aᴅᴍɪɴs ᴏɴʟʏ:*
 ❍ /pin*:* sɪʟᴇɴᴛʟʏ ᴘɪɴs ᴛʜᴇ ᴍᴇssᴀɢᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ - ᴀᴅᴅ `'ʟᴏᴜᴅ'` ᴏʀ `'ɴᴏᴛɪғʏ'` ᴛᴏ ɢɪᴠᴇ ɴᴏᴛɪғs ᴛᴏ ᴜsᴇʀs
 ❍ /unpin*:* ᴜɴᴘɪɴs ᴛʜᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ
 ❍ /invitelink*:* ɢᴇᴛs ɪɴᴠɪᴛᴇʟɪɴᴋ
 ❍ /promote*:* ᴘʀᴏᴍᴏᴛᴇs ᴛʜᴇ ᴜsᴇʀ
 ❍ /demote*:* ᴅᴇᴍᴏᴛᴇs ᴛʜᴇ ᴜsᴇʀ
 ❍ /title <ᴛɪᴛʟᴇ ʜᴇʀᴇ>*:* sᴇᴛs ᴀ ᴄᴜsᴛᴏᴍ ᴛɪᴛʟᴇ ғᴏʀ ᴀɴ ᴀᴅᴍɪɴ ᴛʜᴀᴛ ᴛʜᴇ ʙᴏᴛ ᴘʀᴏᴍᴏᴛᴇᴅ
 ❍ /adminlist*:* ғᴏʀᴄᴇ ʀᴇғʀᴇsʜ ᴛʜᴇ ᴀᴅᴍɪɴs ʟɪsᴛ
 ❍ /antispam <ᴏɴ/ᴏғғ/ʏᴇs/ɴᴏ>*:* Wɪʟʟ ᴛᴏɢɢʟᴇ ᴏᴜʀ ᴀɴᴛɪsᴘᴀᴍ ᴛᴇᴄʜ ᴏʀ ʀᴇᴛᴜʀɴ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs."""
    GTH_TXT = """
 I ᴡɪʟʟ ɢɪᴠᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ɢɪᴛʜᴜʙ ᴘʀᴏғɪʟᴇ
 ❍ /github <ᴜsᴇʀɴᴀᴍᴇ>*:* ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ɢɪᴛʜᴜʙ ᴜsᴇʀ.
"""
    FSUB_TXT = """
*Force Subscribe:*
❍ Athena can mute members who are not subscribed your channel until they subscribe
❍ When enabled I will mute unsubscribed members and show them a unmute button. When they pressed the button I will unmute them
*Setup*
*Only creator*
❍ Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ
❍ Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ 
*Commmands*
 ❍ /fsub {ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ} - Tᴏ ᴛᴜʀɴ ᴏɴ ᴀɴᴅ sᴇᴛᴜᴘ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.
  💡Dᴏ ᴛʜɪs ғɪʀsᴛ...
 ❍ /fsub- Tᴏ ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴇᴛᴛɪɴɢs.
 ❍ /fsubdisable - Tᴏ ᴛᴜʀɴ ᴏғ FᴏʀᴄᴇSᴜʙsᴄʀɪʙᴇ..
  💡Iғ ʏᴏᴜ ᴅɪsᴀʙʟᴇ ғsᴜʙ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ sᴇᴛ ᴀɢᴀɪɴ ғᴏʀ ᴡᴏʀᴋɪɴɢ.. /ғsᴜʙ {ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ} 
 ❍ /fsubclear - Tᴏ ᴜɴᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴍᴜᴛᴇᴅ ʙʏ ᴍᴇ.
""" 
    SPTP_TXT = """
I ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ ᴀɴᴅ ᴠᴏɪᴄᴇ ᴛᴏ ᴛᴇxᴛ..
 ❍ /tts <ʟᴀɴɢ ᴄᴏᴅᴇ>*:* Rᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇᴛ ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ ᴏᴜᴛᴘᴜᴛ
 ❍ /stt*:* Tʏᴘᴇ ɪɴ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠᴏɪᴄᴇ ᴍᴇssᴀɢᴇ(sᴜᴘᴘᴏʀᴛ ᴇɴɢʟɪsʜ ᴏɴʟʏ) ᴛᴏ ᴇxᴛʀᴀᴄᴛ ᴛᴇxᴛ ғʀᴏᴍ ɪᴛ.
*Language Codes*
`af,am,ar,az,be,bg,bn,bs,ca,ceb,co,cs,cy,da,de,el,en,eo,es,
et,eu,fa,fi,fr,fy,ga,gd,gl,gu,ha,haw,hi,hmn,hr,ht,hu,hy,
id,ig,is,it,iw,ja,jw,ka,kk,km,kn,ko,ku,ky,la,lb,lo,lt,lv,mg,mi,mk,
ml,mn,mr,ms,mt,my,ne,nl,no,ny,pa,pl,ps,pt,ro,ru,sd,si,sk,sl,
sm,sn,so,sq,sr,st,su,sv,sw,ta,te,tg,th,tl,tr,uk,ur,uz,
vi,xh,yi,yo,zh,zh_CN,zh_TW,zu`
"""
    NSFW_TXT = """
ᴄᴀɴ ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ғʀᴏᴍ NSFW sᴇɴᴅᴇʀs
 ❍ /addnsfw*:* Aᴅᴅs Tʜᴇ Gʀᴏᴜᴘ ᴛᴏ ɴsғᴡ Wᴀᴛᴄʜ Lɪsᴛ
 ❍ /rmnsfw*:* Rᴇᴍᴏᴠᴇs Tʜᴇ Gʀᴏᴜᴘ Fʀᴏᴍ ɴsғᴡ Wᴀᴛᴄʜ Lɪsᴛ"""

    ENG_TXT = """
❍ /define <text>*:* Tʏᴘᴇ ᴛʜᴇ ᴡᴏʀᴅ ᴏʀ ᴇxᴘʀᴇssɪᴏɴ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ\ɴFᴏʀ ᴇxᴀᴍᴘʟᴇ /define ᴋɪʟʟ
 ❍ /spell*:* ᴡʜɪʟᴇ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ, ᴡɪʟʟ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀ ɢʀᴀᴍᴍᴀʀ ᴄᴏʀʀᴇᴄᴛᴇᴅ ᴠᴇʀsɪᴏɴ
 ❍ /synonyms <word>*:* Fɪɴᴅ ᴛʜᴇ sʏɴᴏɴʏᴍs ᴏғ ᴀ ᴡᴏʀᴅ
 ❍ /antonyms <word>*:* Fɪɴᴅ ᴛʜᴇ ᴀɴᴛᴏɴʏᴍs ᴏғ ᴀ ᴡᴏʀᴅ
"""
    GOG_TXT = """
 ❍ /google <text>*:* Pᴇʀғᴏʀᴍ ᴀ ɢᴏᴏɢʟᴇ sᴇᴀʀᴄʜ
 ❍ /img <text>*:* Sᴇᴀʀᴄʜ Gᴏᴏɢʟᴇ ғᴏʀ ɪᴍᴀɢᴇs ᴀɴᴅ ʀᴇᴛᴜʀɴs ᴛʜᴇᴍ\ɴFᴏʀ ɢʀᴇᴀᴛᴇʀ ɴᴏ. ᴏғ ʀᴇsᴜʟᴛs sᴘᴇᴄɪғʏ ʟɪᴍ, Fᴏʀ ᴇɢ: `/ɪᴍɢ ʜᴇʟʟᴏ ʟɪᴍ=10`
 ❍ /app <appname>*:* Sᴇᴀʀᴄʜᴇs ғᴏʀ ᴀɴ ᴀᴘᴘ ɪɴ Pʟᴀʏ Sᴛᴏʀᴇ ᴀɴᴅ ʀᴇᴛᴜʀɴs ɪᴛs ᴅᴇᴛᴀɪʟs.
 ❍ /reverse: Dᴏᴇs ᴀ ʀᴇᴠᴇʀsᴇ ɪᴍᴀɢᴇ sᴇᴀʀᴄʜ ᴏғ ᴛʜᴇ ᴍᴇᴅɪᴀ ᴡʜɪᴄʜ ɪᴛ ᴡᴀs ʀᴇᴘʟɪᴇᴅ ᴛᴏ.
  💡Ex: `where is distance Chennai to tirupathi?`
"""
    COV_TXT = """
ʜᴇʟᴘ
🦠ᴡᴇ ᴄᴀɴ sᴇᴇ ᴄᴏᴠɪᴅ-19 ᴄᴀsᴇs ᴀɴᴅ ᴇxᴛ...

         /Covid - ᴛᴏ sᴇᴇ ᴛʜᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ

ᴇxᴀᴍᴘʟᴇ
/covid ᴄʜɪɴᴀ
"""
    NEST_TXT = """
♬ 3Ʀᖱ ៣០ᖱ៩ɭ៩ន"""      
    RULES_TXT = """
❍ /rules*:* ɢᴇᴛ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.
*Aᴅᴍɪɴs ᴏɴʟʏ:*
 ❍ /setrules <ʏᴏᴜʀ ʀᴜʟᴇs ʜᴇʀᴇ>*:* sᴇᴛ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.
 ❍ /clearrules*:* ᴄʟᴇᴀʀ ᴛʜᴇ ʀᴜʟᴇs ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.
"""
    REACT_TXT = """
❍ /react*:* Rᴇᴀᴄᴛs ᴡɪᴛʜ ᴀ ʀᴀɴᴅᴏᴍ ʀᴇᴀᴄᴛɪᴏɴ 
"""
    MARK_TXT = """
    ❍ /markdownhelp*:* ϙᴜɪᴄᴋ sᴜᴍᴍᴀʀʏ ᴏғ ʜᴏᴡ ᴍᴀʀᴋᴅᴏᴡɴ ᴡᴏʀᴋs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ - ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴄᴀʟʟᴇᴅ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs
*Pᴀsᴛᴇ:*
"""
    WIKI_TXT = """
❍ /ud <ᴡᴏʀᴅ>*:* Tʏᴘᴇ ᴛʜᴇ ᴡᴏʀᴅ ᴏʀ ᴇxᴘʀᴇssɪᴏɴ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ ᴜsᴇ
*Wɪᴋɪᴘᴇᴅɪᴀ:*
 ❍ /wiki <ϙᴜᴇʀʏ>*:* ᴡɪᴋɪᴘᴇᴅɪᴀ ʏᴏᴜʀ ϙᴜᴇʀʏ
*Wᴀʟʟᴘᴀᴘᴇʀs:*
"""
    WALL_TXT = """
❍ /wall <ϙᴜᴇʀʏ>*:* ɢᴇᴛ ᴀ ᴡᴀʟʟᴘᴀᴘᴇʀ ғʀᴏᴍ ᴡᴀʟʟ.ᴀʟᴘʜᴀᴄᴏᴅᴇʀs.ᴄᴏᴍ
*Cᴜʀʀᴇɴᴄʏ ᴄᴏɴᴠᴇʀᴛᴇʀ:* 
"""
    LIST_TXT = """
Lɪsᴛ ᴀʟʟ sᴘᴇᴄɪᴀʟ ᴜsᴇʀs:*
 ❍ /dragons*:* Lɪsᴛs ᴀʟʟ Dʀᴀɢᴏɴ ᴅɪsᴀsᴛᴇʀs
 ❍ /demons*:* Lɪsᴛs ᴀʟʟ Dᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀs
 ❍ /tigers*:* Lɪsᴛs ᴀʟʟ Tɪɢᴇʀs ᴅɪsᴀsᴛᴇʀs
 ❍ /wolves*:* Lɪsᴛs ᴀʟʟ Wᴏʟғ ᴅɪsᴀsᴛᴇʀs
 ❍ /heroes*:* Lɪsᴛs ᴀʟʟ Hᴇʀᴏ Assᴏᴄɪᴀᴛɪᴏɴ ᴍᴇᴍʙᴇʀs
 ❍ /adddragon*:* Aᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ Dʀᴀɢᴏɴ
 ❍ /adddemon*:* Aᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ Dᴇᴍᴏɴ
 ❍ /addtiger*:* Aᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ Tɪɢᴇʀ
 ❍ /addwolf*:* Aᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ Wᴏʟғ
 ❍ `Aᴅᴅ ᴅᴇᴠ ᴅᴏᴇsɴᴛ ᴇxɪsᴛ, ᴅᴇᴠs sʜᴏᴜʟᴅ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍsᴇʟᴠᴇs`
"""
    PING_TXT = """
*Pɪɴɢ:*
 ❍ /ping*:* ɢᴇᴛs ᴘɪɴɢ ᴛɪᴍᴇ ᴏғ ʙᴏᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ sᴇʀᴠᴇʀ
 ❍ /pingall*:* ɢᴇᴛs ᴀʟʟ ʟɪsᴛᴇᴅ ᴘɪɴɢ ᴛɪᴍᴇs
"""
    GRPINFO_TXT = """
*Gʀᴏᴜᴘs Iɴғᴏ:*
 ❍ /groups*:* Lɪsᴛ ᴛʜᴇ ɢʀᴏᴜᴘs ᴡɪᴛʜ Nᴀᴍᴇ, ID, ᴍᴇᴍʙᴇʀs ᴄᴏᴜɴᴛ ᴀs ᴀ ᴛxᴛ
 ❍ /leave <ID>*:* Lᴇᴀᴠᴇ ᴛʜᴇ ɢʀᴏᴜᴘ, ID ᴍᴜsᴛ ʜᴀᴠᴇ ʜʏᴘʜᴇɴ
 ❍ /stats*:* Sʜᴏᴡs ᴏᴠᴇʀᴀʟʟ ʙᴏᴛ sᴛᴀᴛs
 ❍ /getchats*:* Gᴇᴛs ᴀ ʟɪsᴛ ᴏғ ɢʀᴏᴜᴘ ɴᴀᴍᴇs ᴛʜᴇ ᴜsᴇʀ ʜᴀs ʙᴇᴇɴ sᴇᴇɴ ɪɴ. Bᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ
 ❍ /ginfo ᴜsᴇʀɴᴀᴍᴇ/ʟɪɴᴋ/ID*:* Pᴜʟʟs ɪɴғᴏ ᴘᴀɴᴇʟ ғᴏʀ ᴇɴᴛɪʀᴇ ɢʀᴏᴜᴘ"""

    CONTROL_TXT = """
*Aᴄᴄᴇss ᴄᴏɴᴛʀᴏʟ:* 
 ❍ /ignore*:* Bʟᴀᴄᴋʟɪsᴛs ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ ᴇɴᴛɪʀᴇʟʏ
 ❍ /lockdown <ᴏғғ/ᴏɴ>*:* Tᴏɢɢʟᴇs ʙᴏᴛ ᴀᴅᴅɪɴɢ ᴛᴏ ɢʀᴏᴜᴘs
 ❍ /notice*:* Rᴇᴍᴏᴠᴇs ᴜsᴇʀ ғʀᴏᴍ ʙʟᴀᴄᴋʟɪsᴛ
 ❍ /ignoredlist*:* Lɪsᴛs ɪɢɴᴏʀᴇᴅ ᴜsᴇʀ
"""
    SPEED_TXT = """
*Sᴘᴇᴇᴅᴛᴇsᴛ:*
 ❍ /speedtest*:* Rᴜɴs ᴀ sᴘᴇᴇᴅᴛᴇsᴛ ᴀɴᴅ ɢɪᴠᴇs ʏᴏᴜ 2 ᴏᴘᴛɪᴏɴs ᴛᴏ ᴄʜᴏᴏsᴇ ғʀᴏᴍ, ᴛᴇxᴛ ᴏʀ ɪᴍᴀɢᴇ ᴏᴜᴛᴘᴜᴛ
"""
    REMOTE_TXT = """

*Rᴇᴍᴏᴛᴇ ᴄᴏᴍᴍᴀɴᴅs:*
 ❍ /rban*:* ᴜsᴇʀ ɢʀᴏᴜᴘ*:* Rᴇᴍᴏᴛᴇ ʙᴀɴ
 ❍ /runban*:* ᴜsᴇʀ ɢʀᴏᴜᴘ*:* Rᴇᴍᴏᴛᴇ ᴜɴ-ʙᴀɴ
 ❍ /rpunch*:* ᴜsᴇʀ ɢʀᴏᴜᴘ*:* Rᴇᴍᴏᴛᴇ ᴘᴜɴᴄʜ
 ❍ /rmute*:* ᴜsᴇʀ ɢʀᴏᴜᴘ*:* Rᴇᴍᴏᴛᴇ ᴍᴜᴛᴇ
 ❍ /runmute*:* ᴜsᴇʀ ɢʀᴏᴜᴘ*:* Rᴇᴍᴏᴛᴇ ᴜɴ-ᴍᴜᴛᴇ
"""
    GBAN_TXT = """
*Gʟᴏʙᴀʟ Bᴀɴs:*
 ❍ /gban<ɪᴅ> <ʀᴇᴀsᴏɴ>*:* Gʙᴀɴs ᴛʜᴇ ᴜsᴇʀ, ᴡᴏʀᴋs ʙʏ ʀᴇᴘʟʏ ᴛᴏᴏ
 ❍ /ungban*:* Uɴɢʙᴀɴs ᴛʜᴇ ᴜsᴇʀ, sᴀᴍᴇ ᴜsᴀɢᴇ ᴀs ɢʙᴀɴ
 ❍ /gbanlist*:* Oᴜᴛᴘᴜᴛs ᴀ ʟɪsᴛ ᴏғ ɢʙᴀɴɴᴇᴅ ᴜsᴇʀs
"""
    GBLUE_TXT = """
*Gʟᴏʙᴀʟ Bʟᴜᴇ Tᴇxᴛ*
 ❍ /gignoreblue*:* <ᴡᴏʀᴅ>*:* Gʟᴏʙᴀʟʟʏ ɪɢɴᴏʀᴇᴀ ʙʟᴜᴇᴛᴇxᴛ ᴄʟᴇᴀɴɪɴɢ ᴏғ sᴀᴠᴇᴅ ᴡᴏʀᴅ ᴀᴄʀᴏss MᴀsʜᴀRᴏBᴏᴛ.
 ❍ /ungignoreblue*:* <ᴡᴏʀᴅ>*:* Rᴇᴍᴏᴠᴇ sᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғʀᴏᴍ ɢʟᴏʙᴀʟ ᴄʟᴇᴀɴɪɴɢ ʟɪsᴛ
"""
    
    MATHS_TXT = """
*MATHS*
Sᴏʟᴠᴇs ᴄᴏᴍᴘʟᴇx ᴍᴀᴛʜ ᴘʀᴏʙʟᴇᴍs ᴜsɪɴɢ ʜᴛᴛᴘs://ɴᴇᴡᴛᴏɴ.ɴᴏᴡ.sʜ
❍ /math*:* Mᴀᴛʜ `/math 2^2+2(2)`
❍ /factor*:* Fᴀᴄᴛᴏʀ `/factor x^2 + 2x`
❍ /derive*:* Dᴇʀɪᴠᴇ `/derive x^2+2x`
❍ /integrate*:* Iɴᴛᴇɢʀᴀᴛᴇ `/integrate x^2+2x`
❍ /zeroes*:* Fɪɴᴅ 0's `/zeroes x^2+2x`
❍ /tangent*:* Fɪɴᴅ Tᴀɴɢᴇɴᴛ `/tangent 2ʟx^3`
❍ /area*:* Aʀᴇᴀ Uɴᴅᴇʀ Cᴜʀᴠᴇ `/area 2:4ʟx^3`
❍ /cos*:* Cᴏsɪɴᴇ `/cos ᴘɪ`
❍ /sin*:* Sɪɴᴇ `/sin 0`
❍ /tam*:* Tᴀɴɢᴇɴᴛ `/tan 0`
❍ /arccos*:* Iɴᴠᴇʀsᴇ Cᴏsɪɴᴇ `/arccos 1`
❍ /arcsin*:* Iɴᴠᴇʀsᴇ Sɪɴᴇ `/arcsin 0`
❍ /arctan*:* Iɴᴠᴇʀsᴇ Tᴀɴɢᴇɴᴛ `/arctan 0`
❍ /Abs*:* Aʙsᴏʟᴜᴛᴇ Vᴀʟᴜᴇ `/abs -1`
❍ /log*:* Lᴏɢᴀʀɪᴛʜᴍ `/log 2ʟ8`
_Kᴇᴇᴘ ɪɴ ᴍɪɴᴅ_: Tᴏ ғɪɴᴅ ᴛʜᴇ ᴛᴀɴɢᴇɴᴛ ʟɪɴᴇ ᴏғ ᴀ ғᴜɴᴄᴛɪᴏɴ ᴀᴛ ᴀ ᴄᴇʀᴛᴀɪɴ x ᴠᴀʟᴜᴇ, sᴇɴᴅ ᴛʜᴇ ʀᴇϙᴜᴇsᴛ ᴀs ᴄ|ғ(x) ᴡʜᴇʀᴇ ᴄ ɪs ᴛʜᴇ ɢɪᴠᴇɴ x ᴠᴀʟᴜᴇ ᴀɴᴅ ғ(x) ɪs ᴛʜᴇ ғᴜɴᴄᴛɪᴏɴ ᴇxᴘʀᴇssɪᴏɴ, ᴛʜᴇ sᴇᴘᴀʀᴀᴛᴏʀ ɪs ᴀ ᴠᴇʀᴛɪᴄᴀʟ ʙᴀʀ '|'. Sᴇᴇ ᴛʜᴇ ᴛᴀʙʟᴇ ᴀʙᴏᴠᴇ ғᴏʀ ᴀɴ ᴇxᴀᴍᴘʟᴇ ʀᴇϙᴜᴇsᴛ.
Tᴏ ғɪɴᴅ ᴛʜᴇ ᴀʀᴇᴀ ᴜɴᴅᴇʀ ᴀ ғᴜɴᴄᴛɪᴏɴ, sᴇɴᴅ ᴛʜᴇ ʀᴇϙᴜᴇsᴛ ᴀs ᴄ:ᴅ|ғ(x) ᴡʜᴇʀᴇ ᴄ ɪs ᴛʜᴇ sᴛᴀʀᴛɪɴɢ x ᴠᴀʟᴜᴇ, ᴅ ɪs ᴛʜᴇ ᴇɴᴅɪɴɢ x ᴠᴀʟᴜᴇ, ᴀɴᴅ ғ(x) ɪs ᴛʜᴇ ғᴜɴᴄᴛɪᴏɴ ᴜɴᴅᴇʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛʜᴇ ᴄᴜʀᴠᴇ ʙᴇᴛᴡᴇᴇɴ ᴛʜᴇ ᴛᴡᴏ x ᴠᴀʟᴜᴇs.
Tᴏ ᴄᴏᴍᴘᴜᴛᴇ ғʀᴀᴄᴛɪᴏɴs, ᴇɴᴛᴇʀ ᴇxᴘʀᴇssɪᴏɴs ᴀs ɴᴜᴍᴇʀᴀᴛᴏʀ(ᴏᴠᴇʀ)ᴅᴇɴᴏᴍɪɴᴀᴛᴏʀ. Fᴏʀ ᴇxᴀᴍᴘʟᴇ, ᴛᴏ ᴘʀᴏᴄᴇss 2/4 ʏᴏᴜ ᴍᴜsᴛ sᴇɴᴅ ɪɴ ʏᴏᴜʀ ᴇxᴘʀᴇssɪᴏɴ ᴀs 2(ᴏᴠᴇʀ)4. Tʜᴇ ʀᴇsᴜʟᴛ ᴇxᴘʀᴇssɪᴏɴ ᴡɪʟʟ ʙᴇ ɪɴ sᴛᴀɴᴅᴀʀᴅ ᴍᴀᴛʜ ɴᴏᴛᴀᴛɪᴏɴ (1/2, 3/4).
"""
    ANIME_TXT = """
Gᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀɴɪᴍᴇ, ᴍᴀɴɢᴀ ᴏʀ ᴄʜᴀʀᴀᴄᴛᴇʀs ғʀᴏᴍ [AɴɪLɪsᴛ](ᴀɴɪʟɪsᴛ.ᴄᴏ).
*Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:*
 ❍ /anime <ᴀɴɪᴍᴇ>*:* ʀᴇᴛᴜʀɴs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜᴇ ᴀɴɪᴍᴇ.
 ❍ /character <ᴄʜᴀʀᴀᴄᴛᴇʀ>*:* ʀᴇᴛᴜʀɴs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ.
 ❍ /manga <ᴍᴀɴɢᴀ>*:* ʀᴇᴛᴜʀɴs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜᴇ ᴍᴀɴɢᴀ.
 ❍ /user <ᴜsᴇʀ>*:* ʀᴇᴛᴜʀɴs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ MʏAɴɪᴍᴇLɪsᴛ ᴜsᴇʀ.
 ❍ /upcoming*:* ʀᴇᴛᴜʀɴs ᴀ ʟɪsᴛ ᴏғ ɴᴇᴡ ᴀɴɪᴍᴇ ɪɴ ᴛʜᴇ ᴜᴘᴄᴏᴍɪɴɢ sᴇᴀsᴏɴs.
 ❍ /kaizoku <ᴀɴɪᴍᴇ>*:* sᴇᴀʀᴄʜ ᴀɴ ᴀɴɪᴍᴇ ᴏɴ ᴀɴɪᴍᴇᴋᴀɪᴢᴏᴋᴜ.ᴄᴏᴍ
 ❍ /kayo <ᴀɴɪᴍᴇ>*:* sᴇᴀʀᴄʜ ᴀɴ ᴀɴɪᴍᴇ ᴏɴ ᴀɴɪᴍᴇᴋᴀʏᴏ.ᴄᴏᴍ
 ❍ /airing <ᴀɴɪᴍᴇ>*:* ʀᴇᴛᴜʀɴs ᴀɴɪᴍᴇ ᴀɪʀɪɴɢ ɪɴғᴏ.
"""
    SKYLER_TXT = """

⚙️ <b>Hᴇʟᴘ Cᴏᴍᴍᴀɴᴅs</b>:
❍ /q -Rᴇᴘʟʏ Tᴏ A Mᴇssᴀɢᴇ Tᴏ Tᴇsᴛ Mᴀᴋᴇ Tᴏ Sᴛɪᴄᴋᴇʀ
"""
    BACKUP_TXT = """
*Oɴʟʏ ғᴏʀ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ:*
 ❍ /import: Rᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ʙᴀᴄᴋᴜᴘ ғɪʟᴇ ғᴏʀ ᴛʜᴇ ʙᴜᴛʟᴇʀ / ᴇᴍɪʟɪᴀ ɢʀᴏᴜᴘ ᴛᴏ ɪᴍᴘᴏʀᴛ ᴀs ᴍᴜᴄʜ ᴀs ᴘᴏssɪʙʟᴇ, ᴍᴀᴋɪɴɢ ᴛʀᴀɴsғᴇʀs ᴠᴇʀʏ ᴇᴀsʏ! \
 Nᴏᴛᴇ ᴛʜᴀᴛ ғɪʟᴇs / ᴘʜᴏᴛᴏs ᴄᴀɴɴᴏᴛ ʙᴇ ɪᴍᴘᴏʀᴛᴇᴅ ᴅᴜᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
 ❍ /export: Exᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴅᴀᴛᴀ, ᴡʜɪᴄʜ ᴡɪʟʟ ʙᴇ ᴇxᴘᴏʀᴛᴇᴅ ᴀʀᴇ: ʀᴜʟᴇs, ɴᴏᴛᴇs (ᴅᴏᴄᴜᴍᴇɴᴛs, ɪᴍᴀɢᴇs, ᴍᴜsɪᴄ, ᴠɪᴅᴇᴏ, ᴀᴜᴅɪᴏ, ᴠᴏɪᴄᴇ, ᴛᴇxᴛ, ᴛᴇxᴛ ʙᴜᴛᴛᴏɴs) \
"""
    NEWDATA_TXT = """Here he is the help of 2nd module"""
    UNK_TXT = """
Aᴅᴍɪɴs ᴏɴʟʏ:*
 ❍ /mute<ᴜsᴇʀʜᴀɴᴅʟᴇ>*:* sɪʟᴇɴᴄᴇs ᴀ ᴜsᴇʀ. Cᴀɴ ᴀʟsᴏ ʙᴇ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ, ᴍᴜᴛɪɴɢ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴜsᴇʀ.
 ❍ /tmute <ᴜsᴇʀʜᴀɴᴅʟᴇ> x(ᴍ/ʜ/ᴅ)*:* ᴍᴜᴛᴇs ᴀ ᴜsᴇʀ ғᴏʀ x ᴛɪᴍᴇ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ). `ᴍ` = `ᴍɪɴᴜᴛᴇs`, `ʜ` = `ʜᴏᴜʀs`, `ᴅ` = `ᴅᴀʏs`.
 ❍ /unmute <ᴜsᴇʀʜᴀɴᴅʟᴇ>*:* ᴜɴᴍᴜᴛᴇs ᴀ ᴜsᴇʀ. Cᴀɴ ᴀʟsᴏ ʙᴇ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ, ᴍᴜᴛɪɴɢ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴜsᴇʀ.
"""

    GAMES_TXT = """

    ❍ /define <text>*:* Tʏᴘᴇ ᴛʜᴇ ᴡᴏʀᴅ ᴏʀ ᴇxᴘʀᴇssɪᴏɴ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ\ɴFᴏʀ ᴇxᴀᴍᴘʟᴇ /define ᴋɪʟʟ
 ❍ /spell*:* ᴡʜɪʟᴇ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ, ᴡɪʟʟ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀ ɢʀᴀᴍᴍᴀʀ ᴄᴏʀʀᴇᴄᴛᴇᴅ ᴠᴇʀsɪᴏɴ
 ❍ /synonyms <word>*:* Fɪɴᴅ ᴛʜᴇ sʏɴᴏɴʏᴍs ᴏғ ᴀ ᴡᴏʀᴅ
 ❍ /antonyms <word>*:* Fɪɴᴅ ᴛʜᴇ ᴀɴᴛᴏɴʏᴍs ᴏғ ᴀ ᴡᴏʀᴅ
"""

    BUTTON_TXT = """Help: <b>Bᴜᴛᴛᴏɴs</b>

- Mᴋ sᴜᴘᴘᴏʀᴛ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

Nᴏᴛᴇ
Tᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. Mᴋ  sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. Bᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ."""

    AUTOFILTER_TXT = """Help: <b>Aᴜᴛᴏ Fɪʟᴛᴇʀs</b>

<b>NOTE:</b>
1. Mᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
2. Mᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀɴ ᴀɴᴅ ғᴀᴋᴇ ғɪʟᴇs.
3. Fᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ϙᴜᴏᴛᴇs.
 I'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ."""
     
    CONNECTION_TXT = """Help: <b>Cᴏɴɴᴇᴄᴛɪᴏɴ</b>

- Usᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ PM ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀs 
- Iᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘs.

<b>NOTE:</b>
1. Oɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. Sᴇɴᴅ <ᴄᴏᴅᴇ>/ᴄᴏɴɴᴇᴄᴛ</ᴄᴏᴅᴇ> ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ Oᴜʀ Pᴍ.

<b>Commands and Usage:</b>
• /connect  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ PM.
• /disconnect  - ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.
• /connections - ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs."""

    AUTO_MANUAL_TXT = """Help: <b>Fɪʟᴛᴇʀs</b> 


<b>Sᴇʟᴇᴄᴛ ᴀ ғɪʟᴛᴇʀs ᴛʏᴘᴇ Bᴇʟᴏᴡ:</b>"""

    MAGAN_TXT = """
    ❍ /nightmode on/off
 
**Note:** Nɪɢʜᴛ Mᴏᴅᴇ ᴄʜᴀᴛs ɢᴇᴛ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄʟᴏsᴇᴅ ᴀᴛ 12ᴘᴍ(IST)
ᴀɴᴅ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴏᴘᴇɴɴᴇᴅ ᴀᴛ 6ᴀᴍ(IST) Tᴏ Pʀᴇᴠᴇɴᴛ Nɪɢʜᴛ Sᴘᴀᴍs.
"""

    PASTE_TXT = """Help: <b>Pᴀsᴛᴇ</b>

Pᴀsᴛᴇ sᴏᴍᴇ ᴛᴇxᴛs ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛs ᴏɴ ᴀ ᴡᴇʙsɪᴛᴇ!

<b>Commands and Usage:</b>
• /paste [text] - ᴘᴀsᴛᴇ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ Pᴀsᴛʏ
• /paste [reply] - ᴘᴀsᴛᴇ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴇxᴛ ᴏɴ Pᴀsᴛʏ

<b>NOTE:</b>
• Cʀᴀᴄᴋᴇʀ  sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""

    TGRAPH_TXT = """Help: <b>Tɢʀᴀᴘʜ + Pᴀsᴛᴇ</b>

Dᴏ ᴀs ʏᴏᴜ ᴡɪsʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀ.ᴘʜ ᴍᴏᴅᴜʟᴇ!

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /tgmedia or /tgraph - ᴜᴘʟᴏᴀᴅ sᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ (ᴡɪᴛʜɪɴ 5MB) ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.


<b>NOTE:</b>
• Cʀᴀᴄᴋᴇʀ  sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""

    INFO_TXT = """Help: <b>Iɴғᴏʀᴍᴀᴛɪᴏɴ</b>

Gᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ sᴏᴍᴇᴛʜɪɴɢ ! 

<b>Commands and Usage:</b>
• /id - ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ᴜsᴇʀ.
• /info  - ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.
• /json - ɢᴇᴛ ᴛʜᴇ ᴊsᴏɴ ᴅᴇᴛᴀɪʟs ᴏғ ᴀ ᴍᴇssᴀɢᴇ.


<b>NOTE:</b>
• Cʀᴀᴄᴋᴇʀ  sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""

    GTRANS_TXT = """Help: <b>Gᴏᴏɢʟᴇ Tʀᴀɴsʟᴀᴛᴏʀ</b>

Tʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛs ᴛᴏ ᴀ sᴘᴇᴄɪғɪᴄ ʟᴀɴɢᴜᴀɢᴇ!

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /tr [language code][reply] - ᴛʀᴀɴsʟᴀᴛᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ᴛᴏ sᴘᴇᴄɪғɪᴄ ʟᴀɴɢᴜᴀɢᴇ.

<b>NOTE:</b>
• Cʀᴀᴄᴋᴇʀ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• ʟɪʟʟʏ ᴄᴀɴ ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛs ᴛᴏ 200+ ʟᴀɴɢᴜᴀɢᴇs."""


    SEARCH_TXT = """Help: <b>Iᴍᴅʙ</b>

Sᴇᴀʀᴄʜ ᴍᴀɴʏ ᴛʜɪɴɢs ᴡɪᴛʜᴏᴜᴛ ʟᴇᴀᴠɪɴɢ ᴛᴇʟᴇɢʀᴀᴍ!

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /imdb  - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ IMDʙ sᴏᴜʀᴄᴇ
• /search  - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴜʀᴄᴇs.


<b>NOTE:</b>
• Cʀᴀᴄᴋᴇʀ  sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Mᴏʀᴇ sᴇᴀʀᴄʜ ᴛᴏᴏʟs ᴄᴀɴ ʙᴇ ғᴏᴜɴᴅ ᴏɴ ɪɴʟɪɴᴇ.
• Tʜᴏsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ."""

    PURGE_TXT = """Help: <b>Pᴜʀɢᴇ</b>

Nᴇᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʟᴏᴛs ᴏғ ᴍᴇssᴀɢᴇs? Tʜᴀᴛ's ᴡʜᴀᴛ ᴘᴜʀɢᴇs ᴀʀᴇ ғᴏʀ!

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /purge - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ  Cᴜʀʀᴇɴᴛ Mᴇssᴀɢᴇ.

<b>NOTE:</b>
• Cʀᴀᴄᴋᴇʀ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ Oɴʟʏ ᴀᴅᴍɪɴ."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
• /ban - ban a user.
• /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /mute - mute a user.
• /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    PIN_MESSAGE_TXT = """Help: <b>Pɪɴ Mᴇssᴀɢᴇ</b>

Aʟʟ ᴛʜᴇ ᴘɪɴ ʀᴇʟᴀᴛᴇᴅ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ғᴏᴜɴᴅ ʜᴇʀᴇ; ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀᴛ ᴜᴘ ᴛᴏ ᴅᴀᴛᴇ ᴏɴ ᴛʜᴇ ʟᴀᴛᴇsᴛ ɴᴇᴡs ᴡɪᴛʜ ᴀ sɪᴍᴘʟᴇ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ!

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /pin:  Pɪɴ ᴛʜᴇ ᴍᴇssᴀɢᴇ ʏᴏᴜ ʀᴇᴘʟɪᴇᴅ ᴛᴏ. Aᴅᴅ 'ʟᴏᴜᴅ' ᴏʀ 'ɴᴏᴛɪғʏ' ᴛᴏ sᴇɴᴅ ᴀ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴛᴏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs.
• /unpin: Uɴᴘɪɴ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ. Iғ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ, ᴜɴᴘɪɴs ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ.


<b>NOTE:</b>
• IMDʙ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴʟʏ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ Oɴʟʏ ᴀᴅᴍɪɴ."""

    ADMIN_TXT = """Help: <b>Aᴅᴍɪɴ Mᴏᴅs</b>

<b>NOTE:</b>
Tʜɪs ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋs ғᴏʀ ᴍʏ ᴀᴅᴍɪɴs

<b>Commands and Usage:</b>
• /logs - to get the rescent errors.
• /stats - to get status of files in db.
• /delete - to delete a specific file from db.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids.
• /leave - to leave from a chat.
• /disable - do disable a chat.
• /ban_users - to ban a user.
• /unban_users - to unban a user.
• /channel - to get list of total connected channels.
• /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """ ★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>

★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>

★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>

★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱

★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
  """

    FORCESUB_TXT = """**♦️ READ THIS INSTRUCTION ♦️**

__🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately 🙈__

**👇 JOIN THIS CHANNEL & TRY AGAIN 👇**"""

    MEMES_TXT = """Help: 
ʜᴇʀᴇ sᴏᴍᴇ ғᴜɴs ᴀʀᴇ ᴛʜᴇʀᴇ ᴛʀʏ ᴏᴜᴛ ɴᴏᴡ

<b>ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜsᴀɢᴇ:</b>
• /throw or /dart - ᴛ𝗈 ᴍ𝖺𝗄𝖾 ᴅʀᴀᴛ 
• /roll or /dice -  ʀᴏʟʟ ᴛʜᴇ ᴅɪᴄᴇ
• /goal or /shoot - ᴛᴏ ᴍᴀᴋᴇ ᴀ ɢᴏᴀʟ ᴏʀ sʜᴏᴏᴛ
• /luck or /cownd - sᴘɪɴ ᴛʜᴇ ʟᴜᴄᴋʏ
• /runs sᴛʀɪɴɢs

<b>NOTE:</b>
• IMDʙ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""

    URL_SHORTNER_TXT = """Help: <b>Uʀʟ Sʜᴏʀᴛɴᴇʀ</b>

Sᴏᴍᴇ URLs ɪs Sʜᴏʀᴛɴᴇʀ

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /short <code>(link)</code> - I ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ sʜᴏʀᴛᴇᴅ ʟɪɴᴋs.

<b>Example:</b>
<code>/short https://t.me/mksupport1</code>

<b>NOTE:</b>
• Cʀᴀᴄᴋᴇʀ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""

    TTS_TXT = """Help: <b>Tᴇxᴛ Tᴏ sᴘᴇᴇᴄʜ</b>

ᴀ ᴍᴏᴅᴜʟᴇ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ ᴡɪᴛʜ ʟᴀɴɢᴜᴀɢᴇ sᴜᴘᴘᴏʀᴛ.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢe:</b>
• /tts - Rᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴀs ᴀᴜᴅɪᴏ.

<b>NOTE:</b>
• Cʀᴀᴄᴋᴇʀ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""


    MUSIC_TXT = """Help: <b>Mᴜsɪᴄ</b>

Mᴜsɪᴄ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇs, ғᴏʀ ᴛʜᴏsᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴍᴜsɪᴄ.

<b>Commands and Usage:</b>
• /song or /mp3 (songname) - ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴛ sᴇʀᴠᴇʀs.
• /video or /mp4 (songname) - ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴛ sᴇʀᴠᴇʀs.

<b>YouTube Thumbnail Download</b>
• /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/h6PtzFYaMxQ</code>

<b>Iғ Cᴀɴ Pʟᴀʏ Tʜᴇ Sᴏɴɢ Oɴ Vɪᴅᴇᴏ Cʜᴀᴛ Oɴ Gʀᴏᴜᴘ</b>
🎶Oʜ -Yᴇs Aᴠᴀɪʟᴀʙʟᴇ Yᴏᴜ Mᴜsᴛ Aᴅᴅ Aᴅᴍɪɴ Mʏ Assɪsᴛᴀɴᴛ:@SingerChat]
🎶/Play - Tᴏ Pʟᴀʏ Tʜᴇ Sᴏɴɢ
🎶/vplay-Tᴏ Pʟᴀʏ Tʜᴇ Vɪᴅᴇᴏ Sᴏɴɢ
🎶/Playlist- ᴛᴏ Sᴇᴇ Wʜᴀᴛ Sᴏɴɢ Tʜᴇʀᴇ
🎶ʜᴏᴡ ᴛᴏ ᴘʟᴀʏ ᴛʜᴇ sᴏɴɢ
🎶/ᴘʟᴀʏ [sᴏɴɢ ɴᴀᴍᴇ]
🎶/ᴠᴘʟᴀʏ [sᴏɴɢ ɴᴇᴍᴇ]
ᴇx:
/ᴘʟᴀʏ ʀᴀᴋɪᴛᴀ ʀᴀᴋɪᴛᴀ

<b>NOTE:</b>
•Cʀᴀᴄᴋᴇʀ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

Tʜᴇʀᴇ Is Nᴏᴛʜɪɴɢ Tᴏ Kɴᴏᴡ Mᴏʀᴇ. Sᴇɴᴅ Mᴇ Tʜᴇ Lɪᴍɪᴛ Oғ Yᴏᴜʀ Pᴀssᴡᴏʀᴅ.
- I Wɪʟʟ Gɪᴠᴇ Tʜᴇ Pᴀssᴡᴏʀᴅ Oғ Tʜᴀᴛ Lɪᴍɪᴛ.


<b>Commands and Usage:</b>
• /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
• Oɴʟʏ Dɪɢɪᴛs Aʀᴇ Aʟʟᴏᴡᴇᴅ
• Mᴀxɪᴍᴜᴍ Aʟʟᴏᴡᴇᴅ Dɪɢɪᴛs Tɪʟʟ 84 
(I Cᴀɴ'ᴛ Gᴇɴᴇʀᴀᴛᴇ Pᴀssᴡᴏʀᴅs Aʙᴏᴠᴇ Tʜᴇ Lᴇɴɢᴛʜ 84)
• IMDʙ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""


    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}"""


    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ʀᴇϙᴜɪʀᴇᴅ ᴀʀɢᴜᴍᴇɴᴛs ᴀɴᴅ ɪ ᴡɪʟʟ ᴋɪᴄᴋ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ɢʀᴏᴜᴘ.
• /instatus - ᴛᴏ ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs ᴏғ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀ ғʀᴏᴍ ɢʀᴏᴜᴘ
• /inkick ᴡɪᴛʜɪɴ_ᴍᴏɴᴛʜ ʟᴏɴɢ_ᴛɪᴍᴇ_ᴀɢᴏ - ᴛᴏ ᴋɪᴄᴋ ᴜsᴇʀs ᴡʜᴏ ᴀʀᴇ ᴏғғʟɪɴᴇ ғᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ 6-7 ᴅᴀʏs.
• /inkick ʟᴏɴɢ_ᴛɪᴍᴇ_ᴀɢᴏ - ᴛᴏ ᴋɪᴄᴋ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴀʀᴇ ᴏғғʟɪɴᴇ ғᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ ᴀ ᴍᴏɴᴛʜ ᴀɴᴅ Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛs.
• /dkick - to ᴋɪᴄᴋ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs."""

    CREATOR_REQUIRED = """❗You have to be the group creator to do that."""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """🚮 Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """❗I am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
