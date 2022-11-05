label sotry1:
    $ character = persistent.characters
    $ char0 = Character("???")
    
    
    $ char1 = character[0][CharName]
    $ char2 = character[1][CharName]
    $ char3 = character[2][CharName]
    $ char4 = character[3][CharName]
    $ char5 = character[4][CharName]
    $ char6 = character[5][CharName]
    $ char7 = character[6][CharName]
    $ char8 = character[7][CharName]
    $ char9 = character[8][CharName]
    $ char10 = character[9][CharName]
    if config.developer == True:
        $ renpy.notify("sotry1 called successfully")
        pause 2
    scene black with dissolve
    pause 0.5
    scene bg room_with_incubator with dissolve
    'The clock ticks away in the corner of the room as I pushed the next batch into the incubator.'
    char1 '23:46'
    'I scribble the time onto my clipboard'
    'The test will be over in the morning.'
    'Standing up to return to my office, to grab my clipboard and leave the room.'

    scene bg lab_hallway with dissolve

    'I walk down the hallway, clipboard in hand.'
    'Nobody else is in the lab at this time of night, and I should be home as well.'

    $ char1Upper = char1.upper()
    $ failedLastName = 0
    label definePreTransitionName:
    $ randomLastName = renpy.random.choice(defaultNames)
    $ randomLastNameUpper = randomLastName.upper()
    if char1Upper == randomLastNameUpper:
        $ failedLastName += 1
        jump definePreTransitionName
    if failedLastName > 0:
        call ifDebug("Failed " + str(failedLastName) + " times to generate a last name.")
    $ char1preTransition = char1Upper + " " + randomLastNameUpper

    'I enter my office as the words “[char1preTransition]” “AUTHORISED” appeared on the screen beside the door.'
    # sound ambient_buzz
    # need to find buzz sound

    'My office is silent but for the buzz of the distant air conditioning.'

    stop sound
    
    'I collect my things and head out, the doors locking behind me.'

    scene bg train with dissolve

    'I take the shinjuku line home.'
    'The train is empty, and I sit in the corner, staring out the window.'

    scene bg preBedroom with dissolve

    'Once home I collapse into bed, exhausted after a 26 hour shift.'

    # fade screen to black
    scene black with dissolve
    #play sound rooster_caw
    'A rooster crows from outside the window'
    'I wake up, groggy and disoriented.'
    show bg bedroom at wakeWithBlink
    'I sit up, blinking my eyes.'
    scene bg bedroom
    pause 1
    char1 'Where am I?'
    pause 1
    'A breeze blows through the open window.'
    'I stand up from my bed onto the cold hardwood floor'
    char1 'Ah!'
    'Im nearly knocked off balance by a newfound weightlessness.'
    'I peer out the window.'
    scene bg bedroom_window with dissolve
    char1 'What the hell?'
    char1 "Not to state the obvious, but this isn't Tokyo anymore."

    scene bg bedroom_door_open
    'The door opens behind me and a girl wearing a Victorian style maid outfit walked in.'

    show char2 at center

    char0 'Good morning lady [char1]! I hope you slept well!~'
    char0 'Breakfast will be ready in 20 minutes.'
    char1 'Thanks'

    hide char2

    'I search for and find a mirror'

    scene bg_with_shitty_code_aaaaaaaaa bedroom_mirror
    char1 "Damn it,{cps=1} {/cps}it's an isekai"
    python:
        if character[0][CharGender] == "Male":
            "narrator i guess" 'Previously [char1] was actually male but now that is not true so yea this text box is getting pretty long at some point it will just go off the page\nwhich will be the most boring joke possible to do in renpy i cant think of anymore text to out here now so imma just stop hopefully its gone off the screen by now'
        else:
            prevGender = "previously [char1] actually looked differently but i really dont wanna go code something that makes this text box different from the current state but i may do it later if this is in the final version that sucks but there is alot of other things that i need to do in a very complicated manner because renpy was built to do visual novels and it doesn't like me turning it into madlibs"
    
    '{b}Isekai{/b}' '{i}Noun{/i} ({i}Japanese fiction{/i}) A genre of Japanese fiction involving everyday people transported to alternate fantasy or virtual worlds.\n{i}Verb{/i} ({i}fandom slang{/i}) To transport into an alternate world\n{i} from Wiktionary, the free dictionary{/i}'
    'I need to figure out something about the princess so im not exiled or something for taking over her body'
    'I find a orb in a drawer that ive decided to call {i}"the orb of skipping alot of text that nobody wants to read"{/i} because it skips alot of text that nobody wants to read'
    'anyway nuclear fusion or something and the orb has fused into my hand'
    'also the screen {i}speedyExposition{/i} suddenly has a purpose'

    $ renpy.notify("exposition just sped up")
    call screen speedyExposition("Name: [char1]\nSex: Female\nHeight: 192\nWeight: 59 kg\nClass: Royalty\nFamily: Orisu\nAge: 15\nElemental Class: *\nMana: 999999E+9999")

    'damn,{cps=1} {/cps}its not only an isekai but an RPG'
    'Since I was the one who was transported here and I am in a position of power, I am most likely the main character.'
    
    show char2 at center

    char0 'Lady [char1]! Breakfast is ready!'

    call screen speedyExposition("Name: [char2]\nSex: Female\nHeight: 148 cm\nWeight: 40 kg\nClass: Servant\nFamily: Kiji\nAge: 12\nBlood: A+ | Pressure Nominal | Saturation Nominal\nAilment(s): Xenoderma")

    'It looks like I can see basic medical information about people. My objective is probably related'
    char1 'Alright, lets go'
    char2 'Yes, Lady [char1]!'

    show bg dining_hall with dissolve

    show char3 with dissolve

    char3 'Good morning, [char1], I hope you slept well'
    call screen speedyExposition("Name: [char3]\nSex: "+ character[2][CharGender] + "\nHeight: 201 cm\nWeight: 80 kg\nClass: Royalty\nFamily: Orisu\nAge: 17\nElemental Class: *\nMana: 500")

# 	At the dining hall I find only a boy, aged 17, sitting there. His name is Nomatsu Orisu, Hakaru’s older brother.
# “Good morning Haka, I hope you slept well,”  He said, smiling
# “Yes, it was an unusually sound sleep,” I said, hoping that wasn’t too out of the ordinary for me to say.
# “Well come on, sit down already. Why are you acting weird?”
# “I had a nightmare is all. Nothing to worry you.” I said while taking the seat opposite him. “And how did you sleep?”
# “Fine, I guess. Why are you talking so formal, you are my sister, you don’t need to talk like you are speaking to someone in the town.”
# “Oh yea, reflex I guess,” I say, taking note of the princess’s apparent and consistent informality.
# “The black death has apparently been spotted again in Europe. First time in 200 years,” he said.
# So I guess that's the problem that needs to be solved. That sounds like someone just decided to rush the plot along because they realised the intended plot would not fit on anything less than 50 pages. Luckily in the life I was just plucked out of I was a pharmacologist, and based on story logic and plot armour that means that I will be able to beat this plague and save the kingdom.
# “And how long until it reaches us?” I queried
# “It’s hard to tell but I’ve been assured at least 6 months. The royal pharmacist is already working on a treatment,”
# Whatever concoction that pharmacist is making will most likely do absolutely nothing if the apparent time period has anything to say about it. I’m going to have to take this into my own hands, but my sex and title will definitlely be a hinderance. If I'm going to try to save this kingdom I’ll have two paths I could take: I could spend time proving my proficiency in medicine, or I could attempt to manipulate the royal pharmacist to produce the antibiotic all on his own. My best bet will probably be to produce doxycycline all on my own and then convince my brother to distribute it to the people.

# --------------------------------------------

# 	Back in my room I try to see what other abilities the orb has granted me. Some things displayed on the plane are selectable and provide more information. I click on Elemental Class: * and it displays:
# 	Elemental Class: *
# 	The user wields the ability to manipulate AIR, FIRE, WATER, VOID, LIGHT, ATOMIC STRUCTURE
# 	Base mana usage: 1
# 	Maximum mana usage: 100
# 	Available mana: ? -1

# 	In this world magic seems to be a fact of life, if I’m to stop this plague this will definitely prove helpful. I’ll need to learn how to control my powers or I may cause untold damage.
# 	“Lady Hakaru, you need to get dressed, Lady Shinuki will be here in only a few minutes” said Shinomi who had walked in while I was thinking.
# 	“Alright,” I reply as Shinomi energetically walks over to a door I presume is the closet. From the closet she brings a very expensive looking purple and white dress, it has a skirt going down to the ankles, long sleeves, and a very fancy looking collar. She brings the dress over to me.
# 	“Undress, so I can put it on you,” she said.
# 	This took me by surprise, I still wasn’t used to being a girl and even before I wasn’t comfortable undressing in front of others. I reply, “O-ok” and cautious as to not lose my balance, strip down to my undergarments.
# 	“You seem surprised by this, are you alright?” Shinomi asks while dressing me.
# 	“Y-yea I’m fine. Just tired” I reply, still struggling to adjust for a lower centre of gravity.

# 	“And done!~” Shinomi says while guiding me to a mirror.
# 	Before me stands an actually pretty cute looking girl, at some point my hair was also brushed from a tangled mess to being straight and down to my hips.
# 	“You look beautiful, you highness,” Shinomi says with a hint of excitement in her voice.
# 	“Yes, I think I do,” I reply, slightly smiling towards her.

# --------------------------------------------

# 	Shinomi leads me to the gardens in front of the castle and dismisses herself, it is now that I finally can see the scale of the building.
# 	“Ah, there you are, your highness. I was beginning to believe you had overslept” called a voice from behind me. I turned around and found Shinuki Chinatsu, a 19 year old royal magic tutor. “Did you bring your wand?”
# 	“Uh, wand? I think I forgot it” I replied, trying to remember if I had seen a wand anywhere.
# 	“How could you forget that!? That is essential for our lessons!” she exclaimed exasperatedly.
# 	“I’m sorry, I am still waking up.”
# 	“Hmph. Well I guess if your mana is strong enough we could practice wandless magic.”
# “Here, close your eyes, and imagine your mana flowing into this ” she said, giving me an extremely reflective cube, “Depending on how bright it glows we can see your mana.”
# I do as she says, imagining a purple fluid flowing through my body. I force the fluid to flow towards the cube, and my hand begins to heat.
# “That’s a good amount of mana you have today, may be the most you’ve ever had.”
# I’m not done yet, I try harder. A tsunami of mana is forced into the tiny cube, I open by hand and see a rainbow of colours shining out of the cube.
# “Th-This can’t be, this is too much mana!” Shinuki exclaimes, “I’ve never seen a human capable of conducting this much mana in such a short amount of time!” She starts to back up, panic displaying on her face.
# The wind starts to pick up violently, swirling around me like a tornado. I try to stop channelling mana but it keeps flowing.
# “I can’t stop it!” I yell over the wind.
# 	Sparks begin coming out of the cube and a bush near me catches fire. I’ve got to be approaching this cube’s limit if I’ve not already passed it.
# 	“GET RID OF IT BEFORE IT EXPLODES!” Shinuki screams from across the garden, she is covered in leaves and dirt.
# 	I throw it as hard as I can towards a lake and it flies off, accelerating as it flies. I’m thrown off my feet by a supersonic boom as it far overshoots the river as it flies off towards the sky. It takes only 2 seconds for a second, much larger explosion to shake the ground and a fiery heat to cremate some birds in the faraway sky.
# 	“holy shit” I say under my breath
# 	Shinuki runs over, brushing the dirt and leaves off her white and gold dress. “Are you okay?”
# “Yea, I think I am,” I say while looking myself over. My hand is red but doesn’t burn. I touch it and small arcs of electricity jump to my other hand painlessly. “Whoa”
# “You need to see the royal pharmacist,” she says, grabbing my hand, “You just exerted more mana than you should have had in 20 years.”
# “I’m fine, I don’t need the pharmacist,” I say, resisting her pull.
# “You should be at least unconscious if not dead by now, you could collapse any minute” she persisted.
# “I’m fine,” I say truthfully, I’m not tired or dizzy at all. I try to channel mana into my feet so I can keep resisting her but the grass sparks and bursts into flames instead.
# Shinuki screams and drops my hand as her dress catches fire. She points her wand at her flaming dress and water shoots out, extinguishing it. I try to stomp on the flames to put them out but my dress catches fire instead. Shinuki shoots another jet of water towards me and the ground.
# “Have you forgotten how to control the effects of your mana?” Shinuki asks, with a hint of annoyance in her voice, “You’ve expelled raw mana of 4 elements twice now,” “You shouldn’t have any elements beyond fire and yet you’ve used wind, electricity, and light.”
# “
    return