define titleText = renpy.random.choice(["california", "nobody ever expects the\nspanish inquisition", "*Thumbs up emoji*", "you are going to brazil"])
define persistent.MC1 = []
define character = []
define persistent.characters = character
define CharName = 0
define CharGender = 1
define CharPronoun = 2
define pShe = 0
define pHer = 1
define pHers = 2
define pHerself = 3
default autoFillPrompts = False
default autoFillRejected = False

init python:
    config.use_cpickle = False


init:

    image bg pregen 02:
        "pregen_bg_02.png"
        zoom 0.94

    image black = "#000"
    image white = "#fff"
    #screens

    image bg_start:
        "images/start_bg.png"
        zoom 0.94

    image bg room_with_incubator:
        "modern_laboratory_room__lights_off__incubator_against_a_wall__anime_Seed-7720237_Steps-50_Guidance-7.5.png"
        zoom 0.63

    image bg lab_hallway:
        "images/lab_hallway.png"
        zoom 0.65
    


