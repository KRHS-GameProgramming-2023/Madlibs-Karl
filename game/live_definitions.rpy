label char_name():
    python:
        randomName = renpy.random.choice(defaultNames)
    call screen def_charName(prompt="Enter a name", defaultInput=randomName)

    if _return.lower() in swears:
        call screen dialog(message='Name cannot be "[_return]"', ok_action=Return())
        jump char_name
    if _return.lower() == "":
        call screen dialog(message='Name cannot be blank', ok_action=Return())
        jump char_name
    if _return.lower() == " " or _return.lower() == "  " or _return.lower() == "   " or _return.lower() == "    " or _return.lower() == "     ":
        call screen dialog(message='how the fuck', ok_action=Return())
        jump char_name
    
    $ tempName = _return
    return

label char_gender():
    call screen def_charGender("Enter [tempName]'s gender")
    $ tempGender = _return
    python:
        if tempGender == "Female":
            tempPronounVar = ["She", "Her", "Hers", "Herself"]
        else:
            tempPronounVar = ["He", "Him", "His", "Himself"]

    return
        
label char_arrange:
    $ combinedList = [tempName, tempGender, tempPronounVar]
    $ character.append(combinedList)
    $ persistent.characters = character
    $ del combinedList
    $ del tempName
    $ del tempGender
    $ del tempPronounVar
    return


label chars_create():
    call char_name from _call_char_name
    call char_gender from _call_char_gender
    call char_arrange from _call_char_arrange
    python:
        charsToCreate -= 1
    if 0 < charsToCreate:
        jump chars_create
    else:
        return

label createCharacters(num, defaultName=["Hakaru","Shinomi","Kashita","Minomi","Nomuri","Zekaru","Osake","Rizoto","Chinomi","Kaguya","Asuka","Ake","Ohayou","Sayoru","Yuka","Minesa","Kazeshi","Yunomi","Shitana","Ritama","Tsunde","Yande","Demi","Zoski","Kazeshi","Nomita","Roku","Shiromi","Kasoki","Resoki","Rekezo","Shishi","Takesa","Noabeku","Taoshi","Mineme","Noshiko","Asano"]):
    $ charsToCreate = num
    $ defaultNames = defaultName
    call chars_create from _call_chars_create
    $ del charsToCreate
    $ del defaultNames
    $ del randomName

    if config.developer == True:
        # list the names of the characters
        $ nameList = []
        $ i = 0
        $ numberOfChars = len(persistent.characters)
        while i < numberOfChars:
            $ tempName = persistent.characters[i][CharName]
            $ nameList.append(tempName)
            $ i += 1
        call screen dialog("Succesfully created [numberOfChars] characters.\n[nameList]", ok_action=Return())
        $ del nameList
        $ del numberOfChars
    return