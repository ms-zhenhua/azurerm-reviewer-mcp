import logging
import uuid
from dataclasses import dataclass
from enum import Enum

class Constants:
    GITHUB_TOKEN = "GITHUB_TOKEN"
    MAX_TOKENS = "MAX_TOKENS"
    RESULT_DIRECTORY = "RESULT_DIRECTORY"
    MAX_RULE_LENGTH_PER_PROMPT = "MAX_RULE_LENGTH_PER_PROMPT"

    JSON_FORMAT_FILE = "json_format.json"
    MD_FORMAT_FILE = "md_format.md"
    REVIEW_DRAFT_FILE = "review_draft.txt"
    REVIEW_RESULT_FILE = "review_result.md"

class FileType(Enum):
    GO_RESOURCE = "go_resource"
    GO_TEST = "go_test"
    MARKDOWN_DOC = "markdown_doc"
    UNKNOWN = "unknown"
    
    @classmethod
    def from_filename(cls, filename: str) -> 'FileType':
        """Determine file type from filename"""
        if filename.endswith("_resource_test.go"):
            return cls.GO_TEST
        elif filename.endswith(".go"):
            return cls.GO_RESOURCE
        elif filename.endswith(".html.markdown"):
            return cls.MARKDOWN_DOC
        else:
            return cls.UNKNOWN

@dataclass
class FileToReview:
    file_name: str
    file_type: FileType
    content: str

@dataclass
class ViolationItem:
    """
    Represents a violation item found during the review of a file.

    Attributes:
    - file_name (str): The name of the file that was reviewed.
    - line_no (int): The line number where the violation was found.
    - rule (str): The name of the rule that was violated.
    - message (str): The error message describing the violation.
    """
    file_name: str
    line_no: int
    rule: str
    message: str

@dataclass
class Rules:
    go_resource: list[str]
    go_test: list[str]
    markdown_doc: list[str]


def raise_error(message: str):
    logging.error(message)
    raise ValueError(message)

def is_valid_uuid(uuid_string):
    try:
        uuid_obj = uuid.UUID(uuid_string)
        return str(uuid_obj) == uuid_string
    except ValueError:
        return False
    

def create_uuid() -> str:
    return str(uuid.uuid4())