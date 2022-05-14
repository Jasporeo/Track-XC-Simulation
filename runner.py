# meant to help with the scoring and organization of data

class athlete:
    def __init__(self, name, grade=-1, team='unattatched', score=999):
        self.name = name
        self.grade = grade
        self.events = []
        self.score = score
        self.team = team

    def __str__(self):
        return f'{self.name}, {self.score})'

    def add_event(self, event, time, date):
        print(time)
        if event == "2" or event == "4800":
            time = time + "0"
        if "N" in time or time == '' or time == "0":
            return
        if "h" in time:
            index = time.find("h")
            time = time[:index]
        if len(time) > 7:
            time = 60 * int(time[:2]) + float(time[3:])
        else:
            time = 60 * int(time[:1]) + float(time[2:])
        event = int(event)
        self.events.append((event, time, date))

    def calculate_score(self):
        for tup in self.events:
            current = 0
            if tup[0] == 800:
                current = tup[1] * 2.25
            elif tup[0] == 1600:
                current = tup[1]
            elif tup[0] == 3200:
                current = tup[1] * .476
            else:  # need XC conversion here
                current = 999
            if current < self.score:
                self.score = current
