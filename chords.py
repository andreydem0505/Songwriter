class Chord:
    def __init__(self, keys, neighbours):
        # ноты, из которых состоит аккорд
        self.keys = keys
        # соседи по квинтовому кругу
        self.neighbours = neighbours


chords = {
    "A": Chord(['A', 'C#', 'E'], ['D', 'F#m', 'E', 'Bm', 'C#m']),
    "B": Chord(['B', 'D#', 'F#'], ['E', 'G#m', 'Gb', 'Ebm', 'C#m']),
    "C": Chord(['C', 'E', 'G'], ['G', 'Am', 'F', 'Em', 'Dm']),
    "D": Chord(['D', 'F#', 'A'], ['G', 'A', 'Bm', 'Em', 'F#m']),
    "E": Chord(['E', 'G#', 'B'], ['A', 'B', 'C#m', 'F#m', 'G#m']),
    "F": Chord(['F', 'A', 'C'], ['C', 'Bb', 'Dm', 'Am', 'Gm']),
    "G": Chord(['G', 'B', 'D'], ['D', 'C', 'Em', 'Bm', 'Am']),
    "Bb": Chord(['A#', 'D', 'F'], ['F', 'Eb', 'Gm', 'Dm', 'Cm']),
    "Eb": Chord(['D#', 'G', 'A#'], ['Cm', 'Bb', 'Ab', 'Gm', 'Fm']),
    "Ab": Chord(['G#', 'C', 'D#'], ['Fm', 'Eb', 'Db', 'Cm', 'Bbm']),
    "Db": Chord(['C#', 'F', 'G#'], ['Ab', 'Gb', 'Bbm', 'Fm', 'Ebm']),
    "Gb": Chord(['F#', 'A#', 'C#'], ['Ebm', 'Db', 'B', 'G#m', 'Bbm']),
    "Am": Chord(['A', 'C', 'E'], ['C', 'Dm', 'Em', 'G', 'F']),
    "Em": Chord(['E', 'G', 'B'], ['G', 'Am', 'Bm', 'D', 'C']),
    "Bm": Chord(['B', 'D', 'F#'], ['D', 'F#m', 'Em', 'G', 'A']),
    "F#m": Chord(['F#', 'A', 'C#'], ['A', 'C#m', 'Bm', 'D', 'E']),
    "C#m": Chord(['C#', 'E', 'G#'], ['E', 'G#m', 'F#m', 'A', 'B']),
    "G#m": Chord(['G#', 'B', 'D#'], ['B', 'C#m', 'Ebm', 'E', 'Gb']),
    "Ebm": Chord(['D#', 'F#', 'A#'], ['Gb', 'Bbm', 'G#m', 'Db', 'B']),
    "Bbm": Chord(['A#', 'C#', 'F'], ['Db', 'Ebm', 'Fm', 'Ab', 'Gb']),
    "Fm": Chord(['F', 'G#', 'C'], ['Ab', 'Bbm', 'Cm', 'Eb', 'Db']),
    "Cm": Chord(['C', 'D#', 'G'], ['Eb', 'Fm', 'Gm', 'Bb', 'Ab']),
    "Gm": Chord(['G', 'A#', 'D'], ['Bb', 'Cm', 'Dm', 'F', 'Eb']),
    "Dm": Chord(['D', 'F', 'A'], ['F', 'Gm', 'Am', 'C', 'Bb']),
}

notes_order = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
