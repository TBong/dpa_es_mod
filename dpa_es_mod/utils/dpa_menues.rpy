init -81 python:
    def getXPos(num):
        if num == 1:
            return 42
        return 32

    def getFileSayGui(path):
        return getFile("image/screens/dialog/"+path)    

screen dpa_say_gui_reborn:
    window background None id "window":
        if persistent.font_size == "large":
            add getFileSayGui("gray_reborn/dialog_box_large.png") xpos -5 ypos 863

            if not config.skipping:
                imagebutton auto getFileSayGui("gray_reborn/forward_l_%s.png") xpos 1750 ypos 912 action Skip()
            else:
                imagebutton auto getFileSayGui("gray_reborn/forward_l_f_%s.png") xpos 1750 ypos 912 action Skip()

            imagebutton auto getFileSayGui("gray_reborn/backward_l_%s.png") xpos -10 ypos 912 action ShowMenu("text_history")

            text what id "what" xpos 155 ypos 934 xmaximum 1610 size 35 line_spacing 2
            if who:
                text who id "who" xpos 180 ypos 895 size 35 line_spacing 2
        elif persistent.font_size == "small":
            add getFileSayGui("gray_reborn/dialog_box.png") xpos -5 ypos 913

            if not config.skipping:
                imagebutton auto getFileSayGui("gray_reborn/forward_%s.png") xpos 1816 ypos 972 action Skip()
            else:
                imagebutton auto getFileSayGui("gray_reborn/forward_f_%s.png") xpos 1816 ypos 972 action Skip()

            imagebutton auto getFileSayGui("gray_reborn/backward_%s.png") xpos 14 ypos 972 action ShowMenu("text_history")

            text what id "what" xpos 155 ypos 969 xmaximum 1610 size 28 line_spacing 2
            if who:
                text who id "who" xpos 180 ypos 935 size 28 line_spacing 2    

screen dpa_say_gui:
#Экран диалога
    window background None id "window":
        
        if persistent.font_size == "large":
            imagebutton auto getFileSayGui("gray/backward_%s.png") xpos 38 ypos 949 action ShowMenu("text_history") #тут свой путь
            add getFileSayGui("gray/dialogue_box.png") xpos 174 ypos 916 #тут свой путь
            imagebutton auto getFileSayGui("gray/hide_%s.png") xpos 1508 ypos 933 action HideInterface() #тут свой путь
            imagebutton auto getFileSayGui("gray/save_%s.png") xpos 1567 ypos 933 action ShowMenu('dpa_Save') #тут свой путь
            imagebutton auto getFileSayGui("gray/menu_%s.png") xpos 1625 ypos 933 action ShowMenu('game_menu_selector') #тут свой путь
            imagebutton auto getFileSayGui("gray/load_%s.png") xpos 1682 ypos 933 action ShowMenu('dpa_Load') #тут свой путь
            if not config.skipping:
                imagebutton auto getFileSayGui("gray/forward_%s.png") xpos 1735 ypos 949 action Skip() #тут свой путь
            else:
                imagebutton auto getFileSayGui("gray/fast_forward_%s.png") xpos 1735 ypos 949 action Skip() #тут свой путь
            text what id "what" xpos 194 ypos 959 xmaximum 1541 size 28 line_spacing 2
            if who:
                text who id "who" xpos 194 ypos 925 size 28 line_spacing 2
        elif persistent.font_size == "small":
            imagebutton auto getFileSayGui("gray/backward_%s.png") xpos 38 ypos 949 action ShowMenu("text_history") #тут свой путь
            add getFileSayGui("gray/dialogue_box.png") xpos 174 ypos 916 #тут свой путь
            imagebutton auto getFileSayGui("gray/hide_%s.png") xpos 1508 ypos 933 action HideInterface() #тут свой путь
            imagebutton auto getFileSayGui("gray/save_%s.png") xpos 1567 ypos 933 action ShowMenu('dpa_Save') #тут свой путь
            imagebutton auto getFileSayGui("gray/menu_%s.png") xpos 1625 ypos 933 action ShowMenu('game_menu_selector') #тут свой путь
            imagebutton auto getFileSayGui("gray/load_%s.png") xpos 1682 ypos 933 action ShowMenu('dpa_Load') #тут свой путь
            if not config.skipping:
                imagebutton auto getFileSayGui("gray/forward_%s.png") xpos 1735 ypos 949 action Skip() #тут свой путь
            else:
                imagebutton auto getFileSayGui("gray/fast_forward_%s.png") xpos 1735 ypos 949 action Skip() #тут свой путь
            text what id "what" xpos 194 ypos 959 xmaximum 1541 size 28 line_spacing 2
            if who:
                text who id "who" xpos 194 ypos 925 size 28 line_spacing 2

screen dpa_choice:
    modal True
    window:
        background Frame(getFile("image/screens/menu/choice.png"),50,50)
        xfill True
        yalign 0.5
        left_padding 75
        right_padding 75
        bottom_padding 50
        top_padding 50
        vbox:
            xalign 0.5
            for caption, action, chosen  in items:
                if action and caption:
                    button:
                        background None
                        xalign 0.5
                        action action
                        text caption:
                            font furore 
                            size 35
                            hover_size 35
                            idle_color "#474747"
                            color "#474747"
                            hover_color "#fff"
                            xcenter 0.5
                else:
                    button:
                        background None
                        xalign 0.5
                        action action
                        text caption:
                            font furore
                            size 35
                            hover_size 35
                            idle_color "#474747"
                            color "#474747"
                            hover_color "#fff"
                            xcenter 0.5  
                
            xcenter 0.5 
            ycenter 0.5      

screen dpa_nvl:
    window:
        background Frame(getFile("image/screens/menu/choice.png"),50,50)
        xfill True
        yfill True
        yalign 0.5
        left_padding 125
        right_padding 125
        bottom_padding 100
        top_padding 100
        vbox:
            for who, what, who_id, what_id, window_id  in dialogue:
                window:
                    id window_id
                    hbox:
                        spacing 10
                        if persistent.font_size == "large":
                            if who is not None:
                                text who:
                                    id who_id
                                    size 29
                                    line_spacing 2
                                    
                            text what:
                                id what_id
                                size 26
                                line_spacing 3
                                # font "mods/lampleto/ARIALUNI.TTF"
                                color "#ffffff"

                        elif persistent.font_size == "small":
                            if who is not None:
                                text who:
                                    id who_id
                                    size 28
                                    # font "mods/lampleto/17680.otf"
                                    line_spacing 2
                
                            text what:
                                id what_id
                                size 24
                                # font "mods/lampleto/ARIALUNI.TTF"
                                line_spacing 3
                                kerning 1
                                color "#ffffff" 
    if not config.skipping:
        imagebutton auto getFileSayGui("gray_reborn/forward_%s.png") xalign 0.95 ypos 950 action Skip()
    else:
        imagebutton auto getFileSayGui("gray_reborn/forward_f_%s.png") xalign 0.95 ypos 950 action Skip()
    imagebutton auto getFileSayGui("gray_reborn/backward_%s.png") xalign 0.05 ypos 950 action ShowMenu("text_history")
    
#Главное меню
screen dpa_main_menu:
    tag menu
    modal True
    add getFile("image/screens/menu/fon_text.png")
    imagebutton:
        auto  getFile("image/screens/menu/nachat_2_%s.png")
        xpos 55
        ypos 200
        action (Function(renpy.music.stop,"dpa_music_player", 2)), (Hide("dpa_main_menu", transition=dissolve)), (Call("prolog"))
    imagebutton:
        auto getFile("image/screens/menu/player_button_%s.png")
        xpos 55
        ypos 400
        action [Function(renpy.music.stop, "music", 1), ShowMenu('dpa_player')]
    imagebutton:
        auto getFile("image/screens/menu/gallery_2_%s.png")
        xpos 55
        ypos 600
        action ShowMenu('wip')
    imagebutton:
        auto  getFile("image/screens/menu/exit_2_%s.png")
        xpos 55
        ypos 800
        action [ Function(toDefaultSettings), MainMenu() ]
    text "{font=[furore]}Добро пожаловать в":
        xpos 1000
        ypos 33
        size 58
    text "{font=[furore]}{color=#911010}АД":
        xpos 1350
        ypos 80
        size 70
    timer 0.1 repeat True action [If(renpy.music.get_playing("dpa_music_player") == None and renpy.music.get_playing() == None, true=Function(playInMain))]

#Маленькое меню
screen dpa_menu_selector:
    tag menu
    modal True

    $ timeofday = persistent.timeofday
    $ time_of_day = persistent.timeofday
    button:
        style "blank_button"
        xalign 0
        yalign 0
        xfill True
        yfill True
        action Return()
    
    add getFile("image/screens/menu/lil_menu_back.png"):
        xalign 0.5
        yalign 0.5

    textbutton ["Меню БЛ"]:
        xalign 0.5
        yalign 0.30
        text_style "text_save_load"
        style "button_none"
        action [ Function(toDefaultSettings), MainMenu() ]

    textbutton ["Сохранение"]:
        xalign 0.5
        yalign 0.40
        text_style "text_save_load"
        style "button_none"
        action ShowMenu('dpa_Save')
    
    textbutton ["Загрузка"]:
        xalign 0.5
        yalign 0.50
        text_style "text_save_load"
        style "button_none"
        action ShowMenu('dpa_Load')
    
    textbutton ["Настройки"]:
        xalign 0.5
        yalign 0.60
        text_style "text_save_load"
        style "button_none"
        action ShowMenu('preferences')
    
    textbutton ["Выход"]:
        xalign 0.5
        yalign 0.70
        text_style "text_save_load"
        style "button_none"
        action ShowMenu('quit')
    
    textbutton ["Откл. интерфейс мода"]:
        xalign 1.0
        yalign 1.0
        style "button_none"
        text_style "text_save_load"
        action [ Function(rollbackVisual), Return() ]
 
#Меню загрузки
screen dpa_Load:
    tag menu
    modal True
    window:
        add "menu_back":
            xpos -6
            ypos -6

        textbutton ["Загрузить игру"]:
            ypos 950
            xalign 0.5
            text_style "text_save_load"
            style "button_none"
            action [FileLoad(selected_slot) ]

        textbutton ["Удалить"]:
            xpos 1500
            ypos 950
            text_style "text_save_load"
            style "button_none"
            action FileDelete(selected_slot)

        textbutton ["Назад"]:
            xpos 30
            ypos 950
            text_style "text_save_load"
            style "button_none"
            action Return()

        vbox:
            xalign 0.037
            yalign 0.52
            grid 1 9:
                for i in range(1, 10):
                    textbutton str(i):
                        right_padding 55
                        text_size 60
                        text_style "text_save_load"
                        style "button_none"
                        xpos getXPos(i)
                        action (FilePage(str(i)), SetVariable("selected_slot", False))
        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "file_load_button"
                        fixed:
                            text ( "%s." % i
                                   + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                   + "\n" +FileSaveName(i)):
                                xpos 15
                                ypos 15

#не доделанная часть меню
screen wip:
    tag menu
    modal True
    window:
        add "menu_back":
            xpos -6
            ypos -6

        imagebutton:
            idle getFile("image/screens/menu/wip.png")
            xpos 578
            ypos 152
            action NullAction()
        timer 1.5 action Return()

   
#Меню сохранения
screen dpa_Save:
    tag menu
    modal True
    window:
        add "menu_back":
            xpos -6
            ypos -6

        textbutton ["Сохранить игру"]:
            ypos 950
            xalign 0.5
            text_style "text_save_load"
            style "button_none"
            action FileSave(selected_slot)

        textbutton ["Удалить"]:
            xpos 1500
            ypos 950
            text_style "text_save_load"
            style "button_none"
            action FileDelete(selected_slot)

        textbutton ["Назад"]:
            xpos 30
            ypos 950
            text_style "text_save_load"
            style "button_none"
            action Return()

        vbox:
            xalign 0.037
            yalign 0.52
            grid 1 9:
                for i in range(1, 10):
                    textbutton str(i):
                        right_padding 55
                        text_size 60
                        text_style "text_save_load"
                        style "button_none"
                        xpos getXPos(i)
                        action (FilePage(str(i)), SetVariable("selected_slot", False))
        grid 4 3:
            xpos 0.11
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "file_load_button"
                        fixed:
                            text ( "%s." % i
                                   + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                   + "\n" +FileSaveName(i)):
                                xpos 15
                                ypos 15