# Aiuto (아이우토): 당신의 AI 조력자 🤖 Notion 자동화 비서

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org)
[![Django](https://img.shields.io/badge/Django-4.x-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Notion API](https://img.shields.io/badge/Notion%20API-v1-lightgrey?logo=notion&logoColor=black)](https://developers.notion.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- 추가할 뱃지: 테스트 커버리지, 빌드 상태 등 -->

**Aiuto**는 바쁜 일상 속에서 놓치기 쉬운 할 일들을 음성이나 텍스트로 간편하게 기록하고, AI의 도움을 받아 체계적인 계획 수립과 필요한 정보 탐색을 자동화하여 Notion에 정리해주는 개인 맞춤형 AI 비서 프로젝트입니다.

**(✨ 여기에 프로젝트 핵심 기능을 보여주는 GIF나 스크린샷을 추가하세요! ✨)**
*   _(예: 안드로이드 음성 입력 -> Notion에 자동 등록 및 계획 생성되는 모습)_
*   _(예: Notion에 정리된 작업 계획 및 진행 상황 화면)_

## 🎯 프로젝트 목표 및 동기

개인적인 생산성 향상을 위해 반복적인 계획 수립, 정보 검색, 기록 과정을 자동화하고 싶었습니다. 특히, 안드로이드 환경에서도 iOS의 단축어처럼 편리하게 외부 서비스(AI, Notion)와 연동되는 시스템을 구축하고자 이 프로젝트를 시작했습니다. 이 과정을 통해 Django 백엔드 개발 역량과 AI API 활용 능력, 그리고 외부 서비스 연동 경험을 심화시키는 것을 목표로 합니다.

## ✨ 주요 기능

*   **🗣️ 음성/텍스트 입력:** 안드로이드 기기에서 음성 또는 텍스트로 할 일, 아이디어 등을 간편하게 입력합니다.
*   **🧠 AI 기반 계획 수립:** 입력된 내용을 바탕으로 Google AI (Gemini)가 실행 가능한 세부 계획과 필요 정보를 제안합니다.
*   **🔍 AI 정보 탐색 (예정):** 계획 실행에 필요한 추가 정보(예: 이사업체 후기, 맛집 추천 등)를 Perplexity AI 등을 통해 검색하고 요약합니다.
*   **📝 Notion 자동 기록/관리:** 생성된 계획과 정보는 지정된 Notion 데이터베이스에 자동으로 구조화되어 기록되고, 진행 상황을 추적할 수 있습니다. (페이지 생성, 속성 업데이트 등)
*   **📰 맞춤 뉴스레터 (예정):** 관심 분야의 최신 뉴스를 수집하고 AI가 요약하여 제공합니다.
*   **🔄 API 기반 연동:** Django REST Framework를 사용하여 안드로이드 앱(Tasker 등)과 백엔드 시스템 간의 안정적인 통신을 구현합니다.

## 🛠️ 기술 스택

*   **Backend:** Python, Django, Django REST Framework (DRF)
*   **Database:** SQLite (개발), PostgreSQL (배포)
*   **AI APIs:** Google AI Studio (Gemini API), Perplexity API (예정)
*   **Notion Integration:** `notion-client` Python library
*   **API Key Management:** `python-dotenv`
*   **Android Integration:** Tasker (예정)
*   **Deployment (예정):** Render (Free Tier 활용)
*   **(Optional) Asynchronous Tasks:** Celery, Redis

## 🏗️ 시스템 아키텍처 (예시)
Use code with caution.
Markdown
+-------------+ +----------------------+ +-------------------+ +-----------------+
| Android 앱 | ----> | Django Backend (API) | ----> | AI Services | ----> | External APIs |
| (Tasker 등) | HTTP | (DRF, Gunicorn) | | (Gemini, Perplexity)| | (Google, Notion)|
+-------------+ +----------------------+ +-------------------+ +-----------------+
| | ^ |
| | | |
v | | DB Operations | Notion API Calls
+----------------+ |
| Database | <------------------+
| (PostgreSQL) |
+----------------+
_(간단한 텍스트 기반 다이어그램 예시입니다. Draw.io 등으로 멋지게 그려서 이미지를 삽입하는 것을 추천합니다.)_

## 🚀 시작하기

### 1. 프로젝트 복제

```bash
git clone https://github.com/your-github-username/Aiuto.git # 실제 본인 레포 주소로 변경
cd Aiuto
Use code with caution.
2. 가상환경 생성 및 활성화
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Bash
3. 의존성 설치
pip install -r requirements.txt
Use code with caution.
Bash
4. .env 파일 설정
프로젝트 루트 디렉토리에 .env 파일을 생성하고 필요한 API 키 및 설정값을 입력합니다.
# .env
SECRET_KEY=your_django_secret_key_here  # Django 시크릿 키
DEBUG=True                             # 개발 환경에서는 True

# Notion API
NOTION_API_KEY=your_notion_integration_secret_key
NOTION_DATABASE_ID=your_notion_database_id_for_tasks

# Google AI API
GOOGLE_API_KEY=your_google_ai_studio_api_key

# Perplexity API (선택 사항)
PERPLEXITY_API_KEY=your_perplexity_api_key

# 배포용 PostgreSQL 설정 (나중에 추가)
# DATABASE_URL=postgresql://user:password@host:port/dbname
Use code with caution.
Dotenv
주의: .env 파일은 절대로 Git에 커밋하지 마세요! (.gitignore에 추가되어 있는지 확인)
5. 데이터베이스 마이그레이션
python manage.py migrate
Use code with caution.
Bash
6. 개발 서버 실행
python manage.py runserver
Use code with caution.
Bash
서버가 http://127.0.0.1:8000/ 에서 실행됩니다.
⚙️ 사용 방법
백엔드 서버를 실행합니다.
(예정) 안드로이드 Tasker 또는 다른 HTTP 클라이언트(Postman 등)를 사용하여 백엔드 API 엔드포인트(api/tasks/ 등)로 데이터를 전송합니다.
Request Body (예시): {"text": "4월 30일 이사 준비 시작"}
요청이 성공하면, 백엔드 시스템이 AI 처리를 거쳐 Notion의 지정된 데이터베이스에 새로운 작업 페이지가 생성되거나 업데이트됩니다. Notion에서 결과를 확인하세요.
🗺️ 프로젝트 구조 (예시)
Aiuto/
├── .github/                # GitHub Actions 워크플로우 (선택 사항)
├── aiuto/                  # Django 프로젝트 설정 디렉토리
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/                   # Django 앱 디렉토리
│   ├── core/               # 핵심 모델, 비즈니스 로직, 서비스
│   │   ├── models.py
│   │   ├── services/       # 비즈니스 로직, 외부 API 연동 (notion_service.py, ai_service.py 등)
│   │   ├── migrations/
│   │   └── ...
│   ├── api/                # Django REST Framework 관련 (serializers, views, urls)
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   └── (other_apps...)     # 필요시 추가 앱 (예: users, newsletter)
├── static/                 # 정적 파일 (CSS, JS, Images) - 필요시
├── templates/              # Django 템플릿 - 필요시
├── .env                    # 환경 변수 (Git 무시)
├── .gitignore              # Git 무시 목록
├── manage.py               # Django 관리 스크립트
├── requirements.txt        # Python 의존성 목록
└── README.md               # 현재 파일
Use code with caution.
🚀 향후 개선 계획
뉴스레터 기능 구현 (관심사 기반 뉴스 요약)
진행 상태 업데이트 기능 고도화 (Notion 상태 변경 연동)
음성 입력 기능 안정화 및 정확도 개선 (Tasker 외 다른 방법 탐색)
비동기 처리 도입 (Celery)으로 API 응답 속도 개선
단위 테스트 및 통합 테스트 코드 작성
사용자 인증 기능 추가 (다중 사용자 지원 고려 시)
좀 더 정교한 AI 프롬프트 엔지니어링 적용
프론트엔드 웹 인터페이스 개발 (선택 사항)
🤝 기여 방법 (Contribution)
(오픈소스 프로젝트가 아니므로 생략 가능, 또는 "개인 포트폴리오 프로젝트이므로 현재 기여는 받고 있지 않습니다." 로 명시)
📄 라이선스 (License)
이 프로젝트는 MIT 라이선스 하에 배포됩니다.
🧑‍💻 만든이
[본인 이름 또는 닉네임]
GitHub: [본인 GitHub 프로필 링크]
Email: [본인 이메일 주소]
Blog/Portfolio: [본인 블로그 또는 포트폴리오 링크 (선택)]
---

## 수정된 단계별 프로젝트 진행 계획 (README 반영)

**Phase 0: 준비 및 환경 설정 (README 작성 및 기본 틀 마련)**

1.  **GitHub 저장소 생성 및 README 작성:**
    *   GitHub에 `Aiuto` 저장소 생성.
    *   위에 제안된 README 초안을 바탕으로 프로젝트 설명, 목표, 기술 스택 등을 명확히 작성하고 커밋합니다. (`Jump-to-Django` 프로젝트에서 사용한 마크다운 스타일이나 구조를 참고해도 좋습니다.)
2.  **프로젝트 초기 설정:**
    *   로컬에 저장소 클론 (`git clone`).
    *   가상환경 생성 및 활성화 (`python -m venv venv`, `venv\Scripts\activate`).
    *   Django 프로젝트 생성 (`django-admin startproject aiuto .`).
    *   핵심 기능을 담을 `core` 앱 생성 (`python manage.py startapp core`). (`apps` 디렉토리를 만들어 그 안에 두는 것을 추천: `mkdir apps`, `cd apps`, `python ../manage.py startapp core`, `cd ..`)
    *   `settings.py`에 `apps.core` 추가.
3.  **API Key 관리 설정 (`python-dotenv`):**
    *   `pip install python-dotenv` 설치 및 `requirements.txt` 업데이트 (`pip freeze > requirements.txt`).
    *   프로젝트 루트에 `.env` 파일 생성 및 **.gitignore**에 `.env` 추가.
    *   `.env` 파일에 `SECRET_KEY`, `DEBUG` 설정. (다른 키는 추후 추가)
    *   `settings.py` 상단에 `load_dotenv()` 추가 및 `os.getenv()`로 `SECRET_KEY`, `DEBUG` 불러오도록 수정.

**Phase 1: Notion 연동 기반 구축**

1.  **Notion 설정 및 API 키 발급:**
    *   Notion Developers에서 Integration 생성 및 **API Secret Key** 획득.
    *   사용할 Notion 데이터베이스 생성 (예: 작업 관리 DB) 및 **Database ID** 확인.
    *   생성한 Integration을 해당 데이터베이스에 연결 및 권한 부여.
    *   `.env` 파일에 `NOTION_API_KEY`, `NOTION_DATABASE_ID` 추가. (`settings.py`에서도 `os.getenv()`로 불러오도록 설정)
2.  **Notion 클라이언트 설치 및 연동 테스트:**
    *   `pip install notion-client` 설치 및 `requirements.txt` 업데이트.
    *   `core` 앱 내에 `services` 폴더 생성 (`apps/core/services/`) 하고 `notion_service.py` 파일 생성.
    *   `notion_service.py`에 Notion 클라이언트 초기화 및 Notion 페이지 생성 함수 (`add_task_to_notion`) 작성 (이전 답변 참고).
    *   `python manage.py shell`에서 `from apps.core.services.notion_service import add_task_to_notion` 임포트 후, 테스트 페이지 생성 실행하여 Notion 연동 확인.

**Phase 2: Django 백엔드 핵심 개발 (API 기반)**

1.  **Django REST Framework (DRF) 설정:**
    *   `pip install djangorestframework` 설치 및 `requirements.txt` 업데이트.
    *   `settings.py`의 `INSTALLED_APPS`에 `rest_framework` 추가.
2.  **모델 정의 (`core/models.py`):**
    *   Notion DB 구조와 유사하게 작업(Task) 모델 정의 (예: `title`, `content`, `due_date`, `status`, `notion_page_id` 등). `notion_page_id` 필드는 Notion 페이지와 매핑을 위해 중요.
    *   `python manage.py makemigrations core` 및 `python manage.py migrate` 실행.
3.  **API 개발 (`api` 앱 생성 추천):**
    *   API 관련 코드를 분리하기 위해 `api` 앱 생성 (`python manage.py startapp api`). (`apps` 디렉토리 안에 생성)
    *   `settings.py`에 `apps.api` 추가.
    *   `api/serializers.py`: Task 모델에 대한 Serializer 작성. 사용자 입력을 받을 Serializer도 작성 (예: `TaskInputSerializer`).
    *   `api/views.py`: DRF의 `APIView` 또는 `ViewSet`을 사용하여 Task 생성/조회를 위한 API 엔드포인트 구현.
        *   **POST 요청 처리:** 사용자 입력(`text`)을 받아 -> `ai_service.py` (다음 단계) 호출하여 계획 생성 -> `notion_service.py` 호출하여 Notion에 기록 -> Notion 페이지 ID 등 결과 정보를 Task 모델에 저장 -> 성공 응답 반환.
    *   `api/urls.py`: API 엔드포인트 URL 정의.
    *   프로젝트 `urls.py` (`aiuto/urls.py`)에 `api/urls.py` 포함.
4.  **AI 서비스 구현 (`core/services/ai_service.py`):**
    *   Google AI Studio (Gemini) API 키를 `.env`에 추가 (`GOOGLE_API_KEY`) 및 `settings.py` 연동.
    *   `pip install google-generativeai` 설치 및 `requirements.txt` 업데이트.
    *   `ai_service.py` 파일 생성.
    *   Gemini API 호출 함수 (`generate_plan_with_gemini`) 작성 (JSON 형식 결과 요청).
    *   (선택) Perplexity API 연동 함수 (`research_with_perplexity`) 작성 (API 키 `.env` 추가 필요).
5.  **Postman/Insomnia 등으로 API 테스트:**
    *   백엔드 서버 실행 후, API 테스트 도구를 사용하여 `/api/tasks/` (예시) 엔드포인트로 POST 요청을 보내고, Notion에 정상적으로 페이지가 생성되는지, DB에 데이터가 저장되는지, 응답이 제대로 오는지 확인.

**Phase 3: 안드로이드 입력 연동 (Tasker)**

1.  **Tasker 설정 및 Django API 호출:**
    *   Tasker 설치 및 기본 사용법 익히기.
    *   Django 개발 서버를 외부에서 접근 가능하게 하기 위해 `ngrok` 설치 및 실행 (`ngrok http 8000`). ngrok 주소 확인.
    *   Tasker에 프로필/태스크 생성 (음성 인식 또는 위젯 버튼 트리거).
    *   Tasker의 'HTTP Request' 액션을 사용하여 ngrok 주소의 Django API 엔드포인트로 POST 요청 전송 설정 (Header에 `Content-Type: application/json`, Body에 `{"text": "%variable"}` 형식).
    *   **간단한 API 키 인증 추가:** 보안을 위해 `.env`에 `MY_SECRET_API_KEY` 정의하고, DRF View에 간단한 `BasePermission` 클래스를 만들어 헤더(`X-API-KEY`) 검증 로직 추가. Tasker 요청 헤더에도 `X-API-KEY` 추가.
2.  **연동 테스트:** 안드로이드에서 Tasker 태스크 실행 -> Django 서버 로그 확인 -> Notion 확인.

**Phase 4: 기능 고도화 및 유지보수**

1.  **뉴스레터 기능 (선택):**
    *   관련 모델 생성 (`NewsletterLog`), 뉴스 소스 선택 (RSS/News API), 스케줄링 방법 결정 (Django Management Command + OS 스케줄러 또는 Celery Beat).
    *   AI 요약 기능 추가 (`ai_service.py`), 결과를 DB에 저장하고 조회하는 API 엔드포인트 구현 (`api` 앱).
2.  **Notion 진행 상태 동기화 (선택):**
    *   Task 모델에 `status` 필드 추가, Notion DB에도 '상태' 속성 추가.
    *   Notion 페이지 상태 변경을 위한 API 엔드포인트 구현 (`api` 앱 - 예: `PATCH /api/tasks/{task_id}/`).
    *   `notion_service.py`에 페이지 업데이트 함수 추가 (`update_task_status`).
    *   (고급) 사용자가 "작업 완료" 라고 입력 시, 관련 작업을 찾아 Notion 상태를 업데이트하는 로직 추가.
3.  **코드 개선:**
    *   **비동기 처리:** AI/Notion API 호출 등 시간이 걸리는 작업을 Celery + Redis/RabbitMQ 사용하여 백그라운드로 처리 (API 응답 속도 향상).
    *   **오류 처리:** API 호출 실패, 데이터 검증 오류 등에 대한 예외 처리 로직 강화 및 로깅 추가.
    *   **테스트 코드:** DRF API, 핵심 서비스 로직에 대한 단위 테스트/통합 테스트 작성 (`pytest` 또는 `unittest`).

**Phase 5: 배포 (Render)**

1.  **배포 준비:**
    *   `DEBUG = False` 설정 및 `ALLOWED_HOSTS` 설정 (`settings.py`).
    *   데이터베이스 설정을 PostgreSQL로 변경 (`dj-database-url` 라이브러리 사용 추천). `.env`에 `DATABASE_URL` 추가.
    *   Static 파일 처리 설정 (`whitenoise`).
    *   `gunicorn` 설치 및 `Procfile` 생성 (Render에서 필요).
    *   `requirements.txt` 최종 업데이트.
2.  **Render 배포:**
    *   Render 회원가입 및 로그인.
    *   'New Web Service' 생성 -> GitHub 저장소 연결.
    *   Build Command (`pip install -r requirements.txt`), Start Command (`gunicorn aiuto.wsgi`) 설정.
    *   'New PostgreSQL', 'New Redis' 생성 (모두 Free Tier 선택).
    *   Render 환경 변수 설정 (DB URL, API 키 등 `.env` 내용).
    *   자동 배포 설정 및 배포 진행.
    *   배포된 URL로 접속하여 기능 테스트.
