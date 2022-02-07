screen combat_map:
    imagemap:
        auto getFile("image/screens/menu/image_maps/combat_map/test_map_%s.png")
        hotspot (657,482,35,35) action [ SetVariable("companies_lod", "bamut"), Hide("combat_map", transition=dissolve), Return()] alt Jump("prolog") hover_sound pencil #Бамут
        hotspot (772,474,40,47) action [ SetVariable("companies_lod", "u_m"), Hide("combat_map", transition=dissolve), Return()] alt Jump("prolog") hover_sound pencil #Урус-Мартан
        hotspot (901,397,50,45) action [ SetVariable("companies_lod", "argun"), Hide("combat_map", transition=dissolve), Return()] alt Jump("prolog") hover_sound pencil #Аргун
        hotspot (986,377,50,42) action [ SetVariable("companies_lod", "gudermes"), Hide("combat_map", transition=dissolve), Return()] alt Jump("prolog") hover_sound pencil #Гудермес

label dpa_combat_map:
    show combat_map with dissolve
    call screen combat_map
    return