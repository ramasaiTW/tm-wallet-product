from .enums import PostingInstructionType as PostingInstructionType
from .postings import CustomInstruction as CustomInstruction
from datetime import datetime
from typing import Any, Dict, List, Optional

class PostingInstructionsDirective:
    posting_instructions: List[CustomInstruction]
    client_batch_id: Optional[str]
    value_datetime: Optional[datetime]
    batch_details: Optional[Dict[str, str]]

    def __init__(self, posting_instructions: List[CustomInstruction], *, client_batch_id: Optional[str]=..., value_datetime: Optional[datetime]=..., batch_details: Optional[Dict[str, str]]=..., _from_proto: bool=...) -> None:
        ...