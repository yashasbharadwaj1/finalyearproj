from bson import ObjectId
from . import mongo_connection
comments = mongo_connection.commentsdata
pathan_corpus = comments.find_one({"_id": ObjectId("63e6408ef1a035e59a014ddb")})["Pathan"]

__all__ = ["pathan_corpus"]