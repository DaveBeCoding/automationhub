import subprocess

def print_banner(title=""):
    subprocess.call("clear")
    print("""
 ____                        __  __            _          _
|  _ \ __ _ _ __  ___ _ __  |  \/  | __ _  ___| |__   ___| |_ ___    ________
| |_) / _` | '_ \/ _ \ '__| | |\/| |/ _` |/ __| '_ \ / _ \ __/ _ \  /_______/
|  __/ (_| | |_)|  __/ |    | |  | | (_| | (__| | | |  __/ ||  __/  \_______\\
|_|   \__,_| .__/\___|_|    |_|  |_|\__,_|\___|_| |_|\___|\__\___|  /_______/
           |_|                                                     @==|;;;;;;>
""")
    total_len = 80
    if title:
        padding = total_len - len(title) - 4
        print("== {} {}\n".format(title, "=" * padding))
    else:
        print("{}\n".format("=" * total_len)) 

print_banner()