#################################################################################################################################
#                                                                                                                               #
#          If you want to sell your MOD in Steam with the form of DLC, please contact to yggdrasilgamestudio@gmail.com.         #
#          We welcome Photographers, Illustrators, Musicians, and all INDIE creators who wish to collaborate with us.           #
#                                                                                                                               #
#################################################################################################################################

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
    if persistent.play_mods == "sample":
        jigsaw = random_list("sample_images/")
define sample_scr = 0
image sample = "sample_header.webp"
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
                label _("Random Play")
                style_prefix "radio"
                textbutton _("On") action [SetField(persistent, "play_mods", "sample"), renpy.reload_script]
                textbutton _("Off") action [SetField(persistent, "play_mods", None), renpy.reload_script]
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
                            imagebutton idle im.Grayscale("sample_images_small/"+i) hover im.Grayscale("sample_images_small/"+i) hover_background "#99ccff" action [SetVariable("gview", "sample_images/"+i), SetVariable("mods", "sample"), Jump("start")] xsize 324 ysize 184
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