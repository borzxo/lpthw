class Song(object):
    func = "test"

    def __init__(self, lyrics, artist):
        self.lyrics = lyrics
        self.artist = artist


artist = Song("артист")
artist.sing_me()

happy_bday = Song("Не могу я тебе в день рождения",
"Дорогие подарки дарить",
"Но зато в эти ночи весенние ")
bulls_on_parade = Song("Далеко-далеко на лугу пасется кто?",
"Пейте, дети молоко, будете здороаы!")
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

one = Song("lol")
two = Song("kek")

one.sing_me_a_song()
two.sing_me_a_song()

three = "cheburek"
threee = Song(three)
threee.sing_me_a_song()
