#Дисклеймер
screen disclaimer1:
    key "dismiss" action [ Hide("disclaimer1", transition=dissolve), Pause(1), Return() ]
    text "{font=[furore]}Данная модификация вдохновлена событиями\nПервой Чеченской войны.":
        xpos 101
        ypos 400
        size 60
    text "{font=[furore]}Все совпадения с реальными персонажами\nи событиями являются случайными.":
        xpos 101
        ypos 560
        size 60

screen disclaimer2:
    key "dismiss" action [ Hide("disclaimer2", transition=dissolve), Pause(1), Return() ]
    text "{font=[furore]}В моде имеються случайные события.":
        xalign 0.5
        ypos 420
        size 60
    text "{font=[furore]}Перед тем как они *возможно* произойдут вас оповестит рация.":
        xalign 0.5
        ypos 520
        size 60

screen disclaimer3:
    key "dismiss" action [ Hide("disclaimer3", transition=dissolve), Pause(1), Return() ]
    text "{font=[furore]}В моде имееться QTE.":
        xalign 0.5
        ypos 360
        size 60
    text "{font=[furore]}Что бы все работало правильно, включите англискую раскладку и выключите Caps Lock.":
        xalign 0.5
        ypos 460
        size 60
    text "{font=[furore]}Сейчас будет пример QTE.":
        xalign 0.5
        ypos 640
        size 60

screen disclaimer4:
    key "dismiss" action [ Hide("disclaimer4", transition=dissolve), Pause(0.5), Return() ]
    timer 5.0 action [ Hide("disclaimer4", transition=dissolve), Pause(0.5), Return() ]
    text "{font=[furore]}Приятного прочтения.":
        xalign 0.5
        ypos 500
        size 80

label disclaimer:
    scene black
    call screen disclaimer1 with dissolve
    pause(1)
    show random_alert at ra_disclaimer with dissolve2
    pause (1.4)
    call random_alert_call
    pause (0.1)
    call screen disclaimer2 with dissolve
    pause(1)
    hide random_alert 
    call screen disclaimer3 with dissolve
    pause(1)
    call qte_label(1,5)
    pause(1)
    call screen disclaimer4 with dissolve
    pause(1)
    return