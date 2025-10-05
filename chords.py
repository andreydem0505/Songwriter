from random import choice


class Chord:
    def __init__(self, keys, neighbours):
        # notes from which the chord consists
        self.keys = keys
        # neighbours on the circle of fifths
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


def compose_chords(chords_number):
    """Returns a list of chords based on the circle of fifths. The starting chord is chosen randomly."""
    # choose the first note randomly
    start_note = choice(list(chords.keys()))

    # make a dictionary of distances from one note to all other notes
    distance_map = dict()

    # distance to the first note equals 0
    distance_map[start_note] = 0

    # fill dictionary of distances to other notes
    queue = [start_note]
    while len(queue) > 0:
        note = queue.pop(0)
        for neighbour in chords[note].neighbours:
            if neighbour not in distance_map.keys():
                distance_map[neighbour] = distance_map[note] + 1
                queue.append(neighbour)

    # start choosing chords
    result_chords = [start_note]

    # how far we can go from the starting note
    max_distance = chords_number - 1
    while max_distance > 0:
        result_chords.append(
            choice(list(filter(
                # we can't go far from the starting note, otherwise we shall not close the circle
                lambda x: distance_map[x] <= max_distance and not(distance_map[x] == 0 and max_distance == 1),
                chords[result_chords[-1]].neighbours))
            )
        )
        max_distance -= 1

    print(result_chords)
    return result_chords
