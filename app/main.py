from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise
from Routes.user import router as UserRouter
from Routes.course import router as CourseRouter
from Routes.teacher import router as TeacherRouter


app = FastAPI()
templates = Jinja2Templates(directory="Frontend")
teacherTemplates = Jinja2Templates(directory="Frontend/teacher")

# These are the routes that we have created
app.include_router(CourseRouter)
app.include_router(UserRouter)
app.include_router(TeacherRouter)


# This is the database connection using Tortoise ORM with SQLite
register_tortoise(
    app,
    db_url="sqlite://LMS.db",
    modules={"models": ["Models.user_model", "Models.course_model", "Models.teacher_model"]},
    generate_schemas=True,
    add_exception_handlers=True
)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# @app.get("/dashboard")
# def dashboard_page(request: Request):
#     return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/teacher/register")
def course_page(request: Request):
    return teacherTemplates.TemplateResponse("registerTeacher.html", {"request": request})


@app.get("/teacher/login")
def course_page(request: Request):
    return teacherTemplates.TemplateResponse("loginTeacher.html", {"request": request})


@app.get("/teacher")
def course_page(request: Request):
    return teacherTemplates.TemplateResponse("loginTeacher.html", {"request": request})