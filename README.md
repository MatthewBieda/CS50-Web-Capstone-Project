# CS50-Web-Capstone-Project
My final project for Harvard's CS50 Web

https://youtu.be/lrA_6l2wPiw

Distinctiveness and Complexity:

My final project is a blog implemented with Django, Bootstrap CSS, Javascript and HTML. The database was implemented using default SQLite for 
submission purposes. SQLite does have the advantage of being a serverless database, making it hassle free for anyone to run my code. I was thinking
about using other database products, even branching out to the NoSQL paradigm. However NoSQL is a poor fit for Django, as the entire ORM is built 
around the RDBMS model. As this is a simple low-traffic web app SQLite is perfectly fine, but for deployment I will use PostgreSQL. 

I have used several models, created a complete authentication system and I made use of Django's generic class-based views to cut down on the 
boilerplate code in my views. This requires a stronger understanding of Django and abstraction than sticking to the function-based views used in the
course but it does makes your code much nicer to read for yourself and other developers. I also included a subtle background, a personal reading list
for every user and the ability to live edit your own comments. The superuser (myself) also has the ability to create posts, also using the admin 
panel I have full access to the entire database. However I didn't to expose all this functionality via the API, to ensure I don't accidentally delete
one of my posts for instance. Since it is long-form content is it pre-edited and shouldn't require updating. Users are free to leave comments on my 
articles, and edit them if they want, but I reserve the ability to remove them. 

The site has been developed to be mobile-first through the use of responsive design and media queries and has been tested on various devices. For
instance the elements in the navigation bar collapse into a hamburger menu on small screens. 

static: My CSS, JS and some background images I was testing.

templates: Layout (parent to all), index, login, register, newarticle, articles(listview), article_detail, readinglist

admin.py: Here I registered the models so they would appear in the admin panel.

forms.py:
In this application I made of Django's modelform abstraction. These are extremely useful when you simply want to represent a model as a form and are
very easy to extend and customise. I had one form for creating an article and one for creating comments. Note that the default form provided by 
listview is unstyled so I had to use some code from SO to style it. It should be easier to do this IMO. 

models.py: 
For this application I used four models, the default User model provided by Django because it is battle-tested and has performed well in all 
the applications I have built so far in the course. It is also very easy to extend this model by providing additional attributes to the user model. 
Additionally I included a model for the posts containing various metadata about the post and also a model for the comments in order to relate 
them to the user who submitted it and keep track of this information in the database. Finally there is a model to maintain the reading list, 
I wasn't sure of the optimal way to implement this. I built some validation into the application code to prevent people from adding duplicate 
entries which throws an integrity error. 

views.py:
In order to implement Authentication, I made use of Django's generic class-based views LoginView and LogoutView, these handle all authentication 
functionality interally meaning my code is compact and does not clutter up the views file. For posting a new article, I made use of the CreateView
and for listing my articles I used the ListView. These generic views are great if you aren't trying to extend their functionality too much, in that
case going back to a function-based view generally makes more sense. For instance I first attempted to use DetailView to show the article's full 
attributes, but on this page I also wanted to add a comments form. So I tried to integrate a ModelForm into the same view. This kind of worked, but 
not completely and I realized this was a lot more complicated than just writing it in a FBV. So I reworked it like that. Lastly I kept the 
registration function from a previous project and used a FBV for the reading list display.

settings.py
I had some issues getting started because I had to do everything from scratch this time. It seems like Django doesn't initialize all the settings 
you need so I had to add AUTH_USER_MODEL = 'blog.User', add 'blog' to installed apps, add STATICFILES_DIRS = [os.path.join(BASE_DIR, 'blog', 'static')]
and the same for Template Dirs. Also I needed LOGIN_REDIRECT_URL = 'index' and LOGOUT_REDIRECT_URL = 'index' for the CBV authentication to work.

Additional comments: 
Styling is implemented through Bootstrap's pre-defined CSS classes as they look professional and are easy to add to your codebase. Using Bootstrap 
does limit how creative you can be with your site design, so if you are doing something very creative you will probably want to use your own custom 
CSS or a less opionated framework like Tailwind CSS. 

The functionality of making a post is limited to the superuser account (i.e. myself) but anyone can comment on my articles, although they must first
complete the registration process. This is to mitigate against spam and the proliferation of low-quality comments. 

Since I am intending to use this site as my personal blog I will need to deploy it to the web. This can be done by using an Ubuntu VPS hosted by 
Digital Ocean. I will replace the default Django server with Gunicorn because it is only recommended to use it in a development environment. There 
are also ASGI (Asynchronous Server Gateway Interface) application servers such as Daphne but it would be more difficult to implement Asynchronous 
functionality and you should probably use a framework that treats asyncronous development as a first-class citizen like Fast API if you will leverage
it heavily. 

How to run: 
No special requirements, just run like a regular django application
"python manage.py runserver"

regular users: mike, tom
admin user: matt
all passwords: 123
