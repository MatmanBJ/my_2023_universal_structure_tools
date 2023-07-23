import sys # for arguments from terminal pass
import subprocess # for terminal usage
import os # for terminal usage
import enum # for custom types
#subprocess.Popen('cmd.exe')
# https://stackoverflow.com/questions/70308288/open-a-terminal-with-python-but-keep-it-running
# https://stackoverflow.com/questions/19308415/execute-terminal-command-from-python-in-new-terminal-window
#subprocess.call('cmd.exe')
#os.system('dir')

# https://stackoverflow.com/questions/58608361/string-based-enum-in-python
class YTType(str, enum.Enum):
    p360 = "18"
    p720 = "22"

class VKType(str, enum.Enum):
    p240 = "url240"
    p360 = "url360"
    p480 = "url480"
    p720 = "url720"
    #p1080 = "url1080"

class UNK1Type(str, enum.Enum):
    p240 = "240p"
    p480 = "480p"
    p720 = "720p"
    #p1080 = "1080p"

class UNK2Type(str, enum.Enum):
    p240 = "240p-1000k-1"
    p480 = "480p-2000k-1"
    p720 = "720p-4000k-1"
    #p1080 = "1080p-4000k-1"

def fileRead():

    # https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
    link = []

    # https://pythonz.net/references/named/file.read/
    # https://pythonz.net/references/named/file.readline/
    with open('links.txt') as f:
        while True:
            str = f.readline()
            if not str:
                break
            link.append(str)
        #str = f.read(256) # read 256 symbols
    
    return link

def linkDownload(link, t, n):

    i = 1

    for l in link:
        if l != "\n": # for skipping empty strings if there are some (it often happens in notes)
            print("\n---------- LINK n" + str(i) + " ----------\n")
            if n == True: # numbering is enabled
                # https://superuser.com/questions/1313121/how-to-add-track-numbers-to-the-filename-with-youtube-dl
                # https://superuser.com/a/1366344
                print("yt-dlp --no-check-certificate -f " + t.p720 + " " + "-o" + " \"" + str(i) + " %(title)s.%(ext)s" + "\" " + l)
                # https://unix.stackexchange.com/questions/154427/unexpected-eof-while-looking-for-matching-bash-script
                # https://unix.stackexchange.com/a/154430
                os.system("yt-dlp --no-check-certificate -f " + t.p720 + " " + "-o" + " \"" + str(i) + " %(title)s.%(ext)s" + "\" " + l)
            elif n == False: # numbering is disabled
                print("yt-dlp --no-check-certificate -f " + t.p720 + " " + l)
                # https://stackoverflow.com/questions/11443011/running-terminal-within-a-python-script?rq=3
                # https://stackoverflow.com/a/11443169
                os.system("yt-dlp --no-check-certificate -f " + t.p720 + " " + l)
            i = i + 1
    

# https://stackoverflow.com/questions/4041238/why-use-def-main
# https://stackoverflow.com/a/4041253
def main():
    # https://www.geeksforgeeks.org/command-line-arguments-in-python/
    if len(sys.argv) >= 5:
        # https://stackoverflow.com/questions/664294/is-it-possible-only-to-declare-a-variable-without-assigning-any-value-in-python
        t = None
        n = None
        if sys.argv[1] in ("--type", "-t"):
            if sys.argv[2] in ("yt", "vk", "unk1", "unk2"):
                if sys.argv[2] == "yt":
                    t = YTType
                elif sys.argv[2] == "vk":
                    t = VKType
                elif sys.argv[2] == "unk1":
                    t = UNK1Type
                elif sys.argv[2] == "unk2":
                    t = UNK2Type
            else:
                raise ArgumentError("Incorrect argument \"-t/--type\": expected \"yt\", \"vk\", \"unk1\", \"unk2\", etc.!")
        else:
            raise ArgumentError("Incorrect argument: expected \"-t/--type\"!")
        if sys.argv[3] in ("--numbering", "-n"):
            if sys.argv[4] in ("enabled", "disabled"):
                if sys.argv[4] == "enabled":
                    n = True
                elif sys.argv[4] == "disabled":
                    n = False
            else:
                raise ArgumentError("Incorrect argument \"-n/--numbering\": expected \"enabled\" or \"disabled\"!")
        else:
            raise ArgumentError("Incorrect argument: expected \"-n/--numbering\"!")
        link = fileRead()
        linkDownload(link, t, n)
    else:
        raise ArgumentError("Incorrect argument: expected 5, got " + str(len(sys.argv)) + "!")

if __name__ == "__main__":
    main()
