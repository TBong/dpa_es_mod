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
    $ kp = Character (u'Командир полка', color="4f4031", what_color="fff")
    $ fon1 = getFile("music/fon1.mp3")
    $ mi8 = getFile("music/mi8.mp3")
    $ uaz = getFile("music/uaz.mp3")
    $ song1 = getFile("music/song1.mp3")
    $ song_menu = getFile("music/song_menu.mp3")
    $ song2 = getFile("music/song2.mp3")
    $ an12 = getFile("music/an12.mp3")
    $ veter = getFile("music/veter.mp3")
    
    image gazeta1 = getFile("bg/gazeta1.jpg")
    image combat_map = getFile("menu/combat_map/test_map.png")
    image gruz200 = getFile("bg/gruz200.jpg")
    image eltsin1 = getFile("bg/eltsin1.jpg")
    image palatka = getFile("bg/palatka.jpg")
    image airport = getFile("bg/airport.jpg")
    image airport1 = getFile("bg/airport1.jpg")
    image cabina = getFile("bg/cabina.jpg")
    image angar = getFile("bg/angar.jpg")

    screen example_main_menu:
        tag menu
        modal True
        add getFile("menu/fon.png")
        imagebutton:
            auto  getFile("menu/nachat_2_%s.png")
            xpos 55
            ypos 200
            action Jump("prolog")
        imagebutton:
            auto getFile("menu/load_2_%s.png")
            xpos 55
            ypos 400
            action Jump("dpa_Load")
        imagebutton:
            auto getFile("menu/gallery_2_%s_wip.png")
            xpos 55
            ypos 600
            action Jump("prolog")
        imagebutton:
            auto  getFile("menu/exit_2_%s.png")
            xpos 55
            ypos 800
            action Jump("dpa_exit")
    
    screen combat_map:
        imagemap:
            ground getFile("menu/combat_map/test_map.png")
            auto getFile("menu/combat_map/test_map_%s.png")
            hotspot (657,482,35,35) action Jump("bamut") alt Jump("prolog") #Бамут
            hotspot (772,474,40,47) action Jump("u_m") alt Jump("prolog") #Урус-Мартан
            hotspot (901,397,50,45) action Jump("argun") alt Jump("prolog") #Аргун
            hotspot (986,377,50,42) action Jump("gudermes") alt Jump("prolog") #Гудермес

label dpa_menu:
    play music song_menu
    call screen example_main_menu
    return
    
label dpa_exit:
    return

label dpa_combat_map:
    show combat_map with dissolve
    call screen combat_map 
    return
    
label dpa_Load:
    call screen dpa_Load
    return