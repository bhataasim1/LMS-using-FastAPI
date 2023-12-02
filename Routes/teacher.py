from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from Models.teacher_model import Teacher

router = APIRouter(prefix="/teacher", tags=["Teacher"])
templates = Jinja2Templates(directory="Frontend/teacher")


# This is the Route for the Register Teacher
@router.post("/register")
async def register(request: Request):
    form_data = await request.form()
    name = form_data.get("name")
    username = form_data.get("username")
    password = form_data.get("password")

    existing_user = await Teacher.get_or_none(username=username)
    if existing_user:
        return templates.TemplateResponse("registerTeacher.html", {"request": request, "error": "User already exists"})

    await Teacher.create(name=name, username=username, password=password)

    return RedirectResponse(url="/teacher/login", status_code=302)


# This is the Route for the Login Teacher
@router.post("/login")
async def login(request: Request):
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")

    user = await Teacher.filter(username=username).first()
    if not user:
        return templates.TemplateResponse("loginTeacher.html", {"request": request, "error": "Invalid Credentials"})

    if user.password != password:
        return templates.TemplateResponse("loginTeacher.html", {"request": request, "error": "Invalid Credentials"})

    return RedirectResponse(url="/course/allcourses", status_code=302)
