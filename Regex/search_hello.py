#Anthony Nguyen
#CS4550 Programming Languages
#Dr Tim Ball
import re

# search_file = input("What file do you want to search? ")
# search_file = 'test.txt'
search_file = 'warpeace.txt'
#search_term = input("What are you looking for? ")
with open(search_file, 'r') as sf:
    b = False
    i = 0
    print("Looking for Phone number")
    reg_ex = re.compile("([0-9][0-9][0-9]\-[0-9][0-9][0-9]\-[0-9][0-9][0-9][0-9]|1\-[0-9][0-9][0-9]\-[0-9][0-9][0-9]\-[0-9][0-9][0-9][0-9]|\([0-9][0-9][0-9]\)\s[0-9][0-9][0-9]\-[0-9][0-9][0-9][0-9])")
    for line in sf:
        # m = re.search(reg_ex, line)
        m = re.findall(reg_ex, line)
        if m:
            print("\nFound it!")
            print(line.strip())
            #print(m.group(0))
            for item in m:
                print(item)
                i += 1
            b = True
    if not b:
        print("Didn't find it.")
    else:
        print(f"Found {i} instances.")

with open(search_file, 'r') as sf:
    b = False
    i = 0
    print("Looking for Accounts numbers")
    reg_ex = re.compile("(([A-Z][A-Z])\-([0-9][0-9][0-9][0-9])\-([A-Z][0-9][0-9][0-9][0-9]))")
    for line in sf:
        # m = re.search(reg_ex, line)
        m = re.findall(reg_ex, line)
        if m:
            print("\nFound it!")
            print(line.strip())
            #print(m.group(0))
            for item in m:
                print(item)
                i += 1
            b = True
    if not b:
        print("Didn't find it.")
    else:
        print(f"Found {i} instances.")


with open(search_file, 'r') as sf:
    b = False
    i = 0
    print("Looking for SSN")
    reg_ex = re.compile("([0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9][0-9][0-9])")
    for line in sf:
        # m = re.search(reg_ex, line)
        m = re.findall(reg_ex, line)
        if m:
            print("\nFound it!")
            print(line.strip())
            #print(m.group(0))
            for item in m:
                print(item)
                i += 1
            b = True
    if not b:
        print("Didn't find it.")
    else:
        print(f"Found {i} instances.")
        

with open(search_file, 'r') as sf:
    b = False
    i = 0
    print("Looking for Date")
    reg_ex = re.compile("((0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/[0-9][0-9][0-9][0-9]|(0[1-9]|1[0-2])\-(0[1-9]|[12][0-9]|3[01])\-[0-9][0-9][0-9][0-9]|(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/[0-9][0-9]|(0[1-9]|1[0-2])\-(0[1-9]|[12][0-9]|3[01])\-[0-9][0-9])")
    for line in sf:
        # m = re.search(reg_ex, line)
        m = re.findall(reg_ex, line)
        if m:
            print("\nFound it!")
            print(line.strip())
            #print(m.group(0))
            for item in m:
                print(item)
                i += 1
            b = True
    if not b:
        print("Didn't find it.")
    else:
        print(f"Found {i} instances.")