import pandas as pd
from os import system
from datetime import datetime
import pyautogui

def levelChange(lvl, tolvl):
    tolvl -= 1
    if tolvl == 0:
        if lvl > 0 and lvl < 4:
            lvl += 1
            tolvl = 1
        elif lvl > 3 and lvl < 6:
            lvl += 1
            tolvl = 2
        elif lvl > 5 and lvl < 10:
            lvl += 1
            tolvl = 3
        elif lvl > 9 and lvl < 13:
            lvl += 1
            tolvl = 4
        elif lvl > 12 and lvl < 17:
            lvl += 1
            tolvl = 5

    return str(lvl), str(tolvl)

def seeIfTrue(a, b):
    a, b = str(a),str(b)
    daya, dayb = int(a[:2]), int(b[:2])
    mona, monb = int(a[3:5]), int(b[3:5])
    ya, yb = int(a[6:10]), int(b[6:10])
    ha, hb = int(a[11:13]), int(b[11:13])
    ma, mb = int(a[14:16]), int(b[14:16])
    sa, sb = int(a[17:19]), int(b[17:19])
    if ya < yb:
        return 'YES'
    elif mona < monb:
        return 'YES'
    elif daya < dayb:
        return 'YES'
    elif ha + 3 < hb:
        return 'YES'
    else:
        x = (hb - ha) * 3600 + (mb - ma) * 60 + (sb - sa)
        if x > 10800:
            return 'YES'
        else:
            return 'NO'

def click(pozx, pozy):
    pyautogui.click(x = pozx, y = pozy)

def saveChanges(lista, castel):
    sheets = []
    for i in range(1, 5):
        if i != castel:
            sheets.append([pd.read_excel("Assets/Database.xlsx", sheet_name = f'Sheet{i}'), f'Sheet{i}'])
        else:
            sheets.append([lista, f'Sheet{castel}'])

    writer = pd.ExcelWriter("Assets/Database.xlsx")
    for sheet, name in sheets:
        sheet.to_excel(writer, sheet_name = name, index = False) 

    writer.save()

def getInfoFromExcel(castel, numarDeAtacat, ordine, n, a):

    #citim sheet ul asociat castelului de unde vrem sa atacam 
    lista = pd.read_excel('Assets/Database.xlsx', sheet_name = f'Sheet{castel}')

    #aducem lista la zi; schimbam coloana 'presents'
    lista['present'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    #dam refresh la lista pentru 'can atack'
    for index in range(20):
        lista.at[index,'can atack'] = seeIfTrue(lista.at[index,'last attack date'],lista.at[index, 'present'])

    if ordine == 1:
        #ordonate in functie de distanta
        lista = lista.sort_values(['can atack','dist','lvl', 'lvltolvl','ID'], ascending = [False, True, True, False, True])
    else:
        #ordonate in functie de level
        lista = lista.sort_values(['can atack','lvl', 'lvltolvl','dist','ID'], ascending = [False, True, False, True, True])

    cout = []
    #atasam datele castelelor intr-o ordine specificata
    for index, row in lista.iterrows():
        if row['can atack'] == 'YES' and numarDeAtacat > 0:
            #atasam datele casteleor dorite
            x, y, lvl, lvltolvl = row['pozx'], row['pozy'], row['lvl'], row['lvltolvl']
            cout.append([x, y, lvl, lvltolvl])
            numarDeAtacat -= 1
        
    #dam refresh la lista pentru 'can atack'
    for index in range(20):
        lista.at[index,'can atack'] = seeIfTrue(lista.at[index,'last attack date'],lista.at[index, 'present'])

    #atasam coordonatele castelelor individuale
    for index, row in lista.iterrows():
        if row['can atack'] == 'YES' and row['ID'] in a:
            #atasam datele casteleor dorite
            x, y, lvl, lvltolvl = row['pozx'], row['pozy'], row['lvl'], row['lvltolvl']
            cout.append([x, y, lvl, lvltolvl])

    #dam refresh la lista pentru 'can atack'
    for index in range(20):
        lista.at[index,'can atack'] = seeIfTrue(lista.at[index,'last attack date'],lista.at[index, 'present'])

    lista = lista.sort_values(['ID'])

    # Save the excel file    
    saveChanges(lista, castel)

    return cout

def changeData(castel, pozx, pozy):
    #citim sheet ul asociat castelului de unde vrem sa atacam
    lista = pd.read_excel('Assets/Database.xlsx', sheet_name = f'Sheet{castel}')

    #aducem lista la zi; schimbam coloana 'presents'
    lista['present'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    for index, row in lista.iterrows():
        if row['pozx'] == pozx and row['pozy'] == pozy:
            x, y, lvl, lvltolvl = row['pozx'], row['pozy'], row['lvl'], row['lvltolvl']
            #shimbam datele castelului dorit
            lista.at[index, 'last attack date'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            lista.at[index, 'lvl'], lista.at[index, 'lvltolvl'] = levelChange(lvl, lvltolvl)

    #dam refresh la lista pentru 'can atack'
    for index in range(20):
        lista.at[index,'can atack'] = seeIfTrue(lista.at[index,'last attack date'],lista.at[index, 'present'])

    # Save the excel file    
    saveChanges(lista, castel)
