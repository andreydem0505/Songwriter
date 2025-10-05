from chords import chords
from random import choice, random, randint

CHORD_LENGTH = 384

notes_order = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


class Note:
    def __init__(self, position, length, velocity, key):
        self.position = position
        self.length = length
        self.velocity = velocity
        self.key = key


def chords_to_keys(source_chords, octave, add_bass=False, add_high=False, add_middle=False):
    """Accepts a list of chords and a base octave.
Returns list of notes in a specific format."""
    keys = []

    high_note_length = 48
    odd_chord = True

    position = 0
    for chord in source_chords:
        # add notes of the chord
        chord_keys = chords[chord].keys
        chord_keys_numbers = []
        for i in range(len(chord_keys)):
            note_key = 12 * octave + notes_order.index(chord_keys[i])
            # if current note is lower than the base note of the chord, shift it one octave up
            if i != 0 and notes_order.index(chord_keys[i]) < notes_order.index(chord_keys[0]):
                note_key += 12
            chord_keys_numbers.append(Note(position, CHORD_LENGTH, 100, note_key))

        keys.extend(chord_keys_numbers)

        # add bass note
        if add_bass:
            keys.append(Note(position, CHORD_LENGTH, 100, choice([chord_keys_numbers[0], chord_keys_numbers[1]]).key - 12))

        # add high notes
        if add_high and odd_chord:
            high_key = chord_keys_numbers[0].key + 24
            for x in range(position + CHORD_LENGTH // 4, position + CHORD_LENGTH, high_note_length):
                keys.append(Note(x, high_note_length, randint(60, 90), high_key))
                r = random()
                if r > 0.85:
                    high_key += 1
                elif r > 0.77:
                    high_key += 2
                elif r > 0.7:
                    high_key -= 1

        # add middle notes
        if add_middle and not odd_chord:
            if random() > 0.3:
                start_point = position + CHORD_LENGTH // 4 * randint(2, 3)
                keys.append(Note(start_point, position + CHORD_LENGTH - start_point, 90, choice([chord_keys_numbers[2], chord_keys_numbers[1]]).key))

        position += CHORD_LENGTH
        odd_chord = not odd_chord

    return keys
