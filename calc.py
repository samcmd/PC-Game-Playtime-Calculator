# Playtime stats python script

# Initialize variables to hold total playtime
NV = apex = ps2 = rdr2 = p4g = nier = halo = re4 = re7 = rottr = rl = w3 = y0 = au = wii = fc3 = mc = baa = 0

# Initialize variables to hold number of times played
NVc = apexc = ps2c = rdr2c = p4gc = nierc = haloc = re4c = re7c = rottrc = rlc = w3c = y0c = auc = wiic = fc3c = mcc = baac = 0

# Open playtime file
file1 = open("playtime.txt", "r")

# Read all lines in playtime file into a variable to run through
lines = file1.readlines()

# Read game ID and playtime in minutes from playtime document
for line in lines:

	# Split lines into array before the colon and after
	line1 = line.split(': ')

	# Remove newline characters
	line1[1] = line1[1].rstrip()

	# Add playtime to total and increment counter
	if line1[0] == "NV":
		NV += int(line1[1])
		NVc+=1
	if line1[0] == "wii":
		wii += int(line1[1])
		wiic+=1
	if line1[0] == "fc3":
		fc3 += int(line1[1])
		fc3c+=1
	if line1[0] == "baa":
		baa += int(line1[1])
		baac+=1
	if line1[0] == "rdr2":
		rdr2 += int(line1[1])
		rdr2c+=1
	if line1[0] == "p4g":
		p4g += int(line1[1])
		p4gc+=1
	if line1[0] == "nier":
		nier += int(line1[1])
		nierc+=1
	if line1[0] == "y0":
		y0 += int(line1[1])
		y0c+=1
	if line1[0] == "apex":
		apex += int(line1[1])
		apexc+=1
	if line1[0] == "ps2":
		ps2 += int(line1[1])
		ps2c+=1
	if line1[0] == "halo":
		halo += int(line1[1])
		haloc+=1
	if line1[0] == "re4":
		re4 += int(line1[1])
		re4c+=1
	if line1[0] == "re7":
		re7 += int(line1[1])
		re7c+=1
	if line1[0] == "rottr":
		rottr += int(line1[1])
		rottrc+=1
	if line1[0] == "rl":
		rl += int(line1[1])
		rlc+=1
	if line1[0] == "w3":
		w3 += int(line1[1])
		w3c+=1
	if line1[0] == "au":
		au += int(line1[1])
		auc+=1
	if line1[0] == "mc":
		mc += int(line1[1])
		mcc+=1

# Close playtime file
file1.close()

# Calculate average game time for each game played
if NV > 0:
	NVa = NV/NVc
if apex > 0:
	apexa = apex/apexc
if ps2 > 0:
	ps2a = ps2/ps2c
if rdr2 > 0:
	rdr2a = rdr2/rdr2c
if p4g > 0:
	p4ga = p4g/p4gc
if nier > 0:
	niera = nier/nierc
if halo > 0:
	haloa = halo/haloc
if re4 > 0:
	re4a = re4/re4c
if re7 > 0:
	re7a = re7/re7c
if rottr > 0:
	rottra = rottr/rottrc
if rl > 0:
	rla = rl/rlc
if w3 > 0:
	w3a = w3/w3c
if y0 > 0:
	y0a = y0/y0c
if au > 0:
	aua = au/auc
if wii > 0:
	wiia = wii/wiic
if fc3 > 0:
	fc3a = fc3/fc3c
if mc > 0:
	mca = mc/mcc
if baa > 0:
	baaa = baa/baac

# Create a new file to write playtime stats to
file2 = open("playtime_stats.txt", "w")

# Create total playtime header
file2.write("Total Playtime in minutes:\n\n")

# Write total playtime for each game played
if NV > 0:
	file2.write("     Fallout New Vegas: " + str(NV) + "\n")
if apex > 0:
	file2.write("     Apex Legends: " + str(apex) + "\n")
if ps2 > 0:
	file2.write("     PCSX2: " + str(ps2) + "\n")
if rdr2 > 0:
	file2.write("     Red Dead Redemption 2: " + str(rdr2) + "\n")
if p4g > 0:
	file2.write("     Persona 4 Golden: " + str(p4g) + "\n")
if nier > 0:
	file2.write("     Nier Automata: " + str(nier) + "\n")
if halo > 0:
	file2.write("     Halo Master Chief Collection: " + str(halo) + "\n")
if re4 > 0:
	file2.write("     Resident Evil 4: " + str(re4) + "\n")
if re7 > 0:
	file2.write("     Resident Evil 7: " + str(re7) + "\n")
if rottr > 0:
	file2.write("     Rise of the Tomb Raider: " + str(rottr) + "\n")
if rl > 0:
	file2.write("     Rocket League: " + str(rl) + "\n")
if w3 > 0:
	file2.write("     Witcher 3: " + str(NV) + "\n")
if y0 > 0:
	file2.write("     Yakuza 0: " + str(y0) + "\n")
if au > 0:
	file2.write("     Among Us: " + str(au) + "\n")
if wii > 0:
	file2.write("     Dolphin: " + str(wii) + "\n")
if fc3> 0:
	file2.write("     Far Cry 3: " + str(fc3) + "\n")
if mc > 0:
	file2.write("     Minecraft: " + str(mc) + "\n")
if baa > 0:
	file2.write("     Batman Arkham Asylum: " + str(baa) + "\n")

# Create header for number of times played
file2.write("\n\nNumber of times played:\n\n")

# Write number of times played for each game played
if NV > 0:
	file2.write("     Fallout New Vegas: " + str(NVc) + "\n")
if apex > 0:
        file2.write("     Apex Legends: " + str(apexc) + "\n")
if ps2 > 0:
        file2.write("     PCSX2: " + str(ps2c) + "\n")
if rdr2 > 0:
        file2.write("     Red Dead Redemption 2: " + str(rdr2c) + "\n")
if p4g > 0:
        file2.write("     Persona 4 Golden: " + str(p4gc) + "\n")
if nier > 0:
        file2.write("     Nier Automata: " + str(nierc) + "\n")
if halo > 0:
        file2.write("     Halo Master Chief Collection: " + str(haloc) + "\n")
if re4 > 0:
        file2.write("     Resident Evil 4: " + str(re4c) + "\n")
if re7 > 0:
        file2.write("     Resident Evil 7: " + str(re7c) + "\n")
if rottr > 0:
        file2.write("     Rise of the Tomb Raider: " + str(rottrc) + "\n")
if rl > 0:
        file2.write("     Rocket League: " + str(rlc) + "\n")
if w3 > 0:
        file2.write("     Witcher 3: " + str(w3c) + "\n")
if y0 > 0:
        file2.write("     Yakuza 0: " + str(y0c) + "\n")
if au > 0:
        file2.write("     Among Us: " + str(auc) + "\n")
if wii > 0:
        file2.write("     Dolphin: " + str(wiic) + "\n")
if fc3> 0:
        file2.write("     Far Cry 3: " + str(fc3c) + "\n")
if mc > 0:
        file2.write("     Minecraft: " + str(mcc) + "\n")
if baa > 0:
        file2.write("     Batman Arkham Asylum: " + str(baac) + "\n")

# Create header for average time played
file2.write("\n\nAverage Time Played in minutes:\n\n")

# Write average time played for each game played
if NV > 0:
        file2.write("     Fallout New Vegas: " + str(NVa) + "\n")
if apex > 0:
        file2.write("     Apex Legends: " + str(apexa) + "\n")
if ps2 > 0:
        file2.write("     PCSX2: " + str(ps2a) + "\n")
if rdr2 > 0:
        file2.write("     Red Dead Redemption 2: " + str(rdr2a) + "\n")
if p4g > 0:
        file2.write("     Persona 4 Golden: " + str(p4ga) + "\n")
if nier > 0:
        file2.write("     Nier Automata: " + str(niera) + "\n")
if halo > 0:
        file2.write("     Halo Master Chief Collection: " + str(haloa) + "\n")
if re4 > 0:
        file2.write("     Resident Evil 4: " + str(re4a) + "\n")
if re7 > 0:
        file2.write("     Resident Evil 7: " + str(re7a) + "\n")
if rottr > 0:
        file2.write("     Rise of the Tomb Raider: " + str(rottra) + "\n")
if rl > 0:
        file2.write("     Rocket League: " + str(rla) + "\n")
if w3 > 0:
        file2.write("     Witcher 3: " + str(w3a) + "\n")
if y0 > 0:
        file2.write("     Yakuza 0: " + str(y0a) + "\n")
if au > 0:
        file2.write("     Among Us: " + str(aua) + "\n")
if wii > 0:
        file2.write("     Dolphin: " + str(wiia) + "\n")
if fc3> 0:
        file2.write("     Far Cry 3: " + str(fc3a) + "\n")
if mc > 0:
        file2.write("     Minecraft: " + str(mca) + "\n")
if baa > 0:
        file2.write("     Batman Arkham Asylum: " + str(baaa) + "\n")

# Create array to hold most played game
big = [str(NV),"     Fallout New Vegas"]

# Check to see which game has most play time
if apex > int(big[0]):
	big = [str(apex),"     Apex Legends"]
if ps2 > int(big[0]):
        big = [str(ps2),"     PCSX2"]
if rdr2 > int(big[0]):
        big = [str(rdr2),"     Red Dead Redemption 2"]
if p4g > int(big[0]):
        big = [str(p4g),"     Persona 4 Golden"]
if nier > int(big[0]):
        big = [str(nier),"     Nier Automata"]
if halo > int(big[0]):
        big = [str(halo),"     Halo Master Chief Collection"]
if re4 > int(big[0]):
        big = [str(re4),"     Resident Evil 4"]
if re7 > int(big[0]):
        big = [str(re7),"     Resident Evil 7"]
if rottr > int(big[0]):
        big = [str(rottr),"     Rise of the Tomb Raider"]
if rl > int(big[0]):
        big = [str(rl),"     Rocket League"]
if w3 > int(big[0]):
        big = [str(w3),"     Witcher 3"]
if y0 > int(big[0]):
        big = [str(y0),"     Yakuza 0"]
if au > int(big[0]):
        big = [str(au),"     Among Us"]
if wii > int(big[0]):
        big = [str(wii),"     Dolphin"]
if fc3 > int(big[0]):
        big = [str(fc3),"     Far Cry 3"]
if mc > int(big[0]):
        big = [str(mc),"     Minecraft"]
if baa > int(big[0]):
        big = [str(baa),"     Batman Arkham Asylum"]

# Create heading for most played games
file2.write("\n\nMost Played Game:\n\n")

# Write most played game title to file
file2.write(big[1])

# Close playtime stats file
file2.close()
