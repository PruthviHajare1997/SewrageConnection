from django.db import models

# User Creation

class RoleMaster(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10) 
    hierarchy = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_role_master'
        
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    is_superuser = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    encrypted_password = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    first_time_login = models.IntegerField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    password_text = models.CharField(max_length=128, null=True, blank=True)  
    is_active = models.IntegerField(null=True, blank=True) 

    class Meta:
        db_table = 'tbl_users'

# Masters

class ParameterMaster(models.Model):
    parameter_id = models.AutoField(primary_key=True)
    parameter_name = models.CharField(max_length=100, null=True, blank=True)
    parameter_value = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'tbl_parameter_master'

class NodalMaster(models.Model):
    id = models.AutoField(primary_key=True)
    nodal_office_location = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'tbl_nodal_master'

class DepartmentMaster(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'tbl_department_master'
        
class ServiceMaster(models.Model):
    ser_id = models.AutoField(primary_key=True)
    ser_name = models.CharField(max_length=100, null=True, blank=True)
    dept_id_id = models.ForeignKey('DepartmentMaster', on_delete=models.CASCADE, null=True, blank=True, related_name='dept_id_F', db_column="dept_id_id")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'tbl_service_master'

class StatusMaster(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.IntegerField(default=1)  
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'tbl_status_master'

class DocumentMaster(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=255, null=True, blank=True)
    doc_path = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'tbl_document_master'
        
# Transaction

class WorkflowDetail(models.Model):
    request_no = models.CharField(max_length=255, primary_key=True)  
    level = models.IntegerField(null=True, blank=True)
    user_id_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True, related_name='user_id_F', db_column='user_id_id')
    status = models.CharField(max_length=50, null=True, blank=True)
    action = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'tbl_workflow_details'

class LevelActionMapping(models.Model):
    id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=100, null=True, blank=True)
    next_action = models.CharField(max_length=100, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'tbl_level_action_mapping'
        
from django.db import models

class ServiceMatrix(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly defining the id field
    ser_id_id = models.ForeignKey('ServiceMaster', on_delete=models.CASCADE, null=True, blank=True, related_name='ser_id_id_F', db_column='ser_id_id')
    level = models.IntegerField(null=True, blank=True)
    role_name = models.CharField(max_length=100, null=True, blank=True)
    action = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'tbl_service_matrix'

class CitizenDocument(models.Model):
    userdocumentid = models.AutoField(primary_key=True)       
    file_name = models.CharField(max_length=255, null=True, blank=True)  
    doc_id_id = models.ForeignKey('DocumentMaster', on_delete=models.CASCADE, null=True, blank=True, related_name='doc_id_id_F', db_column='doc_id_id')  
    created_at = models.DateTimeField(auto_now_add=True)           
    created_by = models.CharField(max_length=100, null=True, blank=True) 
    updated_at = models.DateTimeField(null=True, blank=True)                
    updated_by = models.CharField(max_length=100, null=True, blank=True)  

    class Meta:
        db_table = 'tbl_citizen_document'
        
class InternalUserDocument(models.Model):
    request_no_id = models.ForeignKey('WorkflowDetail', on_delete=models.CASCADE, null=True, blank=True, related_name='request_no_F', db_column='request_no_id') 
    file_name = models.CharField(max_length=255, null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)             
    created_by = models.CharField(max_length=100, null=True, blank=True) 
    updated_at = models.DateTimeField(null=True, blank=True)               
    updated_by = models.CharField(max_length=100, null=True, blank=True) 

    class Meta:
        db_table = 'tbl_internal_user_document'


