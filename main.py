import pyflp
from chords import compose_chords
from notes import chords_to_keys


# сколько всего аккордов строим
CHORDS_NUMBER = 8

TEMPO = 200.0

# базовая октава
OCTAVE_NUMBER = 5

result_chords = compose_chords(CHORDS_NUMBER)

# создаем список нот всех аккордов
keys = chords_to_keys(result_chords, OCTAVE_NUMBER, add_bass=True, add_high=False, add_middle=True)


project = pyflp.parse("base.flp")
project.tempo = TEMPO
counter = 0
for note in project.patterns.current.notes:
    if counter < len(keys):
        key = keys[counter]
        note.key = key.key
        note.length = key.length
        note.position = key.position
        note.velocity = key.velocity
        counter += 1
    else:
        note.position = 0
        note.velocity = 0
        note.key = 0

pyflp.save(project, "result.flp")
