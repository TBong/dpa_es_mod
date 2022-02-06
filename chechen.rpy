#Базовые переменные
init -100 python:
    to_steam = False
    if to_steam == True:
        default_dpa_path = ""
    else:
        default_dpa_path = "mods/dpa_es_mod/"

    #Поинты
    gen_fp = 0
    humanity = 0
    dysmoral = 0

    #Прочее 
    ch_memories = "default"

#Базовые функции
init -99 python:
    def getFile(file):
        return default_dpa_path + file

    def getLabelWIP(name):
        if to_steam == True:
            return "th_demo_wip"
        return name
    
    def canEventPlay(probability):
        rolled = renpy.random.randint(1, 100)
        return rolled <= probability

    def getRandomItem(image):
        pick_weight = renpy.random.randint(0, len(image)-1)
        return image[pick_weight]
    
    def bakeSpriteDefaultSizeSold(sizeX, sizeY, posX, posY, character, emo, special="null.png"):
        return ConditionSwitch(
        "persistent.sprite_time=='day'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.83, 0.88, 0.92)),
        "persistent.sprite_time=='sunset'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.63, 0.78, 0.82)))

    def bakeSpriteDefaultPlusSizeSold(sizeX, sizeY, posX, posY, character, emo, special="null.png"):
        return ConditionSwitch(
        "persistent.sprite_time=='day'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_ps_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_ps_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_ps_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt_ps.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.83, 0.88, 0.92)),
        "persistent.sprite_time=='sunset'",
        im.MatrixColor(  
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_ps_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_ps_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_ps_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt_ps.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",
        im.MatrixColor(  
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_ps_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_ps_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_ps_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt_ps.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.63, 0.78, 0.82)))


#Стили
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

#Переменные от функция
init -97 python:
    #Шрифты
    brokenFont = getFile("old-fax.ttf")
    furore = getFile("Furore.ttf")

init:
    if to_steam == False:
        define config.developer = True

    $ mods["dpa_start"]=u"{font=[furore]}Добро пожаловать в {color=#911010}ад"
    #
    $ elt = Character (u'Борис Николаевич', color="949494", what_color="fff")
    $ kp = Character (u'Командир полка', color="4f4031", what_color="fff")
    $ ofic = Character (u'Офицер', color="e3b212", what_color="fff")
    $ pil = Character (u'Вертолётчик', color="8599ff", what_color="fff")
    $ sol = Character (u'Солдат', color="23ad00", what_color="fff")
    #
    $ sol_gen = Character(u"Солдат",color="288110",what_color="fff")
    $ gen = Character(u"Генадий",color="288110",what_color="fff")
    $ sol_rs = Character(u"Солдат",color="da9979",what_color="fff")
    $ rs = Character(u"Бритый",color="da9979",what_color="fff")
    #
    $ gg = Character (u'Саша',color="ddde4e",what_color="fff")
    $ ggnvl = Character (u'Саша',color="ddde4e", kind=nvl)

    $ fon1 = getFile("music/fon1.mp3")
    $ shturm = getFile("music/shturm.mp3")
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
    $ menu_music = getFile(getRandomItem(["music/song1.mp3","music/song2.mp3","music/song_menu.mp3"]))
    
    image menu_back = getFile(getRandomItem(["gui/load/load_menu.jpg","menu/fon.png"]))
    image gazeta1 = getFile("image/cg/gazeta1_draw.jpg")
    image futbol1_cg = getFile("image/cg/futbol1.jpg")
    image grib_cg = getFile("image/cg/grib_draw.jpg")
    image forest_cg = getFile("image/cg/forest_draw.jpg")
    image stadion_cg = getFile("image/cg/stadion_draw.jpg")
    image mi8_in2 = getFile("image/cg/mi8_in2_draw.jpg")
    image mi8 = getFile("image/cg/mi8_draw.jpg")
    image combat_map = getFile("menu/combat_map/test_map.png")
    image gruz200 = getFile("image/cg/gruz200_draw.jpg")
    image eltsin1 = getFile("image/cg/eltsin1_draw.jpg")
    image airport = getFile("image/cg/airport_draw.jpg")
    image airport1 = getFile("image/cg/airport2_draw.jpg")
    image train = getFile("image/cg/train.png")
    image train_open = getFile("image/cg/train_open.png")

    image train_inside_pic = getFile("image/bg/int_train.jpg")
    image cabina = getFile("image/bg/cabina_draw.jpg")
    image angar = getFile("image/bg/angar_draw.jpg")
    image goriScetch = getFile("image/bg/goriScetch.jpg")
    image mi8_in1 = getFile("image/bg/mi8_in1_draw.jpg")
    image palatka = getFile("image/bg/palatka_draw.jpg")

    image random_alert = getFile("menu/random_alert.png")

    image childhood_memories = ConditionSwitch(
        "ch_memories=='grib'", "grib_cg",
        "ch_memories=='futbol1'", "futbol1_cg",
        "ch_memories=='forest'", "forest_cg",
        "ch_memories=='stadion'","stadion_cg",
        True, "angar"
    )

    image gen normal smile = bakeSpriteDefaultPlusSizeSold(900,1080,0,0,"gen/core_v2.png","gen/emo/gen_ord_smile.png")
    image gen mournful = bakeSpriteDefaultPlusSizeSold(900,1080,0,0,"gen/core_v2.png","gen/emo/gen_mournful.png")
    image gen laught = bakeSpriteDefaultPlusSizeSold(900,1080,0,0,"gen/core_v2.png","gen/emo/gen_laught.png")

    image rs furious = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_furious.png")
    image rs furious blik = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_furious.png", "romper_stomper/emo/rs_blik.png")
    image rs normal = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_standart.png")
    image rs normal blik = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_standart.png", "romper_stomper/emo/rs_blik.png")

    screen example_main_menu:
        tag menu
        modal True
        add getFile("menu/fon_text.png")
        imagebutton:
            auto  getFile("menu/nachat_2_%s.png")
            xpos 55
            ypos 200
            action (Hide("example_main_menu", transition=dissolve)), (Call("prolog"))
        imagebutton:
            auto getFile("menu/load_2_%s.png")
            xpos 55
            ypos 400
            action ShowMenu('dpa_Load')
        imagebutton:
            auto getFile("menu/gallery_2_%s.png")
            xpos 55
            ypos 600
            action ShowMenu('wip')
        imagebutton:
            auto  getFile("menu/exit_2_%s.png")
            xpos 55
            ypos 800
            action Return()
        text "{font=[furore]}Добро пожаловать в":
            xpos 1000
            ypos 33
            size 58
        text "{font=[furore]}{color=#911010}АД":
            xpos 1350
            ypos 80
            size 70
    
    screen combat_map:
        imagemap:
            ground getFile("menu/combat_map/test_map.png")
            auto getFile("menu/combat_map/test_map_%s.png")
            hotspot (657,482,35,35) action Jump(getLabelWIP("bamut")) alt Jump("prolog") hover_sound pencil #Бамут
            hotspot (772,474,40,47) action Jump(getLabelWIP("u_m")) alt Jump("prolog") hover_sound pencil #Урус-Мартан
            hotspot (901,397,50,45) action Jump(getLabelWIP("argun")) alt Jump("prolog") hover_sound pencil #Аргун
            hotspot (986,377,50,42) action Jump("gudermes") alt Jump("prolog") hover_sound pencil #Гудермес

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
            xpos 210
            ypos 410
            size 60
        text "{font=[furore]}Перед тем как они *возможно* произойдут вас оповестит рация.":
            xpos 101
            ypos 540
            size 60
    
    screen disclaimer3:
        key "dismiss" action [ Hide("disclaimer3", transition=dissolve), Pause(0.5), Return() ]
        timer 5.0 action [ Hide("disclaimer3", transition=dissolve), Pause(0.5), Return() ]
        text "{font=[furore]}Приятного прочтения.":
            xpos 410
            ypos 500
            size 80

    screen th_for_read:
        key "dismiss" action [ Hide("disclaimer3", transition=dissolve), Pause(0.5), Return() ]
        timer 5.0 action [ Hide("disclaimer3", transition=dissolve), Pause(0.5), Return() ]
        text "{font=[furore]}Благодарим за прочтение мода.":
            xpos 160
            ypos 500
            size 80

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

    transform ra_disclaimer:
        zoom 0.9 pos (545, 0)
        pause (2)
        linear 1.5 zoom 0.1 pos (-18, 7)
    
    transform random_alert_transform:
        zoom 0.1 pos (-18, 7)

label dpa_start:
    call disclaimer
    play music menu_music fadein 2
    $ new_chapter(0, u"Меню DPA")
    $ renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("dpa_say_gui",None)]
    $ persistent.sprite_time = "day"
    call dpa_menu
    return

label dpa_menu:
    scene menu_back with dissolve2
    call screen example_main_menu with dissolve
    return

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
    return
        
label random_alert_call:
    show random_alert at random_alert_transform
    return

label dpa_combat_map:
    show combat_map with dissolve
    call screen combat_map 
    return

label th_demo_wip:
    scene black with dissolve2
    stop sound
    call screen th_for_read with dissolve
    jump dpa_menu
    return