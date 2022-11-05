label first_run:
    stop sound
    stop music
    scene black
    $ renpy.notify("pretend there is high tempo rock music playing that establishes a chaotic mood")
    pause 3
    call screen chaoticNoBorderText("ARE YOU READY FOR")
    call screen chaoticNoBorderText("THE WORST MISHMASH OF RANDOM ASSETS")
    call screen chaoticNoBorderText("YOU HAVE EVER SEEN?")
    call screen chaoticNoBorderText("WELL YOU BETTER BE\nBECAUSE HERE IT COMES")
    call screen chaoticNoBorderText("its like 12 am on nov 5 or something im gonna regret this\nwhen im sitting there tired trying not\nto let the mics start squeaking", timerTime=5)
    if config.developer == True:
        call screen confirm("Set persistent.first_run to False?", yes_action=Return(True), no_action=Return(False))
        if _return:
            $ persistent.first_run = False
            $ renpy.notify("persistent.first_run set to False.")
        else:
            $ renpy.notify("persistent.first_run left at True.")
    else:
        $ persistent.first_run = False
    return