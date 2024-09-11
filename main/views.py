from django.shortcuts import render

# Create your views here.
def add_num(request):
    res=None
    err=None

    if request.method=="POST":
        num1=request.POST.get('num1')
        num2=request.POST.get('num2')

        try:
            sum=float(num1)+float(num2)
            res=f"the sum is:{sum}"
        except:
            err="something went wrong"
    return render(request, 'add.html', {'res': res, 'err':err})


def simple_interest(request):
    result = None
    error = None

    if request.method == "POST":
        p=request.POST.get('p')
        n=request.POST.get('n')
        r=request.POST.get('r')

        try:
            simple=(float(p) * float(n) * float(r))/100
            result = f"The sum is:{simple}"
        except:
            error = "Something went wrong"
    return render(request,'pnr.html',{'result':result,'error':error})
