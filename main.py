#Sten Sax Påste mot slumpade dator, bäst av 3
import random
spelarepoäng = 0
datorpoäng = 0
någon_vunnit = False


while någon_vunnit == False:
    # Skaffar spelares drag

    spelare_val = input("välj sten, sax eller påse: ")
    # Skaffa datorn slumpat

    datorns_val = random.randint(1,3)
    # Loop som kör dragen
        #Kolla om någon har vunnit (fått poäng)
    if datorns_val == 1:
        datorns_val = "sten"
    elif datorns_val == 2:
        datrons_val = "sax"
    else:
        datorns_val = "påse"
   # print(datorns_val)

    #avgöra vem som vann rundan
    if spelare_val == "sten" and datorns_val == "sax": #vinst
        spelarepoäng += 1
    elif spelare_val == "sten" and datorns_val == "påse": #förlust
        datorpoäng +=1
    elif spelare_val == "sax" and datorns_val == "sten": #förlust
        datorpoäng += 1
    elif spelare_val == "sax" and datorns_val == "påse":  # vinst
        spelarepoäng += 1
    elif spelare_val == "påse" and datorns_val == "sten":  # vinst
        spelarepoäng += 1
    elif spelare_val == "påse" and datorns_val == "sax":  # förlust
        datorpoäng += 1
    else:
        print("Lika inga poäng")

    print("spelare poäng: " + str(spelarepoäng))
    print("datorns poäng: " + str(datorpoäng))

    if spelarepoäng == 2:
        någon_vunnit = True
        print("Du vann!!!")
    elif datorpoäng == 2:
        någon_vunnit = True
        print("Du förlorade!!!")
