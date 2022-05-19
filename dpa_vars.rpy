init -999:
    $ to_steam = False
    $ dpa_version = "0.1-A"
    $ dpa_music_list = {}
    $ dpa_music_names = {}
    $ dpa_debug_panel = False
    $ dpa_game_started = False
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
    $ dpa_game_started = False
    $ ch_memories = "default"
    $ g2_memories = "default"
    $ qte_loose = False
    $ qte_count = 0
    $ companies_lod = "th_demo_wip"
    return

