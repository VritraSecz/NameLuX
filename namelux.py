# !/bin/pythyon3
# By github.com/VritraSecz
# https://github.com/VritraSecz/NameLuX.git/

import os
from time import sleep
import signal
import time
import sys


# color defined
gren = "\033[0m\033[38;5;46m"
grenx = "\033[1;32m"
reed = "\033[0m\033[38;5;196m"
reedx = "\033[1;31m"
white = "\033[38;5;15m"
whitex = "\033[1;37m"
reset = "\033[0m"
blue = "\033[1;34m"


os.system('clear')
os.system(f"cat core/main.logo")
sleep(1)

print(f"{gren}")

def print_loading_bar(percentage):
    bar_length = 38
    filled_length = int(bar_length * percentage / 100)
    bar = '█' * filled_length + ' ' * (bar_length - filled_length)
    sys.stdout.write("\rLoading [{}] {}%".format(bar, percentage))
    sys.stdout.flush()

total_time = 1.5  # in seconds
interval = total_time / 100

for i in range(101):
    print_loading_bar(i)
    time.sleep(interval)

#`print() 
#exit()

about_tool = """\033[0m
\033[38;5;15mIntroducing NameLuX: \033[38;5;46mElevate Your Termux Experience with Customized Banners

\033[38;5;15mIntroduction:
    \033[38;5;46mNameLuX is the ultimate banner customization tool, tailored exclusively for Termux enthusiasts. With an extensive array of creative options, NameLuX lets you effortlessly craft personalized banners that breathe life into your terminal. From minimalist elegance to vibrant energy, this tool empowers you to leave your unique mark on your digital workspace.

\033[38;5;15mKey Features:
\033[38;5;46m
    Diverse Banner Selection: Explore 47 diverse banner styles, offering everything from sleek minimalism to bold statements, giving your Termux interface the personality it deserves.

    Signature Name Designs: Choose from 270 name design styles – from modern calligraphy to retro graffiti – to showcase your name in ways that resonate with your identity.

    Seamless PS1 Prompts: Select from 30 meticulously curated PS1 prompt styles that infuse your terminal with aesthetics, ensuring every command is a visual delight.

    Vivid Text Color Palette: Elevate your banners with 21 captivating input text colors, allowing you to add a pop of personality to your terminal creations.
\033[38;5;15m
Endless Possibilities: \033[38;5;46m
    With NameLuX, the number of unique banner combinations you can create is truly limitless. By multiplying the choices across banner styles, name designs, PS1 prompts, and text colors, you have a staggering total of [270 * 47 * 30 * 21 = 7,994,700] different banner possibilities at your fingertips. Your creativity knows no bounds!
\033[38;5;15m
How It Works:
\033[38;5;46m
    Select Your Banner: Choose between displaying just your name, pairing it with a captivating design, or opting for a banner-only experience.
    Design Your Name: Personalize your name's appearance with a variety of creative design options.
    Craft Your Prompt: Elevate your terminal aesthetics by selecting a PS1 prompt style that resonates with your unique style.
    Add Vibrant Text: Make a statement with a text color that complements your banner and adds a touch of flair.

\033[38;5;15mWhy Choose NameLuX:
\033[38;5;46m
    Unleash Your Imagination: NameLuX opens the door to unparalleled customization, turning your terminal into an expressive canvas.
    Effortless Creativity: No need for coding expertise – simply customize and watch your vision come to life.
    Your Terminal, Your Identity: Express yourself through your terminal, making every session a reflection of your creativity.

\033[38;5;15mMeet the Developer - Alex Butler [\033[38;5;46mVritraSecz\033[38;5;15m]
\033[38;5;46mNameLuX was crafted with passion by Alex Butler, a dedicated developer with a flair for enhancing digital experiences. As a terminal enthusiast, Alex Butler believes in the power of customization to transform the mundane into something extraordinary.

\033[38;5;15mConnect with Alex Butler:
\033[38;5;46m
    Instagram: instagram.com/haxorlex
    GitHub: github.com/VritraSecz
    YouTube: youtube.com/@Technolex
    Facebook Page: facebook.com/hackerxmr
    Telegram Channel: t.me/VritraSec
    Telegram Community: t.me/VritraSecz
    Whole Network: t.me/LinkCentralX


\033[38;5;46mElevate your Termux environment today with NameLuX – where banners become an extension of your personality. Redefine your terminal, one customization at a time.
"""

menux = """\033[0m\033[38;5;46m[\033[38;5;15m#\033[38;5;46m] Select an option:

\033[38;5;46m[\033[38;5;15m1\033[38;5;46m] Set Banner Only
\033[38;5;46m[\033[38;5;15m2\033[38;5;46m] Set Name Only
\033[38;5;46m[\033[38;5;15m3\033[38;5;46m] Set Banner With Name
\033[38;5;46m[\033[38;5;15m4\033[38;5;46m] Restore Default
\033[38;5;46m[\033[38;5;15m5\033[38;5;46m] More Tools
\033[38;5;46m[\033[38;5;15m6\033[38;5;46m] About
\033[38;5;46m[\033[38;5;15mE\033[38;5;46m] Exit

\033[38;5;196minputx>\033[1;37m """  

fon_type = """\033[0m\033[38;5;46m[\033[38;5;15m#\033[38;5;46m] Select an option:

\033[38;5;46m[\033[38;5;15m1\033[38;5;46m] Font Set 1
\033[38;5;46m[\033[38;5;15m2\033[38;5;46m] Font Set 2
\033[38;5;46m[\033[38;5;15m3\033[38;5;46m] Font Set 3
\033[38;5;46m[\033[38;5;15m4\033[38;5;46m] Font Set 4
\033[38;5;46m[\033[38;5;15m5\033[38;5;46m] Font Set 5
\033[38;5;46m[\033[38;5;15m6\033[38;5;46m] Font Set 6
\033[38;5;46m[\033[38;5;15m7\033[38;5;46m] Font Set 7

\033[38;5;196minputx>\033[1;37m """

def exited():
    print(f"\n{reset}{gren}🎉 Thank you for using NameLuX! Your creativity knows no limits. Keep designing masterpieces! 🎨\n")
    exit()


def safe_exit(signum, frame):
    print(f"\n\n{reed}[!] Ctrl+C detected. Exiting gracefully...")
    print(f"\n{reset}{gren}🎉 Thank you for using NameLuX! Your creativity knows no limits. Keep designing masterpieces! 🎨\n")
    exit()

signal.signal(signal.SIGINT, safe_exit)

def set_new_bnr():
    print(f"\n{reset}{gren}[{white}+{gren}] Applying new banner in your termux.")
    os.system("chsh -s bash")
    os.system("mkdir /$HOME/.backupx > /dev/null 2>&1 &")
    os.system("mv /data/data/com.termux/files/usr/etc/motd /$HOME/.backupx > /dev/null 2>&1 &")
    os.system("rm /$HOME/.bashrc > /dev/null 2>&1 &")
    os.system("mv bashrc_file /$HOME/.bashrc > /dev/null 2>&1 &")
    sleep(1)
    print(f"\n{gren}[{white}+{gren}] New Banner has been successfully set in your termux. Exit and reopen your termux to see new look. ")
    exited()

def restore_dflt():
    os.system("clear")
    os.system("cat core/banner.bnr")
    print(f"\n{gren}[{white}+{gren}] Restoring Default look of termux.")
    os.system("rm /$HOME/.bashrc > /dev/null 2>&1 &")
    os.system("mv /$HOME/.backupx/motd /data/data/com.termux/files/usr/etc > /dev/null 2>&1 &")
    sleep(1)
    print(f"\n{gren}[{white}+{gren}] Default Banner has been successfully set in your termux. Exit and reopen your termux to see your termux default look.")
    exited()

def bnr_m():
    print(f"{reset}{reed}="*40)
    print(f"{gren}[{white}+{gren}] Select any banner type")
    print(f"{reed}="*40)
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}26{gren}] Android Banner")
    os.system(f"cat core/bnr/android.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}27{gren}] Apple Banner")
    os.system(f"cat core/bnr/apple.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}28{gren}] Biohazared Banner")
    os.system(f"cat core/bnr/biohazared.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}29{gren}] Boy Banner")
    os.system(f"cat core/bnr/boy.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}30{gren}] Danger_skull Banner")
    os.system(f"cat core/bnr/danger_skull.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}31{gren}] Deamon Banner")
    os.system(f"cat core/bnr/deamon.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}32{gren}] Deamonl Banner")
    os.system(f"cat core/bnr/deamonl.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}33{gren}] Funny_skull Banner")
    os.system(f"cat core/bnr/funny_skull.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}34{gren}] Github Banner")
    os.system(f"cat core/bnr/github.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}35{gren}] Hanuman Banner")
    os.system(f"cat core/bnr/hanuman.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}36{gren}] Headphone_skull Banner")
    os.system(f"cat core/bnr/headphone_skull.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}37{gren}] Hydra Banner")
    os.system(f"cat core/bnr/hydra.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}38{gren}] Linux Banner")
    os.system(f"cat core/bnr/linux.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}39{gren}] Lionston Banner")
    os.system(f"cat core/bnr/lionston.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}40{gren}] Panda Banner")
    os.system(f"cat core/bnr/panda.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}41{gren}] Radioactive Banner")
    os.system(f"cat core/bnr/radioactive.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}42{gren}] Single_eye Banner")
    os.system(f"cat core/bnr/single_eye.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}43{gren}] Skull Banner")
    os.system(f"cat core/bnr/skull.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}44{gren}] Stop Banner")
    os.system(f"cat core/bnr/stop.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}45{gren}] Termux Banner")
    os.system(f"cat core/bnr/termux.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}46{gren}] Ubuntu Banner")
    os.system(f"cat core/bnr/ubuntu.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}47{gren}] Warn Banner")
    os.system(f"cat core/bnr/warn.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}B{gren}] Back")
    print(f"{reed}-"*40)
    print()

def bnr_main():
    print(f"{reed}="*40)
    print(f"{reset}{gren}[{white}+{gren}] Select any banner type")
    print(f"{reed}="*40)
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}01{gren}] Fish Banner")
    os.system(f"cat core/bnr/blowfish.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}02{gren}] Frog Banner")
    os.system(f"cat core/bnr/bud-frogs.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}03{gren}] Cheese Banner")
    os.system(f"cat core/bnr/cheese.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}04{gren}] Deamon Banner")
    os.system(f"cat core/bnr/daemon.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}05{gren}] Dragon And Cow Banner")
    os.system(f"cat core/bnr/dragon-and-cow.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}06{gren}] Dragon Banner")
    os.system(f"cat core/bnr/dragon.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}07{gren}] Elephent Banner")
    os.system(f"cat core/bnr/elephant.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}08{gren}] Eyes Banner")
    os.system(f"cat core/bnr/eyes.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}09{gren}] Flaming Sheep Banner ")
    os.system(f"cat core/bnr/flaming-sheep.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}10{gren}] Ghostbuster Banner")
    os.system(f"cat core/bnr/ghostbusters.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}11{gren}] Kiss Banner")
    os.system(f"cat core/bnr/kiss.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}12{gren}] Kitty Banner")
    os.system(f"cat core/bnr/kitty.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}13{gren}] Meow Banner")
    os.system(f"cat core/bnr/meow.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}14{gren}] Milk Banner")
    os.system(f"cat core/bnr/milk.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}15{gren}] Moofasa Banner")
    os.system(f"cat core/bnr/moofasa.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}16{gren}] Moose Banner")
    os.system(f"cat core/bnr/moose.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}17{gren}] Ren Banner")
    os.system(f"cat core/bnr/ren.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}18{gren}] sheep Banner")
    os.system(f"cat core/bnr/sheep.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}19{gren}] Skeleton Banner")
    os.system(f"cat core/bnr/skeleton.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}20{gren}] Stegosaurus Banner")
    os.system(f"cat core/bnr/stegosaurus.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}21{gren}] Stimpy Banner")
    os.system(f"cat core/bnr/stimpy.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}22{gren}] Surgery Banner")
    os.system(f"cat core/bnr/surgery.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}23{gren}] Turkey Banner")
    os.system(f"cat core/bnr/turkey.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}24{gren}] Turtle Banner")
    os.system(f"cat core/bnr/turtle.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}25{gren}] Tux Banner")
    os.system(f"cat core/bnr/tux.bnr")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}B{gren}] Back")
    print(f"{reed}-"*40)
    print()


def fontsta():
    print(f"{reset}")
    print(f"{reed}="*40)
    print(f"{gren}[{white}+{gren}] Select any font type")
    print(f"{reed}="*40)
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}01{gren}] 3D-ASCII Font Style\n")
    os.system(f"cat core/fontxx/3D-ASCII.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}02{gren}] 3D_Diagonal Font Style\n")
    os.system(f"cat core/fontxx/3D_Diagonal.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}03{gren}] 3-D Font Style\n")
    os.system(f"cat core/fontxx/3-D.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}04{gren}] 3d Font Style\n")
    os.system(f"cat core/fontxx/3d.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}05{gren}] 3x5 Font Style\n")
    os.system(f"cat core/fontxx/3x5.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}06{gren}] 4Max Font Style\n")
    os.system(f"cat core/fontxx/4Max.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}07{gren}] 5lineoblique Font Style\n")
    os.system(f"cat core/fontxx/5lineoblique.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}08{gren}] Acrobatic Font Style\n")
    os.system(f"cat core/fontxx/Acrobatic.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}09{gren}] alligator3 Font Style\n")
    os.system(f"cat core/fontxx/alligator3.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}10{gren}] Alligator Font Style\n")
    os.system(f"cat core/fontxx/Alligator.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}11{gren}] Alphabet Font Style\n")
    os.system(f"cat core/fontxx/Alphabet.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}12{gren}] Alpha Font Style\n")
    os.system(f"cat core/fontxx/Alpha.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}13{gren}] AMC_3_Line Font Style\n")
    os.system(f"cat core/fontxx/AMC_3_Line.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}14{gren}] amc3line Font Style\n")
    os.system(f"cat core/fontxx/amc3line.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}15{gren}] AMC_3_Liv1 Font Style\n")
    os.system(f"cat core/fontxx/AMC_3_Liv1.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}16{gren}] amc3liv1 Font Style\n")
    os.system(f"cat core/fontxx/amc3liv1.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}17{gren}] amcaaa01 Font Style\n")
    os.system(f"cat core/fontxx/amcaaa01.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}18{gren}] amcneko Font Style\n")
    os.system(f"cat core/fontxx/amcneko.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}19{gren}] AMC_Neko Font Style\n")
    os.system(f"cat core/fontxx/AMC_Neko.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}20{gren}] amcrazo2 Font Style\n")
    os.system(f"cat core/fontxx/amcrazo2.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}21{gren}] amcrazor Font Style\n")
    os.system(f"cat core/fontxx/amcrazor.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}22{gren}] amcslash Font Style\n")
    os.system(f"cat core/fontxx/amcslash.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}23{gren}] amcslder Font Style\n")
    os.system(f"cat core/fontxx/amcslder.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}24{gren}] amcthin Font Style\n")
    os.system(f"cat core/fontxx/amcthin.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}25{gren}] amctubes Font Style\n")
    os.system(f"cat core/fontxx/amctubes.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}26{gren}] amcun1 Font Style\n")
    os.system(f"cat core/fontxx/amcun1.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}27{gren}] ANSI_Regular Font Style\n")
    os.system(f"cat core/fontxx/ANSI_Regular.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}28{gren}] ANSI_Shadow Font Style\n")
    os.system(f"cat core/fontxx/ANSI_Shadow.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}29{gren}] Arrows Font Style\n")
    os.system(f"cat core/fontxx/Arrows.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}30{gren}] ASCII_New_Roman Font Style\n")
    os.system(f"cat core/fontxx/ASCII_New_Roman.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}31{gren}] Avatar Font Style\n")
    os.system(f"cat core/fontxx/Avatar.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}32{gren}] Banner3-D Font Style\n")
    os.system(f"cat core/fontxx/Banner3-D.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}33{gren}] Banner3 Font Style\n")
    os.system(f"cat core/fontxx/Banner3.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}34{gren}] Banner4 Font Style\n")
    os.system(f"cat core/fontxx/Banner4.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}35{gren}] Banner Font Style\n")
    os.system(f"cat core/fontxx/Banner.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}36{gren}] Barbwire Font Style\n")
    os.system(f"cat core/fontxx/Barbwire.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}37{gren}] Basic Font Style\n")
    os.system(f"cat core/fontxx/Basic.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}38{gren}] Bear Font Style\n")
    os.system(f"cat core/fontxx/Bear.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}39{gren}] Bell Font Style\n")
    os.system(f"cat core/fontxx/Bell.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}40{gren}] bigchief Font Style\n")
    os.system(f"cat core/fontxx/bigchief.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}B{gren}] Get Back")
    print(f"{reed}-"*40)
    print()


def fontstb():
    print(f"{reset}")
    print(f"{reed}="*40)
    print(f"{gren}[{white}+{gren}] Select any font type")
    print(f"{reed}="*40)
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}41{gren}] Big_Chief Font Style\n")
    os.system(f"cat core/fontxx/Big_Chief.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}42{gren}] Bigfig Font Style\n")
    os.system(f"cat core/fontxx/Bigfig.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}43{gren}] Big Font Style\n")
    os.system(f"cat core/fontxx/Big.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}44{gren}] Big_Money-ne Font Style\n")
    os.system(f"cat core/fontxx/Big_Money-ne.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}45{gren}] Big_Money-nw Font Style\n")
    os.system(f"cat core/fontxx/Big_Money-nw.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}46{gren}] Big_Money-se Font Style\n")
    os.system(f"cat core/fontxx/Big_Money-se.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}47{gren}] Big_Money-sw Font Style\n")
    os.system(f"cat core/fontxx/Big_Money-sw.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}48{gren}] Binary Font Style\n")
    os.system(f"cat core/fontxx/Binary.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}49{gren}] Block Font Style\n")
    os.system(f"cat core/fontxx/Block.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}50{gren}] Blocks Font Style\n")
    os.system(f"cat core/fontxx/Blocks.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}51{gren}] Bloody Font Style\n")
    os.system(f"cat core/fontxx/Bloody.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}52{gren}] Bolger Font Style\n")
    os.system(f"cat core/fontxx/Bolger.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}53{gren}] Braced Font Style\n")
    os.system(f"cat core/fontxx/Braced.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}54{gren}] Bright Font Style\n")
    os.system(f"cat core/fontxx/Bright.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}55{gren}] Broadway Font Style\n")
    os.system(f"cat core/fontxx/Broadway.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}56{gren}] Broadway_KB Font Style\n")
    os.system(f"cat core/fontxx/Broadway_KB.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}57{gren}] Bubble Font Style\n")
    os.system(f"cat core/fontxx/Bubble.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}58{gren}] Bulbhead Font Style\n")
    os.system(f"cat core/fontxx/Bulbhead.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}59{gren}] Caligraphy2 Font Style\n")
    os.system(f"cat core/fontxx/Caligraphy2.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}60{gren}] Caligraphy Font Style\n")
    os.system(f"cat core/fontxx/Caligraphy.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}61{gren}] Calvin_S Font Style\n")
    os.system(f"cat core/fontxx/Calvin_S.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}62{gren}] Cards Font Style\n")
    os.system(f"cat core/fontxx/Cards.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}63{gren}] Catwalk Font Style\n")
    os.system(f"cat core/fontxx/Catwalk.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}64{gren}] Chiseled Font Style\n")
    os.system(f"cat core/fontxx/Chiseled.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}65{gren}] Chunky Font Style\n")
    os.system(f"cat core/fontxx/Chunky.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}66{gren}] Coinstak Font Style\n")
    os.system(f"cat core/fontxx/Coinstak.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}67{gren}] Cola Font Style\n")
    os.system(f"cat core/fontxx/Cola.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}68{gren}] Colossal Font Style\n")
    os.system(f"cat core/fontxx/Colossal.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}69{gren}] Computer Font Style\n")
    os.system(f"cat core/fontxx/Computer.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}70{gren}] Contessa Font Style\n")
    os.system(f"cat core/fontxx/Contessa.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}71{gren}] Contrast Font Style\n")
    os.system(f"cat core/fontxx/Contrast.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}72{gren}] Cosmike Font Style\n")
    os.system(f"cat core/fontxx/Cosmike.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}73{gren}] Crawford2 Font Style\n")
    os.system(f"cat core/fontxx/Crawford2.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}74{gren}] Crawford Font Style\n")
    os.system(f"cat core/fontxx/Crawford.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}75{gren}] Crazy Font Style\n")
    os.system(f"cat core/fontxx/Crazy.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}76{gren}] Cricket Font Style\n")
    os.system(f"cat core/fontxx/Cricket.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}77{gren}] Cursive Font Style\n")
    os.system(f"cat core/fontxx/Cursive.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}78{gren}] Cyberlarge Font Style\n")
    os.system(f"cat core/fontxx/Cyberlarge.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}79{gren}] Cybermedium Font Style\n")
    os.system(f"cat core/fontxx/Cybermedium.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}80{gren}] Cybersmall Font Style\n")
    os.system(f"cat core/fontxx/Cybersmall.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}B{gren}] Get Back")
    print(f"{reed}-"*40)
    print()


def fontstc():
    print(f"{reset}")
    print(f"{reed}="*40)
    print(f"{gren}[{white}+{gren}] Select any font type")
    print(f"{reed}="*40)
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}81{gren}] Cygnet Font Style\n")
    os.system(f"cat core/fontxx/Cygnet.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}82{gren}] DANC4 Font Style\n")
    os.system(f"cat core/fontxx/DANC4.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}83{gren}] Dancing_Font Font Style\n")
    os.system(f"cat core/fontxx/Dancing_Font.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}84{gren}] defleppard Font Style\n")
    os.system(f"cat core/fontxx/defleppard.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}85{gren}] Delta_Corps_Priest_1 Font Style\n")
    os.system(f"cat core/fontxx/Delta_Corps_Priest_1.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}86{gren}] Diamond Font Style\n")
    os.system(f"cat core/fontxx/Diamond.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}87{gren}] dietcola Font Style\n")
    os.system(f"cat core/fontxx/dietcola.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}88{gren}] Digital Font Style\n")
    os.system(f"cat core/fontxx/Digital.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}89{gren}] Doh Font Style\n")
    os.system(f"cat core/fontxx/Doh.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}90{gren}] Doom Font Style\n")
    os.system(f"cat core/fontxx/Doom.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}91{gren}] DOS_Rebel Font Style\n")
    os.system(f"cat core/fontxx/DOS_Rebel.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}92{gren}] dotmatrix Font Style\n")
    os.system(f"cat core/fontxx/dotmatrix.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}93{gren}] Double Font Style\n")
    os.system(f"cat core/fontxx/Double.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}94{gren}] doubleshorts Font Style\n")
    os.system(f"cat core/fontxx/doubleshorts.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}95{gren}] drpepper Font Style\n")
    os.system(f"cat core/fontxx/drpepper.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}96{gren}] eftichess Font Style\n")
    os.system(f"cat core/fontxx/eftichess.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}97{gren}] eftifont Font Style\n")
    os.system(f"cat core/fontxx/eftifont.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}98{gren}] eftirobot Font Style\n")
    os.system(f"cat core/fontxx/eftirobot.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}99{gren}] eftitalic Font Style\n")
    os.system(f"cat core/fontxx/eftitalic.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}100{gren}] eftiwall Font Style\n")
    os.system(f"cat core/fontxx/eftiwall.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}101{gren}] eftiwater Font Style\n")
    os.system(f"cat core/fontxx/eftiwater.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}102{gren}] Electronic Font Style\n")
    os.system(f"cat core/fontxx/Electronic.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}103{gren}] Elite Font Style\n")
    os.system(f"cat core/fontxx/Elite.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}104{gren}] Epic Font Style\n")
    os.system(f"cat core/fontxx/Epic.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}105{gren}] Fender Font Style\n")
    os.system(f"cat core/fontxx/Fender.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}106{gren}] Filter Font Style\n")
    os.system(f"cat core/fontxx/Filter.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}107{gren}] Fire_Font-k Font Style\n")
    os.system(f"cat core/fontxx/Fire_Font-k.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}108{gren}] Fire_Font-s Font Style\n")
    os.system(f"cat core/fontxx/Fire_Font-s.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}109{gren}] Flipped Font Style\n")
    os.system(f"cat core/fontxx/Flipped.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}110{gren}] flowerpower Font Style\n")
    os.system(f"cat core/fontxx/flowerpower.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}111{gren}] fourtops Font Style\n")
    os.system(f"cat core/fontxx/fourtops.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}112{gren}] Fraktur Font Style\n")
    os.system(f"cat core/fontxx/Fraktur.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}113{gren}] funface Font Style\n")
    os.system(f"cat core/fontxx/funface.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}114{gren}] funfaces Font Style\n")
    os.system(f"cat core/fontxx/funfaces.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}115{gren}] Fuzzy Font Style\n")
    os.system(f"cat core/fontxx/Fuzzy.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}116{gren}] Georgi16 Font Style\n")
    os.system(f"cat core/fontxx/Georgi16.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}117{gren}] Georgia11 Font Style\n")
    os.system(f"cat core/fontxx/Georgia11.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}118{gren}] Ghost Font Style\n")
    os.system(f"cat core/fontxx/Ghost.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}119{gren}] Ghoulish Font Style\n")
    os.system(f"cat core/fontxx/Ghoulish.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}120{gren}] Glenyn Font Style\n")
    os.system(f"cat core/fontxx/Glenyn.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}B{gren}] Get Back")
    print(f"{reed}-"*40)
    print()

def fontstd():
    print(f"{reset}")
    print(f"{reed}="*40)
    print(f"{gren}[{white}+{gren}] Select any font type")
    print(f"{reed}="*40)
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}121{gren}] Goofy Font Style\n")
    os.system(f"cat core/fontxx/Goofy.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}122{gren}] Gothic Font Style\n")
    os.system(f"cat core/fontxx/Gothic.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}123{gren}] Graceful Font Style\n")
    os.system(f"cat core/fontxx/Graceful.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}124{gren}] Gradient Font Style\n")
    os.system(f"cat core/fontxx/Gradient.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}125{gren}] Graffiti Font Style\n")
    os.system(f"cat core/fontxx/Graffiti.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}126{gren}] Greek Font Style\n")
    os.system(f"cat core/fontxx/Greek.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}127{gren}] halfiwi Font Style\n")
    os.system(f"cat core/fontxx/halfiwi.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}128{gren}] Heart_Left Font Style\n")
    os.system(f"cat core/fontxx/Heart_Left.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}129{gren}] Heart_Right Font Style\n")
    os.system(f"cat core/fontxx/Heart_Right.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}130{gren}] henry3d Font Style\n")
    os.system(f"cat core/fontxx/henry3d.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}131{gren}] Hieroglyphs Font Style\n")
    os.system(f"cat core/fontxx/Hieroglyphs.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}132{gren}] Hollywood Font Style\n")
    os.system(f"cat core/fontxx/Hollywood.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}133{gren}] horizontalleft Font Style\n")
    os.system(f"cat core/fontxx/horizontalleft.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}134{gren}] horizontalright Font Style\n")
    os.system(f"cat core/fontxx/horizontalright.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}135{gren}] Impossible Font Style\n")
    os.system(f"cat core/fontxx/Impossible.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}136{gren}] Invita Font Style\n")
    os.system(f"cat core/fontxx/Invita.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}137{gren}] Isometric1 Font Style\n")
    os.system(f"cat core/fontxx/Isometric1.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}138{gren}] Isometric2 Font Style\n")
    os.system(f"cat core/fontxx/Isometric2.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}139{gren}] Isometric3 Font Style\n")
    os.system(f"cat core/fontxx/Isometric3.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}140{gren}] Isometric4 Font Style\n")
    os.system(f"cat core/fontxx/Isometric4.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}141{gren}] Jacky Font Style\n")
    os.system(f"cat core/fontxx/Jacky.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}142{gren}] Jazmine Font Style\n")
    os.system(f"cat core/fontxx/Jazmine.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}143{gren}] Jerusalem Font Style\n")
    os.system(f"cat core/fontxx/Jerusalem.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}144{gren}] JS_Block_Letters Font Style\n")
    os.system(f"cat core/fontxx/JS_Block_Letters.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}145{gren}] JS_Bracket_Letters Font Style\n")
    os.system(f"cat core/fontxx/JS_Bracket_Letters.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}146{gren}] JS_Capital_Curves Font Style\n")
    os.system(f"cat core/fontxx/JS_Capital_Curves.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}147{gren}] JS_Cursive Font Style\n")
    os.system(f"cat core/fontxx/JS_Cursive.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}148{gren}] JS_Stick_Letters Font Style\n")
    os.system(f"cat core/fontxx/JS_Stick_Letters.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}149{gren}] Katakana Font Style\n")
    os.system(f"cat core/fontxx/Katakana.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}150{gren}] Kban Font Style\n")
    os.system(f"cat core/fontxx/Kban.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}151{gren}] Keyboard Font Style\n")
    os.system(f"cat core/fontxx/Keyboard.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}152{gren}] Knob Font Style\n")
    os.system(f"cat core/fontxx/Knob.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}153{gren}] larry3d Font Style\n")
    os.system(f"cat core/fontxx/larry3d.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}154{gren}] LCD Font Style\n")
    os.system(f"cat core/fontxx/LCD.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}155{gren}] Lean Font Style\n")
    os.system(f"cat core/fontxx/Lean.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}156{gren}] Letters Font Style\n")
    os.system(f"cat core/fontxx/Letters.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}157{gren}] lildevil Font Style\n")
    os.system(f"cat core/fontxx/lildevil.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}158{gren}] lineblocks Font Style\n")
    os.system(f"cat core/fontxx/lineblocks.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}159{gren}] Linux Font Style\n")
    os.system(f"cat core/fontxx/Linux.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}160{gren}] Lockergnome Font Style\n")
    os.system(f"cat core/fontxx/Lockergnome.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}B{gren}] Get Back")
    print(f"{reed}-"*40)
    print()


def fontste():
    print(f"{reset}")
    print(f"{reed}="*40)
    print(f"{gren}[{white}+{gren}] Select any font type")
    print(f"{reed}="*40)
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}161{gren}] Madrid Font Style\n")
    os.system(f"cat core/fontxx/Madrid.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}162{gren}] Marquee Font Style\n")
    os.system(f"cat core/fontxx/Marquee.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}163{gren}] Maxfour Font Style\n")
    os.system(f"cat core/fontxx/Maxfour.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}164{gren}] maxiwi Font Style\n")
    os.system(f"cat core/fontxx/maxiwi.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}165{gren}] Merlin1 Font Style\n")
    os.system(f"cat core/fontxx/Merlin1.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}166{gren}] Merlin2 Font Style\n")
    os.system(f"cat core/fontxx/Merlin2.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}167{gren}] Mini Font Style\n")
    os.system(f"cat core/fontxx/Mini.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}168{gren}] miniwi Font Style\n")
    os.system(f"cat core/fontxx/miniwi.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}169{gren}] Modular Font Style\n")
    os.system(f"cat core/fontxx/Modular.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}170{gren}] Moscow Font Style\n")
    os.system(f"cat core/fontxx/Moscow.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}171{gren}] Muzzle Font Style\n")
    os.system(f"cat core/fontxx/Muzzle.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}172{gren}] Nancyj-Fancy Font Style\n")
    os.system(f"cat core/fontxx/Nancyj-Fancy.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}173{gren}] Nancyj Font Style\n")
    os.system(f"cat core/fontxx/Nancyj.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}174{gren}] Nancyj-Underlined Font Style\n")
    os.system(f"cat core/fontxx/Nancyj-Underlined.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}175{gren}] Nipples Font Style\n")
    os.system(f"cat core/fontxx/Nipples.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}176{gren}] NScript Font Style\n")
    os.system(f"cat core/fontxx/NScript.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}177{gren}] ntgreek Font Style\n")
    os.system(f"cat core/fontxx/ntgreek.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}178{gren}] O8 Font Style\n")
    os.system(f"cat core/fontxx/O8.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}179{gren}] Ogre Font Style\n")
    os.system(f"cat core/fontxx/Ogre.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}180{gren}] oldbanner Font Style\n")
    os.system(f"cat core/fontxx/oldbanner.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}181{gren}] OS2 Font Style\n")
    os.system(f"cat core/fontxx/OS2.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}182{gren}] Patorjk-HeX Font Style\n")
    os.system(f"cat core/fontxx/Patorjk-HeX.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}183{gren}] Patorjk_s_Cheese Font Style\n")
    os.system(f"cat core/fontxx/Patorjk_s_Cheese.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}184{gren}] Pawp Font Style\n")
    os.system(f"cat core/fontxx/Pawp.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}185{gren}] Peaks Font Style\n")
    os.system(f"cat core/fontxx/Peaks.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}186{gren}] peaksslant Font Style\n")
    os.system(f"cat core/fontxx/peaksslant.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}187{gren}] Pebbles Font Style\n")
    os.system(f"cat core/fontxx/Pebbles.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}188{gren}] Pepper Font Style\n")
    os.system(f"cat core/fontxx/Pepper.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}189{gren}] Poison Font Style\n")
    os.system(f"cat core/fontxx/Poison.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}190{gren}] Puffy Font Style\n")
    os.system(f"cat core/fontxx/Puffy.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}191{gren}] Puzzle Font Style\n")
    os.system(f"cat core/fontxx/Puzzle.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}192{gren}] Pyramid Font Style\n")
    os.system(f"cat core/fontxx/Pyramid.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}193{gren}] Rammstein Font Style\n")
    os.system(f"cat core/fontxx/Rammstein.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}194{gren}] Rectangles Font Style\n")
    os.system(f"cat core/fontxx/Rectangles.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}195{gren}] Red_Phoenix Font Style\n")
    os.system(f"cat core/fontxx/Red_Phoenix.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}196{gren}] Relief2 Font Style\n")
    os.system(f"cat core/fontxx/Relief2.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}197{gren}] Relief Font Style\n")
    os.system(f"cat core/fontxx/Relief.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}198{gren}] Reverse Font Style\n")
    os.system(f"cat core/fontxx/Reverse.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}199{gren}] Roman Font Style\n")
    os.system(f"cat core/fontxx/Roman.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}200{gren}] Rotated Font Style\n")
    os.system(f"cat core/fontxx/Rotated.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}B{gren}] Get Back")
    print(f"{reed}-"*40)
    print()


def fontstf():
    print(f"{reset}")
    print(f"{reed}="*40)
    print(f"{gren}[{white}+{gren}] Select any font type")
    print(f"{reed}="*40)
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}201{gren}] Rounded Font Style\n")
    os.system(f"cat core/fontxx/Rounded.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}202{gren}] rowancap Font Style\n")
    os.system(f"cat core/fontxx/rowancap.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}203{gren}] Rozzo Font Style\n")
    os.system(f"cat core/fontxx/Rozzo.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}204{gren}] Runyc Font Style\n")
    os.system(f"cat core/fontxx/Runyc.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}205{gren}] santaclara Font Style\n")
    os.system(f"cat core/fontxx/santaclara.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}206{gren}] sblood Font Style\n")
    os.system(f"cat core/fontxx/sblood.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}207{gren}] Script Font Style\n")
    os.system(f"cat core/fontxx/Script.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}208{gren}] Serifcap Font Style\n")
    os.system(f"cat core/fontxx/Serifcap.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}209{gren}] Shadow Font Style\n")
    os.system(f"cat core/fontxx/Shadow.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}210{gren}] Shimrod Font Style\n")
    os.system(f"cat core/fontxx/Shimrod.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}211{gren}] Short Font Style\n")
    os.system(f"cat core/fontxx/Short.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}212{gren}] Slant Font Style\n")
    os.system(f"cat core/fontxx/Slant.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}213{gren}] Slide Font Style\n")
    os.system(f"cat core/fontxx/Slide.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}214{gren}] slscript Font Style\n")
    os.system(f"cat core/fontxx/slscript.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}215{gren}] SL_Script Font Style\n")
    os.system(f"cat core/fontxx/SL_Script.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}216{gren}] smallcaps Font Style\n")
    os.system(f"cat core/fontxx/smallcaps.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}217{gren}] Small Font Style\n")
    os.system(f"cat core/fontxx/Small.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}218{gren}] smisome1 Font Style\n")
    os.system(f"cat core/fontxx/smisome1.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}219{gren}] smkeyboard Font Style\n")
    os.system(f"cat core/fontxx/smkeyboard.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}220{gren}] smscript Font Style\n")
    os.system(f"cat core/fontxx/smscript.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}221{gren}] smshadow Font Style\n")
    os.system(f"cat core/fontxx/smshadow.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}222{gren}] smslant Font Style\n")
    os.system(f"cat core/fontxx/smslant.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}223{gren}] smtengwar Font Style\n")
    os.system(f"cat core/fontxx/smtengwar.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}224{gren}] Soft Font Style\n")
    os.system(f"cat core/fontxx/Soft.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}225{gren}] Speed Font Style\n")
    os.system(f"cat core/fontxx/Speed.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}226{gren}] Spliff Font Style\n")
    os.system(f"cat core/fontxx/Spliff.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}227{gren}] s-relief Font Style\n")
    os.system(f"cat core/fontxx/s-relief.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}228{gren}] Stacey Font Style\n")
    os.system(f"cat core/fontxx/Stacey.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}229{gren}] Stampate Font Style\n")
    os.system(f"cat core/fontxx/Stampate.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}230{gren}] Stampatello Font Style\n")
    os.system(f"cat core/fontxx/Stampatello.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}231{gren}] Standard Font Style\n")
    os.system(f"cat core/fontxx/Standard.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}232{gren}] starstrips Font Style\n")
    os.system(f"cat core/fontxx/starstrips.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}233{gren}] Star_Strips Font Style\n")
    os.system(f"cat core/fontxx/Star_Strips.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}234{gren}] starwars Font Style\n")
    os.system(f"cat core/fontxx/starwars.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}235{gren}] Star_Wars Font Style\n")
    os.system(f"cat core/fontxx/Star_Wars.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}236{gren}] Stellar Font Style\n")
    os.system(f"cat core/fontxx/Stellar.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}237{gren}] Stforek Font Style\n")
    os.system(f"cat core/fontxx/Stforek.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}238{gren}] Stick_Letters Font Style\n")
    os.system(f"cat core/fontxx/Stick_Letters.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}239{gren}] Stop Font Style\n")
    os.system(f"cat core/fontxx/Stop.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}240{gren}] Straight Font Style\n")
    os.system(f"cat core/fontxx/Straight.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}B{gren}] Get Back")
    print(f"{reed}-"*40)
    print()


def fontstg():
    print(f"{reset}")
    print(f"{reed}="*40)
    print(f"{gren}[{white}+{gren}] Select any font type")
    print(f"{reed}="*40)
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}241{gren}] Stronger_Than_All Font Style\n")
    os.system(f"cat core/fontxx/Stronger_Than_All.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}242{gren}] Sub-Zero Font Style\n")
    os.system(f"cat core/fontxx/Sub-Zero.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}243{gren}] swampland Font Style\n")
    os.system(f"cat core/fontxx/swampland.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}244{gren}] Swan Font Style\n")
    os.system(f"cat core/fontxx/Swan.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}245{gren}] Sweet Font Style\n")
    os.system(f"cat core/fontxx/Sweet.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}246{gren}] Tanja Font Style\n")
    os.system(f"cat core/fontxx/Tanja.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}247{gren}] Tengwar Font Style\n")
    os.system(f"cat core/fontxx/Tengwar.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}248{gren}] Test1 Font Style\n")
    os.system(f"cat core/fontxx/Test1.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}249{gren}] The_Edge Font Style\n")
    os.system(f"cat core/fontxx/The_Edge.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}250{gren}] Thick Font Style\n")
    os.system(f"cat core/fontxx/Thick.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}251{gren}] Thin Font Style\n")
    os.system(f"cat core/fontxx/Thin.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}252{gren}] THIS Font Style\n")
    os.system(f"cat core/fontxx/THIS.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}253{gren}] Thorned Font Style\n")
    os.system(f"cat core/fontxx/Thorned.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}254{gren}] Ticks Font Style\n")
    os.system(f"cat core/fontxx/Ticks.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}255{gren}] ticksslant Font Style\n")
    os.system(f"cat core/fontxx/ticksslant.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}256{gren}] Tiles Font Style\n")
    os.system(f"cat core/fontxx/Tiles.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}257{gren}] Tinker-Toy Font Style\n")
    os.system(f"cat core/fontxx/Tinker-Toy.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}258{gren}] Tombstone Font Style\n")
    os.system(f"cat core/fontxx/Tombstone.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}259{gren}] Train Font Style\n")
    os.system(f"cat core/fontxx/Train.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}260{gren}] Trek Font Style\n")
    os.system(f"cat core/fontxx/Trek.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}261{gren}] Tsalagi Font Style\n")
    os.system(f"cat core/fontxx/Tsalagi.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}262{gren}] Tubular Font Style\n")
    os.system(f"cat core/fontxx/Tubular.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}263{gren}] Twisted Font Style\n")
    os.system(f"cat core/fontxx/Twisted.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}264{gren}] Univers Font Style\n")
    os.system(f"cat core/fontxx/Univers.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}265{gren}] usaflag Font Style\n")
    os.system(f"cat core/fontxx/usaflag.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}266{gren}] Varsity Font Style\n")
    os.system(f"cat core/fontxx/Varsity.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}267{gren}] Wavy Font Style\n")
    os.system(f"cat core/fontxx/Wavy.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}268{gren}] Weird Font Style\n")
    os.system(f"cat core/fontxx/Weird.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}269{gren}] wetletter Font Style\n")
    os.system(f"cat core/fontxx/wetletter.fnt")
    print(f"{reed}-"*40)
    print(f"{reset}{gren}[{white}270{gren}] Whimsy Font Style\n")
    os.system(f"cat core/fontxx/Whimsy.fnt")
    print(f"{reset}{gren}[{white}B{gren}] Get Back")
    print(f"{reed}-"*40)
    print()


def promtx():
    print(f"{reed}="*40)
    print(f"{gren}[{white}+{gren}] Select any prompt type:")
    print(f"{reed}="*40)
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}01{reed} | \033[32m┬─\033[1;32m[\033[1;33mu0_a248\033[1;37m@\033[1;34mlocalhost\033[1;37m:~\033[1;32m]\033[0m\033[32m─\033[1;32m[\033[0m\033[32m03:34:34\033[1;32m]\033[0m\033[32m\n{reed}|    {reed}| \033[32m╰─>\033[1;31m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}02{reed} | \033[1;32m#>\033[0m\033[32m u0_a248\033[36m@\033[1;33mlocalhost\033[0m\033[35m:\033[37m~\033[1;31m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}03{reed} | \033[1;34mu0_a248@localhost \033[1;37m~ \033[1;33m[Wed Aug 09 03:47:55]\n{reed}|    {reed}| \033[1;37m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}04{reed} | \033[1;30m[\033[1;31mu0_a248\033[1;30m@\033[1;36m~\033[1;30m]\033[1;33m 08/09/23 14:00:16\n{reed}|    {reed}| \033[1;30m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}05{reed} | \033[38;5;226mu0_a429\033[1;37m@\033[38;5;208mlocalhost:\033[38;5;48m~\033[1;37m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}06{reed} | \033[4;32mu0_a283@localhost:~$\033[0m {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}07{reed} | \033[1;32mu0_a293 ➜ \033[1;31mlocalhost ➜ \033[1;34m~ ➜ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}08{reed} | \033[38;5;202m▲\033[38;5;208m▲\033[38;5;214m▲\033[38;5;220m▲\033[38;5;226mu0_a238\033[38;5;220m@\033[38;5;214mlocalhost\033[38;5;208m:\033[38;5;202m~\033[1;37m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}09{reed} | \033[38;5;88mu0_a248\033[0m\033[38;5;88m@\033[1;31mlocalhost\033[0m\033[38;5;88m (\033[1;31m~\033[0m\033[38;5;88m)]\033[1;37m $ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}10{reed} | \033[91m-\033[92m\-(\033[94m~\033[92m)\033[1;37m $ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}11{reed} | \033[01;33mu0_256\033[1;32m$\033[01;36m@\033[01;33mlocalhost\033[01;35m ~ \033[01;32m😀😁😂\n{reed}|    {reed}| \033[01;31m❤$\033[01;34mΩ\033[01;33mα\033[01;35mβ\033[01;31mψ\033[01;32m✈\033[01;30m►\033[01;37m🚀$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}12{reed} | \033[38;5;201m- \033[38;5;222mu0_a245\033[38;5;15m@\033[1;30mlocalhost\033[38;5;228m<\033[38;5;222m~\033[38;5;228m>\n{reed}|    {reed}| \033[1;38;5;132m$ \033[38;5;15m- {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}13{reed} | \033[1;35m★\033[1;37m u0_a243\033[37m@\033[1;34mlocalhost:\033[1;32m~\033[1;35m ★ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}14{reed} | \033[1;91m♥\033[1;32m\033[01;93mu0_a245 @localhost\033[1;37m:\033[01;94m~\033[00m\033[1;91m😍 > {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}15{reed} | \033[48;5;16m\033[38;5;10mu0_a245\033[38;5;16m\033[38;5;000m:\033[38;05;039m~\033[38;5;000m\033[38;5;046m:\033[38;5;034m🎼 \033[38;5;226m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}16{reed} | \033[0;32mLife is too short for bad code!\n{reed}|    {reed}| \033[0;36m[u0_a820@localhost ~]\033[0;32m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}17{reed} | \033[1;32mu0_a246@localhost\033[1;31m\n{reed}|    {reed}| ~\n{reed}|    {reed}| \033[0;33m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}18{reed} | \033[1;35m[u0_a243@localhost:~]\n{reed}|    {reed}| \033[1;32m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}19{reed} | \033[38;5;208m[~]\n{reed}|    {reed}| \033[38;5;202m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}20{reed} | \033[0;33m~> \033[38;5;196m~\n{reed}|    {reed}| \033[0m\033[1;32m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}21{reed} | \033[38;5;45mu0_a248\033[0m ➜ \033[38;5;81m~\033[38;5;15m $ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}22{reed} | \033[01;32mlocalhost:~$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}23{reed} | \033[1;33mu0_a249@localhost\033[0m:\033[1;34m~\033[1;37m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}24{reed} | \033[0;33mEat, sleep, code, repeat!\n{reed}|    {reed}| \033[0;36m[u0_a329@localhost ~]\033[0;33m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}25{reed} | \033[01;32m[localhost] \033[01;33mu0_a245\033[01;37m@\033[01;37mlocalhost:\033[01;37m~ \033[01;32m[20:46:23] \n{reed}|    {reed}| \033[01;32m0\033[00;31m$ \033[037mMr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}26{reed} | \033[01;33mu0_a245\033[01;34m@\033[01;31mlocalhost \033[01;36m🦈🦑🐙🐬🐠🐳🦀🦐\033[00m \033[01;35m~\033[1;37m $ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}27{reed} | \033[01;33mu0_a428\033[01;37m@\033[01;31mlocalhost \033[01;32m🍃🌱🌿🍂🍁🌾\033[00m \033[01;35m~\033[1;37m $ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}28{reed} | \033[01;33mu0_a328\033[01;37m@\033[01;31mlocalhost \033[01;35m🎼🎵🎶🎤\033[00m \033[01;36m~\033[1;37m $ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}29{reed} | \033[38;5;214mu0_a638\033[38;05;255m@\033[38;05;214mlocalhost \033[38;05;27m🦋\033[38;05;46m🦋\033[38;05;48m🦋\033[38;05;50m🦋\033[38;05;82m🦋\033[0m \033[38;05;196m~\033[1;37m$ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 + f"\n| {gren}30{reed} | \033[01;31mu0_a924\033[01;37m@\033[01;34mlocalhost \033[01;35m🌸🌺🌼🌻\033[01;36m🏵️🌷\033[00m \033[01;33m~\033[1;37m $ {reset}{white}Mr. Alex")
    print(f"{reed}+" + "-"*4 + "+" + "-"*34 )



def colorsx():
    print()
    print(f"{reed}="*40)
    print(f"{gren}[{white}+{gren}] Select any input text Color")
    print(f"{reed}="*40)
    print(f"\n{reset}{gren}[{white}01{gren}] \033[38;5;196mRed Color")
    print(f"{reset}{gren}[{white}02{gren}] \033[38;5;46mGreen Color")
    print(f"{reset}{gren}[{white}03{gren}] \033[38;5;21mBlue Color")
    print(f"{reset}{gren}[{white}04{gren}] \033[38;5;226mYellow Color")
    print(f"{reset}{gren}[{white}05{gren}] \033[38;5;129mPurple Color")
    print(f"{reset}{gren}[{white}06{gren}] \033[38;5;51mCyan Color")
    print(f"{reset}{gren}[{white}07{gren}] \033[38;5;15mWhite Color")
    print(f"{reset}{gren}[{white}08{gren}] \033[38;5;202mOrange Color")
    print(f"{reset}{gren}[{white}09{gren}] \033[38;5;219mPink Color")
    print(f"{reset}{gren}[{white}10{gren}] \033[38;5;130mBrown Color")
    print(f"{reset}{gren}[{white}11{gren}] \033[38;5;48mLight Green Color")
    print(f"{reset}{gren}[{white}12{gren}] \033[38;5;33mLight Blue Color")
    print(f"{reset}{gren}[{white}13{gren}] \033[38;5;229mLight Yellow Color")
    print(f"{reset}{gren}[{white}14{gren}] \033[38;5;141mLight Purple Color")
    print(f"{reset}{gren}[{white}15{gren}] \033[38;5;87mLight Cyan Color")
    print(f"{reset}{gren}[{white}16{gren}] \033[38;5;7mlight Gray Color")
    print(f"{reset}{gren}[{white}17{gren}] \033[38;5;8mDark Gray Color")
    print(f"{reset}{gren}[{white}18{gren}] \033[38;5;220mGold Color")
    print(f"{reset}{gren}[{white}19{gren}] \033[38;5;183mLavender Color")
    print(f"{reset}{gren}[{white}20{gren}] \033[38;5;200mMagenta Color")
    print(f"{reset}{gren}[{white}21{gren}] \033[38;5;23mTeal Color\n")


def select_clr():
    while True:
        os.system("clear")
        os.system("cat core/banner.bnr")
        colorsx()
        colx = input(f"{reset}{reed}inputx> {white}")
        if colx == "":
            pass
        elif colx == "1" or colx == "01":
            colox = '196m\]"'
            return colox
        elif colx == "2" or colx == "02":
            colox = '46m\]"'
            return colox
        elif colx == "3" or colx == "03":
            colox = '21m\]"'
            return colox
        elif colx == "4" or colx == "04":
            colox = '226m\]"'
            return colox
        elif colx == "5" or colx == "05":
            colox = '129m\]"'
            return colox
        elif colx == "6" or colx == "06":
            colox = '51m\]"'
            return colox
        elif colx == "7" or colx == "07":
            colox = '15m\]"'
            return colox
        elif colx == "8" or colx == "08":
            colox = '202m\]"'
            return colox
        elif colx == "9" or colx == "09":
            colox = '219m\]"'
            return colox
        elif colx == "10":
            colox = '130m\]"'
            return colox
        elif colx == "11":
            colox = '48m\]"'
            return colox
        elif colx == "12":
            colox = '33m\]"'
            return colox
        elif colx == "13":
            colox = '229m\]"'
            return colox
        elif colx == "14":
            colox = '141m\]"'
            return colox
        elif colx == "15":
            colox = '87m\]"'
            return colox
        elif colx == "16":
            colox = '7m\]"'
            return colox
        elif colx == "17":
            colox = '8m\]"'
            return colox
        elif colx == "18":
            colox = '220m\]"'
            return colox
        elif colx == "19":
            colox = '183m\]"'
            return colox
        elif colx == "20":
            colox = '200m\]"'
            return colox
        elif colx == "21":
            colox = '23m\]"'
            return colox
        else:
            pass

def select_pt():
    while True:
        os.system('clear')
        promtx()
        mprot = input(f"{reset}{reed}inputx>{white} ")
        if mprot == '':
            pass
        elif mprot == '01' or mprot == '1':
            aprot = r'PS1="\[\e[0;32m\]┬─\[\e[1;33m\][\u\[\e[1;37m\]@\[\e[1;34m\]\h\[\e[1;37m\]:\w\[\e[1;32m\]]\[\e[0;32m\]─\[\e[1;32m\][\[\e[0;32m\]\D{%T}\[\e[1;32m\]\[\e[1;32m\]]\n\[\e[0;32m\]╰─>\[\e[1;31m\]$ \[\033[38;5;'
            return aprot
        elif mprot == '02' or mprot == '2':
            aprot = r'PS1="\[\e[1;32m\]#> \[\e[0;32m\]\u\[\e[0;36m\]@\[\e[1;33m\]\h\[\e[0;35m\]:\[\e[0;37m\]\w\[\e[1;31m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '03' or mprot == '3':
            aprot = r'PS1="\[\033[38;5;12m\]\u@\h \[\033[38;5;15m\]\w \[\033[38;5;11m\][\d \t]\n\[\033[38;5;15m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '04' or mprot == '4':
            aprot = r'PS1="\[\e[1;30m\][\[\033[1;31m\]\u\[\e[1;30m\]@\[\033[1;36m\]\w\[\e[1;30m\]] \[\033[1;33m\]\D{%x %T}\n\[\e[1;30m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '05' or mprot == '5':
            aprot = r'PS1="\[\033[38;5;226m\]\u\[\033[38;5;15m\]@\[\033[38;5;208m\]\h\[\033[38;5;15m\]:\[\033[38;5;48m\]\w\[\033[38;5;15m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '06' or mprot == '6':
            aprot = r'PS1="\[\033[4;32m\]\u@\h:\w\$ \[\033[38;5;'
            return aprot
        elif mprot == '07' or mprot == '7':
            aprot = r'PS1="\[\e[1;32m\]\u ➜ \[\e[1;31m\]\h ➜ \[\e[1;34m\]\w ➜ \[\033[38;5;'
            return aprot
        elif mprot == '08' or mprot == '8':
            aprot = r'PS1="\[\e[38;5;202m▲\[\e[38;5;208m▲\[\e[38;5;214m▲\[\e[38;5;220m▲\]\[\e[38;5;226m\]\u\[\e[38;5;220m\]@\[\e[38;5;214m\]\h\[\e[38;5;208m\]:\[\e[38;5;202m\]\w\[\e[00m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '09' or mprot == '9':
            aprot = r'PS1="\e[38;5;88m[\[\033[1;31 m\]\u\[\033[0m\]\e[38;5;88m@\[\033[1;31m\]\h\[\033[0m\]\e[38;5;88m (\[\033[1;31m\]\W\[\033[0m\]\e[38;5;88m)]\[\033[00m\]$ \[\033[38;5;'
            return aprot
        elif mprot == '10':
            aprot = r'PS1="\\e[91m\]-\[\e[92m\-(\[\e[94m\]\w\[\e[92m\])\[\033[00m\] $ \[\033[38;5;'
            return aprot
        elif mprot == '11':
            aprot = r'''PS1="\[\033[01;33m\]\u\[\033[1;32m\]\$\[\033[01;36m\]@\[\033[01;33m\]\h\[\033[01;35m\] \$(git branch 2>/dev/null | grep -e '\*' | sed -E  's/\* (.+)/\1/')\[\033[01;36m\] \W \[\033[01;32m\]😀😁😂\n \[\033[01;31m\]❤\$\[\033[01;34m\]Ω\[\033[01;33m\]α\[\033[01;35m\]β\[\033[01;31m\]ψ\[\033[01;32m\]✈\[\033[01;30m\]►\[\033[01;33m\]🚀\$ \[\033[38;5;'''
            return aprot
        elif mprot == '12':
            aprot = r'PS1="\[\033[38;5;201m\]- \[\033[38;5;222m\]\u\[\033[38;5;15m\]@\[\033[38;5;232m\]\h \[\033[38;5;228m\]<\[\033[38;5;222m\]\w\[\033[38;5;228m\]>\n\[\033[1;38;5;132m\]\$ \[\033[38;5;15m\]- \[\033[38;5;'
            return aprot
        elif mprot == '13':
            aprot = r'PS1="\[\e[1;35m\]★\[\e[1;37m\] \u\[\e[0m\]@\[\e[1;34m\]\h:\[\e[1;32m\]\w\[\e[1;35m\] ★ \[\033[38;5;'
            return aprot
        elif mprot == '14':
            aprot = r'PS1="\[\e[1;91m\]♥\[\033[05m\]\[\033[01;93m\]\u@\h\[\033[00m\]:\[\033[01;94m\]\w\[\033[00m\]\[\e[1;91m\]😍 > \[\033[38;5;'
            return aprot
        elif mprot == '15':
            aprot = r'PS1="\[\033[48;5;16m\]\[\033[38;5;10m\]\u\[\e[38;5;16m\]\[\033[38;5;000m\]:\[\033[38;05;039m\]\w\[\033[38;5;000m\]\[\033[38;5;046m\]:\[\033[38;5;034m\]🎼 \[\033[38;5;226m\]\\$ \[\033[38;5;'
            return aprot
        elif mprot == '16':
            aprot = r'PS1="\[\e[0;32m\]Life is too short for bad code! \[\e[0m\] \n\[\e[0;36m\][\u@\h \W]\[\e[0;32m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '17':
            aprot = r'PS1="\[\033[1;32m\]\u@\h \n\[\033[1;31m\]\W\n\[\033[0;33m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '18':
            aprot = r'PS1="\[\033[1;35m\][\u@\h:\w]\n\[\033[1;32m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '19':
            aprot = r'PS1="\[\033[38;5;208m\][\w]\n\[\033[38;5;202m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '20':
            aprot = r'PS1="\[\033[0;33m\]~> \[\033[38;5;196m\]\W\n\[\033[0m\]\[\e[1;32m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '21':
            aprot = r'PS1="\[\033[38;5;45m\]\u\[\033[0m\] ➜ \[\033[38;5;81m\]\W\[\033[38;5;15m\] \$ \[\033[38;5;'
            return aprot
        elif mprot == '22':
            aprot = r'PS1="\[\033[01;32m\]\h:\W\$ \[\033[38;5;'
            return aprot
        elif mprot == '23':
            aprot = r'PS1="\[\033[1;33m\]\u@\h\[\033[0m\]:\[\033[1;34m\]\w\[\033[0m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '24':
            aprot = r'PS1="\[\e[0;33m\]Eat, sleep, code, repeat! \[\e[0m\] \n\[\e[0;36m\][\u@\h \W]\[\e[0;33m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '25':
            aprot = r'PS1="\[\033[01;32m\][\h] \[\033[01;33m\]\u\[\033[01;37m\]@\[\033[01;37m\]\h:\[\033[01;37m\]\w \[\033[01;32m\][\t] \n\[\033[01;32m\]${?#0[\[\033[01;32m\]}\[\033[00;31m\]\$ \[\033[38;5;'
            return aprot
        elif mprot == '26':
            aprot = r'PS1="\[\033[01;33m\]\u\[\033[01;34m\]@\[\033[01;31m\]\h \[\033[01;36m\]🦈🦑🐙🐬🐠🐳🦀🦐\[\033[00m\] \[\033[01;35m\]\w\[\033[00m\] $ \[\033[38;5;'
            return aprot
        elif mprot == '27':
            aprot = r'PS1="\[\033[01;33m\]\u\[\033[01;37m\]@\[\033[01;31m\]\h \[\033[01;32m\]🍃🌱🌿🍂🍁🌾\[\033[00m\] \[\033[01;35m\]\w\[\033[00m\] $ \[\033[38;5;'
            return aprot
        elif mprot == '28':
            aprot = r'PS1="\[\033[01;33m\]\u\[\033[01;37m\]@\[\033[01;31m\]\h \[\033[01;35m\]🎼🎵🎶🎤\[\033[00m\] \[\033[01;36m\]\w\[\033[00m\] $ \[\033[38;5;'
            return aprot
        elif mprot == '29':
            aprot = r'PS1="\[\033[38;5;214m\]\u\[\033[38;05;255m\]@\[\033[38;05;214m\]\h \[\033[38;05;27m\]🦋\[\033[38;05;46m\]🦋\[\033[38;05;48m\]🦋\[\033[38;05;50m\]🦋\[\033[38;05;82m\]🦋\[\033[0m\] \[\033[38;05;196m\]\w\[\033[0m\]$ \[\033[38;5;'
            return aprot
        elif mprot == '30':
            aprot = r'PS1="\[\033[01;31m\]\u\[\033[01;37m\]@\[\033[01;34m\]\h \[\033[01;35m\]🌸🌺🌼🌻\[\033[01;36m\]🏵️🌷\[\033[00m\] \[\033[01;33m\]\w\[\033[00m\] $ \[\033[38;5;'
            return aprot
        else:
            pass



def banners():
    while True:
        os.system('clear')
        os.system('cat core/banner.bnr')
        banerx = input(f"{reset}{gren}[{white}+{gren}] Select an option\n\n{reset}{gren}[{white}1{gren}] Simple banner\n{reset}{gren}[{white}2{gren}] Unique Banner\n\n{reed}inputx> {white}")
        if banerx == "":
            pass

        elif banerx == '01' or banerx == '1':
            while True:
                os.system('clear')
                os.system('cat core/banner.bnr')
                bnr_main()
                s_brx = input(f"\n{reed}inputx> {white}")
                if s_brx == '':
                    pass
                elif s_brx == '1' or s_brx == '01':
                    bnrxc = 'blowfish'
                    return bnrxc
                elif s_brx == '2' or s_brx == '02':
                    bnrxc = 'bud-frogs'
                    return bnrxc
                elif s_brx == '3' or s_brx == '03':
                    bnrxc = 'cheese'
                    return bnrxc
                elif s_brx == '4' or s_brx == '04':
                    bnrxc = 'deamon'
                    return bnrxc
                elif s_brx == '5' or s_brx == '05':
                    bnrxc = 'dragon-and-cow'
                    return bnrxc
                elif s_brx == '6' or s_brx == '06':
                    bnrxc = 'dragon'
                    return bnrxc
                elif s_brx == '7' or s_brx == '07':
                    bnrxc = 'elephent'
                    return bnrxc
                elif s_brx == '8' or s_brx == '08':
                    bnrxc = 'eyes'
                    return bnrxc
                elif s_brx == '9' or s_brx == '09':
                    bnrxc = 'flaming-sheep'
                    return bnrxc
                elif s_brx == '10':
                    bnrxc = 'ghostbusters'
                    return bnrxc
                elif s_brx == '11':
                    bnrxc = 'kiss'
                    return bnrxc
                elif s_brx == '12':
                    bnrxc = 'kitty'
                    return bnrxc
                elif s_brx == '13':
                    bnrxc = 'meow'
                    return bnrxc
                elif s_brx == '14':
                    bnrxc = 'milk'
                    return bnrxc
                elif s_brx == '15':
                    bnrxc = 'moofasa'
                    return bnrxc
                elif s_brx == '16':
                    bnrxc = 'moose'
                    return bnrxc
                elif s_brx == '17':
                    bnrxc = 'ren'
                    return bnrxc
                elif s_brx == '18':
                    bnrxc = 'sheep'
                    return bnrxc
                elif s_brx == '19':
                    bnrxc = 'skeleton'
                    return bnrxc
                elif s_brx == '20':
                    bnrxc = 'stegosaurus'
                    return bnrxc
                elif s_brx == '21':
                    bnrxc = 'stimpy'
                    return bnrxc
                elif s_brx == '22':
                    bnrxc = 'surgery'
                    return bnrxc
                elif s_brx == '23':
                    bnrxc = 'turkey'
                    return bnrxc
                elif s_brx == '24':
                    bnrxc = 'turtle'
                    return bnrxc
                elif s_brx == '25':
                    bnrxc = 'tux'
                    return bnrxc
                elif s_brx == "b" or s_brx == "B":
                    break
                else:
                    pass

        elif banerx == "02" or banerx == "2":
            while True:
                os.system('clear')
                os.system('cat core/banner.bnr')
                bnr_m()
                tr_brx = input(f"\n{reed}inputx> {white}")
                if tr_brx == "":
                    pass
                elif tr_brx == "26":
                    bnrxc = "android"
                    return bnrxc
                elif tr_brx == "27":
                    bnrxc = "apple"
                    return bnrxc
                elif tr_brx == "28":
                    bnrxc = "biohazared"
                    return bnrxc
                elif tr_brx == "29":
                    bnrxc = "boy"
                    return bnrxc
                elif tr_brx == "30":
                    bnrxc = "danger_skull"
                    return bnrxc
                elif tr_brx == "31":
                    bnrxc = "deamon"
                    return bnrxc
                elif tr_brx == "32":
                    bnrxc = "deamonl"
                    return bnrxc
                elif tr_brx == "33":
                    bnrxc = "funny_skull"
                    return bnrxc
                elif tr_brx == "34":
                    bnrxc = "github"
                    return bnrxc
                elif tr_brx == "35":
                    bnrxc = "hanuman"
                    return bnrxc
                elif tr_brx == "36":
                    bnrxc = "headphone_skull"
                    return bnrxc
                elif tr_brx == "37":
                    bnrxc = "hydra"
                    return bnrxc
                elif tr_brx == "38":
                    bnrxc = "linux"
                    return bnrxc
                elif tr_brx == "39":
                    bnrxc = "lionston"
                    return bnrxc
                elif tr_brx == "40":
                    bnrxc = "panda"
                    return bnrxc
                elif tr_brx == "41":
                    bnrxc = "radioactive"
                    return bnrxc
                elif tr_brx == "42":
                    bnrxc = "single_eye"
                    return bnrxc
                elif tr_brx == "43":
                    bnrxc = "skull"
                    return bnrxc
                elif tr_brx == "44":
                    bnrxc = "stop"
                    return bnrxc
                elif tr_brx == "45":
                    bnrxc = "termux"
                    return bnrxc
                elif tr_brx == "46":
                    bnrxc = "ubuntu"
                    return bnrxc
                elif tr_brx == "47":
                    bnrxc = "warn"
                    return bnrxc
                elif tr_brx == "b" or tr_brx == "B":
                    break
                else:
                    pass

        else:
            pass


# Select font type by user

def fontsx():
    while True:
        os.system('clear')
        os.system("cat core/banner.bnr")
        sel_set = input(fon_type)

        if sel_set == "":
            pass

        elif sel_set == "01" or sel_set == "1":
            while True:
                os.system('clear')
                os.system("cat core/banner.bnr")
                fontsta()
                listxa = input(f"{reset}{reed}inputx> {white}")
                
                if listxa == "":
                    pass

                elif listxa == "1" or listxa == "01":
                    bnrx = "3D-ASCII"
                    return bnrx

                elif listxa == "2" or listxa == "02":
                    bnrx = "3D_Diagonal"
                    return bnrx

                elif listxa == "3" or listxa == "03":
                    bnrx = "3-D"
                    return bnrx

                elif listxa == "4" or listxa == "04":
                    bnrx = "3d"
                    return bnrx

                elif listxa == "5" or listxa == "05":
                    bnrx = "3x5"
                    return bnrx

                elif listxa == "6" or listxa == "06":
                    bnrx = "4Max"
                    return bnrx

                elif listxa == "7" or listxa == "07":
                    bnrx = "5lineoblique"
                    return bnrx

                elif listxa == "8" or listxa == "08":
                    bnrx = "Acrobatic"
                    return bnrx

                elif listxa == "9" or listxa == "09":
                    bnrx = "alligator3"
                    return bnrx

                elif listxa == "10":
                    bnrx = "Alligator"
                    return bnrx

                elif listxa == "11":
                    bnrx = "Alphabet"
                    return bnrx

                elif listxa == "12":
                    bnrx = "Alpha"
                    return bnrx

                elif listxa == "13":
                    bnrx = "AMC_3_Line"
                    return bnrx

                elif listxa == "14":
                    bnrx = "amc3line"
                    return bnrx

                elif listxa == "15":
                    bnrx = "AMC_3_Liv1"
                    return bnrx

                elif listxa == "16":
                    bnrx = "amc3liv1"
                    return bnrx

                elif listxa == "17":
                    bnrx = "amcaaa01"
                    return bnrx

                elif listxa == "18":
                    bnrx = "amcneko"
                    return bnrx

                elif listxa == "19":
                    bnrx = "AMC_Neko"
                    return bnrx

                elif listxa == "20":
                    bnrx = "amcrazo2"
                    return bnrx

                elif listxa == "21":
                    bnrx = "amcrazor"
                    return bnrx

                elif listxa == "22":
                    bnrx = "amcslash"
                    return bnrx

                elif listxa == "23":
                    bnrx = "amcslder"
                    return bnrx

                elif listxa == "24":
                    bnrx = "amcthin"
                    return bnrx

                elif listxa == "25":
                    bnrx = "amctubes"
                    return bnrx

                elif listxa == "26":
                    bnrx = "amcun1"
                    return bnrx

                elif listxa == "27":
                    bnrx = "ANSI_Regular"
                    return bnrx

                elif listxa == "28":
                    bnrx = "ANSI_Shadow"
                    return bnrx

                elif listxa == "29":
                    bnrx = "Arrows"
                    return bnrx

                elif listxa == "30":
                    bnrx = "ASCII_New_Roman"
                    return bnrx

                elif listxa == "31":
                    bnrx = "Avatar"
                    return bnrx

                elif listxa == "32":
                    bnrx = "Banner3-D"
                    return bnrx

                elif listxa == "33":
                    bnrx = "Banner3"
                    return bnrx

                elif listxa == "34":
                    bnrx = "Banner4"
                    return bnrx

                elif listxa == "35":
                    bnrx = "Banner"
                    return bnrx

                elif listxa == "36":
                    bnrx = "Barbwire"
                    return bnrx

                elif listxa == "37":
                    bnrx = "Basic"
                    return bnrx

                elif listxa == "38":
                    bnrx = "Bear"
                    return bnrx

                elif listxa == "39":
                    bnrx = "Bell"
                    return bnrx

                elif listxa == "40":
                    bnrx = "bigchief"
                    return bnrx
                
                elif listxa == "b" or listxa == "B":
                    break

                else:
                    pass


        elif sel_set == "02" or sel_set == "2":
            while True:
                os.system('clear')
                os.system("cat core/banner.bnr")
                fontstb()
                listxb = input(f"{reset}{reed}inputx> {white}")
                
                if listxb == "":
                    pass

                elif listxb == "41":
                    bnrx = "Big_Chief"
                    return bnrx

                elif listxb == "42":
                    bnrx = "Bigfig"
                    return bnrx

                elif listxb == "43":
                    bnrx = "Big"
                    return bnrx

                elif listxb == "44":
                    bnrx = "Big_Money-ne"
                    return bnrx

                elif listxb == "45":
                    bnrx = "Big_Money-nw"
                    return bnrx

                elif listxb == "46":
                    bnrx = "Big_Money-se"
                    return bnrx

                elif listxb == "47":
                    bnrx = "Big_Money-sw"
                    return bnrx

                elif listxb == "48":
                    bnrx = "Binary"
                    return bnrx

                elif listxb == "49":
                    bnrx = "Block"
                    return bnrx

                elif listxb == "50":
                    bnrx = "Blocks"
                    return bnrx

                elif listxb == "51":
                    bnrx = "Bloody"
                    return bnrx

                elif listxb == "52":
                    bnrx = "Bolger"
                    return bnrx

                elif listxb == "53":
                    bnrx = "Braced"
                    return bnrx

                elif listxb == "54":
                    bnrx = "Bright"
                    return bnrx

                elif listxb == "55":
                    bnrx = "Broadway"
                    return bnrx

                elif listxb == "56":
                    bnrx = "Broadway_KB"
                    return bnrx

                elif listxb == "57":
                    bnrx = "Bubble"
                    return bnrx

                elif listxb == "58":
                    bnrx = "Bulbhead"
                    return bnrx

                elif listxb == "59":
                    bnrx = "Caligraphy2"
                    return bnrx

                elif listxb == "60":
                    bnrx = "Caligraphy"
                    return bnrx

                elif listxb == "61":
                    bnrx = "Calvin_S"
                    return bnrx

                elif listxb == "62":
                    bnrx = "Cards"
                    return bnrx

                elif listxb == "63":
                    bnrx = "Catwalk"
                    return bnrx

                elif listxb == "64":
                    bnrx = "Chiseled"
                    return bnrx

                elif listxb == "65":
                    bnrx = "Chunky"
                    return bnrx

                elif listxb == "66":
                    bnrx = "Coinstak"
                    return bnrx

                elif listxb == "67":
                    bnrx = "Cola"
                    return bnrx

                elif listxb == "68":
                    bnrx = "Colossal"
                    return bnrx

                elif listxb == "69":
                    bnrx = "Computer"
                    return bnrx

                elif listxb == "70":
                    bnrx = "Contessa"
                    return bnrx

                elif listxb == "71":
                    bnrx = "Contrast"
                    return bnrx

                elif listxb == "72":
                    bnrx = "Cosmike"
                    return bnrx

                elif listxb == "73":
                    bnrx = "Crawford2"
                    return bnrx

                elif listxb == "74":
                    bnrx = "Crawford"
                    return bnrx

                elif listxb == "75":
                    bnrx = "Crazy"
                    return bnrx

                elif listxb == "76":
                    bnrx = "Cricket"
                    return bnrx

                elif listxb == "77":
                    bnrx = "Cursive"
                    return bnrx

                elif listxb == "78":
                    bnrx = "Cyberlarge"
                    return bnrx

                elif listxb == "79":
                    bnrx = "Cybermedium"
                    return bnrx

                elif listxb == "80":
                    bnrx = "Cybersmall"
                    return bnrx

                elif listxb == "b" or listxb == "B":
                    break            

                else:
                    pass

        elif sel_set == "03" or sel_set == "3":
            while True:
                os.system('clear')
                os.system("cat core/banner.bnr")
                fontstc()
                listxc = input(f"{reset}{reed}inputx> {white}")
                
                if listxc == "":
                    pass

                elif listxc == "81":
                    bnrx = "Cygnet"
                    return bnrx

                elif listxc == "82":
                    bnrx = "DANC4"
                    return bnrx

                elif listxc == "83":
                    bnrx = "Dancing_Font"
                    return bnrx

                elif listxc == "84":
                    bnrx = "defleppard"
                    return bnrx

                elif listxc == "85":
                    bnrx = "Delta_Corps_Priest_1"
                    return bnrx

                elif listxc == "86":
                    bnrx = "Diamond"
                    return bnrx

                elif listxc == "87":
                    bnrx = "dietcola"
                    return bnrx

                elif listxc == "88":
                    bnrx = "Digital"
                    return bnrx

                elif listxc == "89":
                    bnrx = "Doh"
                    return bnrx

                elif listxc == "90":
                    bnrx = "Doom"
                    return bnrx

                elif listxc == "91":
                    bnrx = "DOS_Rebel"
                    return bnrx

                elif listxc == "92":
                    bnrx = "dotmatrix"
                    return bnrx

                elif listxc == "93":
                    bnrx = "Double"
                    return bnrx

                elif listxc == "94":
                    bnrx = "doubleshorts"
                    return bnrx

                elif listxc == "95":
                    bnrx = "drpepper"
                    return bnrx

                elif listxc == "96":
                    bnrx = "eftichess"
                    return bnrx

                elif listxc == "97":
                    bnrx = "eftifont"
                    return bnrx

                elif listxc == "98":
                    bnrx = "eftirobot"
                    return bnrx

                elif listxc == "99":
                    bnrx = "eftitalic"
                    return bnrx

                elif listxc == "100":
                    bnrx = "eftiwall"
                    return bnrx

                elif listxc == "101":
                    bnrx = "eftiwater"
                    return bnrx

                elif listxc == "102":
                    bnrx = "Electronic"
                    return bnrx

                elif listxc == "103":
                    bnrx = "Elite"
                    return bnrx

                elif listxc == "104":
                    bnrx = "Epic"
                    return bnrx

                elif listxc == "105":
                    bnrx = "Fender"
                    return bnrx

                elif listxc == "106":
                    bnrx = "Filter"
                    return bnrx

                elif listxc == "107":
                    bnrx = "Fire_Font-k"
                    return bnrx

                elif listxc == "108":
                    bnrx = "Fire_Font-s"
                    return bnrx

                elif listxc == "109":
                    bnrx = "Flipped"
                    return bnrx

                elif listxc == "110":
                    bnrx = "flowerpower"
                    return bnrx

                elif listxc == "111":
                    bnrx = "fourtops"
                    return bnrx

                elif listxc == "112":
                    bnrx = "Fraktur"
                    return bnrx

                elif listxc == "113":
                    bnrx = "funface"
                    return bnrx

                elif listxc == "114":
                    bnrx = "funfaces"
                    return bnrx

                elif listxc == "115":
                    bnrx = "Fuzzy"
                    return bnrx

                elif listxc == "116":
                    bnrx = "Georgi16"
                    return bnrx

                elif listxc == "117":
                    bnrx = "Georgia11"
                    return bnrx

                elif listxc == "118":
                    bnrx = "Ghost"
                    return bnrx

                elif listxc == "119":
                    bnrx = "Ghoulish"
                    return bnrx

                elif listxc == "120":
                    bnrx = "Glenyn"
                    return bnrx

                elif listxc == "b" or listxc == "B":
                    break  

                else:
                    pass

        elif sel_set == "04" or sel_set == "4":
            while True:
                os.system('clear')
                os.system("cat core/banner.bnr")
                fontstd()
                listxd = input(f"{reset}{reed}inputx> {white}")
                
                if listxd == "":
                    pass

                elif listxd == "121":
                    bnrx = "Goofy"
                    return bnrx

                elif listxd == "122":
                    bnrx = "Gothic"
                    return bnrx

                elif listxd == "123":
                    bnrx = "Graceful"
                    return bnrx

                elif listxd == "124":
                    bnrx = "Gradient"
                    return bnrx

                elif listxd == "125":
                    bnrx = "Graffiti"
                    return bnrx

                elif listxd == "126":
                    bnrx = "Greek"
                    return bnrx

                elif listxd == "127":
                    bnrx = "halfiwi"
                    return bnrx

                elif listxd == "128":
                    bnrx = "Heart_Left"
                    return bnrx

                elif listxd == "129":
                    bnrx = "Heart_Right"
                    return bnrx

                elif listxd == "130":
                    bnrx = "henry3d"
                    return bnrx

                elif listxd == "131":
                    bnrx = "Hieroglyphs"
                    return bnrx

                elif listxd == "132":
                    bnrx = "Hollywood"
                    return bnrx

                elif listxd == "133":
                    bnrx = "horizontalleft"
                    return bnrx

                elif listxd == "134":
                    bnrx = "horizontalright"
                    return bnrx

                elif listxd == "135":
                    bnrx = "Impossible"
                    return bnrx

                elif listxd == "136":
                    bnrx = "Invita"
                    return bnrx

                elif listxd == "137":
                    bnrx = "Isometric1"
                    return bnrx

                elif listxd == "138":
                    bnrx = "Isometric2"
                    return bnrx

                elif listxd == "139":
                    bnrx = "Isometric3"
                    return bnrx

                elif listxd == "140":
                    bnrx = "Isometric4"
                    return bnrx

                elif listxd == "141":
                    bnrx = "Jacky"
                    return bnrx

                elif listxd == "142":
                    bnrx = "Jazmine"
                    return bnrx

                elif listxd == "143":
                    bnrx = "Jerusalem"
                    return bnrx

                elif listxd == "144":
                    bnrx = "JS_Block_Letters"
                    return bnrx

                elif listxd == "145":
                    bnrx = "JS_Bracket_Letters"
                    return bnrx

                elif listxd == "146":
                    bnrx = "JS_Capital_Curves"
                    return bnrx

                elif listxd == "147":
                    bnrx = "JS_Cursive"
                    return bnrx

                elif listxd == "148":
                    bnrx = "JS_Stick_Letters"
                    return bnrx

                elif listxd == "149":
                    bnrx = "Katakana"
                    return bnrx

                elif listxd == "150":
                    bnrx = "Kban"
                    return bnrx

                elif listxd == "151":
                    bnrx = "Keyboard"
                    return bnrx

                elif listxd == "152":
                    bnrx = "Knob"
                    return bnrx

                elif listxd == "153":
                    bnrx = "larry3d"
                    return bnrx

                elif listxd == "154":
                    bnrx = "LCD"
                    return bnrx

                elif listxd == "155":
                    bnrx = "Lean"
                    return bnrx

                elif listxd == "156":
                    bnrx = "Letters"
                    return bnrx

                elif listxd == "157":
                    bnrx = "lildevil"
                    return bnrx

                elif listxd == "158":
                    bnrx = "lineblocks"
                    return bnrx

                elif listxd == "159":
                    bnrx = "Linux"
                    return bnrx

                elif listxd == "160":
                    bnrx = "Lockergnome"
                    return bnrx

                elif listxd == "b" or listxd == "B":
                    break  

                else:
                    pass

        elif sel_set == "05" or sel_set == "5":
            while True:
                os.system('clear')
                os.system("cat core/banner.bnr")
                fontste()
                listxe = input(f"{reset}{reed}inputx> {white}")
                
                if listxe == "":
                    pass

                elif listxe == "161":
                    bnrx = "Madrid"
                    return bnrx

                elif listxe == "162":
                    bnrx = "Marquee"
                    return bnrx

                elif listxe == "163":
                    bnrx = "Maxfour"
                    return bnrx

                elif listxe == "164":
                    bnrx = "maxiwi"
                    return bnrx

                elif listxe == "165":
                    bnrx = "Merlin1"
                    return bnrx

                elif listxe == "166":
                    bnrx = "Merlin2"
                    return bnrx

                elif listxe == "167":
                    bnrx = "Mini"
                    return bnrx

                elif listxe == "168":
                    bnrx = "miniwi"
                    return bnrx

                elif listxe == "169":
                    bnrx = "Modular"
                    return bnrx

                elif listxe == "170":
                    bnrx = "Moscow"
                    return bnrx

                elif listxe == "171":
                    bnrx = "Muzzle"
                    return bnrx

                elif listxe == "172":
                    bnrx = "Nancyj-Fancy"
                    return bnrx

                elif listxe == "173":
                    bnrx = "Nancyj"
                    return bnrx

                elif listxe == "174":
                    bnrx = "Nancyj-Underlined"
                    return bnrx

                elif listxe == "175":
                    bnrx = "Nipples"
                    return bnrx

                elif listxe == "176":
                    bnrx = "NScript"
                    return bnrx

                elif listxe == "177":
                    bnrx = "ntgreek"
                    return bnrx

                elif listxe == "178":
                    bnrx = "O8"
                    return bnrx

                elif listxe == "179":
                    bnrx = "Ogre"
                    return bnrx

                elif listxe == "180":
                    bnrx = "oldbanner"
                    return bnrx

                elif listxe == "181":
                    bnrx = "OS2"
                    return bnrx

                elif listxe == "182":
                    bnrx = "Patorjk-HeX"
                    return bnrx

                elif listxe == "183":
                    bnrx = "Patorjk_s_Cheese"
                    return bnrx

                elif listxe == "184":
                    bnrx = "Pawp"
                    return bnrx

                elif listxe == "185":
                    bnrx = "Peaks"
                    return bnrx

                elif listxe == "186":
                    bnrx = "peaksslant"
                    return bnrx

                elif listxe == "187":
                    bnrx = "Pebbles"
                    return bnrx

                elif listxe == "188":
                    bnrx = "Pepper"
                    return bnrx

                elif listxe == "189":
                    bnrx = "Poison"
                    return bnrx

                elif listxe == "190":
                    bnrx = "Puffy"
                    return bnrx

                elif listxe == "191":
                    bnrx = "Puzzle"
                    return bnrx

                elif listxe == "192":
                    bnrx = "Pyramid"
                    return bnrx

                elif listxe == "193":
                    bnrx = "Rammstein"
                    return bnrx

                elif listxe == "194":
                    bnrx = "Rectangles"
                    return bnrx

                elif listxe == "195":
                    bnrx = "Red_Phoenix"
                    return bnrx

                elif listxe == "196":
                    bnrx = "Relief2"
                    return bnrx

                elif listxe == "197":
                    bnrx = "Relief"
                    return bnrx

                elif listxe == "198":
                    bnrx = "Reverse"
                    return bnrx

                elif listxe == "199":
                    bnrx = "Roman"
                    return bnrx

                elif listxe == "200":
                    bnrx = "Rotated"
                    return bnrx

                elif listxe == "b" or listxe == "B":
                    break  

                else:
                    pass

        elif sel_set == "06" or sel_set == "6":
            while True:
                os.system('clear')
                os.system("cat core/banner.bnr")
                fontstf()
                listxf = input(f"{reset}{reed}inputx> {white}")
                
                if listxf == "":
                    pass

                elif listxf == "201":
                    bnrx = "Rounded"
                    return bnrx

                elif listxf == "202":
                    bnrx = "rowancap"
                    return bnrx

                elif listxf == "203":
                    bnrx = "Rozzo"
                    return bnrx

                elif listxf == "204":
                    bnrx = "Runyc"
                    return bnrx

                elif listxf == "205":
                    bnrx = "santaclara"
                    return bnrx

                elif listxf == "206":
                    bnrx = "sblood"
                    return bnrx

                elif listxf == "207":
                    bnrx = "Script"
                    return bnrx

                elif listxf == "208":
                    bnrx = "Serifcap"
                    return bnrx

                elif listxf == "209":
                    bnrx = "Shadow"
                    return bnrx

                elif listxf == "210":
                    bnrx = "Shimrod"
                    return bnrx

                elif listxf == "211":
                    bnrx = "Short"
                    return bnrx

                elif listxf == "212":
                    bnrx = "Slant"
                    return bnrx

                elif listxf == "213":
                    bnrx = "Slide"
                    return bnrx

                elif listxf == "214":
                    bnrx = "slscript"
                    return bnrx

                elif listxf == "215":
                    bnrx = "SL_Script"
                    return bnrx

                elif listxf == "216":
                    bnrx = "smallcaps"
                    return bnrx

                elif listxf == "217":
                    bnrx = "Small"
                    return bnrx

                elif listxf == "218":
                    bnrx = "smisome1"
                    return bnrx

                elif listxf == "219":
                    bnrx = "smkeyboard"
                    return bnrx

                elif listxf == "220":
                    bnrx = "smscript"
                    return bnrx

                elif listxf == "221":
                    bnrx = "smshadow"
                    return bnrx

                elif listxf == "222":
                    bnrx = "smslant"
                    return bnrx

                elif listxf == "223":
                    bnrx = "smtengwar"
                    return bnrx

                elif listxf == "224":
                    bnrx = "Soft"
                    return bnrx

                elif listxf == "225":
                    bnrx = "Speed"
                    return bnrx

                elif listxf == "226":
                    bnrx = "Spliff"
                    return bnrx

                elif listxf == "227":
                    bnrx = "s-relief"
                    return bnrx

                elif listxf == "228":
                    bnrx = "Stacey"
                    return bnrx

                elif listxf == "229":
                    bnrx = "Stampate"
                    return bnrx

                elif listxf == "230":
                    bnrx = "Stampatello"
                    return bnrx

                elif listxf == "231":
                    bnrx = "Standard"
                    return bnrx

                elif listxf == "232":
                    bnrx = "starstrips"
                    return bnrx

                elif listxf == "233":
                    bnrx = "Star_Strips"
                    return bnrx

                elif listxf == "234":
                    bnrx = "starwars"
                    return bnrx

                elif listxf == "235":
                    bnrx = "Star_Wars"
                    return bnrx

                elif listxf == "236":
                    bnrx = "Stellar"
                    return bnrx

                elif listxf == "237":
                    bnrx = "Stforek"
                    return bnrx

                elif listxf == "238":
                    bnrx = "Stick_Letters"
                    return bnrx

                elif listxf == "239":
                    bnrx = "Stop"
                    return bnrx

                elif listxf == "240":
                    bnrx = "Straight"
                    return bnrx

                elif listxf == "b" or listxf == "B":
                    break              

                else:
                    pass

        elif sel_set == "07" or sel_set == "7":
            while True:
                os.system('clear')
                os.system("cat core/banner.bnr")
                fontstg()
                listxg = input(f"{reset}{reed}inputx> {white}")
                
                if listxg == "":
                    pass

                elif listxg == "241":
                    bnrx = "Stronger_Than_All"
                    return bnrx

                elif listxg == "242":
                    bnrx = "Sub-Zero"
                    return bnrx

                elif listxg == "243":
                    bnrx = "swampland"
                    return bnrx

                elif listxg == "244":
                    bnrx = "Swan"
                    return bnrx

                elif listxg == "245":
                    bnrx = "Sweet"
                    return bnrx

                elif listxg == "246":
                    bnrx = "Tanja"
                    return bnrx

                elif listxg == "247":
                    bnrx = "Tengwar"
                    return bnrx

                elif listxg == "248":
                    bnrx = "Test1"
                    return bnrx

                elif listxg == "249":
                    bnrx = "The_Edge"
                    return bnrx

                elif listxg == "250":
                    bnrx = "Thick"
                    return bnrx

                elif listxg == "251":
                    bnrx = "Thin"
                    return bnrx

                elif listxg == "252":
                    bnrx = "THIS"
                    return bnrx

                elif listxg == "253":
                    bnrx = "Thorned"
                    return bnrx

                elif listxg == "254":
                    bnrx = "Ticks"
                    return bnrx

                elif listxg == "255":
                    bnrx = "ticksslant"
                    return bnrx

                elif listxg == "256":
                    bnrx = "Tiles"
                    return bnrx

                elif listxg == "257":
                    bnrx = "Tinker-Toy"
                    return bnrx

                elif listxg == "258":
                    bnrx = "Tombstone"
                    return bnrx

                elif listxg == "259":
                    bnrx = "Train"
                    return bnrx

                elif listxg == "260":
                    bnrx = "Trek"
                    return bnrx

                elif listxg == "261":
                    bnrx = "Tsalagi"
                    return bnrx

                elif listxg == "262":
                    bnrx = "Tubular"
                    return bnrx

                elif listxg == "263":
                    bnrx = "Twisted"
                    return bnrx

                elif listxg == "264":
                    bnrx = "Univers"
                    return bnrx

                elif listxg == "265":
                    bnrx = "usaflag"
                    return bnrx

                elif listxg == "266":
                    bnrx = "Varsity"
                    return bnrx

                elif listxg == "267":
                    bnrx = "Wavy"
                    return bnrx

                elif listxg == "268":
                    bnrx = "Weird"
                    return bnrx

                elif listxg == "269":
                    bnrx = "wetletter"
                    return bnrx

                elif listxg == "270":
                    bnrx = "Whimsy"
                    return bnrx

                elif listxg == "271":
                    bnrx = ""
                    return bnrx

                elif listxg == "b" or listxg == "B":
                    break  

                else:
                    pass

        else:
            pass

os.system("rm bashrc_file > /dev/null 2>&1 &")
os.system("cp core/bashrc bashrc_file > /dev/null 2>&1 &")

while True:
    os.system('clear')
    os.system("cat core/banner.bnr")
    maix = input(menux)
    if maix == "":
        pass

    elif maix == "01" or maix == "1":
        print(f"\n{gren}[{white}+{gren}] Launching NameLuX console")
        sleep(0.5)

        s_ban = banners()
        prt_x = select_pt()
        prt_y = select_clr()
        pro_x = prt_x + prt_y

        filex = "bashrc_file"

        with open(filex, 'a') as file:
            file.write(f"\ncowsay -f {s_ban} 'Welcome To Termux!' | lolcat\n")
            file.write(f"\n{pro_x}\n")
        
        file.close()
        set_new_bnr()

    elif maix == "02" or maix == "2":
        print(f"\n{gren}[{white}+{gren}] Launching NameLuX console")
        sleep(0.5)
        os.system('clear')
        os.system("cat core/banner.bnr")
        print()
        while True:
            namex = input(f"{reset}{gren}[{white}+]{gren} Enter Your Name: {white}")
            if namex == '':
                pass
            else:
                break
        s_fnt = fontsx()
        prt_x = select_pt()
        prt_y = select_clr()
        pro_x = prt_x + prt_y

        filex = "bashrc_file"

        with open(filex, 'a') as file:
            file.write(f"\nfiglet -f {s_fnt} '{namex}' | lolcat\n")
            file.write(f"\n{pro_x}\n")
        
        file.close()
        set_new_bnr()

    elif maix == "03" or maix == "3":
        print(f"\n{gren}[{white}+{gren}] Launching NameLuX console")
        sleep(0.5)
        sn_bnr = banners()
        os.system('clear')
        os.system("cat core/banner.bnr")
        print()
        while True:
            namexx = input(f"{gren}[{white}+]{gren} Enter Your Name: {white}")
            if namexx == '':
                pass
            else:
                break
        sn_fnt = fontsx()
        ps_x = select_pt()
        ps_y = select_clr()
        pr_x = ps_x + ps_y

        filex = "bashrc_file"

        with open(filex, 'a') as file:
            file.write(f"\ncowsay -f {sn_bnr} 'Welcome To Termux!' | lolcat\n")
            file.write("echo")
            file.write(f"\nfiglet -f {sn_fnt} '{namexx}' | lolcat\n")
            file.write(f"\n{pr_x}\n")
        
        file.close()
        set_new_bnr()

    elif maix == "04" or maix == "4":
        restore_dflt()

    elif maix == "05" or maix == "5":
        print(f"\n{gren}[{white}+{gren}] Opening tool list..\n")
        sleep(1)
        os.system("xdg-open https://github.com/VritraSecz?tab=repositories > /dev/null 2>&1 &")
        input(f"{blue}Press ENTER To Back")

    elif maix == "06" or maix == "6":
        os.system('clear')
        os.system("cat core/banner.bnr")
        print()
        print(about_tool)
        print()
        input(f"{blue}Press ENTER To Back")

    elif maix == "e" or maix == "E":
        exited()

    else:
        pass
