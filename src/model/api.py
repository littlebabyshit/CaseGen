from pydantic import BaseModel
from typing import Optional, Dict


class Req(BaseModel):
    method: Optional[str] = None
    path: Optional[str] = None
    headers: Optional[Dict] = None
    files: Optional[str] = None
    data: Optional[Dict] = None
    json: Optional[Dict] = None
    params: Optional[Dict] = None
    auth: Optional[Dict] = None
    cookies: Optional[Dict] = None


class Res(BaseModel):
    body: Optional[str] = None


class Api(BaseModel):
    """
    定义接口，包含请求和响应
    """
    api_id: int
    api_name: str
    api_path: str
    req: Req
    res: Res
    req_schema: str = None
    res_schema: str = None
