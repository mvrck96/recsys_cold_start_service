from pydantic import BaseModel

class PredictData(BaseModel):
    user_id: int
    gender: str
    age: int
    occupation: str
    zip_code: str