# 项目的启动入口
from fastapi import FastAPI
from app.api.knowledge import router as knowledge_router

# 创建 FastAPI 应用实例
app = FastAPI(title="Family Chef Assistant - Knowledge Service")
# 把知识库接口注册到主程序
app.include_router(knowledge_router)

# 根路径 / 健康检查
@app.get("/")
def health():
    return {"status": "ok", "service": "knowledge"}


if __name__ == "__main__":
    import uvicorn
    # app.main:app 从 app/main.py 里找到 app 这个 FastAPI 实例
    # host="0.0.0.0"，让局域网内其他设备也能访问（不只是本机）
    # reload=True，代码改了自动重启服务
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
