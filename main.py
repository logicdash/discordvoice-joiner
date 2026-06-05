import os
import json
import asyncio
import sys

try:
    import discord
    from colorama import init, Fore, Style
except ImportError:
    print("Missing packages, installing...")
    os.system("pip install discord.py-self[voice] colorama")
    import discord
    from colorama import init, Fore, Style

init()

CONFIG_FILE = "config.json"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

BANNER = f"""
{Fore.CYAN}██████╗  █████╗ ███████╗██╗  ██╗    ██╗      ██████╗  ██████╗ ██╗ ██████╗
██╔══██╗██╔══██╗██╔════╝██║  ██║    ██║     ██╔═══██╗██╔════╝ ██║██╔════╝
██║  ██║███████║███████╗███████║    ██║     ██║   ██║██║  ███╗██║██║     
██║  ██║██╔══██║╚════██║██╔══██║    ██║     ██║   ██║██║   ██║██║██║     
██████╔╝██║  ██║███████║██║  ██║    ███████╗╚██████╔╝╚██████╔╝██║╚██████╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝ ╚═════╝
{Fore.MAGENTA}==================== 24/7 Voice Joiner & Status ===================={Style.RESET_ALL}
"""

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {"token": "", "voice_channel_id": "", "custom_status": ""}
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"token": "", "voice_channel_id": "", "custom_status": ""}

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

def setup_config():
    clear_console()
    print(BANNER)
    config = load_config()
    
    dirty = False
    
    if not config.get("token"):
        print(f"{Fore.YELLOW}[!] Token not found in config.json.{Style.RESET_ALL}")
        token = input(f"{Fore.GREEN}[?] Enter Token: {Style.RESET_ALL}").strip()
        config["token"] = token
        dirty = True
        
    if not config.get("voice_channel_id"):
        print(f"\n{Fore.YELLOW}[!] Voice channel ID not found.{Style.RESET_ALL}")
        vc_id = input(f"{Fore.GREEN}[?] Enter Voice Channel ID: {Style.RESET_ALL}").strip()
        config["voice_channel_id"] = vc_id
        dirty = True
        
    if config.get("custom_status") is None or config.get("custom_status") == "":
        print(f"\n{Fore.YELLOW}[!] Custom status is empty.{Style.RESET_ALL}")
        status = input(f"{Fore.GREEN}[?] Enter Custom Status (press Enter to skip): {Style.RESET_ALL}").strip()
        config["custom_status"] = status
        dirty = True
        
    if dirty:
        save_config(config)
        print(f"\n{Fore.GREEN}[+] Settings saved!{Style.RESET_ALL}")
        
    return config

class DashLogicClient(discord.Client):
    def __init__(self, voice_channel_id, custom_status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.voice_channel_id = int(voice_channel_id)
        self.custom_status = custom_status

    async def on_ready(self):
        clear_console()
        print(BANNER)
        print(f"{Fore.GREEN}[+] Logged in as: {Fore.WHITE}{self.user.name} ({self.user.id}){Style.RESET_ALL}")
        
        if self.custom_status:
            print(f"{Fore.GREEN}[+] Setting status to: {Fore.YELLOW}{self.custom_status}{Style.RESET_ALL}")
            try:
                activity = discord.CustomActivity(name=self.custom_status)
                await self.change_presence(activity=activity, status=discord.Status.online)
            except AttributeError:
                activity = discord.Game(name=self.custom_status)
                await self.change_presence(activity=activity, status=discord.Status.online)
        
        await self.connect_to_voice()

    async def connect_to_voice(self):
        channel = self.get_channel(self.voice_channel_id)
        if not channel:
            print(f"{Fore.RED}[-] Error: Voice channel {self.voice_channel_id} not found!{Style.RESET_ALL}")
            return
            
        print(f"{Fore.CYAN}[*] Connecting to voice: {Fore.WHITE}{channel.name} ({channel.guild.name}){Style.RESET_ALL}")
        
        try:
            await channel.connect(reconnect=True, timeout=30)
            
            await self.ws.voice_state(
                guild_id=channel.guild.id,
                channel_id=channel.id,
                self_mute=True,
                self_deaf=False
            )
            print(f"{Fore.GREEN}[+] Connected to voice (Self-Muted).{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] Connection error: {e}{Style.RESET_ALL}")

    async def on_voice_state_update(self, member, before, after):
        if member.id == self.user.id:
            if before.channel is not None and after.channel is None:
                print(f"\n{Fore.YELLOW}[!] Disconnected! Reconnecting in 5s...{Style.RESET_ALL}")
                await asyncio.sleep(5)
                await self.connect_to_voice()

def main():
    config = setup_config()
    
    client = DashLogicClient(
        voice_channel_id=config["voice_channel_id"],
        custom_status=config["custom_status"],
        self_bot=True
    )
    
    try:
        client.run(config["token"])
    except discord.errors.LoginFailure:
        print(f"\n{Fore.RED}[-] Invalid Token! Check config.json.{Style.RESET_ALL}")
        config["token"] = ""
        save_config(config)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Stopped.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
