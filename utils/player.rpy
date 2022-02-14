init 10 python:
    selected_track = -1
    loop_track = False
    leaveFromPlayer = False
    track_name = "Null"
    renpy.music.register_channel("dpa_music_player", "music")
    
    def getSelectedTrackPath():
        return getMusic(list(dpa_music_list)[selected_track])

    def setTrackName():
        tmpSel = list(dpa_music_list)[selected_track]
        global track_name
        track_name = getTrakName(tmpSel)
    
    def getSelectedTrackName():
        return track_name
    
    def getTrakName(track):
        return dpa_music_names[track]
    
    def getTrackIndex(name):
        return list(dpa_music_list).index(name)

    def getNextTrack():
        if selected_track == -1:
            return
        if not loop_track and not leaveFromPlayer: 
            selected_track += 1
            if selected_track >= len(dpa_music_list):
                global selected_track
                selected_track = 0
        renpy.music.queue(getSelectedTrackPath(),channel='dpa_music_player', loop=loop_track, clear_queue=True)
        setTrackName()

    def updSTnPlay(num):
        selected_track += num
        global selected_track
        if selected_track >= len(dpa_music_list):
            selected_track = 0
        elif selected_track < 0:
            selected_track = len(dpa_music_list) - 1
        renpy.music.stop("dpa_music_player")
        renpy.music.queue(getSelectedTrackPath(), channel='dpa_music_player', loop=loop_track, clear_queue=True)
        setTrackName()
    
    def playInMain():
        if selected_track == -1:
            renpy.music.play(menu_music, "music", True)
        else:
            renpy.music.play(getNextTrack(), "music", True)

    def toTrack(num):
        global selected_track
        selected_track = num
        renpy.music.stop("dpa_music_player")
        renpy.music.queue(getSelectedTrackPath(), channel='dpa_music_player', loop=loop_track, clear_queue=True)
        setTrackName()

    def isNonePlaying():
        if renpy.music.get_playing("dpa_music_player") == None:
            getNextTrack()

    def nextTrack():
        updSTnPlay(1)
    
    def prevTrack():
        updSTnPlay(-1)

    def dpaPlLoop():
        dpaSetLoop(not loop_track)
    
    def dpaSetLoop(bool):
        global loop_track
        loop_track = bool

    def dpaSetLeavePl(bool):
        global leaveFromPlayer
        leaveFromPlayer = bool
    
    def randomFirst():
        if selected_track == -1:
            updSTnPlay(renpy.random.randint(1, len(dpa_music_list)))
    
    def resetDPAPlayer():
        global selected_track
        selected_track = -1
        global loop_track
        loop_track = False
        global track_name
        track_name = "Null"
        global nn_count
        nn_count = 0
        renpy.music.stop("dpa_music_player")


screen dpa_player:
    imagebutton xalign 0.365 ypos 150:
        auto getFile("image/screens/player/player_back_%s.png")
        action [Function(prevTrack)]
    imagebutton xalign 0.455 ypos 150:
        auto getFile("image/screens/player/player_play_%s.png")
        selected not renpy.music.get_pause("dpa_music_player")
        action [Function(randomFirst), PauseAudio("dpa_music_player", value="toggle")]
    imagebutton xalign 0.545 ypos 150:
        auto getFile("image/screens/player/player_next_%s.png")
        action [Function(nextTrack)]
    imagebutton xalign 0.635 ypos 150:
        auto getFile('image/screens/player/player_loop_%s.png')
        selected loop_track
        action [Function(dpaPlLoop)]
    text getSelectedTrackName():
        xalign 0.5 
        ypos 120
        size 30
    side "c":
        xalign 0.5
        ypos 300
        xysize (600, 600)

        default sdl_mus_bar_value = ui.adjustment()
        viewport id "vp_playlist":
            mousewheel True
            yadjustment sdl_mus_bar_value

            has vbox spacing 2

            for name in list(dpa_music_list):
                button:
                    xsize 600 
                    ysize 35
                    text getTrakName(name) xalign 0.5 size 30
                    action [Function(toTrack,(getTrackIndex(name)))]
    timer 0.1 repeat True action [Function(setTrackName), Function(isNonePlaying)]
    on "hide" action [Function(dpaSetLoop,False), Function(dpaSetLeavePl, True)]
    on "show" action [Function(dpaSetLeavePl, False)]
