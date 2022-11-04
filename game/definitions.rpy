define titleText = renpy.random.choice(["california", "nobody ever expects the\nspanish inquisition", "*Thumbs up emoji*", "you are going to brazil", "can you hard boil an\negg by putting it\non a muffin tin in the oven\nat 100C?"])
define persistent.MC1 = []
define CharName = 0
define CharGender = 1
define CharPronoun = 2
define pShe = 0
define pHer = 1
define pHers = 2
define pHerself = 3
default autoFillPrompts = False
default autoFillRejected = False
default character = []
default persistent.characters = []
default names = []
default charactersFailed = 0
define testNameSet = ""
default expect = 0
default expectedNumber = 0


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

    transform wiggle:
        ease .1 xalign .2
        ease .1 xalign .8
        ease .1 xalign .3
        ease .1 xalign .7
        ease .1 xalign .4
        ease .1 xalign .6
        ease .1 xalign .5

    transform fade_in_right:
        xalign 0.3
        ease .5 xalign .5

    transform wakeWithBlink:
        alpha 0
        ease 1 alpha .7
        ease .5 alpha 0
        ease .5 alpha .7
        ease .3 alpha 0.3
        ease .4 alpha 1

    


