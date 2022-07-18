from concurrent.futures import ThreadPoolExecutor
import os

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

bash = 512
C2 = int(bash/256)
C1 = int(256/C2)

x = 0
c1 = 0
c2 = 0

for z in range(192,224):
    del x
    
    for x in range(256):
        del c1

        for c1 in range(C1):

            with ThreadPoolExecutor(max_workers=bash) as executor:
                for c2 in range(C2):
                    c = c1 * C2 + c2
                    del c2

                    for v in range(256):
                        ip = f'{z}.{x}.{c}.{v}'
                        del v
                        executor.submit(check_ip, ip)
                        del ip