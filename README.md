# Discord Bot Template (py-cord)

A clean, configurable, and expandable Discord bot template built with [py-cord](https://docs.pycord.dev/en/stable/), designed to make developing your own Discord bot quick and easy.

## 🌟 Features

- **Modular Command System**: Built using py-cord's Cog system for easy organization and scaling
- **Slash Commands Support**: Fully configured for Discord's modern slash command interface
- **Configuration via JSON**: Simple configuration through an external file - no need to modify code
- **Error Handling**: Comprehensive error handling for smooth operation
- **Example Command**: Includes a simple ping command to test latency and confirm functionality

## 📋 Prerequisites

- Python 3.8 or higher
- [py-cord](https://docs.pycord.dev/en/stable/) library
- Discord Bot Token ([How to create a Discord bot](https://discord.com/developers/applications))

## 🚀 Getting Started

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/discord-bot-template.git
   cd discord-bot-template
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your bot by editing `config.json`:
   ```json
  {
      "Token": "YourBotToken",
      "Status": "TheStatusYouWantTheBotToHave"
  }
   ```

4. Start the bot:
   ```
   python main.py
   ```

### Adding New Commands

To add a new command, create a new Python file in the `cogs` directory. 


## 📝 Configuration Options

Edit the `config.json` file to customize your bot:

- `Token`: Your Discord bot token
- `Status`: The status message shown for your bot

## 🛠️ Customization

### Changing the Command Prefix

The default command prefix is `!`. To change it, modify the `command_prefix` parameter in the `Bot` class initialization in `main.py`.

### Customizing Status

You can change the bot's status by editing the `Status` field in `config.json`.

## 📚 Resources

- [py-cord Documentation](https://docs.pycord.dev/en/stable/)
- [Discord Developer Portal](https://discord.com/developers/docs/intro)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📫 Contact

If you have any questions or feedback, please open an issue on GitHub.

---

Happy coding! 🎉
