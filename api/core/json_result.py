from enum import Enum
from typing import Any, Dict


class JsonResult(Enum):
    SUCCESS = (2000, "success")
    ERROR = (4000, "error")

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def to(self, data: Any = None, message: str = None) -> Dict[str, Any]:
        if self == JsonResult.SUCCESS:
            return {"code": self.code, "message": message if message is not None else self.message,
                    "data": data if data is not None else None}
        else:
            return {"code": self.code, "message": message if message is not None else self.message,
                    "data": data if data is not None else None}
