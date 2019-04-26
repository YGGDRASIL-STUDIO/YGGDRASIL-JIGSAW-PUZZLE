#################################################################################################################################
#                                                                                                                               #
#          If you want to sell your MOD in Steam with the form of DLC, please contact to yggdrasilstudio@protonmail.com.         #
#          We welcome Photographers, Illustrators, Musicians, and all INDIE creators who wish to collaborate with us.           #
#                                                                                                                               #
#################################################################################################################################

########## This file combines each sample into a single file, assuming all MOD assets are ready. ##########
########## Replace all >>> sample <<< to your special name that start with english. ##########
########## Replace all >>> MOD name <<< to your real MOD name. ##########
########## Replace >>> MOD description <<< to your real MOD description. ##########
########## Replace all >>> your_url <<< to your real web URL that can represent you. ##########
########## Scroll down and look for starting with '#', then follow the text. ##########
########## After all, find >>> Your Name <<< and write credits, find >>> Your licenses <<< and write MOD license. ##########
init -1 python:
    import re
    def random_list(dir=""):
        list = renpy.list_files()
        rv = []
        for f in list:
            if re.match(dir,f):
                rv.append(dir+f[(len(dir)):])
        return rv
    def file_list(dir=""):
        list = renpy.list_files()
        rv = []
        for f in list:
            if re.match(dir,f):
                rv.append(f[(len(dir)):])
        return rv
    mod_name.append("MOD name")
    mod_desc.append("MOD description")
    mod_image.append("sample")
    sample = file_list("sample_images/")
    if persistent.themes == "sample":
        persistent.open_src = "sample_opening.webp"
        persistent.mainbg_src = "sample_bg.webp"
        persistent.menubg_src = im.Blur("sample_bg.webp", 3)
        persistent.frame_src = "sample_frame.webp"
        persistent.mbottom_src = "sample_bottom.webp"
        persistent.pbottom_src = "sample_bottom.webp"
        persistent.gbottom_src = "sample_bottom.webp"
        first_text = "MOD name"
        first_url = "your_url"
    if persistent.play_mods == "sample":
        jigsaw = random_list("sample_images/")
    if persistent.obsplay == "sample":
        obs_src = "sample_obs"
    if persistent.obsex == "sample":
        obs1 = "sample_obs1"
        obs2 = "sample_obs2"
        obs3 = "sample_obs3"
    if persistent.obsse == 1:
        obsse0 = "sample_sfx_0.opus"
        obsse1 = "sample_sfx_1.opus"
        obsse2 = "sample_sfx_2.opus"
        obsse3 = "sample_sfx_3.opus"
    if persistent.obsseex == "sample":
        obsse4 = "sample_sfx_4.opus"
        obsse5 = "sample_sfx_5.opus"
        obsse6 = "sample_sfx_6.opus"
    if persistent.sample_music is True:
        ########## Replace music files below. ##########
        playlist.append("sample_music_01.opus")
        playlist.append("sample_music_02.opus")
        playlist.append("sample_music_03.opus")
        ################################################
    if persistent.patsound == "sample":
        patsound = "sample_click.opus"
    if persistent.picksound == "sample":
        picksound = "sample_hover.opus"
    if persistent.endsound == "sample":
        winsound = "sample_win.opus"
        gosound = "sample_go.opus"
define sample_scr = 0
default persistent.sample_music = None
image sample = "sample_header.webp"
########## Replace this image defines below to your Obstacle images. ##########
image sample_obs = SnowBlossom("sample_obstacle.webp", count=50, yspeed=(100, 200))
image sample_obs1 = SnowBlossom("sample_obstacle1.webp", count=50, yspeed=(100, 200))
image sample_obs2 = SnowBlossom("sample_obstacle2.webp", count=50, yspeed=(100, 200))
image sample_obs3 = SnowBlossom("sample_obstacle3.webp", count=50, yspeed=(100, 200))
###############################################################################
screen sample():
    $ mods = None
    tag menu
    use game_menu(_("MOD NAME"), scroll="viewport"):
        vbox:
            hbox:
                textbutton _("Theme") action SetVariable("sample_scr", 0)
                textbutton _("Gallery") action SetVariable("sample_scr", 1)
                textbutton _("Credits") action SetVariable("sample_scr", 2)
                textbutton _("License") action SetVariable("sample_scr", 3)
            null height (2 * gui.pref_spacing)
        if sample_scr == 0:
            vbox:
                add "sample_theme.webp"
                hbox:
                    vbox:
                        label _("Theme Set")
                        style_prefix "radio"
                        textbutton _("On") action [SetField(persistent, "themes", "sample"), renpy.reload_script]
                        textbutton _("Off") action [SetField(persistent, "themes", None), renpy.reload_script]
                    vbox:
                        label _("Random Play")
                        style_prefix "radio"
                        textbutton _("On") action [SetField(persistent, "play_mods", "sample"), renpy.reload_script]
                        textbutton _("Off") action [SetField(persistent, "play_mods", None), renpy.reload_script]
                    vbox:
                        label _("Sound Set")
                        style_prefix "check"
                        textbutton _("Music") selected persistent.sample_music == True action If(persistent.sample_music == True, true=[SetField(persistent, "sample_music", None), renpy.music.stop, renpy.reload_script], false=[SetField(persistent, "sample_music", True), renpy.music.stop, renpy.reload_script])
                        textbutton _("Sound") selected persistent.patsound == "sample" action If(persistent.patsound == "sample", true=[SetField(persistent, "patsound", None), SetField(persistent, "picksound", None), SetField(persistent, "endsound", None), renpy.reload_script], false=[SetField(persistent, "patsound", "sample"), SetField(persistent, "picksound", "sample"), SetField(persistent, "endsound", "sample"), renpy.reload_script])
                    vbox:
                        label _("Obstacle Set")
                        style_prefix "radio"
                        textbutton _("On") action [SetField(persistent, "obsplay", "sample"), SetField(persistent, "obsex", "sample"), SetField(persistent, "obsse", 1), SetField(persistent, "obsseex", "sample"), renpy.reload_script]
                        textbutton _("Off") action [SetField(persistent, "obsplay", None), SetField(persistent, "obsex", None), SetField(persistent, "obsse", 0), SetField(persistent, "obsseex", None), renpy.reload_script]
            null height gui.pref_spacing
            text _([theme_set])
        if sample_scr == 1:
            vbox:
                ########## Edit grid to the number of you puzzle images. Default number 4*2 = 8. ##########
                grid 4 2:
                ###########################################################################################
                    xfill True
                    yspacing 25
                    for i in sample:
                        if renpy.seen_image("sample_images/"+i):
                            imagebutton idle "sample_images_small/"+i hover "sample_images_small/"+i hover_background "#99ccff" action [SetVariable("gview", "sample_images/"+i), SetVariable("gfull", "sample_images_full/"+i), SetVariable("mods", "sample"), ShowMenu("sample_nav")] xsize 324 ysize 184
                        else:
                            imagebutton idle im.Grayscale("sample_images_small/"+i) hover im.Grayscale("sample_images_small/"+i) hover_background "#99ccff" action [SetVariable("gview", "sample_images/"+i), SetVariable("mods", "sample"), ShowMenu("sample"), Jump("start")] xsize 324 ysize 184
        if sample_scr == 2:
            text _p("""
            {a="your_url"}Your Name{/color} - Your part in credits

{color=#99ccff}Contributor Name(no link url){/color} - Part in credits

{a=""}Contributor Name{/a} - Part in credits
""")
        if sample_scr == 3:
            text _p("""
            Your licenses goes here.
""")
screen sample_nav():
    tag menu
    style_prefix "main_menu"
    add "[gfull]"
    add "gall_bottom" size(1920,216) ypos 864
    vbox:
        button action OpenURL("your_url"):
            text "MOD NAME":
                style "main_menu_title" size 48
        text "[config.name!t]\n© YGGDRASIL STUDIO":
            style "main_menu_version"
    hbox align(.03,.957):
        textbutton _("Return") action [SetVariable("gview", None), SetVariable("gfull", None), SetVariable("mods", None), ShowMenu("sample")]
        textbutton _("Replay") action [SetVariable("chosen_img", gview), SetVariable("replay_j", True), Jump("start")]
    key "pad_y_press" action [SetVariable("chosen_img", gview), SetVariable("replay_j", True), Jump("start")]