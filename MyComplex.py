import math
from typing import Any, Literal
class Complex:
    """Тут можно писать всякое, чтобы пользователь при создании объекта класса.
    Например для этого класса:
    Это класс для работы с комплексными числами
    """
    def __init__(self, real:float, img: float) -> None:
        self.real = real
        self.img = img
    
    def abs(self) -> float:
        """Docstring также можно создать и для функций. Обычно это выглядит так:
        """
        return (self.real**2+self.img**2)**0.5
    
    def phase(self) -> float:
        return math.atan(self.img/self.real)
    
    def conj(self) -> None:
        self.img *= -1
    
    def __eq__(self, other) -> bool:
        return (self.real, self.img) == (other.real, other.img)
    
    def __add__(self, other):
        if isinstance(other, (int,float)):
            return Complex(self.real+other, self.img)
        elif isinstance(other, Complex):
            return Complex(self.real+other.real, self.img+other.img)
        else:
            raise ValueError(f"other can be Complex, int or float and can not be {type(other)}")
    
    def __abs__(self) -> float:
        return (self.real**2+self.img**2)**0.5# self.abs()
    
    def __radd__(self, other):
        return self+other
    
    def __getitem__(self, key: Literal[1,2,"real","img"]):
        """
        Предоставляет доступ к реальной и мнимой части комплексного числа.
        
        Параметры:
        key (int or "str"): индекс (1 или 0) или ключ-строка (real или img)
        """
        if key in (0,1):
            return self.real if key==0 else self.img
        elif key in ("real", "img"):
            return self.real if key=="real" else self.img
        else:
            raise KeyError(f"key can be either integer equal 0 and 1 or str equal \"real\" and \"img\", not {key}")
        
    def __reversed__(self):
        return Complex(self.img, self.real)

    def __call__(self, *args, **kwargs):
        print(f"Are you stupid or smth?"
              f" I'm Complex number what do you suppose to get calling me with all these {args} and {kwargs}?")

    def __contains__(self, item):
        return item in (self.real, self.img)
    
    def __repr__(self) -> str:
        return f"{self.real}{self.img:+}*i"