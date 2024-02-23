import pathlib
import numpy as np
import librosa as rosa

class AudIO:
    def __init__(self,paths:list[pathlib.Path]):
        self.paths = paths
    
    def getAllAudios(self) -> list[tuple[np.ndarray,int]]:
        audios = []        
        for path in self.paths:
            for file in path.iterdir():
                try:
                    audios.append(tuple(rosa.load(file)))
                except Exception as e:
                    print(f"Warning: Failed to load {file} in {path}")
        return audios