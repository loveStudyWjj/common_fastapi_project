# 通用FastAPI项目

这是一个通用的FastAPI项目模板，包含了生产环境所需的基本功能：

- 数据库连接与ORM (SQLAlchemy)
- 用户认证与授权 (JWT)
- API路由管理
- 配置管理
- 数据库迁移 (Alembic)
- 测试框架

## 安装

1. 克隆仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 复制`.env.example`为`.env`并修改配置
4. 运行数据库迁移：`alembic upgrade head`
5. 启动应用：`python run.py`

## API文档

启动应用后，访问以下URL查看API文档：

- Swagger UI: http://localhost:8000/api/docs
- ReDoc: http://localhost:8000/api/redoc

## 项目结构

- `app/`: 应用代码
  - `main.py`: 应用入口
  - `core/`: 核心配置
  - `api/`: API路由
  - `models/`: 数据库模型
  - `schemas/`: Pydantic模型
  - `services/`: 业务逻辑
- `alembic/`: 数据库迁移
- `tests/`: 测试

## 开发

### 创建新的API端点

1. 在`app/api/v1/endpoints/`中创建新的路由文件
2. 在`app/api/v1/router.py`中注册路由

### 数据库迁移

创建新的迁移：

```bash
alembic revision --autogenerate -m "描述"