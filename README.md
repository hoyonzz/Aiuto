**2025.04.24 주요변경점**
* **안드로이드 연동 방식 변경:** Tasker 대신 웹 인터페이스를 우선 구현한 내용을 반영
* **기술 스택 업데이트:** 'python-dotenv'대신 'django-environ'사용
* **사용 방법 변경:** 웹 브라우저 접속 방법으로 수정
* **시스템 아키텍처 업데이트:** 안드로이드 앱 대신 웹 브라우저가 백엔드와 상호작용하는 형태로 변경
* **향후 개선 계획 조정:** 웹 인터페이스 개선, 네이티브 앱 개발

# Aiuto (아이우토): 당신의 AI 조력자 🤖 Notion 자동화 비서

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org)
[![Django](https://img.shields.io/badge/Django-4.x-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.x-red?logo=django)](https://www.django-rest-framework.org/)
[![Notion API](https://img.shields.io/badge/Notion%20API-v1-lightgrey?logo=notion&logoColor=black)](https://developers.notion.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- 추가할 뱃지: 테스트 커버리지, 빌드 상태 등 -->

**Aiuto**는 바쁜 일상 속에서 놓치기 쉬운 할 일들을 **웹 인터페이스**를 통해 간편하게 기록하고, AI의 도움을 받아 체계적인 계획 수립과 필요한 정보 탐색을 자동화하여 Notion에 정리해주는 개인 맞춤형 AI 비서 프로젝트입니다. 최종적으로는 **모바일 애플리케이션 출시**를 목표로 하고 있습니다.

**(✨ 여기에 프로젝트 핵심 기능을 보여주는 GIF나 스크린샷을 추가하세요! ✨)**
*   _(예: 안드로이드 음성 입력 -> Notion에 자동 등록 및 계획 생성되는 모습)_
*   _(예: Notion에 정리된 작업 계획 및 진행 상황 화면)_

## 🎯 프로젝트 목표 및 동기

개인적인 생산성 향상을 위해 반복적인 계획 수립, 정보 검색, 기록 과정을 자동화하고 싶었습니다. 특히, 안드로이드 환경에서도 iOS의 단축어처럼 편리하게 외부 서비스(AI, Notion)와 연동되는 시스템을 구축하고자 이 프로젝트를 시작했습니다. 이 과정을 통해 Django 백엔드 개발 역량과 AI API 활용 능력, 그리고 외부 서비스 연동 경험을 심화시키는 것을 목표로 합니다.

## ✨ 주요 기능

*   **🌐 웹 기반 입력:** PC 또는 모바일 웹 브라우저를 통해 텍스트로 할 일, 아이디어 등을 간편하게 입력합니다.
*   **🧠 AI 기반 계획 수립:** 입력된 내용을 바탕으로 Google AI (Gemini)가 실행 가능한 세부 계획, 관련 속성(상태, 마감일, 카테고리, 중요도 등)을 제안합니다.
*   **📝 Notion 자동 기록/관리:** 생성된 계획과 속성은 지정된 Notion 데이터베이스에 자동으로 구조화되어 기록됩니다. (페이지 생성 및 속성 채우기)
*   **🔄 API 제공:** Django REST Framework를 사용하여 향후 모바일 앱 등 다른 클라이언트와의 연동을 위한 API 엔드포인트를 제공합니다. (`/api/tasks/create/`)
*   **🔍 AI 정보 탐색 (예정):** 계획 실행에 필요한 추가 정보를 Perplexity AI 등을 통해 검색하고 요약하여 Notion에 추가합니다.
*   **📊 진행 상태 관리 (예정):** Notion 페이지 업데이트 API 및 웹 인터페이스/앱을 통해 작업 진행 상태를 관리하고 동기화합니다.
*   **📰 맞춤 뉴스레터 (예정):** 관심 분야의 최신 뉴스를 수집하고 AI가 요약하여 제공하는 기능을 추가합니다.
*   **📱 모바일 앱 개발 (최종 목표):** 웹에서 검증된 기능을 바탕으로 사용자 친화적인 모바일 앱(Flutter/React Native 등)을 개발하여 출시합니다.

## 🛠️ 기술 스택

*   **Backend:** Python, Django, Django REST Framework (DRF)
*   **Frontend (초기):** Django Templates, HTML, CSS
*   **Database:** SQLite (개발), PostgreSQL (배포 예정)
*   **AI APIs:** Google AI Studio (Gemini API), Perplexity API (예정)
*   **Notion Integration:** `notion-client` Python library
*   **API Key Management:** `django-environ`
*   **Deployment (예정):** Render (Free Tier 활용)
*   **(Optional) Asynchronous Tasks:** Celery, Redis

## 🏗️ 시스템 아키텍처 (예시)

```
+---------------+       +----------------------+       +-------------------+       +-----------------+
| Web Browser   | ----> | Django Backend       | ----> | AI Services       | ----> | External APIs   |
| (HTML Form)   | HTTP  | (Django Views, DRF)  |       | (Gemini, Perplexity)|       | (Google, Notion)|
+---------------+       +----------------------+       +-------------------+       +-----------------+
                          |        | ^                    |
                          |        | |                    |
                          v        | | DB Operations      | Notion API Calls
                      +----------------+                    |
                      | Database       | <------------------+
                      | (PostgreSQL)   |
                      +----------------+
```

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
1.  **백엔드 서버**를 실행합니다 (`python manage.py runserver`).
2.  웹 브라우저를 열고 `http://127.0.0.1:8000/` (또는 설정된 URL) 로 접속합니다.
3.  입력 폼에 할 일이나 아이디어를 텍스트로 입력하고 'AI 비서에게 전달' 버튼을 클릭합니다.
4.  요청이 성공하면, 백엔드 시스템이 AI 처리를 거쳐 **Notion**의 지정된 데이터베이스에 새로운 작업 페이지가 생성되고, 웹 페이지에 성공 메시지가 표시됩니다. Notion에서 결과를 확인하세요.
5.  **(개발/테스트용)** Postman 같은 도구를 사용하여 `/api/tasks/create/` 엔드포인트로 직접 POST 요청을 보낼 수도 있습니다.

🗺️ 프로젝트 구조 
```
Aiuto/
├── .github/
├── aiuto/                  # Django 프로젝트 설정 디렉토리
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/                   # Django 앱 디렉토리
│   ├── core/               # 핵심 모델, 웹 Views, 서비스
│   │   ├── models.py
│   │   ├── views.py        # 웹 페이지 처리 View (task_input_view)
│   │   ├── services/       # 비즈니스 로직, 외부 API 연동 (task_service.py, notion_service.py, ai_service.py)
│   │   ├── urls.py         # 웹 페이지용 URL 설정
│   │   └── ...
│   ├── api/                # Django REST Framework 관련
│   │   ├── serializers.py
│   │   ├── views.py        # API 엔드포인트 View (TaskCreateAPIView)
│   │   ├── urls.py         # API용 URL 설정
│   │   └── ...
│   └── (other_apps...)
├── static/                 # (선택) CSS, JS 등 정적 파일
├── templates/              # Django 템플릿
│   └── core/
│       └── input_form.html # 웹 입력 폼 템플릿
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 향후 개선 계획
*   [ ] **웹 인터페이스 개선:** CSS 스타일링 추가, 입력 피드백 강화, 최근 작업 목록 표시 등
*   **[ ] ✨ AI 결과 기반 상호작용 기능 (웹):**
    *   [ ] 웹 페이지에 AI가 생성한 세부 계획(details) 표시
    *   [ ] 사용자가 표시된 계획을 보고 수정/추가 지시를 입력하는 인터페이스 구현
    *   [ ] 백엔드에서 대화 히스토리 또는 이전 Task 정보를 참조하여 AI 재호출 및 계획 업데이트 로직 구현
*   [ ] **Notion 페이지 업데이트 기능:** 웹/API 통해 작업 상태 변경 및 Notion 반영
*   [ ] **AI 정보 탐색 기능:** Perplexity API 연동 및 결과 표시
*   [ ] **뉴스레터 기능:** 관심사 설정, 뉴스 수집/요약, 웹 페이지 표시
*   [ ] **비동기 처리 도입 (Celery):** AI/Notion API 호출 시 웹 페이지/API 응답 속도 개선
*   [ ] **자동화된 테스트 코드 작성:** `tests.py` 활용하여 핵심 기능 검증
*   [ ] **사용자 인증 기능:** 회원가입/로그인 기능 추가 (다중 사용자 지원)
*   [ ] **모바일 앱 개발:** Flutter/React Native 등을 이용한 네이티브 앱 개발 (최종 목표)
*   [ ] **음성 입력 기능 추가:** 웹 Speech API 또는 앱의 음성 인식 기능 활용
*   [ ] **(고급) 카테고리별 프롬프트 분기:** 작업 유형에 따라 최적화된 프롬프트를 사용하여 AI 응답 품질 향상
```

**(✨ AI 결과 기반 상호작용 기능 추가)**



🧑‍💻 만든이
[신호용]
GitHub: [https://github.com/hoyonzz/Aiuto/tree/main]
Email: [hoyong0511@naver.com]
