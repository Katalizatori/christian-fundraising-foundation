# Christian Fundraising Foundation Website

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

## Installation

### Prerequisites

- Python 3.10.8 or higher
- Node.js and npm (for Tailwind CSS)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd christian-fundraising-foundation-website
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**
   ```bash
   npm install
   ```

5. **Set up environment variables**

   Create a `.env` file in the project root with:
   ```env
   SECRET_KEY=your-secret-key-here
   MAILCHIMP_API_KEY=your-mailchimp-api-key
   MAILCHIMP_LIST_ID=your-mailchimp-list-id
   MAILCHIMP_SERVER_PREFIX=your-server-prefix
   DEBUG=True
   ```

6. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Build Tailwind CSS**
   ```bash
   npm run build  # or npm run dev for development
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your browser.

## Usage

### Development Commands

- **Run server**: `python manage.py runserver`
- **Run tests**: `python manage.py test`
- **Create migrations**: `python manage.py makemigrations`
- **Apply migrations**: `python manage.py migrate`
- **Collect static files**: `python manage.py collectstatic`
- **Build CSS**: `npm run build`

### Content Management

Access the Django admin at `/admin/` to:
- Create and edit blog posts
- Manage training content
- View subscription data
- Configure site settings

### Deployment

The project is configured for deployment on Render.com:

1. **Build command**: `./build.sh`
2. **Start command**: `gunicorn christianfoundation.wsgi:application`
3. **Environment**: `christianfoundation.settings.production`

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

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -am 'Add new feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## Deployment Checklist

- [ ] Configure production.py settings
- [ ] Set up PostgreSQL database
- [ ] Install and configure Gunicorn
- [ ] Configure static file serving
- [ ] Set up domain and SSL certificate
- [ ] Configure environment variables
- [ ] Test all functionality in staging
- [ ] Set up automated backups


```

