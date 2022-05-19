init python:
    #Главный герой
    gg = Character (u'Саша',color="ddde4e",what_color="fff")
    ggnvl = Character (u'Саша',color="ddde4e", kind=nvl)
    
    #Перостепенные герои
    gen_names = [ "Солдат", "Генадий" ]
    gen_name = gen_names[0]
    gen = DynamicCharacter("gen_name",color="288110",what_color="fff")

    rs_names = [ "Солдат", "Бритый" ]
    rs_name = rs_names[0]
    rs = DynamicCharacter("rs_name",color="da9979",what_color="fff")

    #Редкий юз
    elt = Character (u'Борис Николаевич', color="949494", what_color="fff")
    kp = Character (u'Командир полка', color="4f4031", what_color="fff")
    ofic = Character (u'Офицер', color="e3b212", what_color="fff")
    pil = Character (u'Вертолётчик', color="8599ff", what_color="fff")
    sol = Character (u'Солдат', color="23ad00", what_color="fff")
    rac = Character (u'Рация', color="696969", what_color="fff")
    om = Character (u'Старик', color="a16868", what_color="fff")