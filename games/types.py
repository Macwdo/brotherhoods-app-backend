from dataclasses import dataclass, asdict
from games.models import Game

@dataclass
class WeekGames:
    previous: Game | None
    next: Game | None

    dict = asdict