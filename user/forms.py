from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Kullanıcı Adı")
    password=forms.CharField(label="Parola",widget=forms.PasswordInput)
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    mail    =forms.CharField(max_length=200,label="Mail Adresi")
    password=forms.CharField(max_length=50,label="Parola",widget=forms.PasswordInput)
    confirm =forms.CharField(max_length=50,label="Parolayı Doğrula",widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get("username")
        mail=self.cleaned_data.get("mail")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        if password and confirm and password!=confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor.")
        values={
            "username":username,
            "mail":mail,
            "password":password
        }
        return values














