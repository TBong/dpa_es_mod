#Базовые переменные
init -100 python:

    if to_steam:
        default_dpa_path = ""
    else:
        default_dpa_path = "mods/dpa_es_mod/"
        
init 999:
    define config.developer = True

init:
    $ dpa_save_old_visual()

    $ mods["dpa_start"]=u"{font=[furore]}Добро пожаловать в {color=#911010}ад"

    #Музыка
    $ fon1 = dpa_register_music("fon1","NN","sound/song/fon1.mp3")
    $ song_crash= dpa_register_music("song_crash","Свидетельство о смерти - чуть-чуть меня ","sound/song/song_а_little_bit_of_me.mp3")
    $ shturm = dpa_register_music("shturm","Сергей Тимошенко - Штурм","sound/song/shturm.mp3")
    $ song1 = dpa_register_music("song1","В военкомате случай был","sound/song/song1.mp3")
    $ song_ep = dpa_register_music("song_ep","NN","sound/song/song_ep.mp3")
    $ song_menu = dpa_register_music("song_menu","Эрик Осташев - Солдат фортуны","sound/song/song_menu.mp3")
    $ song2 = dpa_register_music("song2","Здравствуй мама","sound/song/song2.mp3")
    $ song_liric = dpa_register_music("song_liric","NN","sound/song/song_liric.mp3")
    $ song_gruz200 = dpa_register_music("song_gruz200","Груз-200","sound/song/song_gruz200.mp3")
    $ song_na_mozdok = dpa_register_music("song_na_mazdok","На Моздок","sound/song/song_na_mozdok.mp3") 
    $ song_rising_sun = dpa_register_music("song_rising_sun","The Animals - House of the Rising Sun","sound/song/song_rising_sun.mp3")
    $ kombat = dpa_register_music("kombat","Любэ - Комбат","sound/song/kombat.mp3")

    $ menu_music = dpa_get_music(dpa_get_random_item(["song1","song2","song_menu","kombat","shturm"]))

    #Звуки окружения
    $ mi8 = dpa_get_file("sound/ambinet/mi8.mp3")
    $ mi8_1 = dpa_get_file("sound/ambinet/mi8_1.mp3")
    $ uaz = dpa_get_file("sound/ambinet/uaz.mp3")
    $ an12 = dpa_get_file("sound/ambinet/an12.mp3")
    $ train_inside_music = dpa_get_file("sound/ambinet/train_inside.mp3")
    $ veter = dpa_get_file("sound/ambinet/veter.mp3")
    $ ring = dpa_get_file("sound/ambinet/ring.mp3")

    #Звуковые эфекты
    $ hit = dpa_get_file("sound/sfx/hit.mp3")
    $ pencil = dpa_get_file("sound/sfx/pencil-scratches.mp3")
    $ hitting_iron = dpa_get_file("sound/sfx/hitting_iron.mp3")
    $ ra_sound = dpa_get_file("sound/sfx/ra_sound.mp3")
    $ ak74_fireselector_down = dpa_get_file("sound/sfx/ak74_fireselector_down.ogg")
    $ pm_far1 = dpa_get_file("sound/sfx/pm_far1.ogg")
    $ grenade_throw = dpa_get_file("sound/sfx/grenade_throw.mp3")
    $ gren_expl1_close = dpa_get_file("sound/sfx/gren_expl1_close.ogg")
    $ ak74_shooting = dpa_get_file("sound/sfx/ak74_shooting.mp3")
    $ shooting_far = dpa_get_file("sound/sfx/shooting_far.mp3")

    #Пикчи позже будет норм сорт 
    image gazeta1 = im.FactorScale(dpa_get_file("image/cg/gazeta1_draw.jpg"),1.1)
    image futbol1_cg = dpa_get_file("image/cg/futbol1.jpg")
    image grib_cg = dpa_get_file("image/cg/grib_draw.jpg")
    image forest_cg = dpa_get_file("image/cg/forest_draw.jpg")
    image stadion_cg = dpa_get_file("image/cg/stadion_draw.jpg")
    image eltsin1 = dpa_get_file("image/cg/eltsin1_draw.jpg")
    image gruz200 = dpa_get_file("image/cg/gruz200_draw.jpg")

    image mi8_in2 = dpa_get_file("image/cg/mi8_in2_draw.jpg")
    image mi8 = dpa_get_file("image/cg/mi8_draw.jpg")
    image combat_map = dpa_get_file("image/screens//image_maps/combat_map/test_map.png")
    image airport = dpa_get_file("image/cg/airport_draw.jpg")
    image airport1 = dpa_get_file("image/cg/airport2_draw.jpg")
    image train = dpa_get_file("image/cg/train.png")
    image train_open = dpa_get_file("image/cg/train_open.png")
    image helichrash_combat = dpa_get_file("image/cg/helichrash_combat.jpg")

    image train_inside_pic = dpa_get_file("image/bg/int_train.jpg")
    image cabina = dpa_get_file("image/bg/cabina_draw.jpg")
    image angar = dpa_get_file("image/bg/angar_draw.jpg")
    image goriScetch = dpa_get_file("image/bg/goriScetch.jpg")
    image mi8_in1 = dpa_get_file("image/bg/mi8_in1_draw.jpg")
    image mi8_crash = dpa_get_file("image/bg/mi8_crash.jpg")
    image palatka = dpa_get_file("image/bg/palatka_draw.jpg")
    image village_evening = dpa_get_file("image/bg/village_evening.jpg")
    image chechen_house = dpa_get_file("image/bg/chechen_house.jpg")

    #Меню и иные приколы
    image menu_back = dpa_get_file(dpa_get_random_item(["image/cg/menu_fon1.jpg","image/cg/menu_fon2.png"]))

    image random_alert:
        dpa_get_file("image/screens/ra_anim/random_alert0.png")
        0.3
        dpa_get_file("image/screens/ra_anim/random_alert2.png")
        0.3
        dpa_get_file("image/screens/ra_anim/random_alert3.png")
        0.3
        dpa_get_file("image/screens/ra_anim/random_alert4.png")
        0.3
        repeat

    image random_alert_for_widget:
        dpa_get_file("image/screens/ra_anim/random_alert0.png")
        zoom .1
        0.3
        dpa_get_file("image/screens/ra_anim/random_alert2.png")
        zoom .1
        0.3
        dpa_get_file("image/screens/ra_anim/random_alert3.png")
        zoom .1
        0.3
        dpa_get_file("image/screens/ra_anim/random_alert4.png")
        zoom .1
        0.3
        repeat

    image qte_anim_button:
        dpa_get_file("image/screens/qte/press_button1.png")
        0.1
        dpa_get_file("image/screens/qte/press_button2.png")
        0.1
        dpa_get_file("image/screens/qte/press_button3.png")
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

    image rs furious = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_furious.png")
    image rs furious blik = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_furious.png", "romper_stomper/emo/rs_blik.png")
    image rs normal = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_standart.png")
    image rs normal blik = bakeSpriteDefaultSizeSold(900,1080,0,0,"romper_stomper/rs_body.png","romper_stomper/emo/rs_standart.png", "romper_stomper/emo/rs_blik.png")
    
label dpa_start:
    $ dpa_update_visual()
    call disclaimer
    jump dpa_menu
    return

label dpa_menu:
    $ dpa_block_rollback()
    play music menu_music fadein 2
    $ new_chapter(0, u"Меню DPA")
    # $ resetDPAPlayer()
    $ dpa_update_visual()
    scene menu_back with dissolve2
    call screen dpa_main_menu with dissolve
    return

label startMod:
    call initVars
    $ dpa_game_started = True
    jump prolog
