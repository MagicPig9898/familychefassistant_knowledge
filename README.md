# familychefassistant_knowledge
家庭厨师助手的知识库服务

used: 
- chromadb 
- fastapi 
- uvicorn

how to run the project:
- git clone 
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- if you add、remove or upgrade the pip install, pleae update requirements.txt and git push the changes
- python -m app.main 或 uvicorn app.main:app --reload，启动服务
- 启动后访问 http://localhost:8000/docs 可看到 Swagger 交互文档，直接测试所有接口。Chroma 数据持久化在 data/chroma/ 目录。

# project struct
```
familychefassistant_knowledge/
├── app/
│   ├── main.py          # FastAPI入口
│   ├── api/             # 路由层
│   ├── service/         # 业务逻辑
│   ├── db/
│   │   └── chroma.py    # Chroma封装
│   └── models/          # 数据结构
│
├── data/
│   └── chroma/          # 向量库数据（本地持久化, 不会提交）
│
├── requirements.txt
├── .gitignore
├── README.md
└── venv/                # 虚拟环境（不会提交）
```