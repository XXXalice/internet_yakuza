import sys


class Alert:

    def __init__(self):
        pass


    def safe_alert(strings):
        sys.stdout.write('[notice.]'+str(strings))
        print()


    def danger_alert(strings):
        sys.stdout.write('[DANGER!]' + str(strings))
        print()