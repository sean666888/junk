import time
from subprocess import call
def tools():
    time.sleep(900)
    call(["bash", "/home/sean/ip.sh"])
    call(["zip", "-r",  "tools.zip", "tools"])
    call(["cp", "tools.zip", "/var/www/html/tools.zip"])
    if count == 10:
        count = 0
        update()
    else:
        count += 1
        tools()
def update():
    call(["rm", "/home/sean/tools/japsetup.exe"])
    call(["rm", "/home/sean/tools/u.zip"])
    call(["wget", "https://anon.inf.tu-dresden.de/win/japsetup.exe", "-O", "/home/sean/tools/japsetup.exe"])
    call(["wget", "https://ultrasurf.us/download/u.zip", "-O", "/home/sean/tools/u.zip"])
    tools()
tools()
