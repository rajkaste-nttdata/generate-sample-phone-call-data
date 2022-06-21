class GenConfig:
    def __init__(self,_cdr,_callback,hours) -> None:
        self.nSets = 1
        self.nFilesPerDump = 1
        self.nCDRPerFile = _cdr
        self.nCallBackPercent = _callback
        self.nDurationHours = hours
