from pydantic import ConfigDict,BaseModel

class NoteCreate(BaseModel):
    body : str
    Role : str
    
class NoteRead(BaseModel):
    id : int
    body : str
    role : str
    
    model_config = ConfigDict(from_attributes=True)
    
    