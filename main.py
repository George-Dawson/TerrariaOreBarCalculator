def main():
    try:
        Ores3 = ['copper','tin','iron','lead','cobalt','palladium','demonite','crimtane','meteorite','hellstone']
        Ores4 = ['silver','tungsten','gold','platinum','mythril','orichalcum']
        Ores5 = ['adamantite','titanium','luminite','chlorophyte']
        bars = ['hallowed','spectre','shroomite']

        whatOre = input('What ore/bar would you like to craft? ')
        howMuch = int(input('How many bars do you want to make? '))
        if whatOre.lower() in Ores3:
            if whatOre.lower() == 'hellstone':
                print('{} needs {} ore and {} obsidian to make {} bars.'.format(whatOre.capitalize(),howMuch*3,howMuch,howMuch))
            else:
                print('{} needs {} ore to make {} bars.'.format(whatOre.capitalize(),howMuch*3,howMuch))

        elif whatOre.lower() in Ores4:
            print('{} needs {} ore to make {} bars.'.format(whatOre.capitalize(),howMuch*4,howMuch))

        elif whatOre.lower() in Ores5:
            print('{} needs {} ore to make {} bars.'.format(whatOre.capitalize(),howMuch*5,howMuch))

        elif whatOre.lower() in bars:
            if whatOre.lower() == 'spectre':
                print('{} needs {} chlorophyte bars and {} ectoplasm to make {} bars.'.format(whatOre.capitalize(),howMuch*2,howMuch,howMuch))
            elif whatOre.lower() == 'shroomite':
                print('{} needs {} chlorophyte bars and {} glowing mushrooms to make {} bars.'.format(whatOre.capitalize(),howMuch,howMuch*15,howMuch))
            else:
                print('These are non-craftable bars either dropped by bosses or crafted using combinations of different materials. LMK if you want to see these come into the program.')

        else:
            print('Invalid ore type')
    except Exception as err:
        print(err)

while True:
    main()