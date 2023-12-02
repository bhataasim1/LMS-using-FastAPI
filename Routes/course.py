from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from Models.course_model import Course
from Schema.course_schema import getCourseSchema, createCourse, updateCourse

router = APIRouter(prefix="/course", tags=["Course"])
templates = Jinja2Templates(directory="Frontend")
courseTemplate = Jinja2Templates(directory="Frontend/course")

# This function is used to render the createCourse.html page
@router.get("/")
def course_page(request: Request):
    return templates.TemplateResponse("createCourse.html", {"request": request})


# This function is used to render the course.html page with all the courses created
@router.get("/allcourses", response_model=list[getCourseSchema])
async def get_all_courses(request: Request):
    courses = await Course.all()
    return courseTemplate.TemplateResponse("course.html", {"request": request, "courses": courses})


# This function is used to render the course.html page with the course that has the id passed in the url
# @router.get("/{id}", response_model=getCourseSchema)
# async def get_course(id: int, request: Request):
#     # course = await Course.get(id=id)
#     course = await Course.filter(id=id).first()
#     return courseTemplate.TemplateResponse("course.html", {"request": request, "course": course})


# This function is used to create a course
@router.post("/create", response_model=getCourseSchema)
async def create_course(request: Request):
    form = await request.form()
    title = form.get("title")
    description = form.get("description")
    instructor = form.get("instructor")
    await Course.create(title=title, description=description, instructor=instructor)
    return templates.TemplateResponse("createCourse.html", {"request": request, "status": "Course Created"})



# This function is used to update a course
@router.put("/{id}")
async def update_course(id: int, request: Request):
    form = await request.form()
    title = form.get("title")
    description = form.get("description")
    instructor = form.get("instructor")

    course = await Course.get(id=id)
    
    course.title = title
    course.description = description
    course.instructor = instructor
    await course.save()
    return RedirectResponse(url="/course", status_code=303)



# This function is used to delete a course
@router.delete("/{id}")
async def delete_course(id: int):
    course = await Course.get(id=id)
    await course.delete()
    return RedirectResponse(url="/course", status_code=303)
