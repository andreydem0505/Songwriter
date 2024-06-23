import pyflp
from chords import chords, notes_order
from random import choice

# сколько всего аккордов строим
NOTES_NUMBER = 4

TEMPO = 100.0

# базовая октава
OCTAVE_NUMBER = 5

# выбираем случайную первую ноту
start_note = choice(list(chords.keys()))

# создаем словарь расстояний до каждой ноты по квинтовому кругу
distance_map = dict()

# расстояние до первой ноты равно 0
distance_map[start_note] = 0

# строим словарь расстояний до остальных нот
queue = [start_note]
while len(queue) > 0:
    note = queue.pop(0)
    for neighbour in chords[note].neighbours:
        if neighbour not in distance_map.keys():
            distance_map[neighbour] = distance_map[note] + 1
            queue.append(neighbour)


# начинаем выбирать аккорды
result_chords = [start_note]

# counter следит за тем, как далеко мы можем уходить от стартовой ноты
counter = NOTES_NUMBER - 1
while counter > 0:
    result_chords.append(
        # выбираем соседа, подходящего под условие
        choice(list(filter(
            # не должны уходить далеко от стартовой ноты, иначе не замкнем круг
            lambda x: distance_map[x] <= counter,
            chords[result_chords[-1]].neighbours))
        )
    )
    counter -= 1

print(result_chords)


# создаем список нот всех аккордов
keys = []
for chord in result_chords:
    for key in chords[chord].keys:
        keys.append(key)


project = pyflp.parse("base.flp")
project.tempo = TEMPO
counter = 0
for note in project.patterns.current.notes:
    note_key = 12 * OCTAVE_NUMBER + notes_order.index(keys[counter])
    # если текущая нота ниже базовой ноты аккорда, то сдвигаем её на октаву выше
    if counter % 3 != 0 and notes_order.index(keys[counter]) < notes_order.index(keys[counter // 3 * 3]):
        note_key += 12
    note.key = note_key
    counter += 1

pyflp.save(project, "result.flp")
