import os
from pathlib import Path

ENV = os.getenv("ENV", "dev")


class PathManager:
    ROOT = Path(__file__).parents[2]
    SOURCE = ROOT / "src"
    CONFIG = SOURCE / "config"
    DEV = CONFIG / "dev"

    @property
    def CONF_DIR(self):
        match ENV:
            case "dev":
                return self.DEV


PATH = PathManager()
