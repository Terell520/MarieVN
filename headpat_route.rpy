transform right:
    xalign -3.5
    yalign 1.0

transform left:
    xalign 4.5
    yalign 1.0

transform the_left:
    xalign 5.0
    yalign 1.0

transform the_right:
    xalign -4.0
    yalign 1.0

transform flip:
    yalign 4.5
    xzoom -1.0

#There are 3 endings: The Headpat, The Musician, The Kiss, another end and another another end
#The max amount of points is 10
## Add with +=, check with == or >= or <=

default mariepoint = 0
default sethpoint = 0

#Defining variables
$ convoWithLucid = False
$ phone = False
$ marieList = False
$ pretzel = False
$ concerned = False
$ illConsiderIt = False
$ regret = False
$ check = False


# The game starts here.

label start:


    scene bg city
    "It's the middle of the night. The city is bright just as the daytime. I can't lie, it looks pretty. "

    "Walking besides me is Marie. Me and her just had dinner at a resturaunt. The food was really good."

    s "Hey, Marie?"

    m "Yes, Seth?"

    s "We've been strolling in the city for a while now. Are we going somewhere else?"

    m "We're almost there..."
    
    s "?"
    scene bg park

    with Dissolve(.5)

    "We ended up going to the local park. 
    
    I'm starting to be bit more confused by the minute. We sat on the nearest bench."

    show mariem normal

    s "Uhhh, what are we doing at the park?"

    m "I'm about the give you your gift of course."

    "Marie puts her head down slightly."

    "I-I-Is this what I think it is?!"

    show mariem serious

    m "Hmm? What are you waiting for? Do you want this headpat or not?"
    stop music 

    play sound "shattered_glass.mp3"

    s "!"

    play sound "heartbeat.mp3" loop

    "My heart starts beat. Am I really going to give Marie a headpat?!"

    "I start to slowly raise my hand to Marie's head."

    s "{size=-10} It's finally happening! I'm going to give Marie a headpat!{/size}"

    "As my hand gets close to Marie's head, I start hearing loud noise."

    play sound "alarmclock.mp3" loop

    "It...{p=1.5} was an alarm clock."

    "{size=+10} I NEED TO HURRY UP! I MUST COMPLETE THE HEADPAT!{/size}"

    "{size=+10} NO! NOOOOOOOOOOOOOOOOOOOOOOOOOOOO!{/size}"

    scene bg bedroom

    with Dissolve(5)

    stop sound fadeout 1.0

    "I woke up from my slumber. I feel groggy. I start looking for my phone."
            
    menu:

        s "Hmm. Where did I put it?"

        "Look under my bed":

            $ sethpoint += 1

            $ phone = True
            
            "I start searching for my phone under my bed. I moved my hand all over the floor until I felt a rectanglar shape. It's my phone!"

            "I turned it to see the time and date."

            "It's 2 in the afternoon. The date is August 29th."

            s "Oh shit it's my birthday."

            "It's nothing too special. It just feels like another day to me."

            s "Welp, I gotta go shower."

        "Check my dresser drawer":

            $ phone = True
            
            "I start searching for my phone in my dresser. I {p=1.5} found it instantly..."

            s "Why would anyone leave their phone in a dresser drawer? That doesn't even make any sense."

            s " *sigh* whatever, I have to bathe."

        "Eh, fuck it, I look for it later":

            $ sethpoint += 2

            $ phone = False
            
            "I don't feel like looking for it right now. I'm gonna go shower."

            "I leave out of my room and went to the bathroom."

    scene bg bathroom

    with Dissolve (.5)

    "I showered, I washed my face and hair. After I did that and dressed up. I looked at the mirror."

    play sound "shine.mp3"

    show kensukeh normal 
    s "Ah, much better!"

    "After looking at the mirror, I went to the kitchen."
    if phone:
        jump kitchen_with_phone
    else:
        jump kitchen_no_phone

label kitchen_with_phone: 
    play music "idle_talk.mp3" fadein 0.5 loop
    scene bg kitchen
    with Dissolve (.5)

    "I went to the kitchen and saw Lucid eating a bag of chips."

    "Wait {p=2} how the hell is he even eating that?"

    s "Hey Lucid."

    show lucid at right

    l "Good Afternoon, Seth. Happy Birthday!"

    show kensukeh smile at left

    s "Thank you!"

    "I looked around the room and I don't see Marie."

    hide kensukeh smile
    show kensukeh normal at left

    s "Hey Lucid, have you've seen Marie?"

    l "Yeah, she went out for some errands. She told me to tell you to get ready."

    s "For what?"

    l "She has made reservations for dinner. It's taking place in the city."

    hide kensukeh normal
    show kensukeh worried at left

    s "That's very far from here..."

    l "Yeah."

menu:
    "*sigh* What should do to kill time?"

    "Talk to Lucid":
        
        $ sethpoint += 2
        $ convoWithLucid = True
        $ illConsiderIt = True
        
        hide kensukeh worried
        show kensukeh normal at left

        s " So Lucid, when's your recording session?"

        l "It's going to be tonight at midnight."

        s "At midnight? Isn't that a bit late?"

        l "Nah, that's my usual time when I make music. You interested in coming?"

        s "I'm a bit curious I can't deny. But I can't because of Marie's reservation."

        l "I don't think the trip over to city is THAT long. Maybe 5 to 6 hrs tops."

        s "How do you get over there? I never see you with a car."

        l "Y'know that pink door I walk in to from time to time?"

        s "Yeah? What about it?"

        l "It can take me anywhere I want."

        s "I should've figured."

        "After I said that, I came to relize something."

        s "Wait, so why can't you just take us to the city through the door?"

        l "Because A, It only works for me and me alone and B Marie has something planned."


        hide kensukeh normal
        show kensukeh surprised at left

        s "Huh?"

        l "Oh, I probably shouldn't have said that. She's a gonna be pissed at me. Can you pretend that you didn't hear it?"

        hide kensukeh surprised
        show kensukeh normal at left

        s "Yeah, sure."
        
        "Though I'm a bit curious about what Marie has planned. I say goodbye to Lucid and left the house."

        if convoWithLucid:
            jump outside
        else: 
            jump kitchen_no_phone
    
    "Leave out the house.":
            
        $ convoWithLucid = True
    
        "I say goodbye to Lucid and left the house."
        
        if convoWithLucid:
            jump outside
        else: 
            jump kitchen_no_phone

label kitchen_no_phone:
    play music "idle_talk.mp3" fadein 0.5 loop 
    scene bg kitchen

    with Dissolve (.5)

    "I went to the kitchen and saw Lucid eating a bag of chips and Marie is writing on a piece of paper."

    "Wait {p=2} how the hell is he even eating that?"

    s "Hey Lucid and Marie."

    show lucid at right
        
        
    l "Good Afternoon, Seth. Happy Birthday!"

    show mariem normal at the_left
                
    m "Happy Birthday, Seth!"

    s "Wait, today's my birthday?"

    "Marie shows me her phone and it's indeed my birthday August 29th."

    s "Thank you you guys!"

    hide mariem normal 
    show mariem serious at the_left

    m "I've made reservations for dinner, so prepare for that. {p=1.5} Now."

    hide lucid
    show kensukeh surprised at right

    s "Now?! It's 2 in the afternoon!"

    m "We're going to the city, which is very far from home."

    s "Oh ok. Is Lucid coming with us?"

    hide mariem serious
    show lucid at left

    l "I can't. I'm working on a track on the studio. You should really drop by one of these days."

    hide kensukeh surprised
    show kensukeh worried at right

    s "I want to, I don't have the talent to make good music like you two."

    l " *sigh* If you say so."

    hide lucid
    show mariem serious at the_left

    m "Alright Seth, get yourself ready. I got to do a couple of quick errands."

    hide kensukeh worried
    show kensukeh surprised at right

    s "I just showered. What else should I even do?!"

    m "I don't know. Figure it out. Well I got to go."

    hide mariem serious
    with Dissolve (.5)

    "Marie left the house."


menu:
    "*sigh* What should do to kill time?"

    "Talk to Lucid":
        
        $ sethpoint += 2
        $ illConsiderIt = True

        hide kensukeh worried
        show kensukeh normal at left

        s "So Lucid, when's your recording session?"

        show lucid at right

        l "It's going to be tonight at midnight."

        s "At midnight? Isn't that a bit late?"

        l "Nah, that's my usual time when I make music. You interested in coming?"

        s "I'm a bit curious I can't deny. But I can't because of Marie's reservation."

        l "I don't think the trip over to city is THAT long. Maybe 5 to 6 hrs tops."

        s "How do you get over there? I never see you with a car."

        l "Y'know that pink door I walk in to from time to time?"

        s "Yeah? What about it?"

        l "It can take me anywhere I want."

        s "I should've figured."

        "After I said that, I came to relize something."

        s "Wait, so why can't you just take us to the city through the door?"

        l "Because A, It only works for me and me alone and B Marie has something planned."

        hide kensukeh normal
        show kensukeh surprised at left

        s "Huh?"

        l "Oh, I probably shouldn't have said that. She's a gonna be pissed at me. Can you pretend that you didn't hear it?"

        s "Yeah, sure."
        
        "Though I'm a bit curious about what Marie has planned."
    
    "Leave out the house":
    
        "I say goodbye to Lucid and left the house."  

label outside:
    stop music fadeout (1.0)
    scene bg outside

    with Dissolve (.5)
    $ convoWithLucid = True

    "I'm outside. The weather is what I expect from the summer. But it's suprisingly windy as well. I see small birds around the house hopping and chirping around."

    "My stomach starts to growl."

    s "Oh yeah, I never ate anything when I woke up. The mall probably has some good food."

    "I start walking my way to the mall."

label mall:
    scene bg mall
    play music "walk_on.mp3" fadein 0.5 loop
    play sound "crowded_mall.mp3" loop fadein 0.5 volume 0.3
    with Dissolve (0.5)


    "After a hour long walk, I made it to the mall."

    s "Holy shit, that was tiring."

menu:
    "Where should I go to get food?"

    "Get something from the pizza shop.":

        $ sethpoint += 1
        $ mariepoint += 1 
        $ marieList = True 


        s "I haven't had pizza in a while. I'm going to get that."

        scene bg pizzastore
        with Dissolve (0.5)

        "I found the pizza shop. The line was fairly short, so I didn't have to wait that long."

        s "Can I have a single cheese slice and a bottle of Sprite please?"

        w "That would be $3.50."
        play sound "kashing.mp3"

        "I paid for my food and went on my way."

        scene bg mall
        with Dissolve (0.5)

        "When I went out of the pizza shop I saw a woman in gray. It was Marie. It looks like she left out of a clothes store. She is holding two bags."

        show mariem serious at right
        with ease

        "She starts looking around and then starts dashing away."

        hide mariem serious
        with easeoutleft

        s "Huh?! She ran extremely quickly..."

        "I saw a piece of paper come out of Marie's pocket. I picked it up and read the contents of it."

        show kensukeh normal
        
        s "Make-up, New clothes, and..."

        "?"

        "The third item of the list looks like it's completely marked off. The marks were so dark that I can't see a single letter."

        "After reading the contents of the paper, I put the list in my pocket and then I looked at the store's name Marie was just in."

        s "Tatefushi, huh? It sounds fancy."

        "I walk inside."

        scene bg clothingstore
        with Dissolve (0.5)

        "I start to look around the store."

        show kensukeh surprised

        s "The clothes here look very high quality."

        "Is this a store Marie regularly goes to?"

        "It can't be. The clothes Marie usually wears are from a brand called Kishimai. It's the same brand that I got my clothes from."

        hide kensukeh surprised
        show kensukeh normal

        "After looking at some of the clothes one of the store workers approached me."

        w "Do you need any assistance finding something?"

        hide kensukeh normal
        show kensukeh worried

        s "Uh, no thank you. I-I was just looking around."

        "The worker walks away."

        s "I'm surprised that she would go THIS far for a single night. It really makes you wonder what else she has planned outside of dinner."

        "After admiring the clothes in the store, I leave and went outside of the mall."

        if illConsiderIt:
            jump lucid_encounter
        else:
            jump mall_outside

    "Go get a Pretzel.":

        $ sethpoint += 3
        $ pretzel = True

        "I decided to go to the pretzel store."

        scene bg pretzelshop
        with Dissolve (0.5)

        s "Can I have 1 original pretzel and a lemonade, please?"

        w "That'll be $8.38."
        play sound "kashing.mp3"

        "I paid for my stuff and went on my way."

        scene bg mall
        with Dissolve (0.5)

        show mariem serious at right
        with ease

        "When I left the pretzel store, I saw Marie coming out of the clothing store. She has a bag of clothes. She looks around the area and starts carefully running away." 

        hide mariem serious
        with easeoutleft

        "Curious of what she's doing I start following her around."

        "I followed her until she stopped by a make-up store."

        scene bg makeupstore
        with Dissolve (0.5)

        "The store it's looks like they sell high quality make-up."

        "I see her about to leave the store."

        s "Oh shit, I need to find a place to hide."

        s "Hmm..."

        s "Where is a good spot to hide..."

        "I looked up in the higher floors and thought of something."

        s "The Third floor!"

        "The Third floor is a good idea to hide. I can still see Marie move around the mall without looking suspicious. Plus I highly doubt she would just look up at the other floors for no reason."

        "I start running to the elevator. I would take the escalators but Marie will notice me."

        scene bg elevator
        with Dissolve (0.5)

        "In the elevator, there's not really much people in it. I pressed the third floor button and waited for my stop."

        "1 stop. {p=1.5} 2 stops {p=1.5} and then 3 stops."

        "I'm at the third floor."

        scene bg thirdfloor
        with Dissolve (0.5)

        "I speedwalked around the third floor to see what Marie is doing in the first floor."

        "I managed to find a sweet spot."

        "I waited for a while, until I saw Marie walk out of an electronics store. She has a big mysterious box in one hand and an extra bag in another."

        "The box is fairly heavy. I genuinely wonder how she would carry all of that..."

        "Marie with all of her strength picked up all of her luggage and leaves the mall."
    
        s "What would she be doing with such heavy luggage? I hope she'll be alright..."

        "After wondering about Marie's shopping items, I leave out of the mall."

        if illConsiderIt:
            jump lucid_encounter
        else:
            jump mall_outside

label lucid_encounter:

    scene bg mall
    with Dissolve (1.0)

    "As I was looking for an exit, I see a guy in a lack coat."

    "It was Lucid."

    "I start calling out to him."

    show kensukeh surprised at left

    s "Hey, Lucid!"

    show lucid at right

    l "Hmm?"

    l "Hey, Seth. Funny to see you here."

    s "I should be saying that to you! What you doing at the mall?"

    l "I was just in the radio station, promoting my music as usual."

    hide kensukeh surprised
    show kensukeh normal at left

    s "I would've figured."

    s "I was very hungry so I just came here to get food."

    l "So, you walked a couple of miles to get here instead of going to the supermarket near the house?"

    hide kensukeh normal
    show kensukeh worried at left

    s "I {p=1} really should've thought of that..."

    l "Well, I'm going back to the house, see ya."

    s "See ya."

    l "Also remember the offer I gave you."

    s "Yeah, I know."

    hide lucid
    with Dissolve (.5)

    "Lucid walks away."

    "Can I really make music that actually sounds good? What it ends up being terrible and embarrass myself in front of others?"

    "*sigh* My head hurts when I think about it."

    jump mall_outside

label mall_outside:
    scene bg malloutside
    with Dissolve (0.5)

    s "That was quite the adventure."

    "I looked at the time. It looks like I still have time until the dinner. I start walking home."
    jump home
    
label home:
    stop music fadeout (1.0)
    stop sound fadeout 1.0
    scene bg living
    with Dissolve (0.5)

    "When I walked in, I see Lucid laying on the couch watching anime."

    show kensukeh normal at right
    s "Lucid, I'm home."

    show lucid at left
    l "Welcome back."

    "Lucid looks at the time on his phone."

    l "It's 4:30. You still have some time until the dinner, y'know?"

    s "Yeah, I know."

    menu:

        "What should I do until then?"

        "I'm going to work on videos.":

            l "Alright."

            scene bg bedroom
            with Dissolve (0.5)

            "I went to my room and start looking for my laptop."

            "Ah ha!"

            "There it is. My gaming laptop."

            "The device that has been carrying me througout my YouTube carrer. I've had it around for 8 whole years. We've been through so much with each other."

            "But...{p=1} It's on it's last legs."

            s "..."

            s "I'm so sorry for putting you through all this. I will let you rest in peace very soon."

            s "Just{p=1}.{p=1}.{p=1}. hold on for a little longer, ok?"

            "I turn on the laptop and start doing my making my videos."

            "I worked a bit on the Monark playable bosses, My CentralFiction Mods and so on."

            "After 2 hours amount of work, I looked at the time. It's 6PM."

            s "I think it might be ready to leave."

            "I looked at my laptop in sadness. I save all of the work I've done and then completely shut it off and left my room."

            $ concerned = True

            scene bg living
            with Dissolve (0.5)
            "In the bathroom, I hear Marie humming Cosmo Dancer."

            s "Ahh, that song NEVER gets old."

            "The song is so good that I start humming it myself."

            s "Chire! Kiete! Mienaku naru made! Hora arasoeba iijyan! Anata-tachi no odoru butai wa atashi no......"

            "After enjoying singing best song, I start waiting in the living room to Marie to finish."

            show lucid at right

            l "Yo."

            show kensukeh normal at left

            s "Hey."

            l "Marie is been in there for a while."

            s "How long has she been in the bathroom for?"

            l   "Almost 2 hours."

            hide kensukeh normal
            show kensukeh surprised at left

            s "Huh?!"

            l "Yeah, she quickly walked in without saying anything. The only time she went out is to get her make-up."

            s "Wow. {p=1.5} Just wow."

            "After that small interaction with Lucid, I hear the bathroom door open."

        "Watch anime with Lucid.":

            hide kensukeh surprised
            show kensukeh normal at right

            s "What are you watching, Lucid?"

            l "Code Geass."

            "On the TV screen I see a guy with a black outfit. One of his eyes was red with a symbol on it."

            "I was not interested until I heard his voice."

            hide kensukeh normal
            show kensukeh surprised at right

            s "I-IS THAT JOHNNY YOUNG BOSCH?!"

            l "Yeah, he is Lelouch's voice actor. He's also the protagonist of the show."

            s "Ok, now you got me COMPLETELY sold!"

            "I dashed towards the other side of the couch and watched a couple of episodes for 2 hours."

            s "That {p=1} was amazing."

            l "Yeah, the show is pretty neat. It's definitely my type of anime."

            "After discussing of what we've watched, I hear the bathroom door opened."

            hide lucid

    "It was Marie."

    hide kensukeh surprised
    show mariea normal at left

    "She looked completely different from what I usually see her."

    hide lucid
    show kensukeh blushing at right

    "That beautiful straight brown hair and the black outfit that complements it's brown color. It {p=2} made my eyes start to dilate like how a cat when they are happy to see their owner."

    s "Y-Y-you look beautiful, Marie."

    hide mariea normal
    show mariea smileblush at left

    $ mariepoint += 2

    m "I worked all day to get this outfit. I'm very glad you liked it!"

    hide mariea smileblush
    show mariea normal at left

    m "Shall we take our leave?"

    s "Y-Yeah."

    l "Alright you two, I'll see y'all later."

    "Me and Marie walk out of the house."

    scene bg outsidenight
    with Dissolve (1.0)

    show kensukeh normal at right

    show mariea normal at left

    s "So, how are we going to go to the city?"

    m "Through car of course."

    play sound "carkeys.mp3"

    "Marie takes out a car key and presses a button. The car that reacted to the button press was a Tesla."

    "Out of pure curiostity, I looked around the car."

    "The more I looked at this car, the more mesmerized I became."

    hide kensukeh normal
    show kensukeh surprised at right

    s "Is this the Model 3 version?! This came out not that long ago!"

    "That job she has must've payed VERY well."

    m "You going inside?"

    s "Of course!"

    scene bg car
    with Dissolve (1.0)

    show mariea normal at left

    "We're inside of the car. The interior looks beautiful. It complements well with the aesthetic Marie is going for."

    "I {p=1.5} start blushing again."

    show kensukeh blushing at right

    show mariea nervoussmile at left

    m "So, uhhhh how does this thing work?"

    hide kensukeh blushing
    show kensukeh surprised at right

    s "Wait. Is this your first time using this car?"

    m "Kind of. I've used this car for todays errands. I'm not that used to these types of cars."

    s "Oh, ok. You just need to push this button over there."

    "The engine starts reving and the lights in the car turns on as well."

    "Marie starts typing on the car's tablet. It looks like she's looking for directions for the city."

    hide mariea nervoussmile
    show mariea serious at left

    m "Alright, here we go!"

    "Marie starts driving."
    
    play sound "driving.mp3" loop fadein 1.0
    scene bg highway
    with Dissolve (2.0)

    "2 Hours have passed by. The roads still looked the same."

    s "Hey Marie, are we there yet?"

    m "No. The GPS says that we're 3 hours away."

    s "Holy fuck..."

    "I start laying on the window out of boredom."

    "I was thinking about things that happened today."

    "I'm still thinking about the list Marie dropped when she was in the mall."

    "I remember her having 3 things. Make-up, new clothes and that mysterious box she was carrying."

    "The first two is obvious. She's wearing the new clothes and make-up right now."

    "That Box is the only thing that is bothering me. I don't know what it supposed to be. An air fryer, a desktop?"

    "*sigh* Who knows? The shopping spree must've payed off. The new stuff she bought looks very good on her. She looks happy while wearing it too."

    "The roads kept looking the same. There wasn't anything interesting that catches my eye."

    "I start fall asleep."

    if sethpoint >= 6:
        jump shadowlord
    else:
        jump knocked_out

label shadowlord:

    stop sound fadeout 5.0
    scene bg black
    with Dissolve (5.0)

    "I wake up in a castle."

    $ curiostity = True

    s "W-What am I doing here?"

    a "What do you mean 'What are we doing here?' We're going to save Marie, remember?"

    s "Huh?"

    a "5 years ago, Marie was kidnapped by the Shadowlord and you needed my help to save her."

    a "After we've beaten Mother Goose, you passed out from exhaustion. I was waiting until you woke up again."

    "I was completely lost with what Aria is saying. I just went on with what she has said."

    s "Oh alright. That fight was rather tiring."

    s "Ok, I'm ready to go now."

    "After a small convo with Aria we arrived at the Shadowlord's chamber."

    play music "shadowlordgestaltver.mp3" fadein 1.0 loop

    "The huge door opens."

    "I see Marie in a fancy bed."

    s "Marie!"

    "I start running towards but a mini black portable starts appearing. What came out of it confuses me."

    "It's me. But it looks very distorted. The body is mostly black with some parts being yellow."

    "The creature comes out the comes out of the portal and floats above us. He flaps his wings imposingly."

    "I summoned my Claymore while Aria sets up her Virtuadoll powers."

    "I point my weapon at the Shadowlord."

    s "How DARE you kidnap Marie you bastard! I'll cut you down!"

    "I run towards the enemy."

    "The Shadowlord rises his hand."

    a "Seth, watch out!"

    "I look at the floor. There's black spots everywhere. Spikes were coming out of them."

    s "Oh, shit!"

    "I immeditely use the Emergancy Barrier."

    s "Phew, that was close!"

    "After I Protected myself, one of Aria's spears zoomed passed me and strikes the Shadowlord."

    "Shadowlord falls down. This is my perfect time to strike!"

    "I drag my sword to the air. A slash of energy rushes towards the enemy and hits him."

    "The Shadowlord gets blown back. He gets up and summons his own claymore."

    "Shadowlord runs towards me. We clash swords. I have an angered expression on my face while his looks emotionless."

    s "Why do you look like me?!"

    "He doesn't respond. Both of us pushed ourselves back. Shadowlord throws a myriad of red orbs on the ground. When the orbs hit the ground, huge fire pillars start appearing."

    "I start getting close the Shadowlord as I keep avoiding his ranged assault."

    "I manage to get close to the enemy but when I saw him, he had 5 spears readed up. I kept running foward."

    "Shadowlord shoots his spears towards me. I avoided the attack."

    "I start spinning myself and my blade in the air. After that, I drag my sword to fling Shadowlord into the air."

    s "Aria!"

    stop music fadeout (1.0)
    play music "shadowlordmusicboxgestalt.mp3" fadein 3.0 loop

    "Aria charges her lasers from her spears and shoots them at Shadowlord. He falls down and he looks like he's severely weakened."

    "I start walking towards the Shade. I get closer and closer."

    "I positioned myself for the final blow."

    "I looked that the Shadowlords face one more time. I start to hesitate but quickly shug it off and finished him off."

    s "It's over..."

    "My body starts to fall down."

    "As my body is laying on the ground, my claymore starts to dissapear. The black stake on my chest starts receding while the flowers on them start to wither away."

    "A black smoke starts surrounding my body and Angelic Script symbols start appearing around my neck and arms."

    a "What the hell is happening?!"

    "Am I dying?"

    "..."
    
    "No. I will NOT accept this! GET UP! GET UP!"

    "My body doesn't react to my cries."

    "My legs starts fading away."

    "Then my torso."

    "I reached out to Marie's resting body. As I do so, my eyes start tearing up."

    s "I never told her how I felt about her..."

    $ regret = True

    "Everything turns to black."

    stop music fadeout 5.0
    scene bg car
    with Dissolve (5.0)
    play sound "driving.mp3" loop fadein 1.0

    "I start to wake up with a tears on my eyes."

    s "Why am I tearing up?"

    m "Hmm? Seth, are you alright?"

    s "Huh? Yeah I'm fine."

    "I wipe away the tears with my arms. After clearing my eyes, I start seeing huge buildings everywhere."

    scene bg thecity
    with Dissolve (1.0) 

    m "We're here at the city! Doesn't it look amazing?"

    s "It's so bright even at night."

    m "I just need to find a parking spot."

    jump dinner



label knocked_out:

    "After a while, I get back up and streched my arms."

    "I looked at the window. There was big buildings everywhere."

    m "Here we are, Seth! The City!"

    scene bg thecity
    with Dissolve (1.0)
    play sound "driving.mp3" loop fadein 1.0

    s "Whoa..."

    "The buildings here look very bright. It looks beautiful."

    m "Here we are! The City!"

    m "I just need to look for a space to park."

label dinner:
    stop sound fadeout 1.0
    scene bg parkinglot
    with Dissolve (1.0)

    "The car we're in goes inside a huge parking spot. We get out of the car."

    "As I start walking away, I hear the car trunk open."

    "I start hearing muffled screaming."

    m "{size=-10} Will you shut the fuck up already? {/size}"

    "The trunk door closes."

    play sound "closetrunk.mp3"

    s "Hmm? What was that?"

    m "Nothing."

    "We started to walk out of the parking spot. When we exit, see a huge fancy resturaunt."

    scene bg restaurant
    with Dissolve (1.0)
    play music "crossroads.mp3" fadein 1.0 loop

    w "Good evening. Have you made a reservation?"

    m "Yeah, for two."

    w "Alright, this way please."

    "The worker sets up our tables and we sat on the chairs."

    show mariea normal at left

    show kensukeh normal at right

    m "Thank you!"

    s "Thank you!"

    "Marie looks at the menu while I look at mine."

    m "You already thought of what you want?"

    s "Yep."

    "The waiter comes to us."

    wa "Are you two already to order?"

    m "Yes."

    s "Can I have the rum and coke please?"

    wa "Sure. What about you miss?"

    m "Can I have red wine, please?"

    hide kensukeh normal
    show kensukeh surprised at right

    s "Is that gonna be alright? Y'know because you're the driver?"

    m "One cup isn't going to fuck me up."

    wa "What food you want to order?"

    m "I'd like to have the rockfish and crab? For the sauce, I want Dashi, please."

    wa "Okay. What about you, sir?"

    hide kensukeh surprised
    show kensukeh normal at right

    s "I would like to have Burger and Fries."

    hide mariea normal
    show mariea deadinside at left

    m "You cannot be serious right now."

    hide kensukeh normal
    show kensukeh worried at right

    s "What? Nothing in the menu interest me!"

    m "Did you really look at the menu or did you just quickly glanced through it?"

    "... She's not wrong. I need to think of something, quick."

    s "Uh, can I have the steak, well done, please?"

    wa "Sure thing! Is there anything else?"

    hide mariea deadinside
    show mariea normal at left

    m "No, thank you."

    wa "Ok, then! I'll get your order."

    hide kensukeh surprised
    show kensukeh normal at right

    "The waiter walks away which leaves the both of us here by ourselves."

    menu:
        
        s "How should I start the conversation?"

        "So, what was your errands like?":

            $ mariepoint += 2

            m "Well, It was stuff to prepare for tonight. Shopping for clothes and stuff."

            s "That's cool. It looked like it all payed off."

            hide mariea normal
            show mariea smiling at left

            m "*Giggles* It looks like it did."

            "I start laughing nervously."

            m "So, what did you do all day, Seth?"

            hide kensukeh normal
            show kensukeh surprised at right

            s "Huh?"

            m "I said what did you do all say?"

            "Oh, fuck."

            s "Oh, I was uhhhh doing Boss mods. Y'know the usual."

            hide mariea smiling
            show mariea serious at left

            m "I see."

        "What made you interested in red wine?":

            $ sethpoint += 4

            m "I mainly picked that because it's usually the typical drink you'd have in this type of setting. I think."

            s "That's nice."

            m "Plus, Red Wine doesn't have alot of alcohol in it. In terms of percentage, there's typically 11-14 percent alcohol by volume. Fact."

            s "Hmm, maybe I should get that next time the waiter comes back."

            m "Yeah that's nice but just don't overdue it, okay? I don't want to drag you back to the car. It would make me look suspicious."

            hide kensukeh normal
            show kensukeh smile at right

            s "I'll try not too, hahahaha."

            show mariea serious at left

            m "I'm being serious."

            $ mariepoint += 1

        "So, what's your job like?":

            $ mariepoint -= 1

            show mariea serious at left

            m "..."

            hide kensukeh normal
            show kensukeh worried at right

            s "A bit touchy? I apologize."

    "Our waiter came back with the drinks and food."

    wa "One red wine and Rum and Coke."

    wa "And here's your food."

    show mariea normal at left

    m "Thank you!"

    hide kensukeh
    show kensukeh normal at right

    s "Thank you!"

    "The waiter walks away."

    "I start drinking. It tastes really good. The soda in it kinda tastes like Pepsi. Not my favorite but it's alright."

    "After drinking some of my drink, I pick up the knife and cut my steak and then eat it."

    "When the steak enters my mouth, my eyes widen."

    hide kensukeh normal
    show kensukeh surprised at right

    "The meat is very tender and well seasoned. It tastes very garlic-y."

    hide kensukeh surprised
    show kensukeh normal at right

    "Marie starts holding her glass and glently swirls it."

    "She takes a sip."

    s "How's the wine?"

    m "It tastes very fresh. I like drinking with these glasses. It really makes you look fancy."

    s "Yeah. I don't think having my drink in those glasses would look fancy, hahaha."

    "Marie puts the glass down and starts eating the rockfish. She's smiling while eating it."

    "I mean it's one of her favorite foods she's having so I cannot blame her. I would've done the same thing."

    "Me and Marie ate all of our food."

    "Our waiter comes back with the bill."

    hide kensukeh surprised
    show kensukeh surprised at right

    s "$600 for 5 items?! That's insane!"

    "Marie pulls out her purse."

    menu:
        "Offer to pay.":

            $ sethpoint += 5

            s "Don't worry. I'll pay for my own stuff."

            m "No, it's your birthday. So, don't you worry."

            show mariea smileblush at left

            m "But, thank you for the gesture."

            $ mariepoint += 5
        
        "Don't offer to pay.":

            "I was about to take out the wallet."

            "Then I remembered the last time I checked it. There was nothing in it."

            hide kensukeh surprised
            show kensukeh worried at right

            s "*sigh*"

            m "Something wrong, Seth?"

            s "Uh, nothing."

    "Marie ends up paying the bill and we end up leaving the resturaunt."

    wa "Have a good night you too!"

    stop music fadeout 3.0
    play music "horoscope.mp3" fadein 0.5 loop
    scene bg city
    with Dissolve (1.0)

    "When I walked out the resturaunt, I looked at the bilboards. 12:15 it says. As we walked around the city, I start to notice it's beauty."

    m "Let's go."

    s "So, where we going?"

    m "Somewhere, follow me."

    "Marie grabs on to my hand and I start walking aside with her."

    scene bg city2
    with Dissolve (1.0)

    "After a bit of walking around, I've checked my phone."

    "It's 1:15. We've been strolling around the city for a whole hour."

    s "Hey, Marie?"

    m "Yes, Seth?"

    s "Where are we going? We've been walking around here for a hour now."

    m "We're almost there."

    s "Huh?"

    "After walking a bit further, I'm starting to recognize this area."

    scene bg park
    with Dissolve (1.0)
    stop music fadeout 3.0

    "I-It's the park! The exact one from my dream this morning!!"

    show mariea serious

    "After looking at my surroundings, I look at Marie."

    "She's looking away from me."

    m "*sigh* C'mon Marie! You've practiced this all week!"

    hide mariea serious
    show mariea normal

    m "*Inhales* *Exhales* Alright, it's time."

    "Marie starts sitting on one of the benches. It looks like she's preparing to do something."

    "Is this a dream? This seems too good to be true. This scenario feels like the one in my dream."

    "Marie starts to slightly put her head down."

    play sound "heartbeat.mp3" loop

    "My heart starts beating."

    hide mariea normal
    show mariea serious 

    m "What are you waiting for? Isn't this what you want?"

    s "!"

    "After she said that sentence, I immeditely raised my hand up."

    "My hand reaches to Marie's head."

    "Closer,{p=1}closer,{p=1}and closer"

    stop sound fadeout 1.0

    "The palm of my hand touches Marie's soft dark brown hair. I start to glently rub her head back and forth."

    "I start to form a huge grind on my face."

    s "{size=-10} OMG, I'm finally giving Marie a headpat! Holy shit, I'm actually doing it! {/size}"

    "I've been doing this hand movement for whole 2 minutes."

    play music "itchy.mp3" loop

    m "Aright, bucko! That's enough!"

    s "Huh?! I wasn't done, yet!"

    m "I was fine with you doing it for a whole minute! Two is REALLY pushing it, pal!"

    s "Please! One more minute!"

    "Marie turns her back away from me with her arms crossed."

    m "Absolutely not."

    m "..."

    hide mariea serious
    show mariea normal

    m "Happy Birthday, Seth. I know I always sound like I'm sick of you, but I genuinely enjoy having you around."

    "Marie starts walking towards me."

    "She {p=2} starts rubbing my head."

    s "What are you doing?"

    hide mariea normal
    show mariea smiling

    m "I'm getting payback, you bastard."

    "Wait."

    "This is my time to get more headpats!"

    "I put my head on Marie's head and start rubbing it again."

    "She starts running away."

    m "You already got your headpats!"

    s "I need to get my paybacks as well!"

    m "Go away!"

    "For whole 10-20 minutes, we've been running back and forth around the park rubbing each others heads."

    scene bg black
    with Dissolve (5.0)
    stop music fadeout 1.0

    "Headpat route: End"

    if check:
        jump headpat_end_extra
    else:
        jump before_main_menu

label headpat_end_extra:

    scene bg rooftop
    with Dissolve (1.0)
    play music "suspense.mp3" fadein 1.0 loop

    "A girl in white flies on top of a building."

    show aria normal at the_right

    a "Hey, Midori!"

    show midori normal at the_left

    mi "Hey, Aria-sama. How was the dream?"

    a "It was nothing too serious. He ended up dying in the end of it."

    hide midori normal
    show midori serious at the_left

    mi "What?"

    a "The dream isn't related to Izanami. The dream was really sad and was filled with regret."

    hide midori serious
    show midori relaxed at the_left

    mi "Thank goodness. We now know that he's safe at least."

    a "So, how are we going to provent Izanami from killing either Seth or Marie?"

    hide midori relaxed
    show midori normal at the_left

    mi "I thought of two solutions. One, we find the reason why she wants to kill them and resolve the issue. This is my perferred option."

    a "You always want to solve things peacefully, as usual. I doubt she'll be open to a compromise."

    mi "For option two, we have to kill her."

    a "How are we going to do that?"

    mi "I was thinking about using fire."

    hide aria normal
    show aria worried at the_right

    a "Huh? Why fire?"

    mi "I've done a bit of research online, saying that she was burned to death when she gave birth Kagutsuchi, the fire God. Thus my reasoning for using fire against her. I can use fire when I change forms, so if I get the timing correctly, I can scorch her."

    a "Midori."

    mi "But what type of powers that she uses? What tricks does she have in her sleeve? Is it possible for her to use multiple elements like in Persona 4? Speaking about P4, why isn't she weak to fire in that game? Like the devs should've at least not make the weakness trigger a 1 more, so it can be accurate to the original myth with sacrificing the diff-"

    hide aria worried
    show aria angry at the_right

    a "Midori!"

    hide midori normal
    show midori serious at the_left

    mi "Huh? What's up?"

    hide aria angry
    show aria worried at the_right

    a "I was about to say that the Izanami we have here is from BlazBlue. So that logic doesn't apply here."

    hide midori serious
    show midori understand at the_left

    mi "Welp. I have no clue of what to do."

    mi "But we need to make ensure that everything goes as intended."

    a "Yeah."

    a "..."

    mi "..."

    hide aria worried
    show aria normal at the_right

    a "So, where the hell are we going to sleep?"

    hide midori understand
    show midori sad at the_left

    stop music

    mi "Oh, fuck."

    play music "hooky.mp3" loop

    hide aria normal
    show aria serious at the_right

    a "You've got to be kidding me."

    mi "I haven't really thought this far ahead."

    a "We cannot just sleep on concrete floors all night!"

    mi "That's true, that's true. Let's look for a hotel around the area or something."

    a "Do you have the money for that?"

    hide midori sad
    show midori smile at the_left

    mi "Probably."

    a "Midori!"

    mi "Relax, relax. I'm just trolling. Haha"

    scene bg black
    with Dissolve (3.0)

    "The End"
    $persistent.headpat = True

    jump kiss_route_start