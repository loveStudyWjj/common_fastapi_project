from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv
from pydantic import ConfigDict

# 加载.env文件
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Common FastAPI Project"
    DEBUG: bool = True
    
    # 数据库配置
    DATABASE_URL: str
    
    # JWT配置
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    model_config = ConfigDict(env_file=".env", case_sensitive=True)

# 创建全局设置对象
settings = Settings()