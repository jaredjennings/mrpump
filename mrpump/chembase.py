import logging

class ChemBase(object):
    def __init__(self):
        self.log = logging.getLogger('Handler')
        pass

    def __call__(self, sender_screen_name, message):
        # avoid "Whoops, you already said that!"
        message = message.lstrip('0123456789 ')
        if ' ' in message:
            firstword, rest = message.split(' ', 1)

        else:
            firstword = message
            rest = ''
        try:
            name = '_msg_' + firstword
            method = getattr(self, name)
            self.log.debug('calling %s with %r', name, rest)
        except AttributeError:
            self.log.error('could not handle message %r', message)
            return 'did not understand'
        try:
            return method(rest)
        except Exception, e:
            self.log.error('while dealing with message %r', message)
            self.log.error('%r', e)
            return 'error: %r' % e
