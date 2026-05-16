# IntervAI ✦

> AI-powered interview question generator — built with Gemini, FastAPI, and vanilla HTML.

---

## What it does

IntervAI takes a job title and instantly generates 3 thoughtful, role-specific interview questions using Google's Gemini AI. Questions vary by type — behavioural, situational, and role-specific knowledge — so you walk into every interview prepared.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, Vanilla JS |
| Backend | Python, FastAPI |
| AI | Google Gemini (`google-generativeai`) |
| Server | Uvicorn |
| Deployment | Vercel (frontend) · Railway (backend) |

---

## Project Structure

```
IntervAI/
├── backend/
│   ├── chat.py          # FastAPI app + Gemini integration
│   ├── requirements.txt # Python dependencies
│   └── .env             # API keys (never commit this)
├── frontend/
│   └── index.html       # Full frontend — single file
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- A Google Gemini API key — get one free at [ai.google.dev](https://ai.google.dev)

### 1. Clone the repo

```bash
git clone https://github.com/Di-nobi/IntervAI.git
cd IntervAI
```

### 2. Set up the virtual environment

```bash
python3 -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside the `backend/` folder:

```bash
touch backend/.env
```

Add your Gemini API key:

```
API_KEY=your-gemini-api-key-here
```

### 5. Run the backend

```bash
uvicorn backend.chat:app --reload
```

The API will be live at `http://localhost:8000`.

### 6. Open the frontend

Open `frontend/index.html` directly in your browser. That's it — no build step needed.

---

## API Reference

### `POST /generate`

Generates 3 interview questions for a given job title.

**Request body:**
```json
{
  "jobTitle": "Customer Success Manager"
}
```

**Response:**
```json
{
  "questions": [
    "How do you handle a situation where a customer is at risk of churning?",
    "Walk me through how you prioritise accounts when your portfolio is large.",
    "What metrics do you use to define and measure customer success?"
  ]
}
```

### `GET /health`

Returns the health status of the API.

```json
{ "status": "ok" }
```

---

## Deployment

### Backend → Railway

1. Push your code to GitHub
2. Go to [railway.app](https://railway.app) and create a new project from your repo
3. Set the root directory to `backend/`
4. Add your `API_KEY` under **Variables**
5. Set the start command to:
   ```
   uvicorn chat:app --host 0.0.0.0 --port $PORT
   ```

### Frontend → Vercel

1. Go to [vercel.com](https://vercel.com) and import your GitHub repo
2. Set the root directory to `frontend/`
3. Update `BACKEND_URL` in `index.html` to your Railway URL:
   ```js
   const BACKEND_URL = "https://your-app.up.railway.app";
   ```
4. Deploy — Vercel handles the rest.

---

## Environment Variables

| Variable | Description |
|---|---|
| `API_KEY` | Your Google Gemini API key |

> ⚠️ Never commit your `.env` file. It's already in `.gitignore`.

---

## Roadmap

- [ ] Follow-up question drilldown per question
- [ ] Full interview kit — questions + ideal answers + red flags
- [ ] Difficulty level toggle (Junior / Mid / Senior)
- [ ] Export questions as PDF
- [ ] Question history with localStorage
- [ ] Candidate answer evaluator

---

## License

MIT — do whatever you want with it.

---

<p align="center">Built by <a href="https://github.com/Di-nobi">Di-nobi</a> · Powered by Gemini</p>