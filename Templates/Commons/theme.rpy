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
    mod_name.append("MOD name")
    mod_desc.append("MOD description")
    mod_image.append("sample")
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
define sample_scr = 0
image sample = "sample_header.webp"
screen sample():
    $ mods = None
    tag menu
    use game_menu(_("MOD name"), scroll="viewport"):
        vbox:
            hbox:
                textbutton _("Theme") action SetVariable("sample_scr", 0)
                textbutton _("Credits") action SetVariable("sample_scr", 1)
                textbutton _("License") action SetVariable("sample_scr", 2)
            null height (2 * gui.pref_spacing)
        if sample_scr == 0:
            vbox:
                add "sample_theme.webp"
                label _("Theme Set")
                style_prefix "radio"
                textbutton _("On") action [SetField(persistent, "themes", "sample"), renpy.reload_script]
                textbutton _("Off") action [SetField(persistent, "themes", None), renpy.reload_script]
                null height gui.pref_spacing
                text _([theme_set])
        if sample_scr == 1:
            text _p("""
            {a="your_url"}Your Name{/color} - Your part in credits

{color=#99ccff}Contributor Name(no link url){/color} - Part in credits

{a=""}Contributor Name{/a} - Part in credits
""")
        if sample_scr == 2:
            text _p("""
            Your licenses goes here.
""")