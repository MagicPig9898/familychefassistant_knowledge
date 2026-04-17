# 接收前端 / 客户端请求 → 调用业务逻辑 → 返回结果
from fastapi import APIRouter, HTTPException
from app.models.schemas import DocumentAdd, DocumentQuery, DocumentUpdate
from app.service import knowledge as knowledge_service

# 创建路由
# 所有接口前面自动加 /knowledge
# tags=["knowledge"]，给接口文档分类用的
router = APIRouter(prefix="/knowledge", tags=["knowledge"])


@router.post("/add")
def add_document(doc: DocumentAdd):
    """添加文档"""
    try:
        return knowledge_service.add_document(doc.id, doc.text, doc.metadata)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/query")
def query_documents(q: DocumentQuery):
    """语义查询"""
    try:
        return knowledge_service.query_documents(q.query, q.n_results)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{doc_id}")
def get_document(doc_id: str):
    """获取单个文档"""
    try:
        return knowledge_service.get_document(doc_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{doc_id}")
def update_document(doc_id: str, doc: DocumentUpdate):
    """更新文档"""
    try:
        return knowledge_service.update_document(doc_id, doc.text, doc.metadata)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{doc_id}")
def delete_document(doc_id: str):
    """删除文档"""
    try:
        return knowledge_service.delete_document(doc_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
