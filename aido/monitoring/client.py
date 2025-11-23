import json
import sys

class WandbTaskLoggerClient:
    def __init__(self):
        pass

    def _send(self, message: dict):
        msg = json.dumps(message) + "\n"
        sys.stdout.write(msg)
        sys.stdout.flush()

    def log_scalars(self, tag, values, step_offset=0):
        if hasattr(values, 'tolist'):
            values = values.tolist()
        self._send({
            "type": "scalars",
            "key": tag,
            "scalars": values,
            "step_offset": step_offset
        })