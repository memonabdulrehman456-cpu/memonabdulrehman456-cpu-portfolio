from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static",
)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

# ----------------------------------------------------------------------
# All portfolio content lives here. Edit this data to update the site —
# the templates render it automatically, no HTML editing required.
# ----------------------------------------------------------------------

PROFILE = {
    "name": "Abdul Rehman",
    "role": "Aspiring Data Scientist · AI Enthusiast · Python Developer",
    "location": "Hyderabad, Sindh, Pakistan",
    "email": "memonabdulrehman456@gmail.com",
    "phone": "+92 315 6711525",
    "phone_href": "+923156711525",
    "linkedin": "https://www.linkedin.com/in/memonabdulrehman456",
    "github": "https://github.com/memonabdulrehman456-cpu",
}

FACTS = [
    {"k": "location", "v": "Hyderabad, PK"},
    {"k": "learning_at", "v": "SMIT"},
    {"k": "degree", "v": "ADS · 2026–2028"},
    {"k": "focus_area", "v": "Data Science & AI"},
    {"k": "open_to", "v": "Internships, Freelance"},
    {"k": "tools", "v": "VS Code, Jupyter, Colab"},
]

SKILLS = [
    {
        "category": "Programming",
        "tags": ["Python", "SQL", "HTML", "CSS"],
        "level": 75,
    },
    {
        "category": "Data Science",
        "tags": ["Data Cleaning", "EDA", "Statistical Analysis", "Data Viz"],
        "level": 70,
    },
    {
        "category": "Libraries",
        "tags": ["Pandas", "NumPy", "Matplotlib", "Seaborn"],
        "level": 70,
    },
    {
        "category": "AI / ML",
        "note": "in progress",
        "tags": ["Machine Learning", "Predictive Analytics", "Model Dev"],
        "level": 40,
    },
    {
        "category": "Tools",
        "tags": ["Git/GitHub", "VS Code", "Jupyter", "Excel"],
        "level": 80,
    },
]

PROJECTS = [
    {
        "num": 1,
        "slug": "student_result_analysis",
        "emoji": "📊",
        "title": "Student Result Analysis",
        "desc": "A complete data analysis project evaluating student performance — covering data cleaning, visualization, and insight-driven reporting.",
        "stack": ["Python", "Pandas", "Matplotlib", "Excel"],
    },
    {
        "num": 2,
        "slug": "sales_data_analysis",
        "emoji": "📈",
        "title": "Sales Data Analysis",
        "desc": "A sales analytics project exploring revenue trends, customer behavior, and business insights to support data-driven decisions.",
        "stack": ["Python", "Pandas", "NumPy", "Matplotlib"],
    },
    {
        "num": 3,
        "slug": "smart_file_organizer",
        "emoji": "📂",
        "title": "Smart File Organizer",
        "desc": "A Python automation tool that sorts files into folders automatically based on file extension — built to save real time.",
        "stack": ["Python", "OS Module", "Automation"],
    },
]

EDUCATION = [
    {
        "year": "2026 – 2028 · Currently Studying",
        "name": "Associate Degree in Science (ADS)",
        "org": "Muslim College",
    },
    {
        "year": "Completed",
        "name": "Intermediate",
        "org": "Board of Intermediate Education Hyderabad",
    },
    {
        "year": "Completed",
        "name": "Matriculation",
        "org": "Board of Secondary Education Hyderabad",
    },
]

CERTS = [
    {"title": "🏆 Python Essentials 1", "org": "Cisco Networking Academy & OpenEDG"},
    {"title": "🏆 Python Essentials 2", "org": "Cisco Networking Academy & OpenEDG"},
    {"title": "🏆 Microsoft Office", "org": "Word, Excel & PowerPoint — Horizon Academy"},
    {"title": "🏆 Certified Computer Operator", "org": "CCO"},
    {
        "title": "📘 Data Science & AI",
        "org": "Saylani Mass IT Training (SMIT)",
        "note": "in progress",
        "highlight": True,
    },
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        facts=FACTS,
        skills=SKILLS,
        projects=PROJECTS,
        education=EDUCATION,
        certs=CERTS,
        year=datetime.now().year,
    )


@app.route("/contact", methods=["POST"])
def contact():
    """Handles the contact form submission.

    No outbound email service is configured yet, so this just validates
    the input and confirms receipt. Wire up an email provider (e.g.
    Resend, SendGrid, or SMTP) here when you're ready to receive real
    messages from this route.
    """
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in every field before sending.", "error")
        return redirect(url_for("home") + "#contact")

    # TODO: send this via an email provider once one is configured.
    print(f"New contact message from {name} <{email}>: {message}")

    flash("Thanks! Your message has been received.", "success")
    return redirect(url_for("home") + "#contact")


# Local development entry point (Vercel imports `app` directly and never
# runs this block).
if __name__ == "__main__":
    app.run(debug=True, port=5000)
