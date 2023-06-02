from .chatgptapi_translator import ChatGPTAPI
from .google_translator import Google
from .gpt3_translator import GPT3
from .caiyun_translator import Caiyun
from .deepl_translator import DeepL

MODEL_DICT = {
    "chatgptapi": ChatGPTAPI,
    "gpt3": GPT3,
    "google": Google,
    "caiyun": Caiyun,
    "deepl": DeepL,
    # add more here
}
