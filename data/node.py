from dataclasses import dataclass
from typing import List, Dict


# @dataclass
class Node:
    def __init__(self, id, lat, lon) -> None:
        self.id = id
        self.lat = lat
        self.lon = lon

    #nodes: List[Dict]
