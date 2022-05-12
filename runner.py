# meant to help with the scoring and organization of data

class athlete:
    def __init__(self, name, grade=-1, team='unattatched'):
        self.name = name
        self.grade = grade
        self.events = []
        self.score = 999
        self.team = team

    def add_event(self, event, time):
        if time == "":
            return
        if 'h' in time:
            index = time.find('h')
            time = time[:index] + time[index + 1:]
        if len(time) > 7:
            time = 60 * int(time[:2]) + float(time[3:])
        else:
            time = 60 * int(time[:1]) + float(time[2:])
        event = int(event)
        self.events.append((event, time))

    
