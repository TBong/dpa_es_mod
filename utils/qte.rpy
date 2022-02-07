#qte
screen qte_start(pressed_key, time):
    add "qte_anim_button" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("qte_start"), Return() ] 
    text "{font=[furore]}[pressed_key]" xalign 0.5 yalign 0.5 size 380 color "#c51d1d"
    text "{font=[furore]}Жми [pressed_key] что бы вернуться!" align(0.5, 0.85) size 60
    timer time action [ Hide("qte_start"), SetVariable("qte_loose", True), Return() ]

transform ra_disclaimer:
    zoom 0.9 pos (545, 0)
    pause (2)
    linear 1.5 zoom 0.1 pos (0, 7)

transform random_alert_transform:
    zoom 0.1 pos (0, 7)

label qte_label(count=1, time=2):
    $ qte_count = count
    while qte_count > 0:
        if qte_loose:
            pass
        else:
            call screen qte_start(getRandomButton(),time)
        $ qte_count -= 1
    return
        
label random_alert_call:
    show random_alert at random_alert_transform
    play sound ra_sound
    return