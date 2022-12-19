class Compatibility(object):
    version = None

    def __init__(self, major=0,minor=2,patch=2):

        self.major = major
        self.minor = minor
        self.patch = patch

        if Compatibility.version is not None:
            raise Exception(f"Justpy compatibility has already been set to {major}.{minor}.{patch}")
        Compatibility.version=self
        
    @classmethod
    def reset(cls):
        cls.version = None
        