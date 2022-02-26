import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from tgxspammer.utils import load_plugins
import logging
from telethon import events
from . import Mam, Mam2, Mam3, Mam4, Mam5, Mam6, Mam7, Mam8, Mam9, Mam10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "tgxspammer/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("TGX SPAM BOT SUCCEDDFULLY DEPLOYED -!")
print("Enjoy! Do visit @MAMBA_NETWORK")

if __name__ == "__main__":
    Mam.run_until_disconnected()
    
if __name__ == "__main__":
    Mam2.run_until_disconnected()

if __name__ == "__main__":
    Mam3.run_until_disconnected()
    
if __name__ == "__main__":
    Mam4.run_until_disconnected()

if __name__ == "__main__":
    Mam5.run_until_disconnected()
    
if __name__ == "__main__":
    Mam6.run_until_disconnected()
    
if __name__ == "__main__":
    Mam7.run_until_disconnected()

if __name__ == "__main__":
    Mam8.run_until_disconnected()
    
if __name__ == "__main__":
    Mam9.run_until_disconnected()

if __name__ == "__main__":
    Mam10.run_until_disconnected()    
