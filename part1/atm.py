import sys
sys.path.append("../")
from library import KVStorage

_g_kvstorage=None

def main():
    if len(sys.argv) < 2:
        print('Usage: %s selfHost:port partner1Host:port partner2Host:port')
        sys.exit(-1)

    selfAddr = sys.argv[1]
    if selfAddr == 'readonly':
        selfAddr = None
    partners = sys.argv[2:]

    global _g_kvstorage
    _g_kvstorage= KVStorage(selfAddr, partners)
    user=input("login: ").strip()

    while True:
        cmd = input(">> ").split()
        if not cmd:
            continue

        elif cmd[0]=="chuser":
            user=cmd[1]
            print(f"Current user: {user}")

        elif cmd[0]=="wd":
            val=_g_kvstorage.get(user)
            if val is None: val=0
            newval=val-float(cmd[1])
            _g_kvstorage.set(user,newval)
            print(f"Rs {cmd[1]} is withdrawn from {user} account")

        elif cmd[0]=="dp":
            val=_g_kvstorage.get(user)
            if val is None: val=0
            newval=val+float(cmd[1])
            _g_kvstorage.set(user,newval)
            print(f"Rs {cmd[1]} is deposited to {user} account")

        elif cmd[0]=="bal":
            val=_g_kvstorage.get(user)
            if val is None:
                print("Account does not exist")
            else:
                print(f"{user} account balance: {val}")

        elif cmd[0]=="trto":
            val=_g_kvstorage.get(user)
            if val is None: val=0
            newval=val-float(cmd[2])
            _g_kvstorage.set(user,newval)
            val=_g_kvstorage.get(cmd[1])
            if val is None: val=0
            newval=val+float(cmd[2])
            _g_kvstorage.set(cmd[1],newval)
            print("Transaction successful")

        elif cmd[0]=="add":
            if user=="admin":
                _g_kvstorage.set(cmd[1], float(cmd[2]))
                print("Account created")
            else:
                print("Unauthorized")

        elif cmd[0]=="rm":
            if user=="admin":
                _g_kvstorage.pop(cmd[1])
                print("Account removed")
            else:
                print("Unauthorized")

        elif cmd[0]=="ls":
            if user=="admin":
                l=_g_kvstorage.ls()
                print(f"Users: {l}")
            else:
                print("Unauthorized")

        else:
            print('Wrong command')

if __name__=='__main__':
    main()