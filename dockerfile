# Python 기반 이미지
FROM python:3.10-slim

# 작업 디렉토리 생성
WORKDIR /usr/src/moatalk

# 의존성 복사 및 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 전체 프로젝트 복사
COPY . .

# 정적 파일 경로 지정 (collectstatic용)
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
