import subprocess

def CatchIPDir():
        catchResult = subprocess.run(['netsh', 'interface', 'ipv4', 'show', 'config'], capture_output=True, text=True)
        cleanResult = catchResult.stdout.split('\n')
        CleanOutPut(str(cleanResult))

def CleanOutPut(chainIndex):
        cleanDDots = chainIndex.split(':')
        it = 0
        for i in cleanDDots:
            cleanApos = i.split("'")
            for i in cleanApos:
                if i.split() != ',':
                    print(i)
                    it += 1

CatchIPDir()