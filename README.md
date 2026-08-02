# Abdul Rehman — Portfolio (Flask)

A Flask-powered portfolio site, ready to deploy on Vercel.

## Project structure

```
portfolio/
├── api/
│   └── index.py        # Flask app + all content data (edit this to update the site)
├── templates/
│   └── index.html       # Jinja2 template
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
├── vercel.json           # Vercel routing config
└── README.md
```

## Run locally

```bash
pip install -r requirements.txt
python api/index.py
```

Then open http://localhost:5000

## Deploy to Vercel

**Option A — Vercel CLI**

```bash
npm install -g vercel
cd portfolio
vercel
```

Follow the prompts (link/create a project). Then run `vercel --prod` to push to production.

**Option B — GitHub + Vercel dashboard**

1. Push this folder to a GitHub repo.
2. Go to https://vercel.com/new and import the repo.
3. Vercel auto-detects `vercel.json` and the Python runtime — no extra config needed.
4. Click **Deploy**. You'll get a live `https://your-project.vercel.app` URL.

## Editing content

All text, skills, projects, education, and certifications live in
`api/index.py` as plain Python lists/dicts (`PROFILE`, `SKILLS`,
`PROJECTS`, `EDUCATION`, `CERTS`). Edit the data there — the template
renders it automatically.

## Contact form

The form on the site posts to `/contact` in `api/index.py`. Right now it
just validates the input and logs it — no email is actually sent yet.
To receive real messages, wire up an email provider (e.g. Resend,
SendGrid, or SMTP) inside the `contact()` view where the `TODO` comment
is.
