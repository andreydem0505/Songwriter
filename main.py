import pyflp
from chords import chords, notes_order, compose_chords


# сколько всего аккордов строим
CHORDS_NUMBER = 8

TEMPO = 100.0

NOTE_LENGTH = 192

NOTES_IN_CHORD = 3

# базовая октава
OCTAVE_NUMBER = 5

result_chords = compose_chords(CHORDS_NUMBER)

# создаем список нот всех аккордов
keys = []
for chord in result_chords:
    for key in chords[chord].keys:
        keys.append(key)


project = pyflp.parse("base.flp")
project.tempo = TEMPO
counter = 0
for note in project.patterns.current.notes:
    if counter < CHORDS_NUMBER * NOTES_IN_CHORD:
        note_key = 12 * OCTAVE_NUMBER + notes_order.index(keys[counter])
        # если текущая нота ниже базовой ноты аккорда, то сдвигаем её на октаву выше
        if counter % NOTES_IN_CHORD != 0 and notes_order.index(keys[counter]) < notes_order.index(keys[counter // NOTES_IN_CHORD * NOTES_IN_CHORD]):
            note_key += 12
        note.key = note_key
        note.length = NOTE_LENGTH
        note.position = counter // NOTES_IN_CHORD * NOTE_LENGTH
        counter += 1
    else:
        note.position = 0
        note.velocity = 0
        note.key = 0

pyflp.save(project, "result.flp")
