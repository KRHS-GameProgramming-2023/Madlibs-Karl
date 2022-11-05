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
default persistent.first_run = True


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

    image main_menu:
        "gui/new_main_menu.png"
        zoom 0.65
        xalign .5
        yalign .5

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

    transform slide_in:
        xalign 1
        ease .5 xalign .5

    transform menu_slide_in:
        xoffset -500
        time 1
        ease 1 xoffset 60

    transform menu_frame_slide_in:
        xoffset -500
        time .5
        ease 1 xoffset 0

    transform title_slide_in:
        yoffset 500
        ease 1 yoffset 0

    transform chaoticText:
        #make the text float around the screen on both the x and y axis

        ease .3 xalign 0.55 yalign 0.45
        ease .3 xalign 0.48 yalign 0.41
        ease .3 xalign 0.56 yalign 0.46
        ease .3 xalign 0.53 yalign 0.54
        ease .3 xalign 0.45 yalign 0.48
        ease .3 xalign 0.52 yalign 0.52
        ease .3 xalign 0.48 yalign 0.45
        ease .3 xalign 0.55 yalign 0.55
        ease .3 xalign 0.45 yalign 0.45
        ease .3 xalign 0.55 yalign 0.55


        repeat


    define music.main_menu = "audio/music/juhani-junkala-gentle-casual-gaming-loop.mp3"
    define music.loud_hum = "audio/fluoresent_light_hum_and_refrigerator-48831.mp3"
    define music.buzz = "audio/old-fan-56737.mp3"

    define pencil_short = "<to 1>audio/pencil-29272.mp3"
    define door_open = "<to 2>audio/door-opening-and-closing-18398.mp3"
    define door_close = "<from 4>audio/door-opening-and-closing-18398.mp3"
    define lock_beep = "<from 0.1 to 0.8>audio/heart-monitor-beep-96554.mp3"
    define lock_click = "<from .8 to 1.5>audio/door-lock-click-33617.mp3"


