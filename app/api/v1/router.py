from fastapi import APIRouter
from app.api.v1.endpoints import auth, users

api_router = APIRouter()

# 添加各个端点的路由
api_router.include_router(auth.router, prefix="/auth", tags=["认证"])
api_router.include_router(users.router, prefix="/users", tags=["用户"])