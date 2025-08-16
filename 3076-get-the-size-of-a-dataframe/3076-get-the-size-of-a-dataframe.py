import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    x = list(players.shape)
    return x