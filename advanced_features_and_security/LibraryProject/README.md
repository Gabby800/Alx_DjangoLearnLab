README.md
# Permissions and Groups Setup

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Usage
- Views are protected using @permission_required('app_name.permission_codename')
- Assign users to groups via Django admin or programmatically

# Security configuration notes

## Settings
- `DEBUG = False` in production.
- `AUTH_USER_MODEL` is `bookshelf.CustomUser`.
- Cookies: `SESSION_COOKIE_SECURE=True` and `CSRF_COOKIE_SECURE=True` require HTTPS.
- Security headers: `X_FRAME_OPTIONS='DENY'`, `SECURE_CONTENT_TYPE_NOSNIFF=True`, `SECURE_BROWSER_XSS_FILTER=True`.

## Templates
- All HTML forms include `{% csrf_token %}`.
- Don't use `|safe` unless content is sanitized.

## Views & Forms
- Use Django Forms to validate and sanitize input.
- Use ORM filters to avoid raw SQL. If raw SQL is required, use parameterized queries.

## CSP
- Use `django-csp` for convenient CSP configuration and monitoring.

## Testing
- Manual tests described in the "Testing checklist" section. Run tests after each deployment.

## Notes
- When turning on `SECURE_SSL_REDIRECT` and cookie `Secure` flags, ensure your app is behind HTTPS (NGINX, Caddy, or managed hosting).
