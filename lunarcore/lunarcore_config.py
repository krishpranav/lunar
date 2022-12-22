from lunarcore.compact import Compatibility
import lunarcore.lunarconfig as lunarconfig
from starlette.config import Config
import logging
import os
from ssl import PROTOCOL_SSLv23
from starlette.config import environ

class LunarConfig(Config):
    config=None
    
    def __init__(self,env_file=None):
        super().__init__(env_file)
        self.cwd=os.getcwd()
        pass
    
    @classmethod
    def set(cls,key:str,value:object):
        environ[key]=value
    
    @classmethod
    def reset(cls):
        cls.config=None
        
    @classmethod
    def setup(cls):
        if cls.config is None:
            config=LunarConfig("lunarconfig.env")
            cls.config=config
            lunarconfig.DEBUG= config("DEBUG", cast=bool, default=True)
            lunarconfig.VERBOSE = config("VERBOSE", cast=bool, default=True)
            lunarconfig.HOST = config("HOST", cast=str, default="127.0.0.1")
            lunarconfig.PORT = config("PORT", cast=int, default=8000)
            lunarconfig.CRASH = config("CRASH", cast=bool, default=False)
            lunarconfig.LATENCY = config("LATENCY", cast=int, default=0)
            if lunarconfig.LATENCY and lunarconfig.VERBOSE:
                print(f"Simulating latency of {lunarconfig.LATENCY} ms")
            lunarconfig.HTML_404_PAGE = "justpy is sorry - that path doesn't exist"
            lunarconfig.MEMORY_DEBUG = config("MEMORY_DEBUG", cast=bool, default=False)
            lunarconfig.SESSIONS = config("SESSIONS", cast=bool, default=True)
            lunarconfig.SESSION_COOKIE_NAME = config("SESSION_COOKIE_NAME", cast=str, default="ln_token")
            lunarconfig.SECRET_KEY = config(
    "SECRET_KEY", default="$$$my_secret_string$$$"
)  
            lunarconfig.LOGGING_LEVEL = config("LOGGING_LEVEL", default=logging.WARNING)
            lunarconfig.UVICORN_LOGGING_LEVEL = config("UVICORN_LOGGING_LEVEL", default="WARNING").lower()
            lunarconfig.COOKIE_MAX_AGE = config(
    "COOKIE_MAX_AGE", cast=int, default=60 * 60 * 24 * 7
)  # One week in seconds

            lunarconfig.SSL_VERSION = config("SSL_VERSION", default=PROTOCOL_SSLv23)
            lunarconfig.SSL_KEYFILE = config("SSL_KEYFILE", default="")
            lunarconfig.SSL_CERTFILE = config("SSL_CERTFILE", default="")

            lunarconfig.STATIC_DIRECTORY = config("STATIC_DIRECTORY", cast=str, default=os.getcwd())
            lunarconfig.STATIC_ROUTE = config("STATIC_MOUNT", cast=str, default="/static")
            lunarconfig.STATIC_NAME = config("STATIC_NAME", cast=str, default="static")
            lunarconfig.FAVICON = config(
    "FAVICON", cast=str, default=""
)  # If False gets value from https://elimintz.github.io/favicon.png
            lunarconfig.TAILWIND = config("TAILWIND", cast=bool, default=True)
            lunarconfig.QUASAR = config("QUASAR", cast=bool, default=False)
            lunarconfig.QUASAR_VERSION = config("QUASAR_VERSION", cast=str, default=None)
            lunarconfig.HIGHCHARTS = config("HIGHCHARTS", cast=bool, default=True)
            lunarconfig.KATEX = config("KATEX", cast=bool, default=False)
            lunarconfig.VEGA = config("VEGA", cast=bool, default=False)
            lunarconfig.BOKEH = config("BOKEH", cast=bool, default=False)
            lunarconfig.PLOTLY = config("PLOTLY", cast=bool, default=False)
            lunarconfig.DECKGL = config("DECKGL", cast=bool, default=False)
            lunarconfig.AGGRID = config("AGGRID", cast=bool, default=True)
            lunarconfig.AGGRID_ENTERPRISE= config("AGGRID_ENTERPRISE", cast=bool, default=False)
            lunarconfig.NO_INTERNET= config("NO_INTERNET", cast=bool, default=True)
            lunarconfig.FRONTEND_ENGINE_TYPE = config("FRONTEND_ENGINE_TYPE", cast=str, default="vue")


if Compatibility.version is None:
    LunarConfig.setup()