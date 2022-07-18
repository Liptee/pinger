from concurrent.futures import ThreadPoolExecutor
import os
import time

def check_ip(ip):
    command = f"ping {ip}"
    response = os.popen(command).read().encode('cp1251').decode('cp866')
    del command
    if "(100%" in response:
        print(f"{ip} - не отвечает")
        res = 'no signal'
    elif "75%" in response:
        print(f"{ip} - слабый сигнал")
        res = 'low signal'
    elif "50%" in response:
        print(f"{ip} - средний сигнал")
        res = 'average signal'
    elif "25%" in response:
        print(f"{ip} - хороший сигнал")
        res = 'fine signal'
    elif "(0%" in response:
        res = 'perfect signal'
        print(f"{ip} - отличный сигнал")
    else:
        print(response)

    del response

    if res != "no signal":
        with open('result.md', 'a', encoding="utf-8") as f:
            f.write(f"{ip} - {res}")
            f.write('\n')

    del ip
    del res
x = 0
c = 0

for z in range(191, 192):
    del x
    for x in range(1,2):
        del c
        for c in range(8):
            start = time.time()
            with ThreadPoolExecutor(max_workers=256) as executor:
                for v in range(256):
                    ip = f'{z}.{x}.{c}.{v}'
                    del v
                    executor.submit(check_ip, ip)
                    del ip

            print((time.time() - start)/256)
            del start