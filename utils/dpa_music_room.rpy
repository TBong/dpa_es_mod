init 10 python:    
    selectedTrackName = 'null'
    dpaMR = MusicRoom(fadeout=0.5,loop=False)

    for track in list(dpa_music_list):
        dpaMR.add(dpa_get_music(track), always_unlocked=True)

    def getSelectedTrackName():
        return selectedTrackName

    def getTrackName(name):
        return dpa_music_names[name]

    def getPlayingInMR():
        path = renpy.music.get_playing()
        if path == None:
            return None
        for k, v in dpa_music_list.items():
            if v == path:
                return k
        return None

    def resetTrackName():
        playingName = getPlayingInMR()
        if playingName == None:
            return
        SetVariable("selectedTrackName",getTrackName(playingName))

    def isNowPlaying(name):
        return getPlayingInMR() == name




screen music_room_dpa_reborn:
    tag menu
    on "show" action [dpaMR.RandomPlay(), resetTrackName()]
    imagebutton xalign 0.365 ypos 200:
        auto dpa_get_file("image/screens/player/player_back_%s.png")
        action dpaMR.Previous()
    imagebutton xalign 0.455 ypos 200:
        auto dpa_get_file("image/screens/player/player_play_%s.png")
        selected not renpy.music.get_pause()
        action dpaMR.TogglePause()
    imagebutton xalign 0.545 ypos 200:
        auto dpa_get_file("image/screens/player/player_next_%s.png")
        action dpaMR.Next()
    imagebutton xalign 0.635 ypos 200:
        auto dpa_get_file('image/screens/player/player_loop_%s.png')
        selected renpy.music.get_loop()
        action dpaMR.ToggleLoop()
    text getSelectedTrackName():
        xalign 0.5 
        ypos 120
        size 30
    side "c":
        xalign 0.5
        ypos 350
        xysize (600, 700)

        default sdl_mus_bar_value = ui.adjustment()
        viewport id "vp_playlist":
            mousewheel True
            yadjustment sdl_mus_bar_value

            has vbox spacing 2

            for name in list(dpa_music_list):
                button:
                    background Solid("#262626")
                    xsize 600 
                    ysize 35
                    text getTrackName(name) xalign 0.5 style "text_select_track"
                    action dpaMR.Play(dpa_get_music(name))
                    selected isNowPlaying(name)
    textbutton ["Назад"]:
            xpos 30
            ypos 950
            text_style "text_save_load"
            style "button_none"
            action Return()
    timer 0.1 repeat True action resetTrackName()