### Deployment tasks
- [] Configure production.py settings
- [] Set up PostGreSQL on SiteGround
- [] Install and configure Gunicorn
- [] Configure NGinx for static files
- [] Set up domain & SSL


### Staging Environment 
- [] SiteGround Staging (cPanel -> Staging Tool -> test deployment scripts)


### Databse Backups
- [] cPanel -> Backups -> Daily database backups in Google Drive / Dropbox
- [] 

```bash
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > db_backup.json
```

### Verify Dependencies 
- [] Generate requirements.txt: pip freeze > requirements.txt
- [] Check for outdated packages: pip list --outdated