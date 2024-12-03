import re
total = 0

File = 'Corrupted.txt'

with open(File, 'r') as f:
        Corrupted = f.readlines()
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(str(pattern), str(Corrupted))

        for match in matches:
            x, y = match
            prod = int(x) * int(y)
            total += prod

        print(f'Total ammount is: ${total}')

        # _______ PT 2 _____
        def ComplicatedThingForNoReason(Data: str):
            total2 = 0
            with open('temp.txt', 'w') as T:
                T.write(Data.replace('\n','').replace('do()','\ndo()').replace("don't()","\ndon't()"))

            with open('temp.txt', 'r') as F:
                pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
                TEMPMatch = []
                Match = []
                for Lines in F:
                    matches = re.findall(str(pattern), str(Lines))
                    if Lines.startswith('do()'):
                        TEMPMatch.append(matches)
                    elif Lines.startswith("don't()"):
                        pass
                    else:
                        TEMPMatch.append(matches)

                for items in TEMPMatch:
                    if isinstance(items, list):
                        Match.extend(items)
                    else:
                        Match.extend(items)

                for match in Match:
                    x, y = match
                    prod = int(x) * int(y)
                    total2 += prod

                print(f'Total ammount is: ${total2}')

        with open(File) as f:
            ComplicatedThingForNoReason(f.read())
