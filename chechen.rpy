init -100 python:
    to_steam = False
    if to_steam == True:
        default_dpa_path = ""
    else:
        default_dpa_path = "mods/dpa_es_mod/"

init -99 python:
    def getFile(file):
        return default_dpa_path + file

init:
    $ mods["dpa_menu"]=u"Добро пожаловать в ад"
    $ elt = Character (u'Борис Николаевич', color="949494", what_color="fff")
    $ sol = Character (u'Солдат', color="23ad00", what_color="fff")
    $ fon1 = getFile("music/fon1.mp3")
    $ mi8 = getFile("music/mi8.mp3")
    $ uaz = getFile("music/uaz.mp3")
    $ song1 = getFile("music/song1.mp3")
    $ song2 = getFile("music/song2.mp3")
    $ an12 = getFile("music/an12.mp3")
    $ veter = getFile("music/veter.mp3")
    
    image gazeta1 = getFile("bg/gazeta1.jpg")
    image gruz200 = getFile("bg/gruz200.jpg")
    image eltsin1 = getFile("bg/eltsin1.jpg")
    image airport = getFile("bg/airport.jpg")
    image airport1 = getFile("bg/airport1.jpg")
    image airport2 = getFile("bg/airport2.jpg")
    image cabina = getFile("bg/cabina.jpg")
    image angar = getFile("bg/angar.jpg")
    image test_map = getFile("menu/combat_map/test_map.png")

    screen example_main_menu:
        tag menu
        modal True
        add getFile("menu/fon.png")
        imagebutton:
            auto  getFile("menu/nachat_%s.png")
            xpos 55
            ypos 200
            action Jump("prolog")
            
        imagebutton:
            auto  getFile("menu/exit_%s.png")
            xpos 55
            ypos 602
            action Jump("dpa_exit")
        
    

label dpa_menu:
    call screen example_main_menu
    return
    
label dpa_exit:
    return
