# -*- coding: utf-8 -*-

CODE_MSG = {
    'system_busy': {'errcode': -1, 'errmsg': 'success'},
    'success': {'errcode': 0, 'errmsg': 'success', 'data':{}},
    'login_failed': {'errcode': 400101, 'errmsg': 'login failed'},
    'auth_check_failed': {'errcode': 400102, 'errmsg': 'auth check failed'},
    'permission_check_failed': {'errcode': 400103, 'errmsg': 'permission check failed'},
    'register_failed': {'errcode': 400104, 'errmsg': 'register failed'},
    'account_exist': {'errcode': 400105, 'errmsg': 'register failed, account'},
    'profile_set_failed': {'errcode': 400201, 'errmsg': 'profile set failed'},
}