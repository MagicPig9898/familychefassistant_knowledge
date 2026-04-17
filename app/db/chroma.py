
# 封装 Chroma 向量数据库的连接，做成全局单例，方便项目里任何地方调用。
import chromadb
from chromadb.config import Settings

# 本地持久化路径
# 把向量数据库全部存在项目里的 data/chroma 文件夹里
CHROMA_PERSIST_DIR = "data/chroma"  

_client: chromadb.ClientAPI | None = None


def get_chroma_client() -> chromadb.ClientAPI:
    """获取 Chroma 客户端单例（本地持久化模式）"""
    global _client # 使用全局变量
    if _client is None: # 如果还没创建
        _client = chromadb.PersistentClient( # 创建本地持久化客户端
            path=CHROMA_PERSIST_DIR,   
            settings=Settings(anonymized_telemetry=False),   # 关闭匿名统计
        )
    return _client


# 获取集合: collection, 相当于一个表, 用来存：文本、向量、元数据
# 这个函数的作用：没有就创建，有就直接获取，默认表名叫 knowledge（知识库）
def get_collection(name: str = "knowledge") -> chromadb.Collection:
    """获取或创建一个 collection"""
    client = get_chroma_client()
    return client.get_or_create_collection(name=name)
