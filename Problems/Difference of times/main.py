event_one_input = list()
event_two_input = list()

for _i in range(3):
    event_one_input.append(int(input()))

for _i in range(3):
    event_two_input.append(int(input()))


def event_in_seconds(input_event):
    hours_to_seconds = 0
    minutes_to_seconds = 0
    seconds = 0

    if input_event[0] >= 1:
        hours_to_seconds = hours_to_seconds + input_event[0] * 3600

    if input_event[1] >= 1:
        minutes_to_seconds = minutes_to_seconds + input_event[1] * 60
    if input_event[2] >= 1:
        seconds = seconds + input_event[2]

    return hours_to_seconds + minutes_to_seconds + seconds


event_one = event_in_seconds(event_one_input)
event_two = event_in_seconds(event_two_input)

print(event_two - event_one)