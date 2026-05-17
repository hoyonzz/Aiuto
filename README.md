**2025.04.26 핵심변경사항**
* **배포 완료:** Render 배포 성공 https://aiuto-web.onrender.com/
* **기술 스택 업데이트:** PostgreSQL, Gunicorn, Whitenoise 
* **핵심 기능 상세화:** AI가 제안하는 속성들, Notion '세부 계획 요약' 연동
* **DB 역할 명확화:** PostgreSQL 사용



# Aiuto (아이우토): 당신의 AI 조력자 🤖 Notion 자동화 비서

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org)
[![Django](https://img.shields.io/badge/Django-5.2-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.15-red?logo=django)](https://www.django-rest-framework.org/)
[![Notion API](https://img.shields.io/badge/Notion%20API-v1-lightgrey?logo=notion&logoColor=black)](https://developers.notion.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-brightgreen?logo=render)](https://render.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Aiuto**는 바쁜 일상 속에서 놓치기 쉬운 할 일들을 **웹 인터페이스**를 통해 간편하게 기록하면, **Google AI (Gemini)** 의 도움을 받아 체계적인 실행 계획과 관련 정보(마감일, 중요도, 카테고리 등)를 자동으로 생성하여 **Notion 데이터베이스에 깔끔하게 정리**해주는 개인 맞춤형 AI 비서 프로젝트입니다.

**🚀 배포된 웹사이트:** [https://aiuto-web.onrender.com](https://aiuto-web.onrender.com)

**(✨ 프로젝트 핵심 기능 시연 GIF ✨)**
![Image](https://github.com/user-attachments/assets/2ec04b5c-fe31-469d-9610-74fff5dea0d0)

## 🎯 프로젝트 목표 및 진행 과정

개인의 생산성 향상을 목표로, 반복적인 계획 수립 및 기록 과정을 자동화하고자 이 프로젝트를 시작했습니다. 초기에는 안드로이드 연동을 구상했으나, **서비스 접근성, 빠른 프로토타이핑, 그리고 향후 앱 개발 확장성**을 고려하여 **웹 기반 인터페이스를 우선 구현**하는 방향으로 진행했습니다.

개발 과정에서 **환경 변수 관리(`django-environ`), Notion API 연동 문제 해결, AI 프롬프트 엔지니어링, PostgreSQL 데이터베이스 설정, 그리고 클라우드 플랫폼(Render) 배포** 등 다양한 백엔드 개발 과제를 경험하고 해결하며 핵심 기능을 완성했습니다. 이 과정을 통해 얻은 문제 해결 능력과 실무 기술을 포트폴리오에 담고자 합니다. 최종적으로는 **사용자 친화적인 모바일 애플리케이션 출시**를 목표로 하고 있습니다.

## ✨ 주요 기능 (현재 구현됨)

*   **🌐 웹 기반 작업 입력:** 간단한 웹 페이지 폼을 통해 할 일, 아이디어 등을 텍스트로 입력 받습니다.
*   **🧠 AI 기반 자동 계획 및 속성 제안:** 입력된 텍스트를 Google Gemini AI가 분석하여 다음과 같은 정보를 포함한 구조화된 계획을 생성합니다.
    *   **작업 제목 (Title):** 명확하고 간결한 작업 제목.
    *   **세부 계획 (Details):** 실행 가능한 단계별 계획 (Markdown 형식), 필요시 사전 확인 사항 제안.
    *   **상태 (Status):** '예정', '후속조치' 등 초기 상태 제안.
    *   **마감일/시간 (Due Date):** 사용자 입력 기반 날짜/시간 인식 및 ISO 8601/YYYY-MM-DD 형식 변환 (UTC 기준).
    *   **카테고리 (Categories):** 미리 정의된 옵션 중에서 관련 카테고리 복수 제안.
    *   **중요도 (Priority):** '긴급', '중요', '나중' 우선순위 제안.
*   **📝 Notion 자동 기록:** AI가 생성한 모든 정보(제목, 세부 계획, 상태, 날짜, 카테고리, 중요도 등)를 지정된 Notion 데이터베이스에 **정확한 속성으로 매핑하여 새로운 페이지를 자동으로 생성**합니다. **'세부 계획 요약'** 속성을 통해 데이터베이스 뷰에서도 내용을 바로 확인할 수 있습니다.
*   **💾 데이터베이스 저장:** 생성된 작업 정보와 Notion 페이지 ID를 **PostgreSQL 데이터베이스**에 저장하여 관리합니다.
*   **☁️ 클라우드 배포:** **Render** 플랫폼에 성공적으로 배포되어 웹 URL을 통해 실제 서비스로 이용 가능합니다.
*   **🔌 API 엔드포인트 제공:** Django REST Framework 기반의 Task 생성 API (`/api/tasks/create/`)를 제공하며, 향후 모바일 앱 등 다른 클라이언트와의 연동 기반을 마련했습니다.

## 🛠️ 기술 스택

*   **Backend:** Python (3.12), Django (5.2), Django REST Framework (3.15), Gunicorn
*   **Frontend (Web Interface):** Django Templates, HTML, CSS
*   **Database:** PostgreSQL (Render), SQLite (Local Fallback)
*   **AI API:** Google AI Studio (Gemini 1.5 Pro)
*   **Notion Integration:** `notion-client` (2.3.0)
*   **Environment Variables:** `django-environ` (0.12.0)
*   **WSGI Server:** `gunicorn` (23.0.0)
*   **Static Files:** `whitenoise` (6.9.0)
*   **DB Connector:** `psycopg2-binary` (2.9.10)
*   **Deployment:** Render
*   **IDE & Tools:** VS Code, Git, GitHub, Postman, pgAdmin

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

## 🚀 시작하기(로컬 개발 환경)

### 1. 프로젝트 복제
```bash
git clone https://github.com/hoyonzz/Aiuto.git
cd Aiuto
```
### 2. 가상환경 생성 및 활성화

### 3. 의존성 설치
```
pip install -r requirements.txt
```
### 4. PostgreSQL 설정 (로컬)
*   로컬에 PostgreSQL 설치 및 실행.
*   `aiuto_db` 데이터베이스 및 `aiuto_user` 생성 (비밀번호 설정).
*   `aiuto_user`에게 `aiuto_db`의 `public` 스키마에 대한 `USAGE`, `CREATE` 권한 부여.

### 5. `.env` 파일 설정
* 프로젝트 루트에 `.env` 파일을 생성하고 다음 형식으로 값을 입력합니다.

### 6. 데이터베이스 마이그레이션

### 7. 개발 서버 실행

⚙️ 사용 방법
1.  **배포된 웹사이트 접속:** [https://aiuto-web.onrender.com](https://aiuto-web.onrender.com)로 접속합니다.
2.  **텍스트 입력:** 입력 폼에 할 일, 아이디어 등을 자연스러운 문장으로 입력합니다.
3.  **전달:** 'AI 비서에게 전달' 버튼을 클릭합니다.
4.  **결과 확인:** 잠시 후 페이지에 성공 메시지가 표시되고, 연결된 **Notion 데이터베이스**에 새로운 작업 페이지가 AI가 제안한 속성들과 함께 생성됩니다.

## 🗺️ 프로젝트 구조 
```
Aiuto/
├── aiuto/                  # Django 프로젝트 설정 디렉토리
├── apps/                   # Django 앱 디렉토리
│   ├── core/               # 핵심 모델, 웹 Views, 서비스, 웹 URL
│   └── api/                # API 엔드포인트 관련
├── templates/              # Django 템플릿
│   └── core/
│       └── input_form.html
├── staticfiles/            # collectstatic으로 생성됨 (Git 무시)
├── .env                    # 환경 변수 (Git 무시)
├── .gitignore
├── manage.py
├── Procfile                # Gunicorn 실행 설정
├── requirements.txt
└── README.md

```

## 💡 개발 과정 및 주요 해결 과제

이 프로젝트를 진행하면서 발생했던 주요 이슈들과 해결 과정은 **[GitHub Issues 탭](https://github.com/hoyonzz/Aiuto/issues)** 에 기록되어 있습니다.
*   환경 변수 관리 방법 결정 (`django-environ` 도입)
*   Notion API 연동 오류 해결 (인증, 속성 매핑, 데이터 형식 등)
*   AI 프롬프트 엔지니어링을 통한 결과 개선 (날짜/시간 처리, 중요도 판단 등)
*   PostgreSQL 설정 및 마이그레이션 오류 해결 (권한 문제)
*   배포 환경에서의 정적 파일 처리 (`whitenoise`) 및 WSGI 서버(`Gunicorn`) 설정
*   클라우드 플랫폼(Render) 배포 및 트러블슈팅 (타임존, 의존성 문제 등)

이러한 문제 해결 과정을 통해 실무적인 백엔드 개발 및 배포 역량을 강화할 수 있었습니다.

## 🚀 향후 개선 계획
*   **✨ AI 결과 기반 상호작용 기능 (웹):** AI 생성 계획을 웹에 표시하고 사용자 피드백을 받아 계획을 수정/보완하는 기능 (최우선 순위)
*   **🔄 Notion 페이지 업데이트 기능:** 웹/API 통해 작업 상태('완료' 등) 변경 및 Notion 반영.
*   **⏰ 날짜/시간 처리 고도화:** AI가 놓치는 정보 Python 로직 처리, UTC 시간 변환 기능 추가.
*   **📊 중요도/카테고리 정확도 향상:** 지속적인 프롬프트 튜닝 및 사용자 피드백 반영.
*   **🔍 AI 정보 탐색 기능:** Perplexity 등 외부 검색 API 연동.
*   **📰 맞춤 뉴스레터 기능:** 관심사 기반 뉴스 수집 및 요약.
*   **⚡ 비동기 처리 (Celery):** AI/Notion API 호출 시 응답 속도 개선.
*   **✅ 자동화된 테스트 코드 작성:** `tests.py` 활용하여 안정성 확보.
*   **👤 사용자 인증 기능:** 회원가입/로그인 기능.
*   **📱 모바일 앱 개발 (최종 목표):** Flutter/React Native 등 활용.
*   **🗣️ 음성 입력 기능:** 웹 Speech API 또는 앱 기능 활용.
*   **💡 (고급) 카테고리별 프롬프트 분기**


🧑‍💻 만든이
[신호용]
GitHub: [https://github.com/hoyonzz/Aiuto/tree/main]
Email: [hoyong0511@naver.com]
