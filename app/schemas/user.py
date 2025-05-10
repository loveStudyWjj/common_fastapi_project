from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict

# 用户基础模型
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False

# 创建用户时的模型
class UserCreate(UserBase):
    email: EmailStr
    username: str
    password: str

# 更新用户时的模型
class UserUpdate(UserBase):
    password: Optional[str] = None

# 数据库中的用户模型
class UserInDBBase(UserBase):
    id: Optional[int] = None
    
    model_config = ConfigDict(from_attributes=True)  # 新方式


# API响应中的用户模型
class User(UserInDBBase):
    pass

# 数据库中存储的用户模型（包含密码）
class UserInDB(UserInDBBase):
    hashed_password: str