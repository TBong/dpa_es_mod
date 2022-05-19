python early:
    debug_page = 1

    def dpa_debug_widget():
        if (not dpa_debug_panel) or (not dpa_game_started):
            return
        else:
            ui.tag("menu")
            ui.vbox(xpos=0.87, background=None, mousewheel=True, yadjustment=ui.adjustment())

            ui.button(clicked=None,background="#072b6b", xsize=0.13)
            ui.text("%s %d" % ("Страница", debug_page), style="text_debug_panel")
            ui.hbox(background=None)
            ui.button(background="#072b6b",xsize=0.067,clicked=SetVariable("debug_page", debug_page+1))
            ui.text("+", style="text_debug_panel")
            ui.button(background="#072b6b",xsize=0.067,clicked=SetVariable("debug_page", debug_page-1))
            ui.text("-", style="text_debug_panel")
            ui.close()
            if debug_page == 0:
                ui.button(background="#2f2f2f", xsize=0.13, clicked=dpa_rollback_visual)
                ui.text("Выключить меню мода", style="text_debug_panel")
                ui.button(background="#2f2f2f", xsize=0.13, clicked=dpa_update_visual)
                ui.text("Включить меню мода", style="text_debug_panel")
            elif debug_page == 1:
                ui.button(clicked=None,background="#2f2f2f", xsize=0.13)
                ui.text("%s %d" % ("Человечность", humanity), style="text_debug_panel")
                ui.hbox(background=None)
                ui.button(background="#2f2f2f", xsize=0.067,clicked=SetVariable("humanity",humanity+1))
                ui.text("+", style="text_debug_panel")
                ui.button(background="#2f2f2f", xsize=0.067,clicked=SetVariable("humanity",humanity-1))
                ui.text("-", style="text_debug_panel")
                ui.close()

                ui.button(clicked=None,background="#2f2f2f", xsize=0.13)
                ui.text("%s %d" % ("Гена ФП", gen_fp), style="text_debug_panel")
                ui.hbox(background=None)
                ui.button(background="#2f2f2f",xsize=0.067,clicked=SetVariable("gen_fp",gen_fp+1))
                ui.text("+", style="text_debug_panel")
                ui.button(background="#2f2f2f",xsize=0.067,clicked=SetVariable("gen_fp",gen_fp-1))
                ui.text("-", style="text_debug_panel")
                ui.close()

                ui.button(clicked=None,background="#2f2f2f", xsize=0.13)
                ui.text("%s %d" % ("Дизмораль", dysmoral), style="text_debug_panel")
                ui.hbox(background=None)
                ui.button(background="#2f2f2f",xsize=0.067,clicked=SetVariable("dysmoral",dysmoral+1))
                ui.text("+", style="text_debug_panel")
                ui.button(background="#2f2f2f",xsize=0.067,clicked=SetVariable("dysmoral",dysmoral-1))
                ui.text("-", style="text_debug_panel")
                ui.close()

            ui.close()
    config.overlay_functions.append(dpa_debug_widget)