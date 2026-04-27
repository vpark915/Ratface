# Auto-generated Ren'Py decision tree template
# Source: ratFace.json

# Subscript and superscript.
init -1 python hide:

    FONT_SIZE = gui.text_size
    SUPERSCRIPT_SCALE = 0.5
    # These values might depend on font and were adjusted to look good
    # on a particular one.
    SUPERSCRIPT_ANCHOR = 0.15
    SUBSCRIPT_ANCHOR = -0.88

    def superscript_tag(tag, arg, text):
        result = []
        for element in text:
            if element[0] == renpy.TEXT_TEXT:
                for letter in element[1]:
                    result += [(
                        renpy.TEXT_DISPLAYABLE,
                        Transform(
                            Text(letter,style="superscript"),
                            yanchor = SUPERSCRIPT_ANCHOR,
                            zoom = SUPERSCRIPT_SCALE
                        ))]
            else:
                result.append(element)
        return result

    def subscript_tag(tag, arg, text):
        result = []
        for element in text:
            if element[0] == renpy.TEXT_TEXT:
                for letter in element[1]:
                    result += [(
                        renpy.TEXT_DISPLAYABLE,
                        Transform(
                            Text(letter,style="subscript"),
                            yanchor = SUBSCRIPT_ANCHOR,
                            zoom = SUPERSCRIPT_SCALE
                        ))]
            else:
                result.append(element)
        return result

    config.custom_text_tags["sup"] = superscript_tag
    config.custom_text_tags["sub"] = subscript_tag

style subscript is default
style superscript is default

default identifyBool = False
default name = "????"
default status = "Oblivion"
default linkedin = "???"
default otterEnd = False
default nameEnd = False
default singEnd = False
default diceRoll = 0
default beerBool = False
default lionName = "Powerful Lion"

define you = Character("[name]", color="#242e78")
define vapeHyena = Character("Hyena Vape-Teen", color="#d12a2a")
define skateHyena = Character("Hyena Skate-Teen", color="#d12a2a")
define normHyena = Character("Hyena Asshole-Teen", color="#d12a2a")
define police = Character("Police",color="#373a77")
define drunkRat = Character("Bum Rat",color="#404c33")
define lion = Character("[lionName]",color="#ffb22d")
define otter = Character("Mr.Otter", color="#2d222c")
define cuteDog = Character("Elegant Small Creature", color="#ccfdff")

image flash = Solid("#ffffff")

#character definition
image ratFace = Transform("ratFace.png",yoffset=200)
image ratFaceSad = Transform("ratFace hurt.png",yoffset=200)
image ratFaceDrunk = Transform("ratFace drunk.png",yoffset=200)
image hyenaNormal = Transform("hyena normal.png",yoffset=200)
image hyenaSkate = Transform("hyena skate.png",yoffset=200)
image hyenaVape = Transform("hyena vape.png",yoffset=200)
image police = Transform("police.png",yoffset=200)
image lion = Transform("lion.png",yoffset=200)
image otter = Transform("otter.png",yoffset=200)
image drunkRat = Transform("drunkRat.png",yoffset=200)
image cuteDog = Transform("friendlyDog.png",yoffset=500)

image cTrain = "cTrainAlternative.png"
image subwayPlat = "subwayPlat.png"
image subwayAlt = "subwayCarAlt.png"
image closingDoors = "closingDoors.png"
image warRoom = "warRoom.png"
image slide = "slide.png"
image subwayOpen = "anotherNeighborhood.png"
image beautiful = "beautifulNeighborhood.png"
image apartmentFront = "apartmentFront.png"
image stairwell = "stairwell.png"
image apartmentDoor = "apartmentDoor.png"

screen stats_display():
    frame:
        xalign 0.5
        yalign 0.02
        background "#00000080"
        padding (20, 10)
        hbox:
            text "Name: [name]    |   Status: [status]    |   Linkedin: [linkedin]" color "#ffffff"

label start:
    stop sound
    # Show it so it stays on screen
    show screen stats_display
    jump Start

label Start:
    stop sound
    # Passage: Start
    scene black with dissolve
    play music "audio/FloatySoundscape.mp3" fadein 2.0 loop
    play sound "audio/Narration/thecolorisblack.mp3"
    "The color is black. A mix of drowsiness and nausea fight for first place in your god-forsaken mind. It's your choice. Risk seeing what's out there, or simply lay flat, practically dead."
    menu:
        "Lay flat":
            jump deadChoice
        "Open eyes":
            jump openEyeChoice

label header:
    stop sound
    # Passage: header
    # Template-only state/setup passage.
    return
label deadChoice:
    stop sound
    # Passage: deadChoice
    play sound "audio/Narration/silenceitsthe.mp3"
    "Silence. It's the one language that you can comprehend. Not impressed, not disappointing. The white bread of experiences."
    menu:
        "Continue to lie down":
            jump deadChoiceAlt
        "Open your eyes":
            jump openEyeChoice

label openEyeChoice:
    stop sound
    # Passage: openEyeChoice
    scene cTrain
    stop music
    play sound "audio/Flashbang.mp3" fadeout 0.2
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 0.5
    hide flash
    "{b}{i}FLASH{/i}{/b}"
    jump openEyeChoice2

label openEyeChoice2:
    stop sound
    play sound "audio/Narration/itssimplytoomuch.mp3"
    "It's simply too much for you to comprehend. The loud grumbles emenating from the floor. The bright LED lights blaring through every oriphace contained on your stained body. What the fuck is {i}Salesforce{/i} and what do they do?"
    jump openEyeChoice3

label openEyeChoice3:
    stop sound
    play sound "audio/Narration/theserandombillboard.mp3"
    "These random billboard advertisements might as well be spoken in a different language at this point. {b}{i}The Streak{sup}TM{/sup}{/i}{/b} is gone. It's all gone..."
    menu:
        "Where am I?":
            jump whereAmIChoice

label whereAmIChoice:
    stop sound
    # Passage: whereAmIChoice
    play music "audio/SubwayTheme.mp3" fadein 2.0 loop
    play sound "audio/Narration/asubwaycar.mp3"
    "A SUBWAY CAR! It could be worse. You could simply be dead. Or maybe that's better? Look around. Take in the fresh air."
    menu:
        "Look around":
            jump ratFaceReveal

label ratFaceReveal:
    stop sound
    # Passage: ratFaceReveal
    play sound "audio/Narration/youseecrowds.mp3"
    "You see crowds. The bright metal poles to hang on while sustaining the turbulence of a subway ride. In the window you see a... reflection of a rat?"
    $ status = "Confused and Lost"
    jump ratFaceReveal2

label ratFaceReveal2:
    stop sound
    play sound "audio/Narration/arat.mp3"
    "A rat?"
    jump ratFaceReveal3

label ratFaceReveal3:
    stop sound
    play sound "audio/Narration/waitbutyoure.mp3"
    "Wait, but you're supposed to see a reflection of you?"
    jump ratFaceReveal4

label ratFaceReveal4:
    stop sound
    play sound "audio/Narration/thatsarat.mp3"
    "That's A RAT."
    jump ratFaceReveal5

label ratFaceReveal5:
    stop sound
    play sound "audio/Narration/oh.mp3"
    "Oh."
    jump ratFaceReveal6

label ratFaceReveal6:
    stop sound
    play sound "audio/Narration/ohno.mp3"
    "Oh no."
    jump ratFaceReveal7

label ratFaceReveal7:
    stop sound
    show ratFace:
        xalign 0.5
        yalign -0.1
        zoom 1.4
    with dissolve

    play sound "audio/Narration/yourearat.mp3"
    "YOU'RE A RAT."
    jump ratFaceReveal8

label ratFaceReveal8:
    stop sound
    play sound "audio/Narration/acrumpledsuit.mp3"
    "A crumpled suit and tie, a briefcase no longer to be found, probably stolen by someone with some actual gumption, you're just a rat. In a both figurative and literal sense. You don't even know how you got here, but you did."
    menu:
        "Observe the environment":
            jump ObservationBase

label ObservationBase:
    stop sound
    # Passage: ObservationBase
    hide ratFace with dissolve
    play sound "audio/Narration/thistraincar.mp3"
    "This train car is a literal zoo. No humans to be found. Various species from the animal kingdom lie here in their various outfits, some shabby, some distinguished, and you, the rat."
    jump ObservationBase2

label ObservationBase2:
    stop sound
    play sound "audio/Narration/inthebottom.mp3"
    "In the bottom corner of the disabled seating area you see brown, glass bottles, with a little bit of their enchanting liquor left."
    jump ObservationBase3

label ObservationBase3:
    stop sound
    play sound "audio/Narration/aloudgroup.mp3"
    show hyenaNormal at left with dissolve
    show hyenaSkate at center with dissolve
    show hyenaVape at right with dissolve
    "A loud group of teen hyenas are chatting on their phones, occasionally looking at you, and then back down to their phones, and cackle in unison. One holds a vape in his hand. One holds a skateboard in his hand. And the other is just living in the moment, only a phone in hand."
    jump ObservationBase4

label ObservationBase4:
    stop sound
    hide hyenaNormal with dissolve
    hide hyenaSkate with dissolve
    hide hyenaVape with dissolve
    play sound "audio/Narration/the7030ratio.mp3"
    "The 70/30 ratio of piss and janitor soap eminates from the ground, which you've become numb to. What will you do?"
    menu:
        "Wait, sorry, who am I?":
            jump identifyChoice
        "Talk to the hyenas" if identifyBool and beerBool:
            jump hyenaChoice
        "Analyze the bottles":
            jump beerChoice
        "I want to attempt a cartwheel! (D15)":
            jump cartwheelChoice

label identifyChoice:
    stop sound
    # Passage: identifyChoice
    play sound "audio/Narration/yournameis.mp3"
    "Your name is... you don't know. How could you forget your own name?"
    menu:
        "I don't know!":
            jump dontKnowNameChoice
        "Can I get at least how I got here?":
            jump howIGotHereChoice

label hyenaChoice:
    stop sound
    # Passage: hyenaChoice
    play sound "audio/Narration/yougoup.mp3"
    "You go up to the group of Hyenas, and each of their gazes slowly fasten onto you. A rut is in your throat as you try to think of what to say to them, what to ask them, it feels like an impossible task. But. You have to try."
    menu:
        "\"Hi I was wondering if you guys know how I got here?\"":
            jump hyenaHowChoice
        "\"I would politely want to ask you guys to stop laughing at me\"":
            jump hyenaHowChoice
        "\"Get the fuck off my train car before I send your asses to the shadow realm\"":
            jump hyenaAggroChoice

label beerChoice:
    stop sound
    scene black with dissolve
    stop music fadeout 1.0
    play music "audio/FloatySoundscape.mp3" fadein 1.5
    # Passage: beerChoice
    $ beerBool = True
    play sound "audio/Narration/thesweetsmell.mp3"
    "The sweet smell of liquor calls you. You can fully forget about {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. It doesn't matter anymore. A siren, laying on its stage (in this case the gunky subway floor), the beer wraps its temptation around you. You clumsily puppeteer your limbs to greet Mr. Beer with a firm handshake. "
    menu:
        "Smell it":
            jump smellBeerChoice
        "Take a filthy swig of it you animal":
            jump chugBeerChoice
        "Escape it's clutches (D10)":
            jump escapeChoice

label cartwheelChoice:
    stop sound
    # Passage: cartwheelChoice
    $ diceRoll = renpy.random.randint(1,20)
    "Your roll: [diceRoll]"
    if diceRoll >= 15:
        jump cartwheelSuccess
    else:
        jump cartwheelFail

label cartwheelSuccess:
    stop sound
    show ratFace at center:
        rotate 0
        linear 2.0 rotate 360
        repeat
    with dissolve
    play sound "audio/Narration/yourhandsare.mp3"
    "Your hands are in the air, rays poking out from your fingers as you line up the preliminary {i}cart{/i} to the {i}wheel{/i}."
    jump cartwheelSuccess2

label cartwheelFail:
    stop sound
    show ratFace at center:
        rotate 0
        linear 2.0 rotate 360
        repeat
    with dissolve
    play sound "audio/Narration/yourhandsare.mp3"
    "Your hands are in the air, rays poking out from your fingers as you line up the preliminary {i}cart{/i} to the {i}wheel{/i}."
    jump cartwheelFail2

label cartwheelFail2:
    stop sound
    hide ratFace
    show ratFaceSad at center with dissolve
    play sound "audio/Narration/slapslapthunkyoufailed.mp3"
    "{i}SLAP, SLAP, THUNK{/i}. You failed. This feeling is all too familiar now. Just keep your wits about you and head back to your seat."
    hide ratFaceSad with dissolve
    menu:
        "Waddle Back":
            jump ObservationBase

label cartwheelSuccess2:
    stop sound
    play sound "audio/Narration/slapslapthunk.mp3"
    "{i}SLAP, SLAP, THUNK{/i}. You did it. You did the cartwheel. Welcome to the big leagues. In your mind, the crowd watches in awe. You sir, are a champion. Now take a victory lap, and head back to your seat to figure out why you're here."
    menu:
        "Strut back":
            jump ObservationBase

label smellBeerChoice:
    stop sound
    # Passage: smellBeerChoice
    play sound "audio/Narration/ohitsa.mp3"
    "Oh it's a good one alright. Coors Banquet. Your favorite. The temptation is too much and the idea of escape, ironically, has escaped you. Might as well chug."
    menu:
        "Fine you got me... Chug chug chug":
            jump chugBeerChoice

label escapeChoice:
    stop sound
    # Passage: escapeChoice
    $ diceRoll = renpy.random.randint(1,20)
    "Your Roll: [diceRoll]"
    if diceRoll >= 10:
        scene cTrain with dissolve
        play sound "audio/Narration/everyfiberof.mp3"
        "Every fiber of your body has been given the directive to resist the sexy alcohol. You're able to successfully prevent another incident that might ruin {b}{i}The Streak{sup}TM{/sup}{/i}{/b}"
        menu:
            "Resist the urge":
                $ beerBool = True;
                jump ObservationBase
    else:
        play sound "audio/Narration/youfailto.mp3"
        "You fail to convince yourself that giving up this beer is worth it and you start chugging your woes away."
        menu:
            "Ohhhh yeah that's the stuff":
                $ beerBool = True;
                jump chugBeerChoice

label chugBeerChoice:
    stop sound
    # Passage: chugBeerChoice
    show ratFaceDrunk:
        xalign 0.5
        yoffset -450
        parallel:
            rotate 0
            linear 5.0 rotate 360
            repeat
    with dissolve
    play sound "audio/Narration/eventhoughyouve.mp3"
    "Even though you've already passed the subway stop for the {b}{i}The Streak{sup}TM{/sup}{/i}{/b}, you couldn't care less. The inflation of balloons of forgetfulness leech your mind, and before you know it, this episode of your life fades to black."
    $ status = "More drunk than when you started"
    jump Start

label dontKnowNameChoice:
    stop sound
    # Passage: dontKnowNameChoice
    $ identifyBool = True
    $ diceRoll = renpy.random.randint(1,20)
    play sound "audio/Narration/shameonyou.mp3"
    "Shame on you! {b}{i}SHAME!{/i}{/b} This is the most important part of a human's origin story. This is why you're simply a rat. Rats don't get names. They just scuttle around without meaning in the infinite labyrinth of the subway tunnels, identifying themselves as the scuttlers of human waste. "
    menu:
        "No no no I can remember my name I promise! (D18)":
            jump nameAttempt
        "I give up":
            jump nameGiveUp

label howIGotHereChoice:
    stop sound
    # Passage: howIGotHereChoice
    $ identifyBool = True
    play sound "audio/Narration/youhavean.mp3"
    "You have an origin story. You know it and feel it. A rat doesn't appear out of thin air in a subway car. It has to scuttle in somehow. You look around to find something, or someone that has led you in on this chase. You're unable to recognize much. But, the smell of the brown, glass, bottle in the corner sticks out in the sea of NYC musk."
    menu:
        "Go back to observation":
            jump ObservationBase

label nameAttempt:
    stop sound
    # Passage: nameAttempt
    "Your Roll: [diceRoll]"
    if diceRoll >= 18:
        play sound "audio/Narration/yousuccessfullyvacuumed.mp3"
        "You successfully vacuumed the shelves of your treacherous memory. Your name is Clint. Clint Kratz. Congratulations, you've successfully named a random rat on the subway."
    else:
        play sound "audio/Narration/inwhatworld.mp3"
        "In what world did you think that would work? This is why rats don't take risks. What good comes out of trying to fight the inevitable. Silly, immature, rat."
    jump ObservationBase

label nameGiveUp:
    stop sound
    # Passage: nameGiveUp
    play sound "audio/Narration/goodasyou.mp3"
    "Good. As you should. What's the point of something as insignificant as a rat taking risks? Just get out of your own head an observe the world from now on"
    jump ObservationBase

label hyenaHowChoice:
    stop sound
    # Passage: hyenaHowChoice
    play sound "audio/Narration/theyoungteens.mp3"
    "The young teens look at you. Look back at each other. Their mouths tighten. Their cheeks puff with anticipation. This is not good for you. And then an explosion of laughter hits."
    jump hyenaHowChoice2

label hyenaHowChoice2:
    stop sound
    show hyenaNormal:
        xalign 0.5
        yalign -0.3
    with dissolve
    normHyena "\"HAHAHAHAHAHAHAHA\""
    jump hyenaHowChoice3

label hyenaHowChoice3:
    stop sound
    hide hyenaNormal
    show hyenaVape:
        xalign 0.5
        yalign -0.3
    with dissolve
    vapeHyena "\"YOUR JACKET AND TIE LOOK SO GOOFY\""
    jump hyenaHowChoice4

label hyenaHowChoice4:
    stop sound
    play sound "audio/Narration/hepuffsa.mp3"
    "He puffs a large vape cloud right in your face. Green apple flavored."
    jump hyenaHowChoice5

label hyenaHowChoice5:
    stop sound
    hide hyenaVape
    show hyenaSkate:
        xalign 0.5
        yalign -0.3
    with dissolve
    skateHyena "\"OMG HE ACTUALLY DOES LOOK LIKE A RAT\""
    jump hyenaHowChoice6

label hyenaHowChoice6:
    stop sound
    play sound "audio/Narration/somethingaboutthat.mp3"
    "Something about that insult feels familiar in a bad way. Laughter fills the train car. Anger for a past version of you bubbles up from the scum."
    menu:
        "{i}*Swing a punch on one of the teens*{/i}":
            jump fightChoice
        "{i}*Accept your shame like a loser*{/i}":
            jump shameChoice

label hyenaAggroChoice:
    stop sound
    # Passage: hyenaAggroChoice
    play sound "audio/Narration/theybeginto.mp3"
    "They begin to mock you."
    jump hyenaAggroChoice2

label hyenaAggroChoice2:
    stop sound
    show hyenaNormal:
        xalign 0.5
        yalign -0.3
    with dissolve
    normHyena "\"YO WHO DOES THIS OLD MAN THINK HE IS?\""
    jump hyenaAggroChoice3

label hyenaAggroChoice3:
    stop sound
    play sound "audio/Narration/youre25or.mp3"
    "You're 25. Or at least you feel like you are."
    jump hyenaAggroChoice4

label hyenaAggroChoice4:
    stop sound
    hide hyenaNormal
    show hyenaSkate:
        xalign 0.5
        yalign -0.3
    with dissolve
    skateHyena "\"YOU THINK YOU'RE SO TOUGH HUH\""
    jump hyenaAggroChoice5

label hyenaAggroChoice5:
    stop sound
    play sound "audio/Narration/youneversaid.mp3"
    "You never said that."
    jump hyenaAggroChoice6

label hyenaAggroChoice6:
    stop sound
    hide hyenaSkate
    show hyenaVape:
        xalign 0.5
        yalign -0.3
    with dissolve
    vapeHyena "\"YOU DRESS LIKE MY STEP-DAD\""
    jump hyenaAggroChoice7

label hyenaAggroChoice7:
    stop sound
    play sound "audio/Narration/hurtful.mp3"
    "Hurtful."
    menu:
        "\"Look you guys just hurt my feelings and I don't really think it's necessary-\"":
            jump hyenaSwingChoice
        "{i}*Walk away in shame*{/i}":
            jump shameChoice

label fightChoice:
    stop sound
    # Passage: fightChoice
    stop music
    hide hyenaSkate
    show hyenaNormal at right:
        xzoom -1.0
    show ratFace at left
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 0.5
    hide flash
    play music "audio/FightTheme.mp3"
    show hyenaNormal:
        rotate 0
        parallel:
            linear 0.5 rotate 360
            repeat
        parallel:
            linear 2.0 xpos 7000  # flies off screen right
    with dissolve
    "{b}*BANG*{/b}"
    hide hyenaNormal
    jump fightChoice2

label fightChoice2:
    stop sound
    play sound "audio/Narration/yourdrunkenstrike.mp3"
    "Your drunken strike lands clean on the chin of the Hyena that mocked your clothing choices. The other two square up, ready to swing their paws and skateboards at your delicate rat jaw. The Hyena holding a vape drops his vape. The tension is through the sewers. Things are beginning to get serious."
    jump fightChoice3

label fightChoice3:
    stop sound
    show hyenaVape at right:
        xzoom -1.0
        yalign -0.3
    with dissolve
    play sound "audio/Narration/hyenavapeteenwinds.mp3"
    "Hyena Vape-Teen winds up a punch"
    menu:
        "Weave left, counter with a quick right jab":
            jump failureWeaveFightChoice
        "Weave right, counter with a haymaker left":
            jump correctFightChoice
        "Swing your leg to trip":
            jump correctTrip
        "Attempt a tactical headbutt":
            jump failureHeadbuttFightChoice

label shameChoice:
    stop sound
    # Passage: shameChoice
    play sound "audio/Narration/youshamefullywalk.mp3"
    "You shamefully walk away from that interaction. A repeat of what happens all the time. {b}{i}The Streak{sup}TM{/sup}{/i}{/b} is continued in a way. But walking away you feel a sense of shame. You lost."
    menu:
        "*Surprise attack on the unsuspecting laughing teens*":
            jump fightChoice
        "*Walk away like a rat*":
            jump ObservationBase

label hyenaSwingChoice:
    stop sound
    stop music
    play music "audio/FightTheme.mp3"
    # Passage: hyenaSwingChoice
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 0.5
    hide flash
    show ratFace:
        xalign 0.5
        rotate 0
        linear 3.0 rotate 360
        repeat
    with dissolve
    "{b}*POW*{/b}"
    $ status = "Deeply Concussed"
    jump hyenaSwingChoice2

label hyenaSwingChoice2:
    stop sound
    play sound "audio/Narration/arighthook.mp3"
    "A right hook hits the bottom of your jaw and rocks your head back. It's now or never."
    jump hyenaSwingChoice3

label hyenaSwingChoice3:
    stop sound
    show hyenaVape:
        xalign 0.5
        yalign -0.3
        zoom 1.4
    with dissolve
    vapeHyena "\"OLD MAN NEXT TIME IT'S GONNA BE THE SKATEBOARD THAT DOES THE TALKING\""
    jump hyenaSwingChoice4

label hyenaSwingChoice4:
    stop sound
    play sound "audio/Narration/forgetaboutthe.mp3"
    "Forget about {b}{i}The Streak{sup}TM{/sup}{/i}{/b} it's time for you get in on the action. This is your calling, your destiny to start a new {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. These teenagers need to experience the real world."
    menu:
        "Crawl up in a ball and cry":
            jump crawlChoice
        "Fight back for your glory! *Swings punch*":
            jump fightChoice

label crawlChoice:
    stop sound
    # Passage: crawlChoice
    show ratFace hurt with dissolve
    play sound "audio/Narration/youcrawlup.mp3"
    "You crawl up in a ball and tears start flowing down your cheeks and whiskers."
    jump crawlChoice2

label crawlChoice2:
    stop sound
    hide ratFace
    show hyenaVape:
        xalign 0.5
        yalign -0.3
        zoom 1.4
    with dissolve
    vapeHyena "\"OH MY GOD, A RANDOM TWEAKER TRIED TO PICK A FIGHT WITH US AND GOT TOO SCARED\""
    jump crawlChoice3

label crawlChoice3:
    stop sound
    play sound "audio/Narration/agreenapple.mp3"
    "A Green Apple flavored vape cloud hurls itself towards your face."
    jump crawlChoice4

label crawlChoice4:
    stop sound
    play sound "audio/Narration/nofightno.mp3"
    "No fight, no guts, you truly are a rat. Might as well just close your eyes, and sleep for the next eternity."
    menu:
        "{i}Close your eyes{i}":
            jump Start
        "{i}Prove your guts{i}":
            jump fightChoice

label correctFightChoice:
    stop sound
    # Passage: correctFightChoice
    "{i}*FWOOSH*{/i}"
    jump correctFightChoice2

label correctFightChoice2:
    stop sound
    # Passage: correctFightChoice
    play sound "audio/Narration/youweavethe.mp3"
    "You weave the first swing from Hyena Vape-Teen and wind up the haymaker..."
    jump correctFightChoice3

label correctFightChoice3:
    stop sound
    # Passage: correctFightChoice
    show hyenaVape at right:
        xzoom -1.0
        rotate 0
        parallel:
            linear 0.5 rotate 360
            repeat
        parallel:
            linear 2.0 xpos 7000  # flies off screen right
    with dissolve
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 0.5
    hide flash
    "{i}*THUNK*{/i}"
    hide hyenaVape
    jump correctFightChoice4

label correctFightChoice4:
    stop sound
    play sound "audio/Narration/youclockhyena.mp3"
    show hyenaSkate at right with dissolve
    show hyenaSkate:
        xzoom -1.0
    "You clock Hyena Vape-Teen in the cheek. A tooth flies out, a prize for your fighting abilities. But Hyena Skate-Teen looks like they're about to swing with their skateboard in hand, a possible deadly blow."
    menu:
        "Duck and trip Hyena Skate-teen":
            jump duckTripChoice
        "Run away":
            jump policeChase

label correctTrip:
    stop sound
    "{i}*FWOOOSH*{/i}"
    jump correctTrip2

label correctTrip2:
    stop sound
    play sound "audio/Narration/youswingyour.mp3"
    show hyenaVape at right:
        xzoom -1.0
        rotate 0
        parallel:
            linear 0.5 rotate 360
            repeat
        parallel:
            linear 2.0 xpos 7000  # flies off screen right
    with dissolve
    hide hyenaVape
    "You swing your leg and the Hyena Vape-Teen falls before they have time to sock you with a haymaker. He lands on his face and is seriously disfigured."
    jump correctTrip3

label correctTrip3:
    stop sound
    play sound "audio/Narration/atoothflies.mp3"
    show hyenaSkate at right:
        xzoom -1.0
    "A tooth flies out, a prize for your fighting abilities. But Hyena Skate-Teen looks like they're about to swing with their skateboard in hand, a possible deadly blow."
    menu:
        "Duck and trip Hyena Skate-Teen":
            jump duckTripChoice
        "Run away":
            jump policeChase

label failureWeaveFightChoice:
    stop sound
    # Passage: failureWeaveFightChoice
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 0.5
    hide ratFace
    hide flash
    show ratFaceSad at left with dissolve
    $ status = "Heavily Concussed"
    play sound "audio/Narration/youguessedwrong.mp3"
    "You guessed wrong. You weave to your left and feel a sustained contact on the bone of your jaw. It's Hyena Vape-Teen's pubescent fist. Your nausea feels like it just got a million times worse. Saliva flies out of your mouth, exhaling pain and suffering. You are heavily concussed."
    menu:
        "Swing back":
            jump standUpChoice
        "Stay down":
            jump layDownChoice

label failureHeadbuttFightChoice:
    stop sound
    # Passage: failureHeadbuttFightChoice
    play sound "audio/Narration/youchargeup.mp3"
    "You charge up your headbutt, to pull the most ferocious attack on the Hyena that insulted your age. 25 is not an old age. Maybe they're just too young."
    jump failureHeadbuttFightChoice2

label failureHeadbuttFightChoice2:
    stop sound
    play sound "audio/Narration/youfireoff.mp3"
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 1
    hide flash
    hide ratFace with dissolve
    show ratFaceSad with dissolve
    "You fire off the headbutt. They see it from a mile away. They easily side step your attempt and you trip and faceplant into a metal support pole. You are now heavily concussed."
    menu:
        "Standup and swing again":
            jump standUpChoice
        "Lay down and accept defeat":
            jump layDownChoice

label standUpChoice:
    stop sound
    hide ratFaceSad
    # Passage: standUpChoice
    show ratFace at left with dissolve
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 0.5
    hide flash
    show hyenaVape at right:
        xzoom -1.0
        rotate 0
        parallel:
            linear 0.5 rotate 360
            repeat
        parallel:
            linear 2.0 xpos 7000  # flies off screen right
    with dissolve
    play sound "audio/Narration/youswingagain.mp3"
    "You swing again. You catch two of them. A collateral! Who knew this rat had paws like these. This will be the new start, the new birth of an iteration of {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. You're on top of the world. A drunk rat man just defeated a gang of entitled rat teenagers ... I guess it sounds better in your own mind."
    $ diceRoll = renpy.random.randint(1,20)
    menu:
        "Celebrate the victory with a victory cartwheel! (D15)":
            jump victoryCartwheelChoice
        "Say a cool line like {i}\"'Tis but a scratch\"{/i} (D12)":
            jump coolLineChoice
        "Walk away in silence, like a mature \"adult\"":
            jump walkAwayChoice

label layDownChoice:
    stop sound
    # Passage: layDownChoice
    stop music fadeout 1.0
    play sound "audio/Narration/youlaydown.mp3"
    "You lay down, heavily concussed from losing a fight. This would be a time when {b}{i}The Streak{sup}TM{/sup}{/i}{/b} has fully ended. Your eyes begin to close, as you plan to rest on the ground, the teenagers now taking photos for their instagram story."
    menu:
        "Get back up, and stay in your own lane":
            jump policeChase
        "Close your eyes to enter the infinite, harmless expanse":
            jump Start

label policeChase:
    stop sound
    # Passage: policeChase
    hide ratFaceSad
    hide ratFace
    hide police
    show ratFace at right with dissolve
    show police at left:
        yoffset -200
    with dissolve
    police "{i}\"SIR, GET AWAY FROM THE TEENAGERS AND PUT YOUR HANDS UP\"{/i}"
    jump policeChase2

label policeChase2:
    stop sound
    play sound "audio/Narration/shititsthe.mp3"
    "Shit it's the police. They were a few cars over when they heard word of a drunken fart beating up on some kids. Someone ratted on you. You're gonna go to prison forever. A different, much less tranquil, infinite expanse."
    jump policeChase3

label policeChase3:
    stop sound
    play sound "audio/Narration/youhearthe.mp3"
    "You hear the subway announcer through the speakers."
    jump policeChase4

label policeChase4:
    stop sound
    stop sound fadeout 1.0
    "{i}\"This is 59th street, Columbus Circle. Transfer is available to the 2, C, B, and D trains. This is an accessible station\"{/i}"
    jump policeChase5

label policeChase5:
    stop sound
    stop music fadeout 1.0
    play sound "audio/Narration/thetrainstops.mp3"
    scene closingDoors
    "The train stops. The crunch of the doors opening initiates."
    play sound "audio/StandClear.mp3"
    $ renpy.pause(delay=4.2, hard=True)
    menu:
        "Make a run for it (D15)":
            jump runChaseChoice
        "Stay in place":
            jump arrestChoice

label victoryCartwheelChoice:
    stop sound
    stop music fadeout 1.0
    play music "audio/SubwayTheme.mp3" fadein 1.0
    # Passage: victoryCartwheelChoice
    $ diceRoll = renpy.random.randint(1,20)
    "Your roll: [diceRoll]"
    jump victoryCartwheelChoice2

label victoryCartwheelChoice2:
    stop sound
    show ratFace at center:
        rotate 0
        linear 2.0 rotate 360
        repeat
    with dissolve
    play sound "audio/Narration/yourdrunkenrage.mp3"
    "Your drunken rage has fully unlocked your physical capabilities. You can finally live out your dream of becoming a gymnast. The hands are in the air, rays poking out from your fingers as you line up the preliminary cart to the wheel."
    jump victoryCartwheelChoice3

label victoryCartwheelChoice3:
    stop sound
    if diceRoll >= 15:
        hide ratFace
        show ratFace at center
        play sound "audio/Narration/slapslapthunkyou.mp3"
        "{i}SLAP, SLAP, THUNK{/i}. You did it. You did the cartwheel. The crowd watches in awe. You sir, are a champion. Now take a victory lap, and head back to your seat to figure out why you're here."
        hide ratFace with dissolve
    else:
        hide ratFace
        show ratFaceSad
        play sound "audio/Narration/slapslipthunkyou.mp3"
        "{i}SLAP, SLIP, THUNK{/i}. You failed. This feeling is all too familiar now. Just keep your wits about you and head back to your seat."
        hide ratFaceSad with dissolve
    jump policeChase

label coolLineChoice:
    stop sound
    stop music fadeout 1.0
    play music "audio/SubwayTheme.mp3" fadein 1.0
    # Passage: coolLineChoice
    "Your roll: [diceRoll]"
    if diceRoll >= 12:
        jump coolLineChoiceSuccess
    else:
        jump coolLineChoiceFail

label coolLineChoiceSuccess:
    stop sound
    you "\"'Tis but a scratch.\""
    jump coolLineChoiceSuccess2

label coolLineChoiceSuccess2:
    stop sound
    play sound "audio/Narration/naileditall.mp3"
    "Nailed it. All the beat up teenagers heard it. All the passengers who watched the fight in horror also heard it. Welcome my friend back to: {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. Nothing will stop you this time"
    menu:
        "Go back to rediscovering your origin story":
            jump policeChase

label coolLineChoiceFail:
    stop sound
    you "\"I have a butt scratch to itch.\""
    jump coolLineChoiceFail2

label coolLineChoiceFail2:
    stop sound
    play sound "audio/Narration/fuckyouresimply.mp3"
    "Fuck. You're simply too drunk to even get out a simple sentence correctly. You just beat up some teenagers to mess up your finishing line. Go back to your seat, and focus on the real mission at hand here."
    menu:
        "Go back to rediscovering your origin story":
            jump policeChase

label walkAwayChoice:
    stop sound
    stop music fadeout 1.0
    play music "audio/SubwayTheme.mp3" fadein 1.0
    # Passage: walkAwayChoice
    "Your roll: [diceRoll]"
    jump walkAwayChoice2

label walkAwayChoice2:
    stop sound
    play sound "audio/Narration/youwalkaway.mp3"
    "You walk away calmly, one step at a time. Nothing needed to be said because your fists did the talking. Say goodbye to being a rat, and welcome home {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. Let it ring through the halls, and walk back to your seat, a victory lap around the appalled spectators."
    menu:
        "Go back to rediscovering your origin story":
            jump policeChase

label duckTripChoice:
    stop sound
    # Passage: duckTripChoice
    "{i}*FWOOSH*{/i}"
    jump duckTripChoice2

label duckTripChoice2:
    stop sound
    show hyenaSkate at right:
        xzoom -1.0
        rotate 0
        parallel:
            linear 0.5 rotate 360
            repeat
        parallel:
            linear 2.0 xpos 7000  # flies off screen right
    with dissolve
    play sound "audio/Narration/theycompletelywhiff.mp3"
    "They completely whiff. You whip your tail around their ankles to trip Hyena Skate-Teen. They fall over, hit their head, and sustain a concussion. You've won. Total victory."
    hide hyenaSkate
    $ diceRoll = renpy.random.randint(1,20)
    menu:
        "Celebrate the victory with a victory cartwheel! (D15)":
            jump victoryCartwheelChoice
        "Say a cool line like {i}\"'Tis but a scratch\"{/i} (D12)":
            jump coolLineChoice
        "Walk away in silence, like a mature \"adult\"":
            jump walkAwayChoice

label runChaseChoice:
    stop sound
    scene subwayPlat with dissolve
    play music "audio/SubwayChaseLoop.mp3" loop
    hide ratFace
    hide police
    show ratFace at right:
        linear 0.2 yoffset -50
        linear 0.2 yoffset -20
        repeat
    show police at left:
        linear 0.2 yoffset -100
        linear 0.2 yoffset -150
        repeat
    # Passage: runChaseChoice
    "Your roll: [renpy.random.randint(15,20)]"
    jump runChaseChoice2

label runChaseChoice2:
    stop sound
    # Passage: runChaseChoice
    play sound "audio/Narration/yourlimbsbeginto.mp3"
    "Your limbs begin to move. Your core has the integrity of a fresh jello. {b}{i}The Streak{sup}TM{/sup}{/i}{/b} is about total victory, and may never contain any interruptions. This firmly breaks the rules of {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. You roll your way through 59th street station, oncoming passerby's stiffly shuffling out the way."
    jump runChaseChoice3

label runChaseChoice3:
    stop sound
    play sound "audio/Narration/constructionblocksthe.mp3"
    "Construction blocks the path."
    menu:
        "Hurdle the warnings (D15)":
            jump runChaseChoice4
        "Run around":
            jump runChaseChoiceFail

label runChaseChoiceFail:
    stop sound
    play sound "audio/Narration/thecopshawk.mp3"
    hide ratFace with dissolve
    show ratFaceSad at right with dissolve
    stop music fadeout 1.0
    "The cops hawk you down and put you in handcuffs. You go on to spend the rest of the next 15 years in prison. This was never part of {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. You've managed to find something worse than being a rat. At least a rat would've preserved their sanctuary. You've managed to fail that too."
    jump runChaseChoiceFail2

label runChaseChoiceFail2:
    stop sound
    play sound "audio/Narration/theendor.mp3"
    scene black with dissolve
    stop music fadeout 1.0
    "The End... or is it?"
    menu:
        "Go back in time a little":
            jump runChaseChoice

label runChaseChoice4:
    stop sound
    "Your roll: [renpy.random.randint(15,20)]"
    jump runChaseChoice5

label runChaseChoice5:
    stop sound
    play sound "audio/Narration/yousuccessfullygo.mp3"
    "You successfully go flying in the air and manage to land on your feet, what people in the business call a \"jump\". The policemen stop in their tracks and pull out their guns, they're about to shoot."
    menu:
        "Stop with your hands up":
            jump runChaseChoiceFail
        "Perform a cartwheel (D15)":
            jump runChaseChoice6

label runChaseChoice6:
    stop sound
    "Your roll: [renpy.random.randint(15,20)]"
    jump runChaseChoice7

label runChaseChoice7:
    stop sound
    show ratFace:
        xoffset 200
        yoffset 100
        rotate 0
        linear 2.0 rotate 360
        repeat
    with dissolve
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 1
    hide flash
    play sound "audio/Narration/bangsingle.mp3"
    "{b}{i}*Bang*{/i}{/b}"
    jump runChaseChoice8

label runChaseChoice8:
    stop sound
    play sound "audio/Narration/bangbarelymissed.mp3"
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 0.5
    hide flash
    "{size=+10}{b}{u}{i}*BANG*{/i}{/u}{/b}{/size}\n\nBarely missed you"
    jump runChaseChoice9

label runChaseChoice9:
    stop sound
    play sound "audio/Narration/bangcompletelywhiffed.mp3"
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 0.5
    hide flash
    "{size=-20}{b}{i}bang{/i}{/b}{/size}\n\nCompletely whiffed. That cop needs to retire"
    jump runChaseChoice10

label runChaseChoice10:
    stop sound
    play sound "audio/Narration/yourcartwheelkeeps.mp3"
    "Your cartwheel keeps you alive. Looks like drunk thinking works sometimes."
    menu:
        "Keep running (D15)":
            jump moreRunChaseChoice
        "Put your hands in the air for celebration and start dancing!":
            jump arrestChoice

label arrestChoice:
    stop sound
    # Passage: arrestChoice
    play sound "audio/Narration/thecopspin.mp3"
    hide ratFace with dissolve
    show ratFaceSad at right with dissolve
    stop music fadeout 1.0
    "The cops pin you down and put you in handcuffs. You go on to spend the rest of the next 15 years in prison. This was never part of {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. You've managed to find something worse than being a rat. At least a rat would've preserved their sanctuary. You've managed to fail that too."
    jump arrestChoice2

label arrestChoice2:
    stop sound
    play sound "audio/Narration/theendor.mp3"
    stop music fadeout 1.0
    scene black with dissolve
    "The End... or is it?"
    menu:
        "Go back in time a little":
            jump runChaseChoice

label moreRunChaseChoice:
    stop sound
    # Passage: moreRunChaseChoice
    "Your roll: [renpy.random.randint(15,20)]"
    jump moreRunChaseChoice2

label moreRunChaseChoice2:
    stop sound
    play sound "audio/Narration/yourcardioisstarting.mp3"
    "Your cardio is starting to give out. But you keep trudging forward. The doors on the 2 train begin to close. Your window of oppportunity is closing. Reach for it son. Take the risk."
    menu:
        "Make a leap for it (D18)":
            jump p_2TrainSuccessChoice
        "Give up":
            jump arrestChoice

label p_2TrainSuccessChoice:
    stop sound
    stop music fadeout 1.0
    # Passage: 2TrainSuccessChoice
    "Your roll: [renpy.random.randint(18,20)]"
    jump p_2TrainSuccessChoice2
    jump p_2TrainObservationBase

label p_2TrainSuccessChoice2:
    stop sound
    scene closingDoors with dissolve
    stop sound fadeout 1.0
    play sound "audio/BING.mp3" fadein 0.1
    "{i}BING{/i}"
    jump p_2TrainSuccessChoice3

label p_2TrainSuccessChoice3:
    stop sound
    "FWIIIIISSHHH"
    jump p_2TrainSuccessChoice4

label p_2TrainSuccessChoice4:
    stop sound
    play sound "audio/BONG.mp3"
    "{i}BONG{/i}"
    jump p_2TrainSuccessChoice5

label p_2TrainSuccessChoice5:
    stop sound
    play sound "audio/Narration/youvemadeit.mp3"
    scene subwayAlt with dissolve
    show ratFace at center with dissolve
    stop music fadeout 1.0
    "You've made it. The police lost you. This wasn't part of {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. But, for some reason, it's more delightful. Still. You're still a rat. You don't know who you are. You don't know how you got here. Rattiness is a mindset."
    menu:
        "Take a seat and think":
            jump p_2TrainObservationBase

label p_2TrainObservationBase:
    stop sound
    # Passage: 2TrainObservationBase
    hide ratFace with dissolve
    play sound "audio/Narration/maybeitsyour.mp3"
    play music "audio/SubwayThemeALT.mp3" fadein 1.0
    "Maybe it's your perception. Maybe it's the train itself. But this habitat flows more dynamically. Families move in and out. The scenery between stops are different. Something is different. Not like {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. It's just different..."
    jump p_2TrainObservationBase2

label p_2TrainObservationBase2:
    stop sound
    show lion at center:
        yoffset -200
    with dissolve
    play sound "audio/Narration/alionfitted.mp3"
    "A lion fitted with dark suit, red striped tie, and portfolio brief bag sits at the edge of the seating to your right. Something about her strikes you as familiar but you don't know what. She's confident though. Emenating power."
    hide lion with dissolve
    jump p_2TrainObservationBase3

label p_2TrainObservationBase3:
    stop sound
    show otter at center:
        yoffset -100
    with dissolve
    play sound "audio/Narration/ontheopposite.mp3"
    "On the opposite side, to your left, an otter in a much shabbier suit ties his tie, paws shaking, with his laptop haphazardly open, about to slip off his lap."
    hide otter with dissolve
    jump p_2TrainObservationBase4

label p_2TrainObservationBase4:
    stop sound
    show drunkRat at center:
        yoffset -100
        rotate 0
        linear 5.0 rotate 360
        repeat
    with dissolve
    play sound "audio/Narration/paralleltoyou.mp3"
    "Parallel to you, in the far, far, right corner, another rat! He seems to be much more at ease than you, sitting, with a couple more of those sexy brown bottles you saw on the previous train. Maybe he'll share some with you."
    hide drunkRat with dissolve
    menu:
        "Approach the familiar figure":
            jump lionChoice
        "Become the otter's therapist":
            jump otterChoice
        "Cahoot with the other rat":
            jump ratChoice

label lionChoice:
    stop sound
    hide ratFaceSad with dissolve
    show ratFace at left with dissolve
    show lion at right:
        yoffset -50
        zoom 1.1
        xzoom -1.0
    with dissolve
    # Passage: lionChoice
    play sound "audio/Narration/thelionseems.mp3"
    "The lion seems to have already noticed you before you noticed her. Blank eyes of will shine through though. You crave information, just anything. You want to break {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. You go up to her, knees shaking, body still sore, and ask:"
    menu:
        "\"Who am I?\"":
            jump idChoice
        "\"How did I get here?\"":
            jump getHereChoice
        "\"Who are you?\"":
            jump whoAreChoice
        "\"Look at her lanyard\"":
            jump lanyardChoice
        "Go back to observing the train":
            hide lion with dissolve
            jump p_2TrainObservationBase

label otterChoice:
    stop sound
    # Passage: otterChoice
    play sound "audio/Narration/youapproachthe.mp3"
    "You approach the Otter with as much sensitivity as possible."
    jump otterChoice2

label otterChoice2:
    stop sound
    show ratFace at left with dissolve
    show otter at right:
        xzoom -1.0
    with dissolve
    you "\"Hey {i}-burrrrrp-{/i} what seems to be issue?\" you ask, with the friendliest face you can put up."
    jump otterChoice3

label otterChoice3:
    stop sound
    otter "\"Arrgghh I can't talk right now this is really tough because the powerpoint - the placeholders - aren't done yet and I'm fucking up the saving, just nothing happening right at all the wrong times and- and- and I'm really scared...\""
    jump otterChoice4

label otterChoice4:
    stop sound
    play sound "audio/Narration/hestopstyping.mp3"
    "He stops typing on his computer and breaks down in tears."
    menu:
        "\"Soo, what seems to be the issue\"":
            jump issueChoice
        "\"Hey it's gonna be alright\"":
            jump alrightChoice
        "\"Just become a rat like me\"":
            jump becomeRatChoice

label ratChoice:
    stop sound
    show ratFace at left with dissolve
    show drunkRat at right:
        xzoom -1.0
        zoom 1.2
    with dissolve
    # Passage: ratChoice
    play sound "audio/Narration/afamiliarsight.mp3"
    "A familiar sight, almost as if you're looking in a mirror (probably because you are also a rat), you walk up to the other rat."
    jump ratChoice2

label ratChoice2:
    stop sound
    drunkRat "\"Heeeyyy friieennd -*burp*- wanna chat?\""
    jump ratChoice3

label ratChoice3:
    stop sound
    play sound "audio/Narration/wowyouprobably.mp3"
    "Wow, you probably sound like this to other people too."
    menu:
        "\"What's your origin story\"":
            jump ratChatChoice
        "\"Would you lend a fellow rat a beer?\"":
            jump beerChatChoice
        "\"Lets sing a song together! Get the wiggles out\"":
            jump songChoice

label idChoice:
    stop sound
    # Passage: idChoice
    lion "\"Ratbrain, what kind of question is that\""
    jump idChoice2

label idChoice2:
    stop sound
    play sound "audio/Narration/ughratbrainthat.mp3"
    "Ugh. Ratbrain. That name irks your soul. And not just because you are a rat. Are they insulting you, or do they think that's your actual name? And that voice. It sends cortisol down your spine. Your teeth seize up."
    menu:
        "\"Are you insulting me or is that my name\"":
            jump nameChoice
        "\"Ratbrain does not answer to an inferior\"":
            jump dumbChoice

label getHereChoice:
    stop sound
    # Passage: getHereChoice
    lion "\"You applied for the job. You filled out your resume. You wrote a cover letter describing all the great things about McKinsey & Co. You took an interview in the war room. When do you want act like a real adult?\""
    hide ratFace with dissolve
    show ratFaceSad at left with dissolve
    jump getHereChoice2

label getHereChoice2:
    stop sound
    play sound "audio/Narration/youareboth.mp3"
    "You are both the same age."
    menu:
        "Talk about something else before you think you might get \"fired\"" if not (nameEnd and otterEnd and singEnd):
            jump lionChoice
        "Talk about something else before you think you might get \"fired\"" if nameEnd and otterEnd and singEnd:
            jump cTrainFulton

label whoAreChoice:
    stop sound
    # Passage: whoAreChoice
    lion "\"{i}Ha ha ha{/i}\""
    jump whoAreChoice2

label whoAreChoice2:
    stop sound
    play sound "audio/Narration/shelooksat.mp3"
    "She looks at your face. You're being serious, or as serious as a deeply buzzed rat can look like. Her straight toothed smile quickly fades to a stern front."
    jump whoAreChoice3

label whoAreChoice3:
    stop sound
    hide ratFace with dissolve
    show ratFaceSad at left with dissolve
    lion "\"Your attention span is that destroyed from your phone huh. Do you even remember your onboarding process? Kids like you are why our firm is losing clients. HR sure isn’t going to be happy when I tell them their screening has fallen this far\""
    jump whoAreChoice4

label whoAreChoice4:
    stop sound
    play sound "audio/Narration/nowshelooks.mp3"
    "Now she looks serious. Maybe you shouldn't have asked that."
    menu:
        "Masterfully switch the topic to something else before your ass gets fired" if nameEnd and otterEnd and singEnd:
            jump cTrainFulton
        "Masterfully switch the topic to something else before your ass gets fired" if not (nameEnd and otterEnd and singEnd):
            jump lionChoice

label nameChoice:
    stop sound
    # Passage: nameChoice
    $ nameEnd = True
    lion "\"Clint, I know what happened in front of Salesforce was embarassing but it's just part of being at the company. It's just simple culture. You'll understand once you get to where I'm at.\""
    jump nameChoice2

label nameChoice2:
    stop sound
    play sound "audio/Narration/ughclintsomething.mp3"
    "Ugh. {i}Clint{/i}. Something about that name irks you more than Ratbrain especially in her too-important-for-you tone. But wait. She said that you work for the same company? Hopefully she didn't see you get chased down by the police. A deep regret of interaction washes over you, as you head back to your seat."
    hide lion with dissolve
    $ status = "Business-Savvy"
    $ name = "Clint"
    $ linkedin = "https://www.linkedin.com/in/clint-kratz-212302217/"
    $ nameEnd = True
    menu:
        "Sit back down in your seat" if not (nameEnd and otterEnd and singEnd):
            jump p_2TrainObservationBase
        "Sit back down in your seat" if nameEnd and otterEnd and singEnd:
            jump cTrainFulton

label dumbChoice:
    stop sound
    # Passage: dumbChoice
    hide ratFace with dissolve
    show ratFaceSad at left with dissolve
    $ nameEnd = True
    $ status = "Business-Savvy"
    $ name = "Clint"
    $ linkedin = "https://www.linkedin.com/in/clint-kratz-212302217/"
    lion "\"Wow Clint, I didn't think my opinion of you could get any lower after the Salesforce incident. Hope you don't show up to the office like this or else you may not make it to the offsite.\" She grins maliciously."
    hide lion with dissolve
    hide ratFaceSad with dissolve
    menu:
        "Sit back down in your seat" if not (nameEnd and otterEnd and singEnd):
            jump p_2TrainObservationBase
        "Sit back down in your seat" if nameEnd and otterEnd and singEnd:
            jump cTrainFulton

label lanyardChoice:
    stop sound
    # Passage: lanyardChoice
    play sound "audio/Narration/youreyesfocus.mp3"
    "Your eyes focus on the lanyard. It shimmers with prestige in the plastic lights of the train car. A clean, uninterrupted streak scopes diagonally across the lanyard canvas. You see the name: {i}\"Trisha Vanderbilt\"{/i} in elegant seriffed font. {i}Mckinsey & Company{/i} nonchalantly loiters in the bottom right corner."
    menu:
        "Look back at her eyeballs to signify that you are about to have a real and professional conversation" if not (nameEnd and otterEnd and singEnd):
            jump lionChoice
        "Look back at her eyeballs to signify that you are about to have a real and professional conversation" if nameEnd and otterEnd and singEnd:
            jump cTrainFulton

label issueChoice:
    stop sound
    # Passage: issueChoice
    otter "\"*sniff* I completely fucked my powerpoint *sniff* I forgot to take out the placeholders and my manager is gonna kill me *sniff* I worked so hard to get here too, my life is overrrr *sobs*\""
    jump issueChoice2

label issueChoice2:
    stop sound
    play sound "audio/Narration/hisglassesalmost.mp3"
    "His glasses almost fall off his snout and his computer lid closes shut. He's fully given up. Your eyes also begin to well up. Something about this scenario feels a too familiar. A moment of deja vu."
    menu:
        "\"Don't worry. {b}{i}The Streak{sup}TM{/sup}{/i}{/b} is a false destiny. I know your potential isn't defined by what happens today\"":
            jump confusedChoice
        "\"Don't worry. {b}{i}The Streak{sup}TM{/sup}{/i}{/b} isn't about success. Just embrace a different streak, and join us rats\"":
            jump confusedChoice

label alrightChoice:
    stop sound
    # Passage: alrightChoice
    play sound "audio/Narration/theotterlooks.mp3"
    "The Otter looks at you in disbelief"
    jump alrightChoice2

label alrightChoice2:
    stop sound
    otter "\"How could it ever be alright? I was doing so well *sniff* everything was perfect. I doubt I'll ever recover\""
    menu:
        "\"Soo, what seems to be the issue\"":
            jump issueChoice
        "\"Just become a rat like me\"":
            jump becomeRatChoice

label becomeRatChoice:
    stop sound
    # Passage: becomeRatChoice
    you "\"{i}-burpppp-{/i} The rat life is the apt life brochacho. No worries, no responsibility\""
    jump becomeRatChoice2

label becomeRatChoice2:
    stop sound
    play sound "audio/Narration/thatdidnot.mp3"
    "That did not come out how you imagined it in your head. You also half believe what you are saying. Maybe it's sobering up. Maybe {b}{i}The Streak{sup}TM{/sup}{/i}{/b} matters less? Maybe it's a combination of both."
    jump becomeRatChoice3

label becomeRatChoice3:
    stop sound
    play sound "audio/Narration/stopthinkingyoure.mp3"
    "Stop thinking. You're meant to be Mr.Otter's therapist. It doesn't seem like this made him feel any better."
    jump becomeRatChoice4

label becomeRatChoice4:
    stop sound
    otter "\"Well *sniffs* I don't really want to be a rat like you. I've got, or maybe at this point *sniffs* had a future ahead of me\""
    $ otterEnd = True
    menu:
        "\"Well fuck you then!\" {i}*walks off, preserving self dignity*{/i}":
            hide ratFace
            hide otter with dissolve
            jump p_2TrainObservationBase
        "\"What is making these tears fall out of your eyes?\"":
            jump issueChoice

label confusedChoice:
    stop sound
    # Passage: confusedChoice
    play sound "audio/Narration/theriverstreaming.mp3"
    "The river streaming down his face stops all of a sudden. He looks at you, and back down at his computer, and back at you."
    jump confusedChoice2

label confusedChoice2:
    stop sound
    otter "\"What the fuck are you even saying\""
    jump confusedChoice3

label confusedChoice3:
    stop sound
    play sound "audio/Narration/heisgenuinely.mp3"
    "He is genuinely confused by YOUR passionate words of wisdom. But you, the therapist, have done job right. He's not crying anymore."
    $ otterEnd = True
    hide ratFace with dissolve
    hide otter with dissolve
    menu:
        "{i}Whisper to yourself \"mission complete\"{/i}" if not (nameEnd and otterEnd and singEnd):
            jump p_2TrainObservationBase
        "{i}Whisper to yourself \"mission complete\"{/i}" if nameEnd and otterEnd and singEnd:
            jump cTrainFulton

label beerChatChoice:
    stop sound
    # Passage: beerChatChoice
    drunkRat "\"Yes mate! I've been scouring for some drinking buddies and it looks like my -*burp*- prayers have been answered\""
    jump beerChatChoice2

label beerChatChoice2:
    stop sound
    play sound "audio/Narration/hehandsyou.mp3"
    "He hands you a beer, smile on mouth, excited that someone like him exists out in this world."
    menu:
        "Take the beer and drink to your hearts content":
            jump drunkChoice
        "Decline the beer, remembering what happened the last time you drank":
            hide ratFace with dissolve
            hide drunkRat with dissolve
            jump p_2TrainObservationBase

label songChoice:
    stop sound
    # Passage: songChoice
    stop music fadeout 1.0
    play music "audio/tswiftback.mp3" fadein 1.0
    show ratFace:
        linear 0.5 yoffset -100
        linear 0.5 yoffset 0
        repeat
    show drunkRat:
        linear 0.5 yoffset 0
        linear 0.5 yoffset -100
        repeat
    play sound "audio/Narration/heputshis.mp3"
    "He puts his arm around your opposite shoulder. You both sing your favorite Taylor Swift song in unison miles out of key: "
    jump songChoice2

label songChoice2:
    stop sound
    "\"You're on the phone with your girlfriend she's upset\""
    menu:
        "\"She's going off about something that you said\"":
            jump taylorSwiftLyric1
        "*Stop singing*":
            jump stopSingingChoice

label drunkChoice:
    stop sound
    # Passage: drunkChoice
    play sound "audio/Narration/theworldaround.mp3"
    scene black with dissolve
    "The world around you turns woozy. Swirls and colors mold together in a both hypnotic and agitating dance. Time passes by in a vaccuum. The fellow rat's speech is going through one ear and out the other, but in your head what he's saying could from the mouth of a professor from Harvard."
    jump drunkChoice2

label drunkChoice2:
    stop sound
    play sound "audio/Narration/youreyelidsbecome.mp3"
    "Your eyelids become heavier. You desire to explore the vast expanses of space. You want to be stuck on this train."
    $ status = "History repeats itself"
    menu:
        "*Close eyes*":
            jump Start

label taylorSwiftLyric1:
    stop sound
    # Passage: taylorSwiftLyric1
    "\"'Cause she doesn't get your humor like I do\"\n\"I'm in the room, it's a typical Tuesday night\"\n\"I'm listening to the kind of music she doesn't like\"\n\"And she'll never know your story like I do\""
    menu:
        "\"But she wears short skirts, I wear T-shirts\"":
            jump taylorSwiftLyric2
        "*Stop singing*":
            jump stopSingingChoice

label stopSingingChoice:
    stop sound
    stop music fadeout 1.0
    play music "audio/SubwayThemeALT.mp3" fadein 1.0
    # Passage: stopSingingChoice
    $ singEnd = True
    drunkRat "Cheerio mate {i}-*burps*-{/i} it was lovely to sing with you"
    hide drunkRat with dissolve
    hide ratFace with dissolve
    menu:
        "Go back to rumination" if not (nameEnd and otterEnd and singEnd):
            jump p_2TrainObservationBase
        "Go back to rumination" if nameEnd and otterEnd and singEnd:
            jump cTrainFulton

label taylorSwiftLyric2:
    stop sound
    # Passage: taylorSwiftLyric2
    play sound "audio/Narration/thetimidnessof.mp3"
    "The timidness of allowing your vocal soprano to flow has been thrown out. You don't care. It's time to be free."
    jump taylorSwiftLyric3

label taylorSwiftLyric3:
    stop sound
    "\"She's Cheer Captain, and I'm on the bleachers\"\n\"Dreaming about the day when you wake up and find\"\n\"That what you're looking for has been here the whole time\""
    menu:
        "*Sing through to the end of the song*":
            jump endSongChoice
        "*Stop singing*":
            jump stopSingingChoice

label endSongChoice:
    stop sound
    # Passage: endSongChoice
    $ singEnd = True
    play sound "audio/Narration/youbothlaugh.mp3"
    "You both laugh as you sing through to the end of the song. No one in the train audience claps, probably because you are both horrendus at singing. Nonetheless the other rat looks at you afterward and gives you a warm, needed, hug, pats you on the back, and simply says:"
    jump endSongChoice2

label endSongChoice2:
    stop sound
    stop music fadeout 1.0
    play music "audio/SubwayThemeALT.mp3" fadein 1.0
    drunkRat "\"Thank you\""
    $ status = "Content"
    hide drunkRat with Dissolve(3.0)
    hide ratFace with Dissolve (3.0)
    menu:
        "Go back to rumination" if not (nameEnd and otterEnd and singEnd):
            jump p_2TrainObservationBase
        "Go back to rumination" if nameEnd and otterEnd and singEnd:
            jump cTrainFulton

label ratChatChoice:
    stop sound
    # Passage: ratChatChoice
    drunkRat "\"Well I was doing a little bit of this and a little bit of that in the big city after college {i}-*burrrrp*-{/i} but it just wasn't for me. I had one big incident and it all came tumbling down after that. How about you?\""
    menu: 
        "\"I don't know\"":
            jump dontKnowChoice

label dontKnowChoice:
    stop sound
    # Passage: dontKnowChoice
    drunkRat "\"Mate what do you mean *you don't know?* What are you doing here ratting away then if you don't even know?\""
    $ status = "Confused"
    menu:
        "Chat about something else":
            jump ratChoice

label cTrainFulton:
    stop sound
    # Passage: cTrainFulton
    "\"{i}This is, Fulton St Station. Transfer is available to the 2; 3; 4; 5; and J trains. This is an accessible station{/i}\""
    jump cTrainFulton2

label cTrainFulton2:
    stop sound
    show otter at center:
        linear 5.0 xoffset 1200
    with dissolve
    show lion at left:
        yoffset -200
        linear 5.0 xoffset 900
    with dissolve
    $ renpy.pause(5.0, hard=True)
    show ratFace at left with dissolve
    play sound "audio/Narration/theotterhunches.mp3"
    "The Otter hunches off, probably off to meekly hand in his presentation. The Lion struts off, probably on her way to boss more of your fellow employees. Before the doors close she looks back to you:"
    jump cTrainFulton3

label cTrainFulton3:
    stop sound
    show lion:
        xzoom -1.0
    lion "\"Next time don't fuck {i}*it*{/i} up {i}*again*{/i} or else it's the real end for you\""
    jump cTrainFulton4

label cTrainFulton4:
    stop sound
    stop music
    hide lion
    hide ratFace
    scene closingDoors with dissolve
    play sound "audio/BING.mp3"
    $ renpy.pause(1.3, hard=True)
    play sound "audio/BONG.mp3"
    "\"{i}BING\"\n\n\"BONG{/i}\""
    jump cTrainFulton5

label cTrainFulton5:
    stop sound
    scene subwayAlt with dissolve
    show ratFace at left with dissolve
    play sound "audio/Narration/thedoorsbecome.mp3"
    "The doors become airtight. What is *it*? What did you do at Mckinsey & Company?"
    menu:
        "Ruminate even harder. Tap into your deepest memories to find your greatest mistake. Close your eyes (D16)":
            scene black with dissolve
            play music "audio/ThinkingSoundscape.mp3" fadein 1.0
            $ diceRoll = renpy.random.randint(1,20)
            jump memoryFlashback

label memoryFlashback:
    stop sound
    "......"
    # Passage: memoryFlashback
    if diceRoll >= 16:
        jump memoryFlashback1_2
    else:
        jump takeABreather

label memoryFlashback1_2:
    "Your roll: [diceRoll]"
    jump memoryFlashback2
label memoryFlashback2:
    stop sound
    scene warRoom with dissolve
    play sound "audio/Narration/thecheerilylit.mp3"
    "The cheerily lit war room materializes. Light escapes from the projector reflection, as the slides that took you and your team restless nights present themselves on the wall. Clean, pristine, and spotless, they're bound to impress the clients. Your read of the vibe is that {b}{i}The Streak{sup}TM{/sup}{/i}{/b} was still in the room with you."
    jump memoryFlashback3

label memoryFlashback3:
    stop sound
    $ diceRoll = renpy.random.randint(1,20)
    play sound "audio/Narration/everythinghasbeen.mp3"
    "Everything has been going smooth so far. Everyone's been on tempo, no cracks of the instruments yet to show. But then you reach the last slide:"
    menu:
        "Continue, endure the pain of the truth (D15)" if diceRoll >= 15:
            jump endurePainChoice
        "Continue, endure the pain of the truth (D15)" if diceRoll < 15:
            jump takeABreatherAlt

label endurePainChoice:
    stop sound
    # Passage: endurePainChoice
    "Your Roll: [diceRoll]"
    jump endurePainChoice2

label endurePainChoice2:
    stop sound
    play sound "audio/Narration/youreachintothe.mp3"
    "You reach into the deepest, darkest, depths of your brain. Stinging nettle of the memories irritate your claw. Your entity is being shredded, but you're getting close. Reach son. Reach."
    jump reachMoreChoice

label takeABreatherAlt:
    stop sound
    # Passage: takeABreather
    "Your Roll: [diceRoll]"
    jump takeABreatherAlt2

label takeABreatherAlt2:
    stop sound
    play sound "audio/Narration/youtryand.mp3"
    "You try and try. The room shakes, like an earthquake."
    jump takeABreatherAlt3

label takeABreatherAlt3:
    stop sound
    "{i}*Blink*{/i}"
    jump takeABreatherAlt4

label takeABreatherAlt4:
    stop sound
    play sound "audio/Narration/nopeitstoo.mp3"
    "Nope it's too much for you to handle. You need to take a breather, and try again"
    $ diceRoll = renpy.random.randint(1,20)
    menu:
        "Try again (D15)" if diceRoll >= 15:
            jump endurePainChoice
        "Try again (D15)" if diceRoll < 15:
            jump takeABreatherAlt

label takeABreather:
    stop sound
    # Passage: takeABreather
    "Your Roll: [diceRoll]"
    jump takeABreather2

label takeABreather2:
    stop sound
    play sound "audio/Narration/youtryand.mp3"
    "You try and try. The room shakes, like an earthquake."
    jump takeABreather3

label takeABreather3:
    stop sound
    "{i}*Blink*{/i}"
    jump takeABreather4

label takeABreather4:
    stop sound
    play sound "audio/Narration/nopeitstoo.mp3"
    "Nope it's too much for you to handle. You need to take a breather, and try again"
    $ diceRoll = renpy.random.randint(1,20)
    menu:
        "Try again (D15)" if diceRoll >= 15:
            jump memoryFlashback1_2
        "Try again (D15)" if diceRoll < 15:
            jump takeABreather

label backstoryChoice:
    stop sound
    play sound "audio/Narration/thelastslide.mp3"
    # Passage: backstoryChoice
    "The last slide:"
    jump backstoryChoice2

label backstoryChoice2:
    stop sound
    show slide with dissolve
    you "So with all the data tallied up Salesforce is currently spen-"
    jump backstoryChoice3

label backstoryChoice3:
    stop sound
    play sound "audio/Narration/amemberof.mp3"
    "A member of the client company raises their hand in the crowd:"
    jump backstoryChoice4

label backstoryChoice4:
    stop sound
    "\"Doesn't this add up to $3,110,000\""
    jump backstoryChoice5

label backstoryChoice5:
    stop sound
    stop music
    scene black with dissolve
    "{i}Flashback over{/i}"
    jump silentTrainChoiceIntro

label silentTrainChoice:
    stop sound
    # Passage: silentTrainChoice
    play music "audio/SubwayThemeALT.mp3"
    scene subwayAlt
    show ratFaceSad at left with dissolve
    play sound "audio/Narration/whatnow.mp3"
    "What now?"
    jump silentTrainChoice2

label silentTrainChoice2:
    stop sound
    # Passage: silentTrainChoice2
    play sound "audio/Narration/whatnow.mp3"
    "{i}What now?{/i}"
    jump silentTrainChoice3

label silentTrainChoice3:
    stop sound
    # Passage: silentTrainChoice3
    play sound "audio/Narration/whatnow.mp3"
    "{b}{i}What now?{/i}{/b}"
    jump dogTrainChoice

label dogTrainChoice:
    stop sound
    # Passage: dogTrainChoice
    play sound "audio/Narration/what.mp3"
    "{b}{i}WHAT{/i}{/b}"
    jump dogTrainChoice2
    jump petChoice

label dogTrainChoice2:
    stop sound
    play sound "audio/Narration/no.mp3"
    "{b}{i}NO-{/i}{/b}"
    jump dogTrainChoice3

label dogTrainChoice3:
    stop sound
    play sound "audio/BING.mp3"
    $ renpy.pause(1.3, hard=True)
    play sound "audio/BONG.mp3"
    "\"{i}BING{/i}\"\n\"{i}BONG{/i}\""
    jump dogTrainChoice4

label dogTrainChoice4:
    stop sound
    show cuteDog at right:
        parallel:
            linear 0.4 yoffset -200
            linear 0.4 yoffset 0
        parallel:
            linear 0.8 rotate 360
        rotate 0
        pause 0.2
        repeat
    play sound "audio/dogBark.mp3"
    cuteDog "\"RUFF RUFF\""
    jump dogTrainChoice5

label dogTrainChoice5:
    stop sound
    play sound "audio/dogBark.mp3"
    cuteDog "\"RUFF RUFF RUFF RUFF\""
    jump dogTrainChoice6

label dogTrainChoice6:
    stop sound
    play sound "audio/Narration/ohmygod.mp3"
    "Oh my god. The cutest dog you've ever seen walks onto the train. Not your weird boozed anthropomorphic versions of it but an actual genuine puppy. It's body so fat but it keeps wagging it's tiny little tail, looking at you with its beady eyes and tongue hanging from the side of its mouth."
    menu:
        "Pet it":
            jump petChoice

label silentTrainChoiceIntro:
    stop sound
    # Passage: silentTrainChoiceIntro
    play sound "audio/Narration/thatwasit.mp3"
    "That was it?"
    jump silentTrainChoiceIntro2

label silentTrainChoiceIntro2:
    stop sound
    play sound "audio/Narration/thatwaswhatcausedtheend.mp3"
    "That was what caused the end of {b}{i}The Streak{sup}TM{/sup}{/i}{/b}?"
    jump silentTrainChoiceIntro3

label silentTrainChoiceIntro3:
    stop sound
    play sound "audio/Narration/thatwaswhat.mp3"
    "That was what caused your entire life to spiral away?"
    jump silentTrainChoiceIntro4

label silentTrainChoiceIntro4:
    stop sound
    play sound "audio/Narration/youreallyare.mp3"
    "You really are pathetic. Everything that led up to this, was simply because you were slightly embarassed of an addition error that no one cared about except for you? Is this what life is about to you?"
    jump silentTrainChoice

label petChoice:
    stop sound
    # Passage: petChoice
    play sound "audio/Narration/asyourub.mp3"
    "As you rub the top of its head its eyes close, smile growing wider. The woes of the past transfer from your hand, through the dog, straight to the ground. The dogwalker holding its leash stands still, sunglasses on, airpods in."
    menu:
        "Say \"Sit\"":
            jump sitChoice

label sitChoice:
    stop sound
    # Passage: sitChoice
    play sound "audio/Narration/thedogdoes.mp3"
    "The dog does a little hop and then sits. Tail waggling on the ground even faster as it pants, spilling some drool on the ground."
    menu:
        "Try to rub its tummy":
            jump rubTummyChoice

label rubTummyChoice:
    stop sound
    # Passage: rubTummyChoice
    play sound "audio/Narration/youdoa.mp3"
    "You do a little finger gesture to convey \"roll over\" to the dog. The dog rolls over, still looking at you, and you start scratching it's tumm-"
    jump rubTummyChoice2

label rubTummyChoice2:
    stop sound
    "\"{b}{i}Attention passengers, this is Church Avenue. Transfer is available to the B, Q, F, and G trains. Stand clear of the closing doors, please.{/i}{/b}\""
    jump rubTummyChoice3

label rubTummyChoice3:
    stop sound
    hide cuteDog with dissolve
    play sound "audio/Narration/ohnoyour.mp3"
    "Oh no. Your joy. Your life. Your risk. It's all going soon. The dogwalker tugs the leash a little. The dog still looks at you as it trots its little legs through the doors on its way out. You could either reach, risk leaving the train, or simply stay, and continue {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. The doors begin to close their shackles."
    $ diceRoll = renpy.random.randint(1,20)
    menu:
        "Reach son. Reach. (D0)":
            jump exitTrainChoice
        "Stay. (D0)":
            jump stayChoice

label exitTrainChoice:
    stop sound
    # Passage: exitTrainChoice
    "Your Roll: [diceRoll]"
    jump exitTrainChoice2

label exitTrainChoice2:
    stop sound
    scene subwayOpen with dissolve
    show ratFace at left with dissolve
    play sound "audio/Flashbang.mp3" fadeout 0.2
    show flash:
        alpha 1.0
        linear 0.3 alpha 0.0
    pause 2
    hide flash
    "**FLASH**"
    jump exitTrainChoice3

label exitTrainChoice3:
    stop sound
    show ratFace:
        linear 0.6 yoffset -100
        linear 0.6 yoffset 100
        repeat
    show cuteDog at right:
        xzoom -1.0
        linear 0.6 yoffset 200
        linear 0.6 yoffset -300
        repeat
    with dissolve
    play sound "audio/Narration/itssimplytoo.mp3"
    "It's simply too much for you to comprehend. The un-plastic air. The smell of wind. The lack of LEDs. You've walked outside."
    jump exitTrainChoice4

label exitTrainChoice4:
    stop sound
    play sound "audio/Narration/butthedog.mp3"
    "But the dog and dogwalker are quick on their feet, making pace to turn the corner at the block."
    menu:
        "Get your drunk ass up and follow":
            jump followChoice

label stayChoice:
    stop sound
    # Passage: stayChoice
    "Your Roll: [diceRoll]"
    jump stayChoice2

label stayChoice2:
    stop sound
    "..."
    menu:
        "Sit in silence":
            jump badEnd1

label followChoice:
    stop sound
    # Passage: followChoice
    scene beautiful with dissolve
    show ratFace at left:
        linear 0.6 yoffset -100
        linear 0.6 yoffset 100
        repeat
    with dissolve
    show cuteDog at right:
        xzoom -1.0
        linear 0.6 yoffset 200
        linear 0.6 yoffset -300
        repeat
    with dissolve
    play sound "audio/Narration/yourlimbsbegin.mp3"
    "Your limbs begin to move. Your core has the integrity of a fresh jello. Fuck {b}{i}The Streak{sup}TM{/sup}{/i}{/b}. You roll your way through Church Av, oncoming passerby's stiffly shuffling out the way."
    jump keepFollowChoice

label keepFollowChoice:
    stop sound
    # Passage: keepFollowChoice
    play sound "audio/Narration/yourcardiois.mp3"
    "Your cardio is starting to give out. But you keep trudging forward. The dog still looks behind at you but the dog walker is moving ground on you. You begin to fear if it's out of reach. I guess it'll be okay if it does."
    jump keepFollowChoice2

label keepFollowChoice2:
    stop sound
    scene apartmentFront with dissolve
    show ratFace at left with dissolve
    show cuteDog at right:
        linear 0.6 yoffset 200
        linear 0.6 yoffset -300
        repeat
    with dissolve
    play sound "audio/Narration/butthedogwalker.mp3"
    "But the dogwalker stops. Right in front of a small apartment complex. She takes off her shades and take out their airpods. As you catch your footing to get closer to the dog the dogwalker looks at you, your heights exactly even."
    jump keepFollowChoice3

label keepFollowChoice3:
    stop sound
    play sound "audio/Narration/shehandsthe.mp3"
    "She hands the handle of the leash to you and opens the door, and then simply walks off with her airpods back in."
    menu:
        "Walk in":
            jump walkChoice

label walkChoice:
    stop sound
    scene stairwell with dissolve
    # Passage: walkChoice
    play sound "audio/Narration/youwalkinside.mp3"
    "You walk inside. Warm lights illuminate the halls. The dog leads the way for you, you just follow the pull until you reach a door."
    jump walkChoice2

label walkChoice2:
    stop sound
    scene apartmentDoor with dissolve
    "{b}2R{/b}"
    jump walkChoice3

label walkChoice3:
    stop sound
    play sound "audio/Narration/youreachinto.mp3"
    "You reach into your pockets expecting a key. There's jack shit in there. Dammit."
    menu:
        "REACH FURTHER SON!":
            jump reachFurtherChoice

label reachFurtherChoice:
    stop sound
    # Passage: reachFurtherChoice
    play sound "audio/Narration/youreachand.mp3"
    "You reach and reach, nothing there but void and destruc-"
    jump reachFurtherChoice2

label reachFurtherChoice2:
    stop sound
    play sound "audio/dogBark.mp3"
    "{b}RUFF RUFFF RUFFF{/b}"
    jump reachFurtherChoice3

label reachFurtherChoice3:
    stop sound
    play sound "audio/Narration/thedogbarks.mp3"
    "The dog barks loudly and you hear the click of the lock on the door unfasten."
    jump preEnd

label preEnd:
    stop sound
    "{b}HAPPY BIRTHDAY CLINT!{/b}"
    jump preEnd2

label preEnd2:
    stop sound
    play sound "audio/Narration/itsyourfriends.mp3"
    "It's your friends and family. They've decided to hold a birthday party for you: someone they deem special enough to hold it for. Your family lives across the country but flew out to see you. Your roommates let them in and set up the large frosted cake on the shabby dining table. You're 26 now, one year older than that {i}douchebag{/i} manager Trash-sta Vanderbelch or whatever her name is. Your {b}{i}Streak{sup}TM{/sup}{/i}{/b} of being 25 is now over, and you couldn't be happier."
    jump goodEnd

label goodEnd:
    stop sound
    # Passage: goodEnd
    "THE END"
    # End node
    return

label badEnd1:
    stop sound
    # Passage: badEnd1
    "{b}{i}Last stop, Flatbush Avenue-Brooklyn College. Everyone please leave the train. This is the last stop.{/i}{/b}"
    menu:
        "Sit in silence":
            jump badEnd2

label badEnd2:
    stop sound
    # Passage: badEnd2
    play sound "audio/Narration/timepassespeople.mp3"
    play sound "audio/Narration/timepassespeople.mp3"
    "Time passes. People walk. Rats stay. You get on the same exact train but it's now uptown.This was your choice."
    menu:
        "Sit in silence":
            jump badEnd3

label badEnd3:
    stop sound
    # Passage: badEnd3
    "{b}{i}This is Fulton Street. Transfer is available to the 3, 4, 5, J, Z, and A, C, E trains. Stand clear of the closing doors, please.{/i}{/b}"
    menu:
        "Sit in silence":
            jump badEnd4

label badEnd4:
    stop sound
    # Passage: badEnd4
    play sound "audio/Narration/standclearof.mp3"
    "{b}{i}Stand clear of the closing doors, please.{/i}{/b}"
    menu:
        "Sit in silence":
            jump badEnd5

label badEnd5:
    stop sound
    # Passage: badEnd5
    "..."
    menu:
        "Sit in silence":
            jump badEnd5_2

label badEnd5_2:
    stop sound
    play sound "audio/Narration/theotherrat.mp3"
    "The other rat in the corner nods at you approvingly, a beer in his hand."
    menu:
        "Sit in silence":
            jump badEnd6

label badEnd6:
    stop sound
    # Passage: badEnd6
    play sound "audio/Narration/youseethedog.mp3"
    "You see the dog walking, through the window in the station with the same dog walker."
    menu:
        "Sit in silence":
            jump badEnd7

label badEnd7:
    stop sound
    # Passage: badEnd7
    play sound "audio/Narration/atadifferent.mp3"
    "At a different stop you see the Otter through the window. He seems to have bounced back from his powerpoint issues. It also seems like he's still employed."
    menu:
        "Sit in silence":
            jump badEnd8

label badEnd8:
    stop sound
    # Passage: badEnd8
    play sound "audio/Narration/youseethe.mp3"
    "You see the Lion through the window. She's got a new promotion."
    menu:
        "Sit in silence":
            jump badEnd9

label badEnd9:
    stop sound
    # Passage: badEnd9
    "..."
    menu:
        "Sit in silence":
            jump badEnd10

label badEnd10:
    stop sound
    # Passage: badEnd10
    play sound "audio/Narration/youareratface.mp3"
    "You are Ratface."
    menu:
        "Sit in silence":
            jump badEnd11

label badEnd11:
    stop sound
    stop music fadeout 1.0
    play sound "audio/Narration/theend.mp3"
    "THE END"
    return

label reachMoreChoice:
    stop sound
    # Passage: reachMoreChoice
    play sound "audio/Narration/evenmoreson.mp3"
    "Even more son."
    menu:
        "*Reach further*":
            jump backstoryChoice

label deadChoiceAlt:
    stop sound
    # Passage: deadChoiceAlt
    play sound "audio/Narration/occassionalrumblesyoure.mp3"
    "Occassional rumbles, you're like a celestial body. This is what the dead planets and quarks will experience after the heat death of the universe. You're just getting a preview."
    menu:
        "Continue to lay down":
            jump deadChoice
        "Open your eyes":
            jump openEyeChoice
