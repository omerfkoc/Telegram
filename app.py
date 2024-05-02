from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
api_id = 23905794
api_hash = 'fa95fb37e11c5fcd7416c403d5ce791f'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    await client.send_message('me', 'Hello, myself!')
    
with client:
    client.loop.run_until_complete(main())