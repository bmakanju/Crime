from django.urls import path, include
from account.views import Contact, Logging, Register, Logout, ViewOtherProfile, Settings,PasswordUpdate, UpdateProfile, About#, ProfileView, UpdateProfile
app_name = "account"
urlpatterns = [
    path("Login", Logging, name="login"),
    path("Register", Register, name="register"),
    path("Settings", Settings, name="setting"),
    path("About", About.as_view(), name="About"),
    path("ChangePassword", PasswordUpdate, name="changepass"),
    path("Logout", Logout, name="logout"),
    path("ViewProfile/<str:name>", ViewOtherProfile, name="viewotherprofile"),
    path("Contact Us", Contact, name="contactus"),
    path("Profile_Update", UpdateProfile, name="profileupdate"),
]