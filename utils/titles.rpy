#Титры
screen th_for_read:
    key "dismiss" action [ Hide("th_for_read", transition=dissolve), Pause(0.5), Return() ]
    timer 5.0 action [ Hide("th_for_read", transition=dissolve), Pause(0.5), Return() ]
    text "{font=[furore]}Благодарим за прочтение мода.":
        xalign 0.5
        ypos 500
        size 80

label th_demo_wip:
    scene black with dissolve2
    stop sound
    stop music fadeout 4
    call screen th_for_read with dissolve
    jump dpa_menu
    return