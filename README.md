Requirements
===============

* Python 3.8 or higher
* Discord account with [developer mode][dev] enabled
* [discord.py][wrapper] wrapper for python

Installation
===============

Enable [message intent][intent] for your bot, and make sure you give it the `Send Messages` and `Read Message History` permission.

Usage
===============
Use the `.ping` command to check the bot's latency. 

To select a random message or attachement from a channel, follow this command format: `.draw <channelID> <messageCount>` or  `.d <channelID> <messageCount>` 

Message count is the number of messages in the specified channel to be taken into consideration while drawing a random winner.

[dev]: https://www.golinuxcloud.com/discord-developer-mode/
[wrapper]: https://pypi.org/project/discord.py/
[intent]: https://autocode.com/discord/threads/what-are-discord-privileged-intents-and-how-do-i-enable-them-tutorial-0c3f9977/
