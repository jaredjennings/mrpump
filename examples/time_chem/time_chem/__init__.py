from datetime import datetime
from mrpump.chem import Chem

class TimeChem(Chem):
    def __init__(self, **kwargs):
        super(TimeChem, self).__init__(**kwargs)
        self.format = kwargs.get('format', '%Y/%m/%d %H:%M:%S')

    def appliesTo(self, text):
        return text.lower().strip().startswith('time')

    def __call__(self, sender_screen_name, text, reply):
        reply(datetime.now().strftime(self.format))
