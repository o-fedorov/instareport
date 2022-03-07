import sys
from pathlib import Path

VENDOR = Path(__file__).parent
REPORTER_PATH = str(VENDOR / "InstaReporter")

sys.path.append(REPORTER_PATH)

from libs import attack, proxy_harvester, user_agents

sys.path.remove(REPORTER_PATH)
