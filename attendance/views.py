from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from attendance.models import Course, Register, Student, AttendanceCode
import re
import datetime

# Create your views here.
def ifCourseExists(courseCode):
	if Course.objects.filter(code=courseCode).exists():
		return True
	return False

def register(entrynumber,attendanceCode, courseCode):
	entrynumber = entrynumber.upper()
	attendanceCode = attendanceCode.upper()
	courseCode = courseCode.upper()
	#validate entry number
	if(len(entrynumber)!=11):
		return False
	p = re.compile(ur'^20\d{2}[A-Z][A-Z]\d{5}$')
	if not p.match(entrynumber):
		return False
	if(len(attendanceCode)!=6):
		return False
	#validate attendance code	
	if not Student.objects.filter(entry_no=entrynumber).exists():
		return False
	course = Course.objects.get(code=courseCode.upper())
	if not AttendanceCode.objects.filter(code=attendanceCode, 
					course=course, date=datetime.date.today()):
		return False
	#check the data in database
	#retreive student
	student = Student.objects.get(entry_no=entrynumber)
	print student, course
	if Register.objects.filter(date=datetime.date.today(),
		student=student,course=course, present=True).exists():
		return True
	newAttendance = Register(date=datetime.date.today(),
			student=student,course=course, present=True)
	newAttendance.save()
	return True

def success(request, course):
	courseObj = get_object_or_404(Course,code=course.upper())
	return render 

def failed(request, course):
	courseObj = get_object_or_404(Course,code=course.upper())

def index(request, course):
	courseObj = get_object_or_404(Course,code=course.upper())
	if request.method=='POST':
		#get parameters
		entrynumber = request.POST['username']
		attendanceCode = request.POST['attendance']
		if register(entrynumber,attendanceCode, course.upper()):#success
			template = loader.get_template('attendance/success.html')
			context = RequestContext(request, {
        		'courseCode': course.upper(),
        		'entryNum': entrynumber.upper()
    		})
			return HttpResponse(template.render(context))
		else:
			template = loader.get_template('attendance/failed.html')
			context = RequestContext(request, {
        		'courseCode': course.upper(),
    		})
			return HttpResponse(template.render(context))
	else:
		context = {'courseCode':course.upper()}
		return render(request,'attendance/index.html',context)
	