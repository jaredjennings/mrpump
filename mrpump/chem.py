from mrpump.chembase import ChemBase

class Chem(ChemBase):
    def _msg_ping(self, rest, reply):
        reply('pong')
