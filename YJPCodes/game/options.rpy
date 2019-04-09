define config.name = _("YGGDRASIL JIGSAW PUZZLE")
define gui.show_name = True
define build_date = _("April 10, 2019")
define config.version = "1.0"
define config.hw_video = True
define config.gl_enable = True
define config.optimize_texture_bounds = True
define config.cache_surfaces = True
define config.image_cache_size_mb = 300
define config.framerate = 60
define config.manage_gc = True
define config.developer = False
define config.fast_skipping = False
define config.debug = False
define config.debug_sound = False
define config.autosave_on_quit = False
define config.has_autosave = False
define config.default_fullscreen = True
define config.save_on_mobile_background = False
define gui.about = _p("""
{color=#99ccff}© YGGDRASIL STUDIO Co, Pte.{/color} All Rights Reserved. All literary works/trademarks are property of their respective owners.
""")
define gui.ren_license = _p("""
This program contains free software under a number of licenses, including the MIT License and GNU Lesser General Public License. A complete list of software, including links to full source code, can be found {a=jump:renlicense}here{/a}.
""")
define gui.credits = _p("""
{color=#99ccff}CREDITS{/color}\n
{a=https://github.com/Lee-Yunseok}Lee Yunseok{/a} - Directing, Design, Programming, Music, Sound, Retouched CG, Packaging, Movie, Website

{a=https://renpy.org/}PyTom{/a} - Ren'Py Visual Novel Engine, Original Ren'Py Cardgame Framework

{a=https://lemmasoft.renai.us/forums/viewtopic.php?t=16151}SusanTheCat{/a} - Original Ren'Py Jigsaw Puzzle

{a=https://lemmasoft.renai.us/forums/viewtopic.php?t=16151#p294340}Alex{/a} - Improvement Ren'Py Jigsaw Puzzle

{a=https://pixabay.com/}Pixabay Community{/a} - Original Graphic Assets

{a=https://dejavu-fonts.github.io/}Bitstream, Inc.{/a} - DejaVu Sans
""")
define gui.code_license = _p("""
{color=#99ccff}YGGDRASIL JIGSAW PUZZLE\n
Copyright (C) 2019 YGGDRASIL STUDIO Co, Pte.{/color}

The {a=https://github.com/YGGDRASIL-STUDIO/YGGDRASIL-JIGSAW-PUZZLE}source codes of YGGDRASIL JIGSAW PUZZLE{/a} is covered by the terms of the {color=#99ccff}GNU Lesser General Public License v3.0{/color}.

                   {color=#99ccff}==========GNU LESSER GENERAL PUBLIC LICENSE=========={/color}\n
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. {a=https://fsf.org}<https://fsf.org/>{/a}
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

  This version of the GNU Lesser General Public License incorporates
the terms and conditions of version 3 of the GNU General Public
License, supplemented by the additional permissions listed below.

  {color=#99ccff}0. Additional Definitions.{/color}

  As used herein, "this License" refers to version 3 of the GNU Lesser
General Public License, and the "GNU GPL" refers to version 3 of the GNU
General Public License.

  "The Library" refers to a covered work governed by this License,
other than an Application or a Combined Work as defined below.

  An "Application" is any work that makes use of an interface provided
by the Library, but which is not otherwise based on the Library.
Defining a subclass of a class defined by the Library is deemed a mode
of using an interface provided by the Library.

  A "Combined Work" is a work produced by combining or linking an
Application with the Library.  The particular version of the Library
with which the Combined Work was made is also called the "Linked
Version".

  The "Minimal Corresponding Source" for a Combined Work means the
Corresponding Source for the Combined Work, excluding any source code
for portions of the Combined Work that, considered in isolation, are
based on the Application, and not on the Linked Version.

  The "Corresponding Application Code" for a Combined Work means the
object code and/or source code for the Application, including any data
and utility programs needed for reproducing the Combined Work from the
Application, but excluding the System Libraries of the Combined Work.

  {color=#99ccff}1. Exception to Section 3 of the GNU GPL.{/color}

  You may convey a covered work under sections 3 and 4 of this License
without being bound by section 3 of the GNU GPL.

  {color=#99ccff}2. Conveying Modified Versions.{/color}

  If you modify a copy of the Library, and, in your modifications, a
facility refers to a function or data to be supplied by an Application
that uses the facility (other than as an argument passed when the
facility is invoked), then you may convey a copy of the modified
version:

   a) under this License, provided that you make a good faith effort to
   ensure that, in the event an Application does not supply the
   function or data, the facility still operates, and performs
   whatever part of its purpose remains meaningful, or

   b) under the GNU GPL, with none of the additional permissions of
   this License applicable to that copy.

  {color=#99ccff}3. Object Code Incorporating Material from Library Header Files.{/color}

  The object code form of an Application may incorporate material from
a header file that is part of the Library.  You may convey such object
code under terms of your choice, provided that, if the incorporated
material is not limited to numerical parameters, data structure
layouts and accessors, or small macros, inline functions and templates
(ten or fewer lines in length), you do both of the following:

   a) Give prominent notice with each copy of the object code that the
   Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the object code with a copy of the GNU GPL and this license
   document.

  {color=#99ccff}4. Combined Works.{/color}

  You may convey a Combined Work under terms of your choice that,
taken together, effectively do not restrict modification of the
portions of the Library contained in the Combined Work and reverse
engineering for debugging such modifications, if you also do each of
the following:

   a) Give prominent notice with each copy of the Combined Work that
   the Library is used in it and that the Library and its use are
   covered by this License.

   b) Accompany the Combined Work with a copy of the GNU GPL and this license
   document.

   c) For a Combined Work that displays copyright notices during
   execution, include the copyright notice for the Library among
   these notices, as well as a reference directing the user to the
   copies of the GNU GPL and this license document.

   d) Do one of the following:

       0) Convey the Minimal Corresponding Source under the terms of this
       License, and the Corresponding Application Code in a form
       suitable for, and under terms that permit, the user to
       recombine or relink the Application with a modified version of
       the Linked Version to produce a modified Combined Work, in the
       manner specified by section 6 of the GNU GPL for conveying
       Corresponding Source.

       1) Use a suitable shared library mechanism for linking with the
       Library.  A suitable mechanism is one that (a) uses at run time
       a copy of the Library already present on the user's computer
       system, and (b) will operate properly with a modified version
       of the Library that is interface-compatible with the Linked
       Version.

   e) Provide Installation Information, but only if you would otherwise
   be required to provide such information under section 6 of the
   GNU GPL, and only to the extent that such information is
   necessary to install and execute a modified version of the
   Combined Work produced by recombining or relinking the
   Application with a modified version of the Linked Version. (If
   you use option 4d0, the Installation Information must accompany
   the Minimal Corresponding Source and Corresponding Application
   Code. If you use option 4d1, you must provide the Installation
   Information in the manner specified by section 6 of the GNU GPL
   for conveying Corresponding Source.)

  {color=#99ccff}5. Combined Libraries.{/color}

  You may place library facilities that are a work based on the
Library side by side in a single library together with other library
facilities that are not Applications and are not covered by this
License, and convey such a combined library under terms of your
choice, if you do both of the following:

   a) Accompany the combined library with a copy of the same work based
   on the Library, uncombined with any other library facilities,
   conveyed under the terms of this License.

   b) Give prominent notice with the combined library that part of it
   is a work based on the Library, and explaining where to find the
   accompanying uncombined form of the same work.

  {color=#99ccff}6. Revised Versions of the GNU Lesser General Public License.{/color}

  The Free Software Foundation may publish revised and/or new versions
of the GNU Lesser General Public License from time to time. Such new
versions will be similar in spirit to the present version, but may
differ in detail to address new problems or concerns.

  Each version is given a distinguishing version number. If the
Library as you received it specifies that a certain numbered version
of the GNU Lesser General Public License "or any later version"
applies to it, you have the option of following the terms and
conditions either of that published version or of any later version
published by the Free Software Foundation. If the Library as you
received it does not specify a version number of the GNU Lesser
General Public License, you may choose any version of the GNU Lesser
General Public License ever published by the Free Software Foundation.

  If the Library as you received it specifies that a proxy can decide
whether future versions of the GNU Lesser General Public License shall
apply, that proxy's public statement of acceptance of any version is
permanent authorization for you to choose that version for the
Library.
""")
define gui.renpy_license = _p("""
{color=#99ccff}Most of Ren'Py is covered by the terms of the following (MIT) license:{/color}

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation files
    (the "Software"), to deal in the Software without restriction,
    including without limitation the rights to use, copy, modify, merge,
    publish, distribute, sublicense, and/or sell copies of the Software,
    and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
    LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
    OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Portions of Ren'Py are derived from code that is licensed under the
GNU Lesser General Public License, so Ren'Py games must be distributed in a
manner that satisfies the LGPL.

Please see each individual source file for a list of copyright
holders. The artwork in the demo is released by various copyright
holders, under the same terms.

{color=#99ccff}Ren'Py binaries include code from the following projects:{/color}

- Python (Python License)\n
- Pygame_SDL2 (MIT License, GNU LGPL)\n
- SDL2 (Zlib License)\n
- SDL2_image (Zlib License)\n
- SDL2_ttf (Zlib License)\n
- Freetype (Zlib License)\n
- Fribidi (GNU LGPL)\n
- ffmpeg (GNU LGPL) (libav in some older versions, also GNU LGPL)\n
- libjpeg-turbo (GNU LGPL)\n
- libpng (PNG License)\n
- zlib (Zlib License)\n
- bzip2 (Bzip2 License)\n
- pyobjc (MIT License)\n
- py2exe (MIT License)\n
- GLEW (Modified BSD, MIT License)\n
- zsync (Artistic License)

{color=#99ccff}For the purposes of LGPL compliance, all source code that Ren'Py depends
on is located in one of the following repositories:{/color}

- {a=https://github.com/renpy/renpy}https://github.com/renpy/renpy{/a} (Ren'Py)\n
- {a=https://github.com/renpy/pygame_sdl2}https://github.com/renpy/pygame_sdl2{/a} (Pygame_SDL2)\n
- {a=https://github.com/renpy/renpy-deps}https://github.com/renpy/renpy-deps{/a} (Desktop dependencies)\n
- {a=https://github.com/renpy/python-for-android}https://github.com/renpy/python-for-android{/a} (Android)\n
- {a=https://github.com/renpy/rapt}https://github.com/renpy/rapt{/a} (Android Build Tools)\n
- {a=https://github.com/renpy/renios}https://github.com/renpy/renios{/a} (iOS)

Although we are unable to provide legal advice, we believe compliance can be
achieved by including a copy of this license with every copy of Ren'Py you
distribute, and linking to this license from your project's README file or
App Store description. We suggest using the wording:

    This program contains free software licensed under a number of licenses,
    including the GNU Lesser General Public License. A complete list of software
    is available at {a=http://www.renpy.org/doc/html/license.html}here{/a}.
""")
define gui.assets = _p("""
{color=#99ccff}==========Pixabay License=========={/color}

This is a human-readable summary of the {a=https://pixabay.com/service/terms/#license}Pixabay License (read the full text){/a}.

You can use all images and videos published on Pixabay for free (except as set out below). You may use them for commercial and non-commercial purposes, in altered and unaltered form. You don't need to ask permission from or provide credit to the image author or Pixabay, although it is appreciated when possible.

{color=#99ccff}What is not allowed?{/color}

This section only applies to image users and not to the appropriate image authors.

- Do not redistribute images or videos on other stock photo or wallpaper platforms.\n
- Identifiable people may not appear in a bad light or in a way that is offensive.\n
- Don't imply endorsement of your product by the image author or depicted persons or brands.\n
- Don't sell unamended or unaltered copies of an image or video, e.g. don't sell it as a stock photo, poster, print or on a physical product, without adding any value.

{color=#99ccff}Brands, products, and people in images and videos{/color}

Please note that some of the things depicted in the images and videos - such as identifiable people or logos - may have other rights such as copyright or trademarks that require consent or a license from a third party.

{color=#99ccff}==========DejaVu Sans=========={/color}

Fonts are (c) Bitstream (see below). DejaVu changes are in public domain.
Glyphs imported from Arev fonts are (c) Tavmjong Bah (see below)

{color=#99ccff}Bitstream Vera Fonts Copyright{/color}

Copyright (c) 2003 by Bitstream, Inc. All Rights Reserved. Bitstream Vera is
a trademark of Bitstream, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of the fonts accompanying this license ("Fonts") and associated
documentation files (the "Font Software"), to reproduce and distribute the
Font Software, including without limitation the rights to use, copy, merge,
publish, distribute, and/or sell copies of the Font Software, and to permit
persons to whom the Font Software is furnished to do so, subject to the
following conditions:

The above copyright and trademark notices and this permission notice shall
be included in all copies of one or more of the Font Software typefaces.

The Font Software may be modified, altered, or added to, and in particular
the designs of glyphs or characters in the Fonts may be modified and
additional glyphs or characters may be added to the Fonts, only if the fonts
are renamed to names not containing either the words "Bitstream" or the word
"Vera".

This License becomes null and void to the extent applicable to Fonts or Font
Software that has been modified and is distributed under the "Bitstream
Vera" names.

The Font Software may be sold as part of a larger software package but no
copy of one or more of the Font Software typefaces may be sold by itself.

THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OF COPYRIGHT, PATENT,
TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL BITSTREAM OR THE GNOME
FOUNDATION BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, INCLUDING
ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM OTHER DEALINGS IN THE
FONT SOFTWARE.

Except as contained in this notice, the names of Gnome, the Gnome
Foundation, and Bitstream Inc., shall not be used in advertising or
otherwise to promote the sale, use or other dealings in this Font Software
without prior written authorization from the Gnome Foundation or Bitstream
Inc., respectively. For further information, contact: fonts at gnome dot
org. 

{color=#99ccff}Arev Fonts Copyright{/color}

Copyright (c) 2006 by Tavmjong Bah. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining
a copy of the fonts accompanying this license ("Fonts") and
associated documentation files (the "Font Software"), to reproduce
and distribute the modifications to the Bitstream Vera Font Software,
including without limitation the rights to use, copy, merge, publish,
distribute, and/or sell copies of the Font Software, and to permit
persons to whom the Font Software is furnished to do so, subject to
the following conditions:

The above copyright and trademark notices and this permission notice
shall be included in all copies of one or more of the Font Software
typefaces.

The Font Software may be modified, altered, or added to, and in
particular the designs of glyphs or characters in the Fonts may be
modified and additional glyphs or characters may be added to the
Fonts, only if the fonts are renamed to names not containing either
the words "Tavmjong Bah" or the word "Arev".

This License becomes null and void to the extent applicable to Fonts
or Font Software that has been modified and is distributed under the 
"Tavmjong Bah Arev" names.

The Font Software may be sold as part of a larger software package but
no copy of one or more of the Font Software typefaces may be sold by
itself.

THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL
TAVMJONG BAH BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM
OTHER DEALINGS IN THE FONT SOFTWARE.

Except as contained in this notice, the name of Tavmjong Bah shall not
be used in advertising or otherwise to promote the sale, use or other
dealings in this Font Software without prior written authorization
from Tavmjong Bah. For further information, contact: tavmjong @ free
. fr.

$Id: LICENSE 2133 2007-11-28 02:46:28Z lechimp $
""")
define build.name = "YJP-codes"
define config.has_sound = True
define config.has_music = False
define config.has_voice = False
define config.mouse = None
define config.sample_sound = "pat.opus"
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.end_splash_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
define config.save_directory = "YJP-20190410"
default preferences.gl_framerate = 60
default preferences.gl_powersave = True
default preferences.text_cps = 0
default preferences.afm_time = 15
init python:
    build.exclude_empty_directories = True
    build.include_update = False
    build.allow_integrated_gpu = True
    build.archive("yjp", "all")
    build.classify("**~", None)
    build.classify("**/#**", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/**.rpy", None)
    build.classify("**/thumbs.db", None)
    build.classify("saves/**.**", None)
    build.classify("game/**.**", "yjp")