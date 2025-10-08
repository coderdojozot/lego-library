from usys import stdin
from uselect import poll
import ujson

SEP = chr(183)
EOF = '\n'


class AiBrick:
    """Base class for AiBrick communication."""
    frames = {}

    def __init__(self):
        self.buffer = ''
        self.nuart = poll()
        self.nuart.register(stdin)
        self._flush()
        
    def _flush(self):
        while self.nuart.poll(0):
            stdin.read(1)

    def _send(self, cmd: str, message: str):
        """Sends the frame with given command's name and message."""
        print(cmd, SEP, message, '\n', sep='')

    def _process(self, cmd: str, message: str):
        """This method should be implemented in the derived class."""
        ...
    
    def receive(self):
        """
        Listens to Blueooth transmission and pushes the received bytes into 
        buffer until end of frame (EOF) byte is received. Then calls _process()
        to interpret contents of the frame and returns frame's name (command).
        If EOF was not yet received, None is returned.
        """
        while self.nuart.poll(0):
            char = stdin.read(1)  
            if char == EOF:
                received, self.buffer = self.buffer, ''
                if SEP in received:
                    cmd, message = received.split(SEP, 1)
                else:
                    cmd, message = '', received
                self._process(cmd, message)
                return self.frames.get(cmd, cmd)
            else: 
                self.buffer += char
        return None


class AiBrickTeachableMachine(AiBrick):
    """
    Implements communication with aiBrick web application, running TeachableMachine AI/ML model.
    """
    frames = {"d": "detection", "p": "probability"}

    def __init__(self, model='', detection=True, probability=False):
        super().__init__()
        self.config = {
            "type": "teachablemachine",
            "model": model,
            "detection": detection,
            "probability": probability
        }
        self.labels = []
        self.detection = ""
        self.probability = {}

    def _process(self, cmd: str, message: str):
        """
        Processes the frame content to respond with setup configuration
        or assign `labels`, `detection` or `probability` properties.
        """
        if cmd == 'setup':
            self._send('setup', ujson.dumps(self.config))
        elif cmd == 'labels':
            self.labels = message.split('"')[1::2]
        if cmd == 'd' and self.config['detection']:
            self.detection = self.labels[int(message)]
        elif cmd == 'p' and self.config['probability']:
            probabilities = message.split(',')
            self.probability = {label: int(p) if p.isdigit() else 0 
                                for label, p in zip(self.labels, probabilities)}
        else:
            # for debug purposes
            print("cmd", cmd, len(cmd), "message", message)