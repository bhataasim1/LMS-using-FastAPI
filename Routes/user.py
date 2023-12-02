from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from Models.course_model import Course
from Models.user_model import User

router = APIRouter(prefix="/user", tags=["User"])
templates = Jinja2Templates(directory="Frontend")

# This is the Route for the Register user
@router.post("/register")
async def register(request: Request):
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")

    existing_user = await User.get_or_none(username=username)
    if existing_user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "User already exists"})

    await User.create(username=username, password=password)

    return RedirectResponse(url="/login", status_code=302)


# This is the Route for the Login user
@router.post("/login")
async def login(request: Request):
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")

    user = await User.filter(username=username).first()
    if not user:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid Credentials"})

    if user.password != password:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid Credentials"})

    return RedirectResponse(url="/user/dashboard", status_code=302)


# This is the Route for the Dashboard of user
@router.get("/dashboard")
async def dashboard(request: Request):
    courses = await Course.all()
    return templates.TemplateResponse("dashboard.html", {"request": request, "courses": courses})