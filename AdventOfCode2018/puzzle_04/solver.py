import datetime


class NightShift:
    """
    example shift log:
        data = {
            datetime.date(1518, 2, 21): {
                "guard_id": "2239",
                "shift": ['.'] * 60
            }
        }
    """
    actions = ["begins shift", "falls asleep", "wakes up"]

    def __init__(self):
        self.data = dict()

    @staticmethod
    def parse_line(line):
        date, time, description = line.strip('[\n').replace(']', '').split(' ', maxsplit=2)
        date = datetime.date(*[int(i) for i in date.split('-')])
        hour, minute = [int(i) for i in time.split(':')]

        if hour == 23:
            date += datetime.timedelta(days=1)
            minute = 0

        return date, minute, description

    @property
    def actions_mapping(self):
        return {
            "begins shift": self.begins_shift,
            "falls asleep": self.falls_asleep,
            "wakes up": self.wakes_up
        }

    def add_log_entry(self, line):
        date, minute, description = self.parse_line(line)
        action = [action for action in self.actions if action in description][0]

        self.actions_mapping[action](
            date=date,
            minute=minute,
            description=description
        )

    def get_all_guards(self):
        return set(log['guard_id'] for log in self.data.values())

    def get_slept_minutes(self):
        slept_minutes = dict()

        for log in self.data.values():
            guard_id = log['guard_id']

            if slept_minutes.get(guard_id) is None:
                slept_minutes[guard_id] = 0

            slept_minutes[guard_id] += log['shift'].count('#')

        return slept_minutes

    def get_most_sleepy_guard(self, slept_minutes_log):
        return [key for key in slept_minutes_log.keys() if slept_minutes_log[key] == max(slept_minutes_log.values())][0]

    def get_guard_log(self, guard_id):
        return [log['shift'] for log in self.data.values() if log['guard_id'] == guard_id]

    def get_most_sleepy_night(self, log):
        return max(([log[minute] for log in log].count('#'), minute) for minute in range(60))[1]

    def get_most_sleepy_minute(self, log):
        return max(([entry[minute] for entry in log].count('#'), minute) for minute in range(60))

    def begins_shift(self, **kwargs):
        date = kwargs["date"]
        guard_id = kwargs["description"].partition('#')[-1].partition(' ')[0]

        self.data[date] = {
            "guard_id": guard_id,
            "shift": ['.'] * 60
        }

    def falls_asleep(self, **kwargs):
        date = kwargs["date"]
        minute = kwargs["minute"]
        shift_log = self.data[date]['shift']

        self.data[date]['shift'] = shift_log[:minute] + ['#'] * (60 - minute)

    def wakes_up(self, **kwargs):
        date = kwargs["date"]
        minute = kwargs["minute"]

        shift_log = self.data[date]['shift']

        self.data[date]['shift'] = shift_log[:minute] + ['.'] * (60 - minute)


def solver1(data):
    night_shift = NightShift()

    for line in data:
        night_shift.add_log_entry(line)

    slept_minutes_log = night_shift.get_slept_minutes()
    most_sleepy_guard = night_shift.get_most_sleepy_guard(slept_minutes_log)
    sleepy_guard_log = night_shift.get_guard_log(most_sleepy_guard)
    most_sleepy_night = night_shift.get_most_sleepy_night(sleepy_guard_log)

    return int(most_sleepy_guard) * most_sleepy_night


def solver2(data):
    night_shift = NightShift()

    for line in data:
        night_shift.add_log_entry(line)

    guards = night_shift.get_all_guards()

    most_sleepy_minutes = []

    for guard in guards:
        guard_log = night_shift.get_guard_log(guard)
        most_sleepy_minute = night_shift.get_most_sleepy_minute(guard_log)

        most_sleepy_minutes.append((most_sleepy_minute, guard))

    (_, minute), guard = max(most_sleepy_minutes)

    return minute * int(guard)


if __name__ == '__main__':
    # Solution

    with open('input.txt') as f:
        data = sorted(f.readlines())

    answer1 = solver1(data)
    print(answer1)

    answer2 = solver2(data)
    print(answer2)

    # Tests

    example_data = [
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up"
    ]

    expected_data = {
        datetime.date(1518, 11, 1): {
            'guard_id': '10',
            'shift': list('.....####################.....#########################.....')
        },
        datetime.date(1518, 11, 2): {
            'guard_id': '99',
            'shift': list('........................................##########..........')
        },
        datetime.date(1518, 11, 3): {
            'guard_id': '10',
            'shift': list('........................#####...............................')
        },
        datetime.date(1518, 11, 4): {
            'guard_id': '99',
            'shift': list('....................................##########..............')
        },
        datetime.date(1518, 11, 5): {
            'guard_id': '99',
            'shift': list('.............................................##########.....')
        }
    }

    night_shift = NightShift()

    for line in example_data:
        night_shift.add_log_entry(line)

    assert night_shift.data == expected_data

    answer = solver1(example_data)
    assert answer == 240

    slept_minutes_log = night_shift.get_slept_minutes()
    assert slept_minutes_log == {
        '10': 50,
        '99': 30
    }

    most_sleepy_guard = night_shift.get_most_sleepy_guard(slept_minutes_log)
    assert most_sleepy_guard == '10'

    sleepy_guard_log = night_shift.get_guard_log(most_sleepy_guard)
    assert sleepy_guard_log == [
        list('.....####################.....#########################.....'),
        list('........................#####...............................')
    ]

    most_sleepy_night = night_shift.get_most_sleepy_night(sleepy_guard_log)
    assert most_sleepy_night == 24

    all_guards = night_shift.get_all_guards()
    assert all_guards == {'10', '99'}

    guard_log = night_shift.get_guard_log('99')

    most_sleepy_minute = night_shift.get_most_sleepy_minute(guard_log)
    assert most_sleepy_minute == (3, 45)

    assert solver1(example_data) == 240
    assert solver2(example_data) == 4455
