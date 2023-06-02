from abc import ABC, abstractmethod


class BaseBookLoader(ABC):

    @abstractmethod
    def make_book(self, sentences):
        pass

