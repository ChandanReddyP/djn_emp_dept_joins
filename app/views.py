from django.shortcuts import render

from app.models import *

# Create your views here.

def equi_joins(request):
    LEDO=Employee.objects.select_related('dept_no').all()
    LEDO=Employee.objects.select_related('dept_no').filter(emp_name='SCOTT')
    LEDO=Employee.objects.select_related('dept_no').filter(comm__isnull=True)
    LEDO=Employee.objects.select_related('dept_no').filter(comm__isnull=False)
    LEDO=Employee.objects.select_related('dept_no').filter(dept_no__dept_name='ACCOUNTING')
    LEDO=Employee.objects.select_related('dept_no').filter(mgr=1111)
    
    d={'LEDO':LEDO}
    return render(request,'equi_joins.html',d)



def emp_dept_mgr(request):
    LEDMO=Employee.objects.select_related('dept_no','mgr').all()
    LEDMO=Employee.objects.select_related('dept_no','mgr').filter(dept_no__dept_name='RESEARCH')
    LEDMO=Employee.objects.select_related('dept_no','mgr').filter(mgr__isnull=False)
    LEDMO=Employee.objects.select_related('dept_no','mgr').filter(mgr__emp_name='BLAKE')
    LEDMO=Employee.objects.select_related('dept_no','mgr').filter(emp_name='ADAM')
    
    d={'LEDMO':LEDMO}
    return render(request,'emp_dept_mgr.html',d)