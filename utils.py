import random #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
import time #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
import math #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
import os #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
from vars import CREDIT #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
from pyrogram.errors import FloodWait #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
from datetime import datetime,timedelta #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

class Timer: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    def __init__(self, time_between=5): #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        self.start_time = time.time() #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        self.time_between = time_between #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

    def can_send(self): #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        if time.time() > (self.start_time + self.time_between): #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            self.start_time = time.time() #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            return True #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        return False #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

#lets do calculations #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
def hrb(value, digits= 2, delim= "", postfix=""): #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    """Return a human-readable file size. #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    """ #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    if value is None: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        return None #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTSS
    chosen_unit = "B" #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    for unit in ("KB", "MB", "GB", "TB"): #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        if value > 1000: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            value /= 1024 #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            chosen_unit = unit #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        else: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            break #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

def hrt(seconds, precision = 0): #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    """Return a human-readable time delta as a string. #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    """ #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    pieces = [] #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    value = timedelta(seconds=seconds) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

    if value.days: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        pieces.append(f"{value.days}day") #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

    seconds = value.seconds #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

    if seconds >= 3600: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        hours = int(seconds / 3600) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        pieces.append(f"{hours}hr") #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        seconds -= hours * 3600 #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

    if seconds >= 60: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        minutes = int(seconds / 60) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        pieces.append(f"{minutes}min") #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        seconds -= minutes * 60 #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

    if seconds > 0 or not pieces: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        pieces.append(f"{seconds}sec") #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

    if not precision: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        return "".join(pieces) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

    return "".join(pieces[:precision]) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

timer = Timer() #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

async def progress_bar(current, total, reply, start): #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
    if timer.can_send(): #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        now = time.time() #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        diff = now - start #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        if diff < 1: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            return #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
        else: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            perc = f"{current * 100 / total:.1f}%" #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            elapsed_time = round(diff) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            speed = current / elapsed_time #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            remaining_bytes = total - current #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            if speed > 0: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                eta_seconds = remaining_bytes / speed #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                eta = hrt(eta_seconds, precision=1) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            else: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                eta = "-" #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            sp = str(hrb(speed)) + "/s" #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            tot = hrb(total) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            cur = hrb(current) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            bar_length = 10 #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            completed_length = int(current * bar_length / total) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            remaining_length = bar_length - completed_length #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

            symbol_pairs = [ #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                ("▬", "▭"), #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                ("✅", "☑️"), #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                ("🐬", "🦈"), #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                ("💚", "💛"), #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                ("🌟", "⭐"), #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                ("▰", "▱") #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            ] #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            chosen_pair = random.choice(symbol_pairs) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
            completed_symbol, remaining_symbol = chosen_pair #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS

            try: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋{🏌️ՏᕼᗩᑌᖇYᗩ🏌️}🦋✨═══─╯`') 
                #await reply.edit(f'`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🏌️ՏᕼᗩᑌᖇYᗩ🏌️✨═══─╯`') 
            except FloodWait as e: #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
                time.sleep(e.x) #🏌️ՏᕼᗩᑌᖇYᗩ🏌️ BOTS
