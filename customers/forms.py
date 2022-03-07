from xmlrpc.client import DateTime
from django import forms
from .models import Contact, Customer, Department, Employee, Note, ServiceItem, Supplier


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['parent']

class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['parent']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ['company']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        exclude = ['company']


class ServiceItemForm(forms.ModelForm):
    class Meta:
        model = ServiceItem
        fields = "__all__"
        exclude = ['company']

class CreateEmployeeForm(forms.ModelForm):
    salaryamount = forms.FloatField(required=False)
    weekdayrate = forms.FloatField(required=False)
    saturdayrate = forms.FloatField(required=False)
    sundayrate = forms.FloatField(required=False)
    publicholidayrate = forms.FloatField(required=False)
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ['company',]
    
    def clean_idnumber(self):
        data = self.cleaned_data.get("idnumber")
        dob : DateTime = self.cleaned_data.get("dateofbirth",None)
        if data and dob:
            print(dob.strftime("%y%m%d"),data[:6])
            if data[:6] != str(dob.strftime("%y%m%d")):
                raise forms.ValidationError("The id number and date of birth do not match")
        return data

class CreateDepartmentForm(forms.ModelForm):
    class Meta:        
        model = Department
        fields = "__all__"
        exclude = ['company']