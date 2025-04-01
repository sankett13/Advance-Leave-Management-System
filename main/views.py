import datetime
from django.shortcuts import render, redirect,get_object_or_404, Http404
from django.http import HttpResponse, JsonResponse
from .models import StudentBasicDetail, LeaveHistory, StudentContactDetail, FacultyDetail
from .serializers import LeaveHistorySerializer, StudentBasicDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from datetime import date

# def student(request):
#     if request.method == 'GET':
#         print("get method hai")
#         return render(request, 'Student.html')
#     if request.method=="POST":
#         sp_id=request.session.get("sp_id")
#         print("hello",sp_id)
        

def FA(request):
    return render(request, 'FA.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        user_id = request.POST.get('sp_id')
        password = request.POST.get('password')

        try:
            faculty = get_object_or_404(FacultyDetail, fp_id=user_id)
            if faculty.password == password:
                request.session['fp_id'] = user_id
                return redirect('faculty_advisor')
            else:
                print("here")
                messages.error(request, "Login failed. Incorrect password.")
                return redirect('login')
        except Http404:
            try:
                print("here")
                student = get_object_or_404(StudentBasicDetail, sp_id=user_id)
                print(student)
                if student.password == password:
                    request.session['sp_id'] = user_id
                    print("here in student")
                    c_detail=StudentContactDetail.objects.get(id=student.id)
                    print(c_detail)
                    
                    return render(request,"Student.html",{"student":student,"info":c_detail})
                else:
                    messages.error(request, "Login failed. Incorrect password.")
                    return redirect('login')
            except Http404:
                messages.error(request, "Login failed. User not found.")
                return redirect('login')
        
            


def leaveapply(request):
    if request.method == 'GET':
        return render(request, 'apply_leave.html')

    elif request.method == 'POST':
        sp_id = request.session.get('sp_id') #Get student id from session.
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        reason = request.POST.get('reason')
        block = request.POST.get('block')
        room = request.POST.get('room')
        visiting_address = request.POST.get('visiting_address')

        try:
            start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()

            no_of_days = (end_date - start_date).days + 1 #Add 1 to include the end date.

            if no_of_days <= 0:
                return HttpResponse("End date must be on or after start date.")

            student = StudentBasicDetail.objects.get(sp_id=sp_id)

            leave = LeaveHistory.objects.create(
                student_id=student,
                start_date=start_date,
                end_date=end_date,
                no_of_days=no_of_days,
                reason=reason,
                place_to_visit=visiting_address, 
            )

            if leave:
                details = StudentContactDetail.objects.get(StudentID=student)
                print(details.Parent_Email)

                return HttpResponse("Leave Application Successful")
            else:
                return HttpResponse("Leave Application Failed")

        except ValueError:
            return HttpResponse("Invalid date format. Please use YYYY-MM-DD.")
        except StudentBasicDetail.DoesNotExist:
            return HttpResponse("Student not found.")
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")


def faculty_advisor(request):
    id = request.session.get('fp_id')
    faculty_advisor = get_object_or_404(FacultyDetail, fp_id=id)
    students = StudentBasicDetail.objects.filter(Batch_Year=faculty_advisor.Batch_Year, department=faculty_advisor.department)

    today = date.today()
    leave_applications = LeaveHistory.objects.filter(student_id__in=students, status_fa='pending')

    pending_count = LeaveHistory.objects.filter(student_id__in=students, status_fa='pending').count()
    approved_count = LeaveHistory.objects.filter(student_id__in=students, status_fa='approved').count()
    rejected_count = LeaveHistory.objects.filter(student_id__in=students, status_fa='rejected').count()

    context = {
        'faculty_advisor': faculty_advisor,
        'leave_applications': leave_applications,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'rejected_count': rejected_count,
    }

    return render(request, 'FA.html', context)


def approve_leave(request, leave_id):
    if request.method == 'POST':
        try:
            leave = get_object_or_404(LeaveHistory, id=leave_id)
            leave.status_fa = 'approved'
            leave.save()
            return JsonResponse({'message': 'Leave approved successfully', 'ok': True}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e), 'ok': False}, status=500)
    return JsonResponse({'error': 'Invalid request method', 'ok': False}, status=400)

def reject_leave(request, leave_id):
    if request.method == 'POST':
        try:
            leave = get_object_or_404(LeaveHistory, id=leave_id)
            leave.status_fa = 'rejected'
            leave.save()
            return JsonResponse({'message': 'Leave rejected successfully', 'ok': True}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e), 'ok': False}, status=500)
    return JsonResponse({'error': 'Invalid request method', 'ok': False}, status=400)