# Christian Fundraising Foundation Website


<p align="center">
  <img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/ffd35de1-510b-4332-bfe5-c711763ffb33" />
</p>




A comprehensive Django-based website for the Christian Fundraising Foundation, providing fundraising training, blog content, and community engagement tools.

## Features

- **Blog System**: Full-featured blog with categories, rich text editing, and image optimization
- **Training Programs**: Dedicated training section for fundraising education
- **Email Subscriptions**: Mailchimp integration for newsletter management
- **Call Booking**: Contact form for scheduling fundraising consultations
- **Responsive Design**: Modern UI built with Tailwind CSS
- **Admin Panel**: Django admin interface for content management
- **SEO Optimized**: Meta tags and structured content for search engines

## Tech Stack

- **Backend**: Django 5.1.6
- **Database**: PostgreSQL (production) / SQLite (development)
- **Frontend**: HTML, Tailwind CSS 4.0
- **Rich Text Editor**: CKEditor
- **Email Marketing**: Mailchimp API
- **Deployment**: Render.com with Gunicorn
- **Static Files**: WhiteNoise middleware

## Project Structure

```
christian-fundraising-foundation-website/
├── christianfoundation/          # Main Django project
│   ├── settings/                 # Environment-specific settings
│   ├── urls.py                   # Main URL configuration
│   └── views.py                  # Main views
├── blog/                         # Blog application
├── training/                     # Training application
├── subscriptions/                # Email subscription management
├── calls/                        # Call booking functionality
├── static/                       # Static files (CSS, images)
├── templates/                    # HTML templates
├── requirements.txt              # Python dependencies
├── package.json                  # Node.js dependencies
├── render.yaml                   # Render deployment config
└── build.sh                      # Build script
```


## Content Management

Access the Django admin at `/admin/` to:
- Create and edit blog posts
- Manage training content
- View subscription data
- Configure site settings

## Deployment

The project is configured for deployment on Render.com:

1. **Build command**: `./build.sh`
2. **Start command**: `gunicorn christianfoundation.wsgi:application`
3. **Environment**: `christianfoundation.settings.production`



## Deployment Checklist

- [x] Configure production.py settings
- [x] Set up PostgreSQL database
- [x] Install and configure Gunicorn
- [x] Configure static file serving
- [x] Set up domain and SSL certificate
- [x] Configure environment variables
- [x] Test all functionality in staging
- [x] Set up automated backups





