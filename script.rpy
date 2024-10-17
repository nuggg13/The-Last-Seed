# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

image bg blck = "images/Solid_black.png"
image bg gurun = "images/Frame 3.png"
image bg terbengkalai = "images/Frame 4.png"
image bg kumuh = "images/Frame 5.png"
image bg lab = "images/Frame 6.png"
image bg tas = "images/frame 7.png"
image bg rumah = "images/Frame 8.png"

init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("beeping.mp3", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

# Deklarasikan karakter yang digunakan di game.
define r = Character('Raya', color="#00FFFF", callback=callback)
define t = Character('Timas', color="#00ff55", callback=callback)
define b = Character('Buto Ijo', color="#064606", callback=callback)


# Game dimulai disini.
label start:
    stop music fadeout 0.5

    # Deklarasi variabel tas_pertama dan tas_kedua
    $ tas_pertama = False
    $ tas_kedua = False

    scene bg blck with dissolve
    "Anda akan bermain sebagai Timun Mas, atau yang biasa dipanggil Timas"
    "seorang anak muda yang hidup di tengah reruntuhan kota, berjuang keras untuk bertahan hidup"
    "dimasa depan pasca-apokaliptik"
    "dunia telah mengalami kehancuran besar akibat perang nuklir dan bencana ekologis"
    "Tanah menjadi tandus, dan 80\% populasi manusia punah"
    "Di satu tempat yang dikenal sebagai AcT-0, konon dihuni oleh makhluk aneh bernama Buto Ijo yang memiliki sebuah Seed of Life"
    "Benih ini dikatakan sebagai satu-satunya harapan umat manusia"
    "untuk mengembalikan kehidupan dan keseimbangan di Bumi"

    "Di sebuah reruntuhan kota"
    "ada seorang anak bernama Timun Mas, yang sering dipanggil Timas, berjuang untuk bertahan hidup"
    "Suatu hari, dia menemukan sebuah dokumen lama pada sebuah mayat"
    "Di dalamnya, terdapat banyak data aneh seperti spesimen tumbuhan baru, percobaan benih tumbuhan pada manusia"
    "tetapi perhatian Timas tertuju pada dua dokumen: sebuah peta menuju AcT-0 dan informasi tentang spesimen tumbuhan bernama Seed of Life"
    "Setelah melihat dokumen tersebut, Timas menemui temannya yang seorang ilmuwan, bernama Raya"

    menu:
        "Raya, aku menemukan dokumen di gurun tadi":
            jump mulai
        "Raya, aku menemukan sebuah mayat":
            jump mulai

label mulai:
    # latar rumah
    scene bg rumah with dissolve
    t "Raya, aku menemukan sebuah mayat"

    show raya at left with dissolve
    r "jadi, kenapa?"

    show raya_dark at left with dissolve
    t "Ada sebuah dokumen yang menarik. Kamu mau melihatnya?"

    hide raya_dark with dissolve
    show raya at left with dissolve
    r "Dokumen? Hmmm, iya, aku mau lihat"
    r "Hmmm... AcT-0 dan Seed of Life, Jika apa yang tertulis di dokumen ini benar, kita bisa menyelamatkan umat manusia"

    show raya_dark at left with dissolve
    t "benar, sepertinya kita bisa mengembalikan kehidupan lagi"

    hide raya_dark with dissolve
    show raya at left with dissolve
    r "Kalau begitu, ayo kita pergi ke AcT-0 dan menemukan Seed of Life"

    show raya_dark at left with dissolve
    t "Kapan?"

    play sound "gun_sound.mp3"
    "Klik! (raya sedang memegang senjata)"
    stop sound

    t "Untuk apa pistol itu, Raya?"

    hide raya_dark with dissolve
    show raya at left with dissolve
    r "Untuk bundir kalau terjadi sesuatu. hehe!"

    menu:
        "Kayaknya aku gak jadi pergi deh":
            jump opsi1
        "Meskipun tidak ada tangan dan kaki, kita harus tetap melanjutkan hidup":
            jump opsi2

label opsi1:
    r "hehe, maaf"
    jump pilihtas

label opsi2:
    r "Hah, mending aku bunuh diri kalau seperti itu"
    jump pilihtas

label pilihtas:
    r "kamu udah siap-siap?"

    scene bg tas with dissolve
    menu:
        "Pilih tas pertama":
            $ tas_pertama = True
        "Piih tas kedua":
            $ tas_kedua = False

label perjalanan:
    scene bg gurun with dissolve
    "Keesokan harinya, Timas dan Raya pergi menaiki mobil dan memulai perjalanan mereka menuju AcT-0 dengan tujuan menyelamatkan umat manusia" 

    "Dalam perjalanan, Timun Mas dan Raya harus melewati tanah yang terkena radiasi"

    show raya at left with dissolve
    r "Ini, pakai pakaian anti-radiasi dulu"

    show raya_dark at left with dissolve
    t "Oke"

    "Mereka melanjutkan perjalanan sambil melewati tempat yang memiliki radiasi rendah dengan bantuan detektor radiasi"

    "Di tengah perjalanan, mereka melihat beberapa makhluk mutan"
    
    scene bg blck with dissolve
    t "Eh lihat itu, raya!"
    t "ada satu makhluk mutan seperti manusia, untung makhluk disini tidak mengejar ya"
    r "Mereka bukan hanya satu, Timas"

    play sound "tabrak.mp3" fadein 0.5
    "GLUKKK!!!"
    stop sound fadeout 0.5

    t "Ra! ngapain kamu nabrak makluk itu?"
    r "Gak sengaja! Lagi pula gak ngejar kan?"

    "makhluk yang ditabrak oleh raya berdiri dan mulai mengejar mobil mereka, diikuti oleh makhluk-makhluk lainnya"

    r "Iya"
    
    "raya mempercepat mobilnya hingga mereka masuk ke kawasan yang beradiasi tinggi"
    "dimana semakin banyak makhluk mutan muncul"

    play sound "drakk.mp3" fadein 0.5 
    "...."
    "DRAKKK!!!! DRAKKKK!!!! DRAKK!!!!!"
    stop sound 

    "Raya tidak peduli lagi, semua makhluk yang berada di depan ditabraknya"
    "hingga akhirnya, di peta terdapat dua rute"
    "melewati kota enitas atau melewati kota atlan"

    menu:
        "Aku dengar kota enitas adalah kota mati":
            jump kota1
        "Kota atlan... bukankah itu tempat asalmu dulu?":
            jump kota2

label kota1:
    scene bg terbengkalai with dissolve

    show raya at left with dissolve
    r "Aku baru mendengarnya"
    r "Ayoo kita ke kota enitas"

    "Mereka pun memasuki kawasan kota enitas, di mana gedung-gedung telah hancur"
    "Raya berhenti dan menyuruh timas untuk membuang pakaian anti-radiasi dan meninggalkan mobil"

    show raya_dark at left with dissolve
    t "Kenapa kita harus membuang baju dan meninggalkan mobil, raya?"

    hide raya_dark with dissolve
    show raya at left with dissolve
    r "Biar kita gak terpapar radiasi, Pakaian dan mobil kita sudah terkontaminasi"

    show raya_dark at left with dissolve
    t "Benarkah? jadi bagaimana sekarang?"

    hide raya_dark with dissolve
    show raya at left with dissolve
    r "Aku mau mencari mobil baru, Pasti ada di kota ini"

    scene bg blck with dissolve
    "Timas dan Raya pun mencari mobil baru sampai masuk ke beberapa rumah"
    "Di salah satu rumah, Timas terkejut melihat seorang manusia terkurung dalam sebuah penjara"

    t "HAAAA! RAYA!"
    r "HAAAAA! Aku tidak percaya ini"
    t "Apa yang harus kita lakukan ini?"
    r "Kita biarkan saja. Dia sudah tidak bisa apa-apa lagi. Kaki dan tangannya sudah tidak ada"
    t "Kok dibiarkan? Kita sama saja menyiksanya"

    play sound "pistol-shot.mp3"
    "DORRRR!!!!"
    stop sound

    r "MAAFF!!!!"
    r "Tapi tidak ada pilihan lain selain mengakhiri penderitaannya"

    "Timas terdiam, dan Raya melanjutkan pencarian mobil. Setelah menemukan mobil, mereka melanjutkan perjalanan, tetapi Timas masih terdiam"

    r "Maafkan aku timas, karena tiba-tiba menembaknya"

    menu:
        "Enggak apa-apa":
            jump mausampai
        "Iya, tembakan yang bagus":
            jump mausampai

label mausampai:
    t "Aku cuma kepikiran, kenapa dia dikurung?"
    r "Sepertinya dia dipelihara untuk dimakann..."
    t "Pasti dia sangat menderita selama ini"
    r "........."
    jump sampai

label kota2:
    show raya at left with dissolve
    r "Iya, tempat ini adalah tempat di mana orang-orang kaya yang dapat bertahan"

    "Mereka pun menuju Kota Atlan. Setelah sampai di kota tersebut"
    "sebelum masuk ke dalamnya"
    "Raya menyuruh Timas untuk meninggalkan mobil dan membuang pakaian anti-radiasinya"
    
    show raya_dark at left with dissolve
    t "Mobilnya mau kamu buang juga?"

    hide raya_dark with dissolve
    show raya at left with dissolve
    r "Iya, tadi kita lewat area radiasi yang tinggi, jadi mobil itu telah terpapar radiasi"

    show raya_dark at left with dissolve
    t "Jadi kita harus cari mobil baru lagi?"

    hide raya_dark with dissolve
    show raya at left with dissolve
    r "Iya, tapi tidak akan sulit mencari mobil di sini"

    scene bg kumuh with dissolve
    "Mereka pun masuk ke dalam kota, dan melihat pemukiman kumuh di mana banyak orang kelaparan"
    "Tiba-tiba, ada seseorang yang menghampiri Timas dan Raya"

    show orang_aneh at right with dissolve
    "Orang aneh" "Hei, nona-nona, kalian baru datang ke sini kan? Apakah kalian lapar? Mau membeli tangan saya ini?"

    show raya at left with dissolve
    r "Maaf, kami tidak lapar"

    "Orang aneh" "Eh, tapi..."
    hide orang_aneh with dissolve

    show raya_dark at left with dissolve
    t "Raya, apa maksudnya dia ingin menjual tangannya untuk kita makan?"

    hide raya_dark with dissolve
    show raya at left with dissolve
    r "Di pemukiman ini, banyak orang yang menjual bagian tubuhnya untuk membayar hutang atau untuk bertahan hidup"

    show raya_dark at left with dissolve
    t "Sangat tidak manusiawi..."

    hide raya_dark with dissolve
    show raya at left with dissolve
    r "Tidak heran, setelah perang nuklir menghilangkan hampir seluruh populasi makhluk hidup, hanya orang-orang kaya yang bisa bertahan hidup sekarang"

    scene bg blck with dissolve
    "Mereka pun terus berjalan dan memasuki pemukiman orang-orang elit yang terlihat berbeda sekali dari pemukiman sebelumnya"
    "Di sini lebih bersih. Raya lalu menuju seseorang yang baru turun dari mobil"

    r "Hei, maukah kamu bertukar mobil denganku?"
    "Orang mobil" "Hah? Bertukar mobil? Untuk apa? Aku tidak mau"
    r "Aku bisa menambahkan sejumlah uang jika kamu mau"
    "orang mobil" "Hmm, sepertinya bisa kupikirkan"

    "Raya pun melakukan kesepakatan dan mendapatkan mobil baru dari orang tersebut, lalu mereka melanjutkan perjalanan"
    jump sampai


label sampai:
    "Setelah perjalanan panjang, Timun Mas dan Raya akhirnya mencapai AcT-0"
    "Begitu mereka menginjakkan kaki, mereka langsung bertemu dengan makhluk besar berwarna hijau yang dikenal sebagai Buto Ijo"

    t "Itu adalah salah satu makhluk mutan yang aku lihat di dokumen. Namanya Buto Ijo"
    r "Ya, mereka sangat agresif dan tidak pandang bulu"

    "Raya dengan cepat meraih tasnya dan melemparkan molotov ke arah Buto Ijo, lalu mereka berlari dengan sangat cepat"

    t "Cepat, Raya, lewat sini!"
    r "Eh, ada tiga, bukan sembilan Buto Ijo"

    "Timas dan Raya Terus berlari, menuju sebuah pintu dan memasuki ruangan. Di dalam ruangan itu, mereka menemukan berbagai macam tumbuhan"
    "Namun, dari pintu lain muncul Buto Ijo yang membuat mereka panik"

    scene bg lab with dissolve
    show buto_ijo at right with dissolve
    b "Oh, kamu sudah pulang ya, Timun Mas"

    show raya_kaget at left with dissolve
    r "Eh... Apa?"
    r "Kamu kenal Buto Ijo ini, Timas?"

    "Raya terlihat bingung dan terkejut"

    menu:
        "Ya, Dia yang yang menciptakan ku!":
            jump end
        "Ya, Dia adalah ayahku":
            jump end

label end:
    scene bg blck with dissolve
    r "Haa, Kamu itu manusia kan?"
    b "Sebenarnya, kami dulunya ilmuwan. Kami sedang mengembangkan sebuah seed yang bisa mengembalikan kehidupan dunia seperti semula"
    b "Namun, bocornya radiasi mengubah kami menjadi seperti ini"
    r "Lalu kenapa kamu berbeda?"
    b "Aku bertahan karena segera menyadari mutasi yang terjadi pada tubuhku dan mencegah agar kesadaranku tidak hilang"
    t "Bagaimana dengan Seeds of Life?"
    b "HAHA... Sabar dong teman mu ini masih kebingungan, intinya Timas adalah eksperimen kami, wadah yang sempurna untuk 'Seeds of Life'"
    r "Apa maksudnya ini, Timas? Apa yang dia bicarakan?"
    t "Maafkan aku, Raya... Sebenarnya, aku bukan menemukan dokumen itu dari mayat di gurun"
    t "Itu adalah dokumen lama yang sudah lama kusimpan. Aku tahu tentang 'Seeds of Life' sejak dulu"
    r "Jadi, selama ini kau tahu... bahwa kau akan berakhir seperti ini?"
    t "Ya, Raya. Tapi aku tak bisa melakukannya sendirian. Aku butuhmu di sisiku, sampai akhir"

    if tas_pertama:
        # Ending pertama dengan pilihan tas pertama
        jump end_game_1
    else:
        # Ending pertama dengan pilihan tas kedua
        jump end_game_2

label end_game_1:
    scene bg blck with dissolve
    t "Tetapi setelah melihat apa yang terjadi didunia ini"

    "Timas mengambil sesuatu dari tasnya dan DOORRRR!!! Timas menembak kapsul tersebut"

    t "Aku sudah tidak menginginkan seed itu lagi"
    t "Manusia tidak layak diperjuangkan lagi. Mereka akan tetap mengulangi kesalahan yang sama"
    t "Percuma memperjuangkan mereka"

    "Timas mengarahkan pistolnya ke kepalanya"

    t "Kamu benar, Raya. Pistol ini untuk keadaan seperti ini"
    r "Apa yang kamu lakukan, Timas?"
    t "Ayo ikut bersamaku. Untuk apa hidup di dunia ini?"

    play sound "pistol-shot.mp3"
    "DOORRRR!!!"
    stop sound

    play sound "gun_sound.mp3"
    "Cklik"
    stop sound

    play sound "pistol-shot.mp3"
    "DOORRRR"
    jump tamat


label end_game_2:
    scene bg blck with dissolve
    "Timas mengambil sesuatu dari tasnya dan memberikannya kepada Raya"

    t "Kalau begitu, tolong jaga dan rawat aku ya"
    r "Timas, kamu serius?!"

    "Timas langsung mengambil seed itu dan menyuntikannya ke tubuhnya"

    r "TIMASSSSS!"
    t "Selamat tinggal, Raya. Terima kasih atas segalanya"

    "50 Tahun Kemudian"
    "Pohon tersebut memberikan kehidupan kembali kepada dunia. Semua orang hidup tenang dan damai di sekitar pohon itu"
    "Tanah menjadi subur kembali, muncul tanaman-tanaman baru, dan banyak hewan yang telah dinyatakan punah berkembang biak di sana"
    jump tamat

label tamat:
    "tamat"







    return

