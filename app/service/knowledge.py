# 对 Chroma 向量数据库的 增、查、改、删、单查 封装
# 项目里所有知识库操作
# 导入db包中的 get_collection()
# 给上层 FastAPI 接口调用
from app.db.chroma import get_collection


def add_document(doc_id: str, text: str, metadata: dict | None = None):
    """添加文档到知识库"""
    col = get_collection()  # 拿到数据库表
    col.add(  # Chroma 要求必须传列表，支持一次添加多条。
        ids=[doc_id],  # 文档ID（必须放列表里）
        documents=[text],  # 文档内容（列表）
        metadatas=[metadata or {}]  # 元数据（没有就给空字典）
    )  
    return {"id": doc_id, "status": "added"}


# 自动匹配最相似的知识库内容
def query_documents(query: str, n_results: int = 5):
    """语义查询知识库"""
    col = get_collection()
    results = col.query(
        query_texts=[query],  # 用户的问题
        n_results=n_results   # 返回几条最相似的，不传就默认5条
    )
    return results

# 根据 ID 获取单条文档
def get_document(doc_id: str):
    """根据 id 获取文档"""
    col = get_collection()
    results = col.get(
        ids=[doc_id]  
    )
    return results


def update_document(doc_id: str, text: str, metadata: dict | None = None):
    """更新文档"""
    col = get_collection()
    col.update(ids=[doc_id], documents=[text], metadatas=[metadata or {}])
    return {"id": doc_id, "status": "updated"}


def delete_document(doc_id: str):
    """删除文档"""
    col = get_collection()
    col.delete(ids=[doc_id])
    return {"id": doc_id, "status": "deleted"}
