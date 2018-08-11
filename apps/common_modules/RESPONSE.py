# -*- coding: utf-8 -*-

CODE_MSG = {
    'success': {'errcode': 0, 'errmsg': 'success', 'data':{}},
    
    'database_error': {'error': -2, 'errmsg': 'database error'},
    'system_busy': {'errcode': -1, 'errmsg': 'system busy'},

    'login_failed': {'errcode': 400101, 'errmsg': 'login failed'},
    'auth_check_failed': {'errcode': 400102, 'errmsg': 'auth check failed'},
    'permission_check_failed': {'errcode': 400103, 'errmsg': 'permission check failed'},
    'register_failed': {'errcode': 400104, 'errmsg': 'register failed'},
    'account_exist': {'errcode': 400105, 'errmsg': 'register failed, account'},
    'profile_set_failed': {'errcode': 400201, 'errmsg': 'profile set failed'},
    'website_set_failed': {'errcode': 400202, 'errmsg': 'website set failed'},
    'object_does_not_exist': {'errcode': 400301, 'errmsg': 'object does not exist'},
    'multiple_objects_returned': {'errcode': 400302, 'errmsg': 'multiple objects returned'}, 
}