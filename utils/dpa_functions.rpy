
init -1 python:
    
    def dpa_save_old_visual():
        renpy.display.screen.screens[("dpa_say_gui_old",None)] = renpy.display.screen.screens[("say",None)]
        renpy.display.screen.screens[("dpa_game_menu_selector_old",None)] = renpy.display.screen.screens[("game_menu_selector",None)]
        renpy.display.screen.screens[("dpa_nvl_old",None)] = renpy.display.screen.screens[("nvl",None)]
        renpy.display.screen.screens[("dpa_choice_old",None)] = renpy.display.screen.screens[("choice",None)]

    def dpa_update_visual():
        renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("dpa_say_gui_reborn",None)]
        renpy.display.screen.screens[("game_menu_selector",None)] = renpy.display.screen.screens[("dpa_menu_selector",None)]
        renpy.display.screen.screens[("choice",None)] = renpy.display.screen.screens[("dpa_choice",None)]
        renpy.display.screen.screens[("nvl",None)] = renpy.display.screen.screens[("dpa_nvl",None)]
    
    def dpa_rollback_visual():
        renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("dpa_say_gui_old",None)]
        renpy.display.screen.screens[("game_menu_selector",None)] = renpy.display.screen.screens[("dpa_game_menu_selector_old",None)]
        renpy.display.screen.screens[("choice",None)] = renpy.display.screen.screens[("dpa_choice_old",None)]
        renpy.display.screen.screens[("nvl",None)] = renpy.display.screen.screens[("dpa_nvl_old",None)]

    def dpa_to_default_settings():
        Call("initVars")
        dpa_rollback_visual()
    
    def dpa_new_chapter(dayNum, chapterName):
        dpa_set_chapter(dayNum, chapterName)
        dpa_update_visual()

#Базовые функции
init -99 python:

    # Работа с файлами
    def dpa_get_file(file):
        return default_dpa_path + file

    def dpa_get_label_WIP(name):
        if to_steam == True:
            return "th_demo_wip"
        return name

    # Работа с аудио файлами
    def dpa_register_music(song_name,ru_lang,m_file):
        toRet = dpa_get_file(m_file)
        dpa_music_list[song_name] = toRet
        if ru_lang == "NN":
            dpa_music_names[song_name] = "??? - Без имени"
        else:
            dpa_music_names[song_name] = ru_lang
        return toRet
    
    def dpa_get_music(music_name):
        return dpa_music_list[music_name]

    # Работа со случайными значениями
    def dpa_get_random_item(items):
        num = renpy.random.randint(0, len(items)-1)
        return items[num]

    def dpa_get_random_button():
        return dpa_get_random_item(['1','2','3','4','5','6','7','8','9','0','z','x','c','j','i','o','b','t','h'])
    
    # Установка названия главы
    def dpa_set_chapter(dayNum, chapterName):
        global save_name
        save_name = (u"DPA v%s: День %s %s") % (dpa_version, dayNum, chapterName)
    
    # ДПАшный блок ролбэка (онли для дебага)
    def dpa_block_rollback():
        if to_steam:
            renpy.block_rollback()

    # Ренейм персонажей, чисто для понимания и удобства посика ренеймов
    def dpa_rename_character(character_name, name):
        SetVariable(character_name, name)

    def dpa_rename_character_from_list(character_name, names_array, pos):
        if len(names_array) >= pos:
            return
        dpa_rename_character(character_name, names_array[pos]) 

    # Работа с изображениями
    def bakeSpriteDefaultSizeSold(sizeX, sizeY, posX, posY, character, emo, special="null.png"):
        return ConditionSwitch(
        "persistent.sprite_time=='day'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), dpa_get_file("image/sprites/form_v2_bottom.png"),
            (posX,posY), dpa_get_file("image/sprites/form_v2_top.png"),
            (posX,posY), dpa_get_file("image/sprites/"+character),
            (posX,posY), dpa_get_file("image/sprites/form_v2_middle.png"),
            (posX,posY), dpa_get_file("image/sprites/"+emo),
            (posX,posY), dpa_get_file("image/sprites/belt.png"),
            (posX,posY), dpa_get_file("image/sprites/"+special)),
            im.matrix.tint(0.83, 0.88, 0.92)),
        "persistent.sprite_time=='sunset'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), dpa_get_file("image/sprites/form_v2_bottom.png"),
            (posX,posY), dpa_get_file("image/sprites/form_v2_top.png"),
            (posX,posY), dpa_get_file("image/sprites/"+character),
            (posX,posY), dpa_get_file("image/sprites/form_v2_middle.png"),
            (posX,posY), dpa_get_file("image/sprites/"+emo),
            (posX,posY), dpa_get_file("image/sprites/belt.png"),
            (posX,posY), dpa_get_file("image/sprites/"+special)),
            im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), dpa_get_file("image/sprites/form_v2_bottom.png"),
            (posX,posY), dpa_get_file("image/sprites/form_v2_top.png"),
            (posX,posY), dpa_get_file("image/sprites/"+character),
            (posX,posY), dpa_get_file("image/sprites/form_v2_middle.png"),
            (posX,posY), dpa_get_file("image/sprites/"+emo),
            (posX,posY), dpa_get_file("image/sprites/belt.png"),
            (posX,posY), dpa_get_file("image/sprites/"+special)),
            im.matrix.tint(0.63, 0.78, 0.82)))

    def bakeSpriteDefaultPlusSizeSold(sizeX, sizeY, posX, posY, character, emo, special="null.png"):
        return ConditionSwitch(
        "persistent.sprite_time=='day'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), dpa_get_file("image/sprites/form_v2_ps_bottom.png"),
            (posX,posY), dpa_get_file("image/sprites/form_v2_ps_top.png"),
            (posX,posY), dpa_get_file("image/sprites/"+character),
            (posX,posY), dpa_get_file("image/sprites/form_v2_ps_middle.png"),
            (posX,posY), dpa_get_file("image/sprites/"+emo),
            (posX,posY), dpa_get_file("image/sprites/belt_ps.png"),
            (posX,posY), dpa_get_file("image/sprites/"+special)),
            im.matrix.tint(0.83, 0.88, 0.92)),
        "persistent.sprite_time=='sunset'",
        im.MatrixColor(  
            im.Composite((sizeX,sizeY), 
            (posX,posY), dpa_get_file("image/sprites/form_v2_ps_bottom.png"),
            (posX,posY), dpa_get_file("image/sprites/form_v2_ps_top.png"),
            (posX,posY), dpa_get_file("image/sprites/"+character),
            (posX,posY), dpa_get_file("image/sprites/form_v2_ps_middle.png"),
            (posX,posY), dpa_get_file("image/sprites/"+emo),
            (posX,posY), dpa_get_file("image/sprites/belt_ps.png"),
            (posX,posY), dpa_get_file("image/sprites/"+special)),
            im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",
        im.MatrixColor(  
            im.Composite((sizeX,sizeY), 
            (posX,posY), dpa_get_file("image/sprites/form_v2_ps_bottom.png"),
            (posX,posY), dpa_get_file("image/sprites/form_v2_ps_top.png"),
            (posX,posY), dpa_get_file("image/sprites/"+character),
            (posX,posY), dpa_get_file("image/sprites/form_v2_ps_middle.png"),
            (posX,posY), dpa_get_file("image/sprites/"+emo),
            (posX,posY), dpa_get_file("image/sprites/belt_ps.png"),
            (posX,posY), dpa_get_file("image/sprites/"+special)),
            im.matrix.tint(0.63, 0.78, 0.82)))
