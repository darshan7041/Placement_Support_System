from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import logout as logout
import openpyxl 
from django.http import HttpResponse

# Create your views here.


# <----------------------------- Admin login Only------------------------------>
def admin_login(request):
        return render(request,'admin/admin_logins.html')
def profile(request):
        return render(request,'admin/profile.html')

def admin_logout(request):
        logout(request)
        print("not login")
        messages.error(request,"You have successfully logout")
        return redirect('/admin_login/')


def adminloginsave(request):
    if request.method == 'POST': 
        ademail=request.POST.get('email')
        adpass=request.POST.get('password')
        admin1=Admin.objects.filter(a_email=ademail,a_password=adpass)
        if admin1:
            request.session['a_email']=ademail
        #     messages.success(request,"you are successfully login")
            return redirect('/admin_home/')
        else:
            messages.error(request,"You have Invalid Email or Password")
            return redirect('/admin_login/')
    else:
        return render(request,'admin/admin_logins.html')
    


# <------------------------ Admin Only------------------------->

def main_admin_master(request):
        hy=request.session.get('a_email')
        if hy:
                print("welcome",hy)
        else:
                print("not login")
                return redirect('/admin_login/')
        

        admin_id_to_show = request.session.get('a_email')
        # admins = AdminCollege.objects.get(a_email = admin_id_to_show)
        return render(request,'admin/main_admin.html',{'adminss':admin_id_to_show})

def admin_home(request):
        hy=request.session.get('a_email')
        if hy:
                print("welcome",hy)
        else:
                print("not login")
                return redirect('/admin_login/')
        return render(request,'admin/admin_home.html')




# <-------------- Student data | admin Only--------------->

def student_table(request):
        hy=request.session.get('a_email')
        if hy:
                print("welcome",hy)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        st_list=Student.objects.all()
        return render(request,'admin/student_table.html',{'student_list':st_list})

def student_delete(request,id):
        s_delete=Student.objects.get(s_id=id)
        s_delete.delete()
        return redirect('/student_table/')




# <-------------- Company data | admin Only--------------->

def company_table(request): 
        hy=request.session.get('a_email')
        if hy:
                print("welcome",hy)
        else:
                print("not login")
                return redirect('/admin_login/')
        c_list=CompanyRegistration.objects.all()
        return render(request,'admin/company_table.html',{'company_list':c_list})

def company_delete(request,id):
        c_delete=CompanyRegistration.objects.get(c_id=id)
        c_delete.delete()
        return redirect('/company_table/')




# <-------------- PS report data | admin Only--------------->


def ps_report_table(request):
        hy=request.session.get('a_email')
        if hy:
                print("welcome",hy)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        ps_list=PsReport.objects.all()
        return render(request,'admin/ps_report_table.html',{'PS_report_list':ps_list})


def download_ps_report(request):
    # Fetching data from database
    ps_reports = PsReport.objects.all()

    # Creating new xl
    wb = openpyxl.Workbook()
    ws = wb.active

    # Write header row
    headers = ['PS_id', 'Student Name', 'Company Name', 'PS Date', 'Performance', 'Status']
    ws.append(headers)

    # Write data rows
    for ps_report in ps_reports:
        ws.append([
            ps_report.ps_id,
            ps_report.s.s_f_name if ps_report.s else '',  # Assuming 'name' is a field in the Student model
            ps_report.c.c_name if ps_report.c else '',  # Assuming 'name' is a field in the Company model
            ps_report.ps_date.strftime('%Y-%m-%d') if ps_report.ps_date else '',
            ps_report.ps_performance,
            ps_report.ps_status
        ])

    # Save the workbook
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=ps_reports.xlsx'
    wb.save(response)

    return response













# <------------------------ Student Only------------------------->

# <------------------------ Company Only------------------------->