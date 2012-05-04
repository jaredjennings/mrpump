from mrpump.chembase import ChemBase

class Chem(ChemBase):
    def _msg_ping(self, rest):
        return 'pong'
