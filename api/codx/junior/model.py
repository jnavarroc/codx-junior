from __future__ import annotations
from pydantic import BaseModel, Field


from typing import List, Dict, Union

from codx.junior.settings import GPTEngineerSettings

class ImageUrl(BaseModel):
    url: str = Field(default="")

class Content(BaseModel):
    type: str = Field(default='text')
    text: str = Field(default=None)
    image_url: ImageUrl = Field(default=None)

class ChatMessage(BaseModel):
    role: str = Field(default='')
    content: List[Content] = Field(default=[])

class Message(BaseModel):
    role: str = Field(default='')
    content: str = Field(default='')
    hide: bool = Field(default=False)
    improvement: bool = Field(default=False)
    created_at: str = Field(default='')
    images: List[str] = Field(default=[])
    files: List[str] = Field(default=[])

class Chat(BaseModel):
    id: str = Field(default='')
    parent_id: str = Field(default='')
    status: str = Field(default='')
    tags: List[str] = Field(default=[])
    file_list: List[str] = Field(default=[])
    profiles: List[str] = Field(default=[])
    name: str = Field(default='')
    messages: List[Message] = Field(default=[])
    created_at: str = Field(default='')
    updated_at: str = Field(default='')
    mode: str = Field(default='chat')
    board: str = Field(default='')
    column: str = Field(default='')
    column_index: int = Field(default=-1)
    chat_index: int = Field(default=-1)
    live_url: str = Field(default='')

class Logprobs(BaseModel):
    tokens: List[str]
    token_logprobs: List[float]
    top_logprobs: List[Dict[str, float]]
    text_offset: List[int]

class Choice(BaseModel):
    index: int
    message: Message
    logprobs: Optional[Logprobs]
    finish_reason: str

class ChatResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    system_fingerprint: str
    choices: List[Choice]
    usage: Dict[str, int]

class KnowledgeReloadPath(BaseModel):
    path: str

class KnowledgeDeleteSources(BaseModel):
    sources: List[str]

class KnowledgeSearch(BaseModel):
    search_term: str
    search_type: str = Field(default=None)
    document_search_type: str = Field(default=None)
    document_count: int = Field(default=None)
    document_cutoff_score: float = Field(default=None)

class Profile(BaseModel):
    name: str
    content: str

class Settings(BaseModel, GPTEngineerSettings):
  pass

class Document(BaseModel):
    id: int = Field(default=None)
    page_content: str
    metadata: dict

class LiveEdit(BaseModel):
    chat_name: str
    html: str
    url: str
    message: str

class OpenAISettings(BaseModel):
    openai_api_url: str = Field(default=None)
    openai_api_key: str = Field(default=None)
    openai_model: str = Field(default="gpt-4o")
    

class AnthropicAISettings(BaseModel):
    anthropic_api_url: str = Field(default=None)
    anthropic_api_key: str = Field(default=None)
    anthropic_model: str = Field(default="claude-3-5-sonnet-20240620")

class GlobalSettings(BaseModel):
    openai: OpenAISettings = Field(default=OpenAISettings())
    anthropic_ai: AnthropicAISettings = Field(default=AnthropicAISettings())
    log_ai: bool = Field(default=False)
    projects_root_path: str = Field(default='/codx-junior/projects')
    ai_temperature: str = Field(default="0.8")

