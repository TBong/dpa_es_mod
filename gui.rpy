init -80:
    screen dpa_say_gui:
    #Экран диалога
        window background None id "window":

            $ timeofday = persistent.timeofday

            if persistent.font_size == "large":

                imagebutton auto getFile("gui/gray/backward_%s.png") xpos 38 ypos 949 action ShowMenu("text_history") #тут свой путь

                add getFile("gui/gray/dialogue_box.png") xpos 174 ypos 916 #тут свой путь

                imagebutton auto getFile("gui/gray/hide_%s.png") xpos 1508 ypos 933 action HideInterface() #тут свой путь
                imagebutton auto getFile("gui/gray/save_%s.png") xpos 1567 ypos 933 action ShowMenu('save') #тут свой путь
                imagebutton auto getFile("gui/gray/menu_%s.png") xpos 1625 ypos 933 action ShowMenu('game_menu_selector') #тут свой путь
                imagebutton auto getFile("gui/gray/load_%s.png") xpos 1682 ypos 933 action ShowMenu('load') #тут свой путь

                if not config.skipping:
                    imagebutton auto getFile("gui/gray/forward_%s.png") xpos 1735 ypos 949 action Skip() #тут свой путь
                else:
                    imagebutton auto getFile("gui/gray/fast_forward_%s.png") xpos 1735 ypos 949 action Skip() #тут свой путь

                text what id "what" xpos 194 ypos 959 xmaximum 1541 size 28 line_spacing 2
                if who:
                    text who id "who" xpos 194 ypos 925 size 28 line_spacing 2

            elif persistent.font_size == "small":

                imagebutton auto getFile("gui/gray//backward_%s.png") xpos 38 ypos 949 action ShowMenu("text_history") #тут свой путь

                add getFile("gui/gray/dialogue_box.png") xpos 174 ypos 916 #тут свой путь

                imagebutton auto getFile("gui/gray/hide_%s.png") xpos 1508 ypos 933 action HideInterface() #тут свой путь
                imagebutton auto getFile("gui/gray/save_%s.png") xpos 1567 ypos 933 action ShowMenu('save') #тут свой путь
                imagebutton auto getFile("gui/gray/menu_%s.png") xpos 1625 ypos 933 action ShowMenu('game_menu_selector') #тут свой путь
                imagebutton auto getFile("gui/gray/load_%s.png") xpos 1682 ypos 933 action ShowMenu('load') #тут свой путь

                if not config.skipping:
                    imagebutton auto getFile("gui/gray/forward_%s.png") xpos 1735 ypos 949 action Skip() #тут свой путь
                else:
                    imagebutton auto getFile("gui/gray/fast_forward_%s.png") xpos 1735 ypos 949 action Skip() #тут свой путь

                text what id "what" xpos 194 ypos 959 xmaximum 1541 size 28 line_spacing 2
                if who:
                    text who id "who" xpos 194 ypos 925 size 28 line_spacing 2
                    
                    
                    
screen dpa_Load:
    tag menu
    modal True
    window:
        add getFile("gui/load/load_menu.jpg"):
            xpos -4
            ypos -4

        textbutton ["Загрузить игру"]:
            ypos 950
            xalign 0.5
            action FileLoad(selected_slot)

        textbutton ["Удалить"]:
            xpos 1500
            ypos 950
            action FileDelete(selected_slot)

        textbutton ["Назад"]:
            xpos 30
            ypos 950
            action Jump("dpa_menu")

        vbox:
            xalign 0.037
            yalign 0.52
            grid 1 9:
                for i in range(1, 10):
                    textbutton str(i):
                        right_padding 55
                        text_size 60
                        xpos 32
                        action (FilePage("dpa_menu_FilePage_"+ str(i)), SetVariable("selected_slot", False))
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
                        fixed:
                            text ( "%s." % i
                                   + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                   + "\n" +FileSaveName(i)):
                                xpos 15
                                ypos 15
                                