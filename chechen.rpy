init -100 python:
    to_steam = False
    if to_steam == True:
        default_dpa_path = ""
    else:
        default_dpa_path = "mods/dpa_es_mod/"
    
    ch_memories = "default"



init -99 python:
    def getFile(file):
        return default_dpa_path + file

    def getLabelWIP(name):
        if to_steam == True:
            return "th_demo_wip"
        return name
    
    def canEventPlay(probability):
        rolled = renpy.random.randint(1, 100)
        return rolled == probability

    def getRandomPick(image):
        pick_weight = renpy.random.randint(0, len(image)-1)
        return image[pick_weight]

    brokenFont = getFile("old-fax.ttf")

    def bakeSprite(sizeX, sizeY, posX, posY, clothes, character, emo, other1, other2):
        return ConditionSwitch(
        "persistent.sprite_time=='day'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/"+clothes),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/"+other1),
            (posX,posY), getFile("image/sprites/"+other2)),
            im.matrix.tint(0.83, 0.88, 0.92)),
        "persistent.sprite_time=='sunset'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/"+clothes),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/"+emo), 
            (posX,posY), getFile("image/sprites/"+other1),
            (posX,posY), getFile("image/sprites/"+other2)),
            im.matrix.tint(0.83, 0.88, 0.92)),
        "persistent.sprite_time=='night'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/"+clothes),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/"+emo), 
            (posX,posY), getFile("image/sprites/"+other1),
            (posX,posY), getFile("image/sprites/"+other2)),
            im.matrix.tint(0.83, 0.88, 0.92)))


#styles
init -98 python:
    style.text_save_load                          = Style(style.default)
    style.text_save_load.font                     = getFile("Furore.ttf")
    style.text_save_load.size                     = 60
    style.text_save_load.color                    = "#ffffff"
    style.text_save_load.hover_color              = "#808080"
    style.text_save_load.selected_color           = "#ffffff"
    style.text_save_load.selected_idle_color      = "#ffffff"
    style.text_save_load.selected_hover_color     = "#808080"
    style.text_save_load.insensitive_color        = "#ffffff"

    style.button_none = Style(style.button)
    style.button_none.background = None
    style.button_none.hover_background = None
    style.button_none.selected_background = None
    style.button_none.selected_hover_background = None
    style.button_none.selected_idle_background = None

    style.file_load_button = Style(style.button)
    style.file_load_button.background = getFile("gui/load/load_Button_idle.png")
    style.file_load_button.hover_background = getFile("gui/load/load_Button_hover.png")
    style.file_load_button.selected_background = getFile("gui/load/load_Button_selected.png")
    style.file_load_button.selected_hover_background = getFile("gui/load/load_Button_selected.png")
    style.file_load_button.selected_idle_background = getFile("gui/load/load_Button_selected.png")


# $ randImg = getRandomPick(["mi8_in1","gazeta1"])
# $ renpy.show(randImg)
# $ renpy.hide(randImg) 


# Идеи для названия: 
#     "Первая, но не последняя"
#     ""
#     ""

init:
    $ mods["dpa_menu"]=u"Добро пожаловать в ад"
    #
    $ elt = Character (u'Борис Николаевич', color="949494", what_color="fff")
    $ kp = Character (u'Командир полка', color="4f4031", what_color="fff")
    $ ofic = Character (u'Офицер', color="e3b212", what_color="fff")
    $ pil = Character (u'Вертолётчик', color="8599ff", what_color="fff")
    $ sol = Character (u'Солдат', color="23ad00", what_color="fff")
    #
    $ sol_gen = Character(u"Солдат",color="288110",what_color="fff")
    $ gen = Character(u"Генадий",color="288110",what_color="fff")
    #
    $ gg = Character (u'Саша',color="ddde4e",what_color="fff")
    $ ggnvl = Character (u'Саша',color="ddde4e", kind=nvl)

    $ fon1 = getFile("music/fon1.mp3")
    $ mi8 = getFile("music/mi8.mp3")
    $ hit = getFile("music/hit.mp3")
    $ mi8_1 = getFile("music/mi8_1.mp3")
    $ uaz = getFile("music/uaz.mp3")
    $ song1 = getFile("music/song1.mp3")
    $ song_ep = getFile("music/song_ep.mp3")
    $ song_menu = getFile("music/song_menu.mp3")
    $ song2 = getFile("music/song2.mp3")
    $ song_liric = getFile("music/song_liric.mp3")
    $ song_liric2 = getFile("music/song_liric2.mp3")
    $ song_gruz200 = getFile("music/song_gruz200.mp3")
    $ song_na_mozdok = getFile("music/song_na_mozdok.mp3")
    $ an12 = getFile("music/an12.mp3")
    $ veter = getFile("music/veter.mp3")
    $ song_rising_sun = getFile("music/song_rising_sun.mp3")
    $ pencil = getFile("music/pencil-scratches.mp3")
    $ hitting_iron = getFile("music/hitting_iron.mp3")
    $ train_inside_music = getFile("music/train_inside.mp3")
    
    image gazeta1 = getFile("image/cg/gazeta1.jpg")
    image futbol1_cg = getFile("image/cg/futbol1.jpg")
    image grib_cg = getFile("image/cg/grib.jpg")
    image forest_cg = getFile("image/cg/forest.jpg")
    image stadion_cg = getFile("image/cg/stadion.jpg")
    image mi8_in2 = getFile("image/cg/mi8_in2.jpg")
    image mi8 = getFile("image/cg/mi8.jpg")
    image combat_map = getFile("menu/combat_map/test_map.png")
    image gruz200 = getFile("image/cg/gruz200.jpg")
    image eltsin1 = getFile("image/cg/eltsin1.jpg")
    image airport = getFile("image/cg/airport.jpg")
    image airport1 = getFile("image/cg/airport1.jpg")
    image train = getFile("image/cg/train.png")
    image train_open = getFile("image/cg/train_open.png")

    image train_inside_pic = getFile("image/bg/int_train.jpg")
    image cabina = getFile("image/bg/cabina.jpg")
    image angar = getFile("image/bg/angar.jpg")
    image goriScetch = getFile("image/bg/goriScetch.jpg")
    image mi8_in1 = getFile("image/bg/mi8_in1.jpg")
    image palatka = getFile("image/bg/palatka.jpg")

    
    image childhood_memories = ConditionSwitch(
        "ch_memories=='grib'", "grib_cg",
        "ch_memories=='futbol1'", "futbol1_cg",
        "ch_memories=='forest'", "forest_cg",
        "ch_memories=='stadion'","stadion_cg",
        True, "angar"
    )

    image gen ordin_smile = bakeSprite(900,1080,0,0,"form_w_plus_a_pos0.png","gen/core_v2.png","gen/emo/gen_ord_smile.png", "belt_w_plus_a.png", "null.png")
    image gen mournful = bakeSprite(900,1080,0,0,"form_w_plus_a_pos0.png","gen/core_v2.png","gen/emo/gen_mournful.png", "belt_w_plus_a.png", "null.png")


    screen example_main_menu:
        tag menu
        modal True
        add getFile(getRandomPick(["gui/load/load_menu.jpg","menu/fon.png"]))

        imagebutton:
            auto  getFile("menu/nachat_2_%s.png")
            xpos 55
            ypos 200
            action Jump("prolog")
        imagebutton:
            auto getFile("menu/load_2_%s.png")
            xpos 55
            ypos 400
            action ShowMenu('dpa_Load')
        imagebutton:
            auto getFile("menu/gallery_2_%s_wip.png")
            xpos 55
            ypos 600
            action Jump("wip_label")
        imagebutton:
            auto  getFile("menu/exit_2_%s.png")
            xpos 55
            ypos 800
            action Jump("dpa_exit")
    
    screen combat_map:
        imagemap:
            ground getFile("menu/combat_map/test_map.png")
            auto getFile("menu/combat_map/test_map_%s.png")
            hotspot (657,482,35,35) action Jump(getLabelWIP("bamut")) alt Jump("prolog") hover_sound pencil #Бамут
            hotspot (772,474,40,47) action Jump(getLabelWIP("u_m")) alt Jump("prolog") hover_sound pencil #Урус-Мартан
            hotspot (901,397,50,45) action Jump(getLabelWIP("argun")) alt Jump("prolog") hover_sound pencil #Аргун
            hotspot (986,377,50,42) action Jump("gudermes") alt Jump("prolog") hover_sound pencil #Гудермес

    #эффекты
    transform fall:
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.1 pos (-50, 50)
        linear 0.1 pos (50, -50)
        linear 0.1 pos (50, 50)
        linear 0.1 pos (-50, -50)
        repeat

    transform zoom_to(time=1, an_x=0.5, an_y=0.5, zoom_value=2):
        linear time zoom zoom_value anchor(an_x,an_y)

    transform leap(dyz=0.01, dxz=0.005, dt=.4):
        yzoom 1.0
        easein dt*0.25 yzoom 1.0+dyz xzoom 1.0-dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0
        easein dt*0.25 yzoom 1.0-dyz xzoom 1.0+dxz
        easeout dt*0.25 yzoom 1.0 xzoom 1.0




label dpa_menu:
    play music song_menu
    $ new_chapter(0, u"Меню DPA")
    $ renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("dpa_say_gui",None)]
    $ persistent.sprite_time = "day"
    call screen example_main_menu
    return
    
label dpa_exit:
    return

label dpa_combat_map:
    show combat_map with dissolve
    call screen combat_map 
    return

label wip_label:
    "Данный функционал находится в разработке."
    jump dpa_menu
    return

label th_demo_wip:
    scene black with dissolve2
    stop sound
    "Благодарим за уделенное время. Это пока что только начало, мод находится в активной стадии разработки."
    return