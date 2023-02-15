from dataclasses import dataclass

@dataclass
class ServerInfo:
    name: str
    map: str
    players: int
    wave: int
    version: int
    vertype: str
    gamemode: str
    limit: int
    description: str
    modename: str

