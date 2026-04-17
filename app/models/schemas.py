# FastAPI 接口专用的数据格式定义
# 规定前端 / 调用方传什么数据过来，保证数据格式不乱、不报错。
# BaseModel 是 Pydantic 的数据模型基类
# 你定义的每个类，都会自动校验数据格式对不对
from pydantic import BaseModel


class DocumentAdd(BaseModel):
    """添加文档请求"""
    id: str  # 文档ID，必须是字符串
    text: str  # 文档内容，必须是字符串
    metadata: dict | None = None  # 元数据（比如来源、时间、作者），可以不传，不传就是 None


class DocumentQuery(BaseModel):
    """查询请求"""
    query: str  # 查询文本
    n_results: int = 5  # 想返回几条最相似的结果，不传默认就是 5


class DocumentUpdate(BaseModel):
    """更新文档请求"""
    id: str  # 文档ID，必须是字符串
    text: str  # 新的文本
    metadata: dict | None = None  # 可选，更新附加信息
