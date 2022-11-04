label strToHEX(str):
    
    python:
        inpStr = str
        hexStr = ""
        if inpStr == "red":
            hexStr = "FF0000"
        elif inpStr == "green" or inpStr == "lime":
            hexStr = "00FF00"
        elif inpStr == "blue":
            hexStr = "0000FF"
        elif inpStr == "purple" or inpStr == "magenta":
            hexStr = "8400FF"
        elif inpStr == "yellow" or inpStr == "gold":
            hexStr = "FFFF00"
        elif inpStr == "white":
            hexStr = "FFFFFF"
        elif inpStr == "black":
            hexStr = "000000"
        elif inpStr == "orange":
            hexStr = "FFA500"
        elif inpStr == "pink":
            hexStr = "FFC0CB"
        elif inpStr == "brown":
            hexStr = "A52A2A"
        elif inpStr == "grey" or inpStr == "gray" or inpStr == "silver":
            hexStr = "808080"
        elif inpStr == "cyan":
            hexStr = "00FFFF"
    return