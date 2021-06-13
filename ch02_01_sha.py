# SHA-256 으로 파일 복사 검증하기
# 해시는 입력값이 같으면 생성되는 해시값도 같아서 파일의 변경여부를 파악하거나
# 두 파일의 내용이 동일한지 비교하는데 주로 사용됨

import hashlib

sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open('src.png','rb') as sf , open('dst.png','rb') as df :
    sha_src.update(sf.read())
    sha_dst.update(df.read())

print("src.png's hash :{}".format(sha_src.hexdigest()))
print("dst.png's hash :{}".format(sha_dst.hexdigest()))
