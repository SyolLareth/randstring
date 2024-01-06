import random
#system variables
open("banlist.txt", "a").write("")
open("bank.txt", "a").write("")
bank=dict(open("bank.txt").read())
banlist=set(open("banlist.txt").read())
alph="aàáâäǎæãåābcdeèéêëěẽēėęfghiìíîïǐĩīıįjklmnñoóòôöǒœøõōpqrstuùúûüǔũūűůvwxyz '"
print("system: use /help to get system commands")
safemode=True
learnmode=True
while True:
    #cycle variables
    reply=input("you: ")
    string=""
    word=""
    count=0
    sentence=[]
    talkback=[]
    command=[]
    if reply[0]!="/":
        #processing phase
        for i in range(len(reply)):
            if reply[i].lower() in alph:
                word+=reply[i]
        sentence=word.split()
        #learning phase
        if len(sentence)!=1:
            for i in range(1, len(sentence)):
                if sentence[i-1] in bank:
                    bank[sentence[i-1]].append(sentence[i])
                else:
                    bank[sentence[i-1]]=[sentence[i]]
                if sentence[i] not in bank:
                    bank[sentence[i]]=[]
        elif sentence[0] not in bank:
            bank[sentence[0]]=[]
        open("bank.txt", "w").write(str(bank))
        #response phase(not functional. please fix banned word treatment)
        while bank!={}:
            suggest=""
            confirm=True
            randnum=0
            if talkback==[]:
                randnum=random.randint(0, len(bank)-1)
                suggest=list(bank.keys())[randnum]
                talkback.append(suggest)
                word=suggest
                count+=1
            elif bank[talkback[count-1]]!=[]:
                randnum=random.randint(0, len(bank[talkback[count-1]])-1)
                suggest=bank[talkback[count-1]][randnum]
                if learnmode:
                    print(bank[talkback[count-1]])
                    print("bot:", word, "/"+suggest+"/")
                    confirm=bool(int(input("system: confirm or deny the suggestion?(1/0)\nyou: ")))
                if confirm:
                    talkback.append(suggest)
                    word+=" "+suggest
                    count+=1
                else:
                    bank[talkback[count-1]].pop(randnum)
            else:
                break
        for i in range(len(talkback)):
            if safemode and talkback[i] in banlist:
                talkback[i]="[redacted]"
            string+=talkback[i]+" "
        print("bot:", string)
    else:
        #commands
        command=reply.split()
        if command[0]=="/banlist":
            for i in range(1, len(command)):
                banlist.add(command[i])
                open("banlist.txt", "w").write(str(banlist))
            print("system: banlist has been updated to", open("banlist.txt").read())
        elif command[0]=="/modeswitch":
            if command[1]=="safemode":
                safemode=not safemode
                print("system: safemode has switched to", safemode)
            elif command[1]=="learnmode":
                learnmode=not learnmode
                print("system: learnmode has switched to", learnmode)
            else:
                print("system: unknown mode")
        elif command[0]=="/help":
            print("system: /help: prints all system commands", "system: /modeswitch ['safemode'/'learnmode]:switches the state of the given mode", "system: /banlist [banword]: adds every provided word(separate by spaces) to the banlist", sep="\n")
        else:
            print("system: unknown command")