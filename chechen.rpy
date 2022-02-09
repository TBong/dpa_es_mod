#Базовые переменные
init -100 python:

    if to_steam:
        default_dpa_path = ""
    else:
        default_dpa_path = "mods/dpa_es_mod/"
        




init:
    define config.developer = True
    $ saveOldVisual()

    $ mods["dpa_start"]=u"{font=[furore]}Добро пожаловать в {color=#911010}ад"

    #Главный герой
    $ gg = Character (u'Саша',color="ddde4e",what_color="fff")
    $ ggnvl = Character (u'Саша',color="ddde4e", kind=nvl)

    #Перостепенные герои
    $ sol_gen = Character(u"Солдат",color="288110",what_color="fff")
    $ gen = Character(u"Генадий",color="288110",what_color="fff")
    $ sol_rs = Character(u"Солдат",color="da9979",what_color="fff")
    $ rs = Character(u"Бритый",color="da9979",what_color="fff")

    #Редкий юз
    $ elt = Character (u'Борис Николаевич', color="949494", what_color="fff")
    $ kp = Character (u'Командир полка', color="4f4031", what_color="fff")
    $ ofic = Character (u'Офицер', color="e3b212", what_color="fff")
    $ pil = Character (u'Вертолётчик', color="8599ff", what_color="fff")
    $ sol = Character (u'Солдат', color="23ad00", what_color="fff")

    #Музыка
    $ fon1 = getFile("sound/song/fon1.mp3")
    $ shturm = getFile("sound/song/shturm.mp3")
    $ song1 = getFile("sound/song/song1.mp3")
    $ song_ep = getFile("sound/song/song_ep.mp3")
    $ song_menu = getFile("sound/song/song_menu.mp3")
    $ song2 = getFile("sound/song/song2.mp3")
    $ song_liric = getFile("sound/song/song_liric.mp3")
    $ song_liric2 = getFile("sound/song/song_liric2.mp3")
    $ song_gruz200 = getFile("sound/song/song_gruz200.mp3")
    $ song_na_mozdok = getFile("sound/song/song_na_mozdok.mp3") 
    $ song_rising_sun = getFile("sound/song/song_rising_sun.mp3")
    $ kombat = getFile("sound/song/kombat.mp3")

    $ menu_music = getFile("sound/song/"+getRandomItem(["song1","song2","song_menu","kombat","shturm"])+".mp3")

    #Звуки окружения
    $ mi8 = getFile("sound/ambinet/mi8.mp3")
    $ mi8_1 = getFile("sound/ambinet/mi8_1.mp3")
    $ uaz = getFile("sound/ambinet/uaz.mp3")
    $ an12 = getFile("sound/ambinet/an12.mp3")
    $ train_inside_music = getFile("sound/ambinet/train_inside.mp3")
    $ veter = getFile("sound/ambinet/veter.mp3")

    #Звуковые эфекты
    $ hit = getFile("sound/sfx/hit.mp3")
    $ pencil = getFile("sound/sfx/pencil-scratches.mp3")
    $ hitting_iron = getFile("sound/sfx/hitting_iron.mp3")
    $ ra_sound = getFile("sound/sfx/ra_sound.mp3")

    #Пикчи позже будет норм сорт 
    image gazeta1 = getFile("image/cg/gazeta1_draw.jpg")
    image futbol1_cg = getFile("image/cg/futbol1.jpg")
    image grib_cg = getFile("image/cg/grib_draw.jpg")
    image forest_cg = getFile("image/cg/forest_draw.jpg")
    image stadion_cg = getFile("image/cg/stadion_draw.jpg")
    image eltsin1 = getFile("image/cg/eltsin1_draw.jpg")
    image gruz200 = getFile("image/cg/gruz200_draw.jpg")

    image mi8_in2 = getFile("image/cg/mi8_in2_draw.jpg")
    image mi8 = getFile("image/cg/mi8_draw.jpg")
    image combat_map = getFile("image/screens//image_maps/combat_map/test_map.png")
    image airport = getFile("image/cg/airport_draw.jpg")
    image airport1 = getFile("image/cg/airport2_draw.jpg")
    image train = getFile("image/cg/train.png")
    image train_open = getFile("image/cg/train_open.png")

    image train_inside_pic = getFile("image/bg/int_train.jpg")
    image cabina = getFile("image/bg/cabina_draw.jpg")
    image angar = getFile("image/bg/angar_draw.jpg")
    image goriScetch = getFile("image/bg/goriScetch.jpg")
    image mi8_in1 = getFile("image/bg/mi8_in1_draw.jpg")
    image mi8_crash = getFile("image/bg/mi8_crash.jpg")
    image palatka = getFile("image/bg/palatka_draw.jpg")

    #Меню и иные приколы
    image menu_back = getFile(getRandomItem(["image/cg/menu_fon1.jpg","image/cg/menu_fon2.png"]))

    image random_alert:
        getFile("image/screens/ra_anim/random_alert0.png")
        0.3
        getFile("image/screens/ra_anim/random_alert1.png")
        0.3
        getFile("image/screens/ra_anim/random_alert2.png")
        0.3
        getFile("image/screens/ra_anim/random_alert3.png")
        0.3
        getFile("image/screens/ra_anim/random_alert4.png")
        0.3
        repeat

    image qte_anim_button:
        getFile("image/screens/qte/press_button1.png")
        0.1
        getFile("image/screens/qte/press_button2.png")
        0.1
        getFile("image/screens/qte/press_button3.png")
        0.1
        repeat

    image childhood_memories = ConditionSwitch(
        "ch_memories=='grib'", "grib_cg",
        "ch_memories=='futbol1'", "futbol1_cg",
        "ch_memories=='forest'", "forest_cg",
        "ch_memories=='stadion'","stadion_cg",
        True, "angar"
    )

    #Спрайт. Билдер выше
    image gen normal smile = bakeSpriteDefaultPlusSizeSold(900,1080,0,0,"gen/core_v2.png","gen/emo/gen_ord_smile.png")
    image gen mournful = bakeSpriteDefaultPlusSizeSold(900,1080,0,0,"gen/core_v2.png","gen/emo/gen_mournful.png")
    image gen laught = bakeSpriteDefaultPlusSizeSold(900,1080,0,0,"gen/core_v2.png","gen/emo/gen_laught.png")

    image rs furious = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_furious.png")
    image rs furious blik = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_furious.png", "romper_stomper/emo/rs_blik.png")
    image rs normal = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_standart.png")
    image rs normal blik = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_standart.png", "romper_stomper/emo/rs_blik.png")
    
label dpa_start:
    $ updVisual()
    call disclaimer
    call dpa_menu
    return

label dpa_menu:
    play music menu_music fadein 2
    $ new_chapter(0, u"Меню DPA")
    call initVars
    $ renpy.fix_rollback()
    scene menu_back with dissolve2
    call screen dpa_main_menu with dissolve
    return


