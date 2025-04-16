Welcome to the Futurama Blog Project, a Django-powered web app where you can browse and read summaries of your favorite Futurama episodes! This project fetches episode data from an API and lets you view details like air date, writers, and episode descriptions.

Features 

✅ View all Futurama episodes – Titles, descriptions, and air dates

✅ Click to view details – Open a dedicated page for each episode

Tech Stack

    Backend: Django

    Frontend: HTML, CSS

    Database: SQLite (default)

    API Requests: requests library

Installation

1. Clone the Repository:
    
    git clone https://github.com/saks786/blog_project.git
    
    cd blog_project
2. Libraries requires:

    Python version: 3.10

   pip install django djangorestframework requests os
4. Start the Server
    
    python manage.py runserver

Deployment on AWS using AWS ElasticBeanstalk service
   ![image](https://github.com/user-attachments/assets/58103c9e-4281-4bab-90e5-5a4d1e055b1f)
   ![image](https://github.com/user-attachments/assets/b31f0283-adff-4590-b0c5-651defc21dc4)
   ![image](https://github.com/user-attachments/assets/cfae8995-50a7-4105-8a31-190ec20e3c70)
   ![image](https://github.com/user-attachments/assets/79ec6f00-bb69-4eba-8495-210c0ecb7045)
   ![image](https://github.com/user-attachments/assets/67b7b033-1487-4fd7-b7f8-d60ab373a776)

   AWS ElasticBeanstalk link- http://Sky-django-env.eba-m3bvmjpu.us-east-1.elasticbeanstalk.com

   Main focus for deploying it on AWS was to provide uptime to the website without any kind of failure. The website will be available and run till the servers are on, if the servers are off then their will be the downtime for the website.





