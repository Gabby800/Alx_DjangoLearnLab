README.md
# Permissions and Groups Setup

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Usage
- Views are protected using @permission_required('app_name.permission_codename')
- Assign users to groups via Django admin or programmatically
