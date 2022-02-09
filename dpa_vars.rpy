init -999:
    $ oldMenuWasSaved = False
    $ to_steam = False
    call initVars

label initVars:
    #Поинты
    call initPoint
    #Прочее 
    call initOther
    return

label initPoint:
    $ gen_fp = 0
    $ humanity = 0
    $ dysmoral = 0
    return

label initOther:
    $ ch_memories = "default"
    $ qte_loose = False
    $ qte_count = 0
    $ companies_lod = "th_demo_wip"
    return

