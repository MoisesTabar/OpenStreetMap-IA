from dataclasses import dataclass, field


@dataclass
class Tags:

    highway: str
    oneway: str
    max_speed: int


@dataclass
class Way:

    id: str
    nodes: list = field(default_factory=list)
    tags: list[Tags] = field(default_factory=list)
