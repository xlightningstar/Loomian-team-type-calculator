import colorama
from colorama import Fore
from prettytable import PrettyTable

#fire-0,water-1,plant-2,light-3,dark-4,ice-5,electric-6,air-7,bug-8,earth-9,toxic-10,metal-11,ancient-12,spirit-13,brawler-14,mind-15,typeless-16,none-17
table = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #None
  [0.5,2,0.5,1,1,0.5,1,2,0.5,2,1,0.5,1,1,1,1,1], #Fire
  [0.5,0.5,2,1,1,0.5,2,1,1,1,2,0.5,1,1,1,1,1], #Water
  [2,0.5,0.5,0,2,2,0.5,1,2,0.5,2,1,1,1,1,1,1], #Plant
  [0.5,1,1,0.5,2,1,1,1,1,1,1,2,0.5,0,1,1,1], #Light
  [2,1,1,2,0.5,1,1,1,2,1,1,1,1,0.5,1,0.5,1], #Dark
  [2,1,1,1,1,0.5,1,0.5,1,1,1,2,1,1,2,1,0.5], #Ice
  [1,2,1,1,1,1,0.5,0.5,1,2,1,0.5,1,1,1,1,1], #Electric
  [1,1,1,1,1,2,2,1,0.5,0,1,1,1,1,0.5,1,1],   #Air
  [1,1,0.5,1,0.5,2,1,2,0.5,0.5,1,1,1,1,2,1,1], #Bug
  [1,2,2,1,1,2,0,1,1,1,0.5,1,1,1,1,1,1],      #Earth
  [1,1,0.5,1,1,1,1,1,1,2,0.5,1,1,1,0.5,2,1],  #Toxic
  [2,1,1,1,1,0.5,2,0.5,0.5,2,1,0.5,0.5,1,2,0.5,0.5], #Metal
  [0.5,0.5,0.5,2,1,1,0.5,1,1,1,1,2,2,0.5,1,1,1],    #Ancient
  [1,1,1,2,0.5,1,0.5,1,1,1,0.5,1,2,2,0,1,0.5],    #Spirit
  [1,1,1,1,1,0.5,1,2,0.5,1,2,1,1,2,1,2,1],      #Brawler
  [1,1,1,0.5,2,1,1,1,2,1,1,1,1,2,0.5,0.5,1],   #Mind
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1]          #Typeless
  ]

loomtypes = [["/",0],["fire",1],["water",2],["plant",3],["light",4],["dark",5],["ice",6],["electric",7],["air",8],["bug",9],["earth",10],["toxic",11],["metal",12],["ancient",13],["spirit",14],["brawler",15],["mind",16],["typeless",17]]
loomlist = []

#info on how to work the program
print("")
print(Fore.WHITE+"Type your loomian types one after the other e.g. 'mind spirit' or 'fire'")
print("")

#Gets the number of loomians on the team
def howManyLooms():
    while True:
        loomnum = input("How many loomians do you want to include in your team? (1-6) ")
        try:
          loomnum = int(loomnum)
        except ValueError:
          pass
        if type(loomnum) == int and loomnum > 0 and loomnum <= 6:
            break
        else:
            print("The number entered appears to be invalid, try again")
    return(loomnum)

#checks if the loom types entered are valid
def checkIfValid(loomtypes,loomtype):
  valid = False
  typenum = len(loomtype)
  for i in range(0,typenum):
      for x in range(0,len(loomtypes)):
        if loomtypes[x][0] == loomtype[i]:
          loomtype.insert(i+2,loomtypes[x][1])
          if typenum == 1:
            valid = True
          elif typenum == 2:
            if i == 0:
                valid = "Half"
            if i == 1 and valid == "Half":
                valid = True
  if valid == True:
    return True
  else:
    return False

#finds the effectivenesses against every loomian overall
def findTeamTypeEffects(loomlist):
  teamEffects = []

  for i in range(len(loomlist)):
    effects = []
    if len(loomlist[i]) == 2:
        typenum = 1
    elif len(loomlist[i]) == 4:
        typenum = 2

    for tableval in range(len(table[0])):
      
      if typenum == 2:
        value=table[loomlist[i][2]][tableval]*table[loomlist[i][3]][tableval]
      elif typenum == 1:
        value=table[loomlist[i][1]][tableval]
      effects.append(value)

    teamEffects.append(effects)
  return teamEffects

#finds the effectivenesses against the entire team
def findAllEffects(teamEffects):
  allEffects = []
  for i in range(len(teamEffects[0])):
    effects = []
    add = 0
    for loom in range(len(teamEffects)):
      effects.append(teamEffects[loom][i])
    for num in range(len(effects)):
      if effects[num] > 1:
        add += 1
      elif effects[num] > 0 and effects[num] < 1:
        add -= 1
      elif effects[num] == 0:
        add -= 1
    allEffects.append(add)
  return allEffects

loomnum = howManyLooms()
print("")
    
#gets the loomian type inputs
for i in range(loomnum):
  while True:
    loomtype = input("What type is loomian "+str(i+1)+"? ")
    loomtype.lower()
    loomtype = loomtype.split()
    if len(loomtype) != 1 and len(loomtype) != 2:
      print("Make sure you enter either one or two loomian types")
    elif checkIfValid(loomtypes,loomtype) == True:
      loomlist.append(loomtype)
      break
    else:
      print("Loomian type entered is invalid")
print("")

teamEffects = findTeamTypeEffects(loomlist)
allEffects = findAllEffects(teamEffects)

type_table = PrettyTable()
type_table.field_names = ["Loom","Weaknesses","Resistances"]

#prints overall weaknesses and resistances
resisted = []
for i in range(len(teamEffects)):
  row = []
  row.append("loom "+str(i+1))
  row.append("")
  for j in range(len(teamEffects[0])):
    if teamEffects[i][j] == 2:
      row[len(row)-1]+=("["+Fore.YELLOW+loomtypes[j+1][0]+Fore.WHITE+"]"+" ")
  for j in range(len(teamEffects[0])):
    if teamEffects[i][j] > 2:
      row[len(row)-1]+=("["+Fore.RED+loomtypes[j+1][0]+" x"+str(teamEffects[i][j])+Fore.WHITE+"]"+" ")
  row.append("")
  for j in range(len(teamEffects[0])):
    if teamEffects[i][j] == 0.5:
      row[len(row)-1]+=("["+Fore.GREEN+loomtypes[j+1][0]+Fore.WHITE+"]"+" ")
      if loomtypes[j+1][0] not in resisted:
        resisted.append(loomtypes[j+1][0])
  for j in range(len(teamEffects[0])):
    if teamEffects[i][j] < 0.5 and teamEffects[i][j] > 0:
      row[len(row)-1]+=("["+Fore.CYAN+loomtypes[j+1][0]+" x"+str(int(1/teamEffects[i][j]))+Fore.WHITE+"]"+" ")
      if loomtypes[j+1][0] not in resisted:
        resisted.append(loomtypes[j+1][0])
  for j in range(len(teamEffects[0])):
    if teamEffects[i][j] == 0:
      row[len(row)-1]+=("["+Fore.MAGENTA+loomtypes[j+1][0]+" imn"+Fore.WHITE+"]"+" ")
      if loomtypes[j+1][0] not in resisted:
        resisted.append(loomtypes[j+1][0])
  type_table.add_row(row)

row = ["","",""]
type_table.add_row(row)

row = []
row.append("team")
row.append("")
for j in range(len(allEffects)):
  if allEffects[j] == 1:
    row[len(row)-1]+=("["+Fore.YELLOW+loomtypes[j+1][0]+Fore.WHITE+"]"+" ")
for j in range(len(allEffects)):
  if allEffects[j] >= 2:
    row[len(row)-1]+=("["+Fore.RED+loomtypes[j+1][0]+" x"+str(allEffects[j])+Fore.WHITE+"]"+" ")
row.append("")
for j in range(len(allEffects)):
  if allEffects[j] == -1:
    row[len(row)-1]+=("["+Fore.GREEN+loomtypes[j+1][0]+Fore.WHITE+"]"+" ")
for j in range(len(allEffects)):
  if allEffects[j] < -1:
    row[len(row)-1]+=("["+Fore.CYAN+loomtypes[j+1][0]+" x"+str(int(-1*allEffects[j]))+Fore.WHITE+"]"+" ")
type_table.add_row(row)

print(Fore.WHITE)
print(type_table)

unresisted = []
for i in range(1,len(loomtypes)):
  if loomtypes[i][0] not in resisted:
    unresisted.append(loomtypes[i][0])

print(Fore.YELLOW+"Unresisted: ",end=" ")
for i in range(len(unresisted)):
  print(Fore.YELLOW+"["+unresisted[i]+"]",end=" ")

if unresisted == []:
  print(Fore.RED+"N"+Fore.LIGHTYELLOW_EX+"o"+Fore.YELLOW+"t"+Fore.GREEN+"h"+Fore.BLUE+"i"+Fore.CYAN+"n"+Fore.MAGENTA+"g"+Fore.WHITE+"!")

print(Fore.WHITE)
print("")