from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from table_user import User
from table_post import Post


class Feed(Base):
    __tablename__ = "feed_action"
    post_id = Column(Integer, ForeignKey("post.id"), primary_key=True)
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    user = relationship(User)
    action = Column(String)
    time = Column(TIMESTAMP)
