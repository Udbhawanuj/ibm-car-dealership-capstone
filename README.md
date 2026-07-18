# DriveSphere — IBM Cars Dealership Full-Stack Capstone

**Project name:** DriveSphere Cars Dealership Review Portal  
**Course:** IBM Full Stack Software Developer Capstone

This repository is a complete, self-contained Django dealership application prepared to run locally, pass GitHub Actions, build with Docker, and deploy to IBM Cloud Code Engine.

## What is included

- Responsive dealership landing page with state filtering
- User registration, login, logout, and visible logged-in username
- Dealer details and customer reviews
- Authenticated review submission
- Positive/neutral/negative sentiment analysis
- Django Admin with seeded root user
- About Us and Contact Us pages
- REST-style API endpoints used by the rubric
- GitHub Actions CI workflow
- Dockerfile and IBM Code Engine deployment helpers
- One-click local setup scripts
- Automatic generation of real local cURL evidence files

## Fastest way to run

### Windows

Double-click:

```text
RUN_PROJECT_WINDOWS.bat
```

### Linux/macOS

```bash
chmod +x RUN_PROJECT_LINUX_MAC.sh
./RUN_PROJECT_LINUX_MAC.sh
```

Then open:

- Application: `http://127.0.0.1:8000/`
- Django Admin: `http://127.0.0.1:8000/admin/`
- Health check: `http://127.0.0.1:8000/health/`

## Demo credentials

| Role | Username | Password |
|---|---|---|
| Reviewer | `reviewer` | `Reviewer@123` |
| Root admin | `root` | `Root@123` |

## Generate real cURL evidence automatically

You do not need to type each request manually.

### Windows

Double-click:

```text
CREATE_ALL_LOCAL_EVIDENCE_WINDOWS.bat
```

### Linux/macOS

```bash
./CREATE_ALL_LOCAL_EVIDENCE_LINUX_MAC.sh
```

The script starts the Django server, sends real HTTP requests, and writes these files into `evidence/`:

- `django_server`
- `loginuser`
- `logoutuser`
- `getdealerreviews`
- `getalldealers`
- `getdealerbyid`
- `getdealersbyState`
- `getallcarmakes`
- `analyzereview`

The logout evidence uses a real **GET** request and includes the logged-out username. The sentiment evidence uses a real **POST** request to `/djangoapp/analyzeReview/` with the text `Fantastic services`.

## Important API endpoints

| Purpose | Method | Endpoint |
|---|---|---|
| Login | POST | `/djangoapp/login` |
| Logout | GET or POST | `/djangoapp/logout/` |
| All dealers | GET | `/djangoapp/get_dealers/` |
| Kansas dealers | GET | `/djangoapp/get_dealers/KS` |
| Dealer details | GET | `/djangoapp/dealer/1` |
| Dealer reviews | GET | `/djangoapp/reviews/dealer/1` |
| Car makes and models | GET | `/djangoapp/get_cars` |
| Sentiment | POST | `/djangoapp/analyzeReview/` |
| Add review | POST | `/djangoapp/add_review` |

Compatibility aliases with and without trailing slashes are included.

## Run manually

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r server/requirements.txt
cd server
python manage.py migrate
python manage.py seed_demo
python manage.py runserver 0.0.0.0:8000
```

## Test the project

```bash
cd server
python manage.py check
python manage.py test --verbosity 2
```

## Docker

```bash
docker build -t cars-dealership:latest .
docker run --rm -p 8000:8000 cars-dealership:latest
```

The container automatically runs migrations, seeds demo data, collects static files, and starts Gunicorn.

## GitHub Actions

Upload the **contents of this folder directly to the repository root**. Do not place the whole project inside another folder.

The workflow `.github/workflows/ci.yml` runs:

1. Checkout Repository
2. Setup Python 3.13
3. Install Dependencies
4. Run Django System Check
5. Run Django Migrations
6. Seed Demo Data
7. Run Unit Tests
8. Validate Required Frontend Files
9. Collect Static Files
10. Build Docker Image

It also supports manual execution through **Actions → Car Dealership CI → Run workflow**.

## IBM Cloud Code Engine

Inside the Skills Network Code Engine CLI:

```bash
cd IBM_Car_Dealership_Capstone_Complete
./DEPLOY_CODE_ENGINE_FROM_LOCAL.sh cars-dealership
```

Or deploy from a public GitHub repository:

```bash
./DEPLOY_CODE_ENGINE_FROM_GITHUB.sh \
  https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git \
  cars-dealership
```

The script saves the real public URL in `evidence/deploymentURL`.

## Screenshots

Follow [CAPTURE_SCREENSHOTS.md](CAPTURE_SCREENSHOTS.md). It lists the exact local and deployed screenshots, filenames, URLs, and login states required.

## Required GitHub URLs

After uploading to a public repository, the code URLs follow these patterns:

```text
https://github.com/USERNAME/REPOSITORY/blob/main/README.md
https://github.com/USERNAME/REPOSITORY/blob/main/server/frontend/static/About.html
https://github.com/USERNAME/REPOSITORY/blob/main/server/frontend/static/Contact.html
https://github.com/USERNAME/REPOSITORY/blob/main/server/frontend/src/components/Register/Register.jsx
```

## Project structure

```text
.
├── .github/workflows/ci.yml
├── Dockerfile
├── entrypoint.sh
├── RUN_PROJECT_WINDOWS.bat
├── RUN_PROJECT_LINUX_MAC.sh
├── CREATE_ALL_LOCAL_EVIDENCE_WINDOWS.bat
├── CREATE_ALL_LOCAL_EVIDENCE_LINUX_MAC.sh
├── DEPLOY_CODE_ENGINE_FROM_LOCAL.sh
├── DEPLOY_CODE_ENGINE_FROM_GITHUB.sh
├── evidence/
├── screenshots/
├── scripts/
└── server/
```

The project does not include fabricated cloud evidence. GitHub Actions logs, deployment URL, and deployed screenshots are generated from your own accounts when you run the included workflow and deployment scripts.
