#Базовые переменные
init -100 python:

    if to_steam:
        default_dpa_path = ""
    else:
        default_dpa_path = "mods/dpa_es_mod/"
        
init 999:
    define config.developer = True

init:
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
    $ rac = Character (u'Рация', color="696969", what_color="fff")
    $ om = Character (u'Старик', color="a16868", what_color="fff")

    #Музыка
    $ grob_song1 = regMusic("grob_song1","Гражданская оборона - Моя оборона(минус)","sound/song/song_grob.mp3")
    $ fon1 = regMusic("fon1","NN","sound/song/fon1.mp3")
    $ song_crash= regMusic("song_crash","Свидетельство о смерти - чуть-чуть меня ","sound/song/song_а_little_bit_of_me.mp3")
    $ shturm = regMusic("shturm","Сергей Тимошенко - Штурм","sound/song/shturm.mp3")
    $ song1 = regMusic("song1","В военкомате случай был","sound/song/song1.mp3")
    $ song_ep = regMusic("song_ep","NN","sound/song/song_ep.mp3")
    $ song_menu = regMusic("song_menu","Эрик Осташев - Солдат фортуны","sound/song/song_menu.mp3")
    $ song2 = regMusic("song2","Здравствуй мама","sound/song/song2.mp3")
    $ song_liric = regMusic("song_liric","NN","sound/song/song_liric.mp3")
    $ song_gruz200 = regMusic("song_gruz200","Груз-200","sound/song/song_gruz200.mp3")
    $ song_na_mozdok = regMusic("song_na_mazdok","На Моздок","sound/song/song_na_mozdok.mp3") 
    $ song_rising_sun = regMusic("song_rising_sun","The Animals - House of the Rising Sun","sound/song/song_rising_sun.mp3")
    $ kombat = regMusic("kombat","Любэ - Комбат","sound/song/kombat.mp3")
    $ song_muts = regMusic("song_muts","Тимур Муцураев - Если духом ты слаб","sound/song/song_muts.mp3")

    $ menu_music = getMusic(getRandomItem(["song1","song2","song_menu","kombat","shturm","grob_song1"]))

    #Звуки окружения
    $ mi8_lopasti = getFile("sound/ambinet/mi8_lopasti.mp3")
    $ mi8 = getFile("sound/ambinet/mi8.mp3")
    $ mi8_1 = getFile("sound/ambinet/mi8_1.mp3")
    $ uaz = getFile("sound/ambinet/uaz.mp3")
    $ an12 = getFile("sound/ambinet/an12.mp3")
    $ train_inside_music = getFile("sound/ambinet/train_inside.mp3")
    $ veter = getFile("sound/ambinet/veter.mp3")
    $ ring = getFile("sound/ambinet/ring.mp3")

    #Звуковые эфекты
    $ ak74m_indoor = getFile("sound/sfx/ak74m_indoor.ogg")
    $ hit = getFile("sound/sfx/hit.mp3")
    $ pencil = getFile("sound/sfx/pencil-scratches.mp3")
    $ hitting_iron = getFile("sound/sfx/hitting_iron.mp3")
    $ ra_sound = getFile("sound/sfx/ra_sound.mp3")
    $ ak74_fireselector_down = getFile("sound/sfx/ak74_fireselector_down.ogg")
    $ pm_far1 = getFile("sound/sfx/pm_far1.ogg")
    $ grenade_throw = getFile("sound/sfx/grenade_throw.mp3")
    $ gren_expl1_close = getFile("sound/sfx/gren_expl1_close.ogg")
    $ ak74_shooting = getFile("sound/sfx/ak74_shooting.mp3")
    $ shooting_far = getFile("sound/sfx/shooting_far.mp3")
    $ body_hit = getFile("sound/sfx/body_hit.mp3")
    $ knife_hit = getFile("sound/sfx/knife_hit.mp3")

    #Пикчи позже будет норм сорт 
    image gazeta1 = im.FactorScale(getFile("image/cg/gazeta1_draw.jpg"),1.1)
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
    image helichrash_combat = getFile("image/cg/helichrash_combat.jpg")

    image train_inside_pic = getFile("image/bg/int_train.jpg")
    image cabina = getFile("image/bg/cabina_draw.jpg")
    image angar = getFile("image/bg/angar_draw.jpg")
    image goriScetch = getFile("image/bg/goriScetch.jpg")
    image mi8_in1 = getFile("image/bg/mi8_in1_draw.jpg")
    image mi8_crash = getFile("image/bg/mi8_crash.jpg")
    image palatka = getFile("image/bg/palatka_draw.jpg")
    image village_evening = getFile("image/bg/village_evening.jpg")
    image chechen_house = getFile("image/bg/chechen_house.jpg")

    image derevnya_night = getFile("image/bg/derevnya_night.jpg")
    image rescue = getFile("image/cg/rescue.jpg")
    image rescue1 = getFile("image/cg/rescue1.jpg")
    image mi8_flight = getFile("image/cg/mi8_flight.jpg")
    image kazn = getFile("image/cg/kazn.jpg")
    image next_day = getFile("image/screens/next_day.png")

    #Меню и иные приколы
    image menu_back = getFile(getRandomItem(["image/cg/menu_fon1.jpg","image/cg/menu_fon2.png"]))

    image random_alert:
        getFile("image/screens/ra_anim/random_alert0.png")
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
        "ch_memories=='fish'", "black",
        "ch_memories=='grib'", "grib_cg",
        "ch_memories=='futbol1'", "futbol1_cg",
        "ch_memories=='forest'", "forest_cg",
        "ch_memories=='stadion'","stadion_cg",
        True, "angar"
    )
    image gruz200_memories = ConditionSwitch(
        "g2_memories=='g2'", "gruz200",
        True, "angar"
    )

    #Спрайт. Билдер выше
    image gen normal smile = bakeSpriteDefaultPlusSizeSold(900,1080,0,0,"gen/core_v2.png","gen/emo/gen_ord_smile.png")
    image gen mournful = bakeSpriteDefaultPlusSizeSold(900,1080,0,0,"gen/core_v2.png","gen/emo/gen_mournful.png")
    image gen laught = bakeSpriteDefaultPlusSizeSold(900,1080,0,0,"gen/core_v2.png","gen/emo/gen_laught.png")

    image gen_new normal = bakeNewSpriteDefaultSizeSold (900,1080,0,0,"gen_new/gen_new_body.png","gen_new/emo/gen_new_standart.png")
    image gen_new smile = bakeNewSpriteDefaultSizeSold (900,1080,0,0,"gen_new/gen_new_body.png","gen_new/emo/gen_new_smile.png")

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
    # $ resetDPAPlayer()
    call initVars
    $ updVisual()
    scene menu_back with dissolve2
    call screen dpa_main_menu with dissolve
    return
