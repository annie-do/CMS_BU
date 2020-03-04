**Database**
# Add postgres (DATABASE)
    > CMS > settings.py 
        ex:
                DATABASES = {
                     'default': {
                       'ENGINE': 'django.db.backends.postgresql_psycopg2',
                         'NAME': '',
                         'USER': '',
                         'PASSWORD': '',
                         'HOST': '',
                         'PORT': '',
                     }
                }

**Routing**
# Setup routing
    > CMS > CMS > urls.py
        ex:
                urlpatterns = [
                    path('admin/', admin.site.urls),

                    ## this adds the routing path 
                    path('', include('CMS.urls'))
                ]
       
# Add NEW routing on both views.py & urls.py (ROUTE)
    > CMS > CMS > CMS__Base > views.py
        ex: 
                def home(request):
                    return render(request, 'CMS/')

                def about(request): 
                    return render(request, 'CMS/aboutTemplate.html')

                def contact(request):
                    return render(request, 'CMS/contactTemplate.htm')
    > CMS > CMS > CMS__Base > urls.py
        ex: 
                urlpatterns = [
                    path('', views.home),
                    path('about/', views.about),
                    path('contact/', views.contact),
                ]

# Add NEW html template (VIEW)
    > CMS > CMS > CMS__base > ...Template.html
        ex: 
                CMS/aboutTemplate.html
                CMS/contactTemplate.html

# Add NEW db table (MODEL)
    > CMS > CMS > CMS__Base > models.py
        ex:
                class tbl_profiles(models.Model):
                    vcTitle = models.CharField(max_length=200, null=True)
                    vcDescription = models.CharField(max_length=200, null=True)                