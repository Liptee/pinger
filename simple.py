import os

for z in range(192, 224):
    for x in range(256):
        for c in range(256):
            count = 0
            for v in range(256):
                if count < 10:
                    ip = f"{z}.{x}.{c}.{v}"
                    command = f'ping {ip}'
                    response = os.popen(command).read().encode('cp1251').decode('cp866')
                    if "(100%" in response:
                        print(f"{ip} - не отвечает")
                        res = 'no signal'
                        count+=1
                    elif "75%" in response:
                        print(f"{ip} - слабый сигнал")
                        res = 'low signal'
                        count-=1
                    elif "50%" in response:
                        print(f"{ip} - средний сигнал")
                        res = 'average signal'
                        count = 0
                    elif "25%" in response:
                        print(f"{ip} - хороший сигнал")
                        res = 'fine signal'
                        count = 0
                    elif "(0%" in response:
                        res = 'perfect signal'
                        print(f"{ip} - отличный сигнал")
                        count = 0
                    else:
                        print(response)

                    if res != "no signal":
                        with open('result.md', 'a', encoding="utf-8") as f:
                            f.write(f"{ip} - {res}")
                            f.write('\n')
                else:
                    pass