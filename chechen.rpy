init -100 python:
    to_steam = False
    if to_steam == True:
        default_dpa_path = ""
    else:
        default_dpa_path = "mods/DPA/"

init -99 python:
    def getFile(file):
        return default_dpa_path + file

init:
    $ mods["dpa_menu"]=u"Добро пожаловать в ад"
    $ elt = Character (u'Борис Николаевич', color="949494", what_color="fff")
    $ sol = Character (u'Солдат', color="23ad00", what_color="fff")
    $ fon1 = "music/fon1.mp3"
    $ mi8 = "music/mi8.mp3"
    $ uaz = "music/uaz.mp3"
    $ song1 = "music/song1.mp3"
    $ song2 = "music/song2.mp3"
    $ an12 = "music/an12.mp3"
    $ veter = "music/veter.mp3"
    
    image gazeta1 = getFile("bg/gazeta1.jpg")
    image 200 = "bg/200.jpg"
    image eltsin1 = "bg/eltsin1.jpg"
    image airport = "bg/airport.jpg"
    image airport1 = "bg/airport1.jpg"
    image airport2 = "bg/airport2.jpg"
    image cabina = "bg/cabina.jpg"
    image angar = "bg/angar.jpg"

    screen example_main_menu:
        tag menu
        modal True
        add "menu/fon.png"
        imagebutton:
            auto  "menu/nachat_%s.png"
            xpos 55
            ypos 200
            action Jump("prolog")
            
        imagebutton:
            auto  "menu/exit_%s.png"
            xpos 55
            ypos 602
            action Jump("dpa_exit")

label dpa_menu:
    call screen example_main_menu
    return
    
label dpa_exit:
    return
