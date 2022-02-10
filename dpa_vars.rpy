init -999:
    $ to_steam = False
    $ dpa_version = "0.1-A"
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
    $ g2_memories = "default"
    $ qte_loose = False
    $ qte_count = 0
    $ companies_lod = "th_demo_wip"
    return

