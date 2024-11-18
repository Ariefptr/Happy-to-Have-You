# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Itsuka", color="#8e82fe", who_bold=True, who_outlines=[(1, "#000")])
define t = Character("Tohka", color="#ca0147", who_bold=True, who_outlines=[(1, "#000")])
define s = Character("Suna", color="#ee520e", who_bold=True, who_outlines=[(1, "#000")])
define u = Character("????" , color= "#1b1919ff", who_bold=True, who_outlines=[(1, "#000")])

image pagi = im.Scale("pagi.jpg",1280,720)
image kota = im.Scale("kota.jpg",1280,719)
image klas = im.Scale("klas.png",1280,720)
image sekolah = im.Scale("sekolah.jpg",1280,719)
image gang = im.Scale("gang.jpg",1280,720)
image lorong = im.Scale("lorong.jpg", 1280,719)
image restoran = im.Scale("restoran.jpg", 1280, 720)
image sore = im.Scale("sore.jpg", 1280,719)
image malam = im.Scale("malam.jpg", 1280, 719)
image toilet = im.Scale("toilet.jpg", 1280, 720)
image splash1 = im.Scale("splash1.png", 1280,717)

default rajin = 0
default pemalas = 0
default cinta = 0
default sangatcinta = []


# The game starts here.
style screentext:
    color"#3aa1eb"
    size 18

style game_tb:
    size 16
    background Frame("images/Icon/button_idle.png",0,0)
    hover_background Frame("images/Icon/button_hover.png",0,0)
    xsize 120 ysize 40

style game_bc:
    size 12
    background Frame("images/Icon/button_out.png",0,0)
    hover_background Frame("images/Icon/button_out1.png",0,0)
    xsize 60 ysize 35


init python:
    
    def piece_dragged(drags, drop):
        
        if not drop:
            return
        
        p_x = drags[0].drag_name[0]
        p_y = drags[0].drag_name[1]
        t_x = drop.drag_name[0]
        t_y = drop.drag_name[1]
        
        if p_x == t_x and p_y == t_y:
            renpy.music.play("click.ogg", channel="sound")
            my_x = int(p_x)*100+25
            my_y = int(p_y)*100+25
            drags[0].snap(my_x,my_y)
            drags[0].draggable = False
            placedlist[int(p_x),int(p_y)] = True
            for i in range(6):
                for j in range(4):
                    if placedlist[i,j] == False:
                        return
            return True
        return

screen minigame:

    draggroup:

        for i in range(6):
            for j in range(4):
                $ name = "%s%s"%(i,j)
                $ my_x = i*100+50
                $ my_y = j*100+50
                drag:
                    drag_name name
                    child "blanks_space.png"
                    draggable False
                    xpos my_x ypos my_y
            
            
        for i in range(6):
            for j in range(4):
                $ name = "%s%s piece"%(i,j)
                drag:
                    drag_name name
                    child imagelist[i,j]
                    droppable False
                    dragged piece_dragged
                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]

label puzzle:
    call screen minigame
    jump menang


label splashscreen:
    scene black
    $renpy.pause(1.0, hard=True)
    show splash with dissolve:
        xalign 0.5
        yalign 0.5
    $renpy.pause(3.0, hard=True)
    hide splash with dissolve
    $renpy.pause(2.0, hard=True)

    scene black
    $renpy.pause(1.0, hard=True)
    show splash2 with dissolve:
        xalign 0.5
        yalign 0.5
    $renpy.pause(3.0, hard=True)
    hide splash1 with dissolve
    $renpy.pause(2.0, hard=True)

    return

    
label start:
    play sound "click.ogg"
    play music "morning.mp3"
    queue music "morning.mp3"
    scene pagi

    "Pagi hari yang cerah...."
    play sound "bird.mp3" fadeout 1.0
    "Dimana matahari begitu indah saat terbit, ditemani merdunya suara kicauan burung..."
    "Namaku Itsuka. Aku adalah salah satu siswa kelas tahun pertama di High School."
    "Aku adalah siswa yang cukup terkenal dan cukup populer di sekolah karena sering berkenalan."
    "Banyak siswa yang menjauhiku, tetapi tidak untuk siswi yang aku suka bernama Tohka."
    stop sound fadeout 1.0
    scene black
    with dissolve
    jump part1

label part1:
    scene kota
    with dissolve
    show i1 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Wah pagi hari ini udaranya sejuk sekali, jadi makin semangat nih untuk berangkat ke sekolah"
    with dissolve
    hide i1
    show i2 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Walaupun jalan kaki... tapi ini cukup menyenangkan daripada naik kendaraan"
    hide i2
    show i5 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Jalanan di kota ini begitu ramai dan padat seperti biasanya"
    stop music
    hide i5
    show i4 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    play sound "cat.mp3"
    "*Melihat seekor kucing dijalan....."
    hide i4
    play music "morning.mp3"

    show i3 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    play sound "cat 1.mp3"
    "*Sedang mengelus-elus kucing jalanan....!"
    hide i3
    show i1 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    menu:
        "Enaknya kita bermain dulu dengan kucing atau langsung pergi ke sekolah ya?"
        "Bermain dengan kucing":
            hide i1
            play sound "click.ogg"
            scene gang
            with fade
            play music "happy.mp3" fadeout 1.4
            play sound "cat 1.mp3"
            "(meooooww....)"
            show i1 at left:
                zoom 0.46 xalign 0.07 yalign 0.39
            with dissolve
            k "Halo mpuss.... lucu banget kucingnya jadi pengen pelihara!"
            hide i1
            show i3 at left:
                zoom 0.46 xalign 0.07 yalign 0.39
            k "Tapi nanti aja deh bawa pulangnya setelah aku sudah pulang sekolah, semoga mpus masih ada disini"
            hide i3
            with dissolve
            "Itsuka terus saja bermain dengan kucing sehingga tidak melihat waktu," 
            extend " dan pada akhirnya itsuka terburu-buru ke sekolah namun masuk terlambat" 
            $pemalas += 1
        "Pergi ke sekolah":
            play sound "click.ogg"
            show i1 at right:
                zoom 0.46 xalign 0.97 yalign 0.39
            k "Sepertinya aku harus ke sekolah sebelum terlambat"
            hide i1
            with dissolve
            "(Berlari menuju sekolah.....)"
            scene sekolah
            with fade
            show i6 at right:
                zoom 0.46 xalign 0.97 yalign 0.39
            k "Aduh!! capek banget aku lari untung aja udah sampai di depan pintu gerbang sekolah"
            hide i6
            show i2 at right:
                zoom 0.46 xalign 0.97 yalign 0.39
            k "Langsung masuk aja deh sebelum kelas dimulai"
            hide i2
            with dissolve
            $rajin += 1        
    scene black
    stop music
    with dissolve
    jump part2

label part2:
    play music "love.mp3"
    scene lorong
    with dissolve

    show i4 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Gawat!! di lorong sudah pada sepi saya harus masuk ke kelas sekarang"
    hide i4
    show t4 at left:
        zoom 0.46 yalign 0.39
    t "Eh, kamu telat itsuka?"
    show s6 at left:
        zoom 0.46 xalign 0.24 yalign 0.39
    s "Halo itsuka."
    show i3 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Iya aku sedikit telat tohka. Halo juga suna"
    hide t4
    with dissolve
    hide s6
    with dissolve
    show s4 at left:
        zoom 0.46 xalign 0.09 yalign 0.39
    s "Aku baru pertama kali melihat kamu telat ke sekolah, apa yang membuat kamu telat itsuka?"
    hide i3
    hide s4
    show i2 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Itu rahasia, ceritanya panjang"
    hide i2
    show s3 at left:
        zoom 0.46 xalign 0.09 yalign 0.39
    s "Kamu selalu bilang seperti itu saat aku bertanya!!, tapi giliran sama tohka kamu selalu saja asik berduaan"
    hide s3
    show s5 at left:
        zoom 0.46 xalign 0.09 yalign 0.39
    s "Lebih baik aku ke kelas aja deh gak mau jadi nyamuk, dah aku duluan"
    hide s5
    with dissolve
    show i4 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Ada apa dengan suna?"
    hide i4
    show t6 at left:
        zoom 0.46 xalign 0.09 yalign 0.39
    t "Entahlah, aku juga tidak tau kenapa suna akhir-akhir ini suka menjauh dari kita"
    t "Aku pikir dia cemburu kalau kita sering asik berduaan itsuka"
    hide t6
    show i2 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Bisa jadi, sudahlah biarkan saja"
    hide i2
    show t4 at left:
        zoom 0.46 xalign 0.09 yalign 0.39
    t "Mari masuk ke kelas itsuka, guru sudah ada didalam kelas"
    hide t4
    show i4 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Guru sudah ada didalam kelas?"
    hide i4
    show t4 at left:
        zoom 0.46 xalign 0.09 yalign 0.39
    t "Iya sudah ada, makanya cepat masuk nanti kamu bisa kena hukuman loh itsuka"
    hide t4
    show i5 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Aduh!! jangan sampai aku kena hukuman lagi, aku langsung masuk ke kelas aja deh"
    hide i5
    with dissolve
    hide t2
    with dissolve
    menu:
        "Yakin kamu ingin masuk ke kelas atau ingin kena hukuman?"
        "Masuk ke kelas":
            play sound "click.ogg"
            scene klas
            with fade
            show i6 at left:
                zoom 0.46 xalign 0.09 yalign 0.39
            k "Untung saja aku gak kena hukuman lagi, tapi semua baik-baik saja sih"
            hide i6
            show i2 at left:
                zoom 0.46 xalign 0.09 yalign 0.39
            k "Kebetulan pelajaranya baru dimulai sekarang"
            hide i2
            $rajin +=1
        "Bolos ke toilet":
            play sound "click.ogg"
            scene toilet
            with fade
            show i6 at left:
                zoom 0.46 xalign 0.09 yalign 0.39
            k "Mending bolos satu pelajaran aja deh, malas juga pelajaran pertamanya matematika"
            hide i6
            show i2 at left:
                zoom 0.46 xalign 0.09 yalign 0.39
            k "Di toilet sekolah juga sepi jadi bisa santai dulu disini, semoga aja tidak ada siswa yang tau kalau aku bolos di toilet"
            hide i2
            show i6 at left:
                zoom 0.46 xalign 0.09 yalign 0.39
            k "Bisa gawat kalau aku ketauan bolos disini"
            hide i6
            "Gak lama kemudian itsuka ketauan oleh guru dan masuk ke BK"
            jump kalah
            $pemalas +=1
    scene black
    stop music
    "MARI KITA SELESAIKAN PUZZLE NYA!!"
    image whole = "restoran1.jpg"
    image whole1 = "Lose.png"
    play music "love.mp3"
    scene klas
    python:
        pajel = im.Composite((650, 450),(25, 25), "restoran1.jpg")
        piecelist = dict()
        imagelist = dict()
        placedlist = dict()
        for i in range(6):
            for j in range(4):
                piecelist[i,j] = [renpy.random.randint(0, 600)+600, renpy.random.randint(0, 480)]
                tempimage = im.AlphaMask(pajel,"pieces_puzzle/%s_%s.png"%(j+1,i+1))
                imagelist[i,j] = im.Crop(tempimage, i*100,j*100, 150, 150)
                placedlist[i,j] = False
    jump puzzle

label menang:
    scene black
    show whole at Position(xalign=0.5,yalign=0.5)
    stop music
    play sound "victory.mp3"
    "PUZZLE BERHASIL TERPECAHKAN"
    stop sound
    $rajin +=1
    jump part3

label kalah:
    scene black
    show whole1 at Position(xalign=0.5,yalign=0.5)
    play sound "gagal.mp3"
    $pemalas +=1
    menu:
        "Main lagi?"
        
        "Ya":
            jump part2
            
        "Tidak":
            return

label part3:
    play music "love.mp3"
    scene lorong
    with dissolve
    
    show i2 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Akhirnya pelajaran sudah berakhir sungguh melelahkan, sekarang waktunya pulang"
    hide i2
    show i1 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Oh iya apakah kucing yang tadi pagi masih ada, seharusnya sih masih ada"
    hide i1
    scene sore
    with dissolve
    show i6 at right:
        zoom 0.46 xalign 0.97 yalign 0.39
    k "Yah!! kucing nya sudah pergi padahal mau aku pelihara"












            



            





    # This ends the game.

    return
