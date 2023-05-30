# CRUD
#   - CREATE    :   생성
#   - READ        :   조회
#   - UPDATE    :   수정
#   - DELETE    :   삭제

from db.connection import conn
# 리뷰 저장
def add_review(data):
    collection = conn()
    collection.insert_one(data)

# 리뷰 조회 (Mongo DB)
def get_reviews():
    pass
