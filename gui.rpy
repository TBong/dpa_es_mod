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