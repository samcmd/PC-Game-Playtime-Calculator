import subprocess
import time

NV = apex = ps2 = rdr2 = p4g = nier = halo = re4 = re7 = rottr = rl = w3 = y0 = au = wii = fc3 = mc = baa = 0
loop = 1

while loop == 1:
    command = 'powershell "gps | where {$_.MainWindowTitle } | select ProcessName'
    apps = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    for line in apps.stdout:
        if line.rstrip():
            if line.decode().rstrip() == "NordVPN":
                loop = 0
            if line.decode().rstrip() == "FalloutNV":
                NV += 5
            elif line.decode().rstrip()== "r5apex":
                apex += 5
            elif line.decode().rstrip()== "pcsx2":
                ps2 += 5
            elif line.decode().rstrip()== "RDR2":
                rdr2 += 5
            elif line.decode().rstrip()== "P4G":
                p4g += 5
            elif line.decode().rstrip()== "NieRAutomata":
                nier += 5
            elif line.decode().rstrip()== "MCC-Win64-Shipping":
                halo += 5
            elif line.decode().rstrip()== "bio4":
                re4 += 5
            elif line.decode().rstrip()== "re7":
                re7 += 5
            elif line.decode().rstrip()== "ROTTR":
                rottr += 5
            elif line.decode().rstrip()== "RocketLeague":
                rl += 5
            elif line.decode().rstrip()== "witcher3":
                w3 += 5
            elif line.decode().rstrip()== "Yakuza0":
                y0 += 5
            elif line.decode().rstrip()== "Among Us":
                au += 5
            elif line.decode().rstrip()== "Dolphin":
                wii += 5
            elif line.decode().rstrip()== "farcry3_d3d11":
                fc3 += 5
            elif line.decode().rstrip()== "javaw":
                mc += 5
            elif line.decode().rstrip()== "ShippingPC-BmGame":
                baa += 5

                    
            # only print lines that are not empty
            # decode() is necessary to get rid of the binary string (b')
            # rstrip() to remove `\r\n`
            # print(line.decode().rstrip())

    time.sleep(300)
    
file1 = open("playtime.txt", "a")
if NV > 0:
    file1.write("NV: " + str(NV) + "\n")
if apex > 0:
    file1.write("apex: " + str(apex) + "\n")
if ps2 > 0:
    file1.write("ps2: " + str(ps2) + "\n")
if rdr2 > 0:
    file1.write("rdr2: " + str(rdr2) + "\n")
if p4g > 0:
    file1.write("p4g: " + str(p4g) + "\n")
if nier > 0:
    file1.write("nier: " + str(nier) + "\n")
if halo > 0:
    file1.write("halo: " + str(halo) + "\n")
if re4 > 0:
    file1.write("re4: " + str(re4) + "\n")
if re7 > 0:
    file1.write("re7: " + str(re7) + "\n")
if rottr > 0:
    file1.write("rottr: " + str(rottr) + "\n")
if rl > 0:
    file1.write("rl: " + str(rl) + "\n")
if w3 > 0:
    file1.write("w3: " + str(w3) + "\n")
if y0 > 0:
    file1.write("y0: " + str(y0) + "\n")
if au > 0:
    file1.write("au: " + str(au) + "\n")
if wii > 0:
    file1.write("wii: " + str(wii) + "\n")
if fc3 > 0:
    file1.write("fc3: " + str(fc3) + "\n")
if mc > 0:
    file1.write("mc: " + str(mc) + "\n")
if baa > 0:
    file1.write("baa: " + str(baa) + "\n")
file1.close()

# FalloutNV
# r5apex
# pcsx2
# RDR2
# P4G
# NieRAutomata
# MCC-Win64-Shipping
# bio4
# re7
# ROTTR
# RocketLeague
# witcher3
# Yakuza0
# Among Us
# Dolphin
# farcry3_d3d11
# javaw
# ShippingPC-BmGame
