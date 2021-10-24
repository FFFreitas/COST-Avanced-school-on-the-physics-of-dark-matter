import sys
input_csv = sys.argv[1]
output_csv = sys.argv[2]


# modify these if you want a max number of objects
maxmet = 1
maxmetphi = 1
maxjet = 3
maxbjet = 2
maxelec = 2
maxpos = 2
maxmumin = 2
maxmuplus = 2
maxgam = 1
lengths = [maxmet, maxmetphi,maxjet*4,maxbjet*4,maxelec*4,maxpos*4,maxmumin*4,maxmuplus*4,maxgam*4]
objects = [[],[],[],[],[],[],[],[],[]]
m  = 0
txt = open(input_csv)
for line in txt:
	obhold = [[],[],[],[],[],[],[],[],[]]
	if ";" in line:
		split = line.split(";")
		obhold[0].append(split[3])
		obhold[1].append(split[4])
		for k in range(3, len(split)):
			new=split[k].split(",")
			#print(new[0], len(new))
			if new[0] == "j":
				for l in range(1,len(new)):
					obhold[2].append(new[l])
			elif new[0] == "b":
				for l in range(1,len(new)):
					obhold[3].append(new[l])
			elif new[0] == "e+":
				for l in range(1,len(new)):
					obhold[4].append(new[l])
			elif new[0] == "e-":
				for l in range(1,len(new)):
					obhold[5].append(new[l])
			elif new[0] == "m+":
				for l in range(1,len(new)):
					obhold[6].append(new[l])
			elif new[0] == "m-":
				for l in range(1,len(new)):
					obhold[7].append(new[l])
			elif new[0] == "a":
				for l in range(1,len(new)):
					obhold[8].append(new[l])
	for k in range(0,9):
		objects[k].append(obhold[k])
	m = m + 1

txt.close()	
txt = open(output_csv,"w")
for i in range(0,9):
	if lengths[i] < 0:
		txt.write(str(max([len(k) for k in objects[i]]))+" ")
		lengths[i] = int(max([len(k) for k in objects[i]]))
	else:
		txt.write(str(lengths[i])+" ")
txt.write("\n")
for k in range(0,m):
	linewrite = ""
	for i in range(0,9):
		for l in range(0,lengths[i]):
			if l+1 > lengths[i] and lengths[i]>=0:
				continue
			if l+1 > len(objects[i][k]):
				linewrite = linewrite+"0"+","
			else:
				linewrite=linewrite+str(objects[i][k][l])+","
	txt.write(linewrite[:-1]+"\n")
txt.close()
