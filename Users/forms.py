from django import forms

from Users.models import Contact, Feedback


class StudentForm(forms.Form):
    name = forms.CharField(label='Enter Your Name', max_length=50, required=True)
    email = forms.CharField(label='Enter Your Email', max_length=50, required=True)
    password = forms.CharField(label='Enter Your Password', max_length=50, required=True)
    age = forms.IntegerField(label='Enter Your Age', required=True, min_value=18)
    check = forms.BooleanField(label='Do you want to subscribe for email updates')
    category = forms.ChoiceField(choices=[('student', 'Student'),
                                          ('teacher', 'teacher'),
                                          ('parent', 'parent')])


class StudentComplains(forms.ModelForm):
    class Meta:
        model = Contact  # name of the field
        fields = ['name', 'email', 'message']  # passes them as a list


class TeacherFeedback(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'email', 'feedback']
