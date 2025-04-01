import datetime
from django.shortcuts import render, redirect,get_object_or_404, Http404
from django.http import HttpResponse, JsonResponse
from .models import StudentBasicDetail, LeaveHistory, StudentContactDetail, FacultyDetail
from .serializers import LeaveHistorySerializer, StudentBasicDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages

def student(request):
    return render(request, 'student.html')

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
                    return redirect('leaveapply')
                else:
                    messages.error(request, "Login failed. Incorrect password.")
                    return redirect('login')
            except Http404:
                messages.error(request, "Login failed. User not found.")
                return redirect('login')
        
            


def leaveapply(request):
    if request.method == 'GET':
        sp_id = request.session.get('sp_id')
        student = StudentBasicDetail.objects.get(sp_id=sp_id)
        serializer = StudentBasicDetailSerializer(student)
        return render(request, 'form.html', {'student': serializer.data})

    elif request.method == 'POST':
        student_name = request.POST.get('student_name')
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        reason = request.POST.get('reason')
        place_to_visit = request.POST.get('place_to_visit')

        try:
            start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()

            no_of_days = (end_date - start_date).days

            if no_of_days < 0:
                return HttpResponse("End date must be after start date.")

            student = StudentBasicDetail.objects.get(name=student_name)

            leave = LeaveHistory.objects.create(
                student_id=student,
                start_date=start_date,
                end_date=end_date,
                no_of_days=no_of_days,
                reason=reason,
                place_to_visit=place_to_visit
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
    faculty_advisor = FacultyDetail.objects.get(fp_id=id)
    students = StudentBasicDetail.objects.filter(Batch_Year=faculty_advisor.Batch_Year,department=faculty_advisor.department)
    
    leave_students = LeaveHistory.objects.filter(student_id__in=students, status_fa='pending')
    
    print(leave_students)

    for leave in leave_students:
        print(leave.status_fa)

    return render(request, 'faculty_advisor.html', {'leave_students': leave_students})


def approve_leave(request, leave_id):
    try:
        leave = LeaveHistory.objects.get(id=leave_id)
        leave.status_fa = 'approved'
        leave.save()
        return Response({'message': 'Leave approved successfully'})
    except LeaveHistory.DoesNotExist:
        return Response({'error': 'Leave not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
def reject_leave(request, leave_id):
    try:
        leave = LeaveHistory.objects.get(id=leave_id)
        leave.status_fa = 'rejected'
        leave.save()
        return Response({'message': 'Leave rejected successfully'})
    except LeaveHistory.DoesNotExist:
        return Response({'error': 'Leave not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)