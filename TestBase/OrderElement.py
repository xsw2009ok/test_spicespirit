#coding=utf-8

from selenium import webdriver

#
ORDER_MAINPAGE_CUSTOMER = r"//div/ul/li/a[i[@class='i11']]"
ORDER_CUSTOMER_MEMBER = u"//li/ul/li/a[contains(text(),'综合管理')]"
ORDER_CUSTOMER_MEMBER_INFO = 'customer_member_info'
ORDER_CUSTOMER_INVOICE_INVOICE = 'customer_invoice_invoice'
ORDER_CUSTOMER_MEMBER_EXPORT = 'customer_invoice_export'

ORDER_INFO_INPOUT_PHONE = 'phone'
ORDER_INFO_INPUT_USERNAME = 'username'
ORDER_INFO_PHONE_SAVE = 'member_save'
ORDER_INFO_DESK_MORE = r"//div[@class='con-box']/div[4]/div/a"
ORDER_INFO_DESK_TYPE = r"//select[@id='desk_type']"
ORDER_INFO_DESK_REASON = 'desk_reason'
ORDER_INFO_DESK_SAVE = 'desk_save'
ORDER_INFO_DESK_REMARK = 'order_desc_remark'
ORDER_INFO_ADDRESS_MORE = r"//div[@id='address_head']/div/a"
ORDER_INFO_ADDRESS_USERNAME = 'address_username'
ORDER_INFO_ADDRESS_PHONE1 = 'address_phone1'
ORDER_INFO_ADDRESS_DISTRICT = 'district'
ORDER_INFO_ADDRESS_LIST = r"//div[@id='tangram-suggestion--TANGRAM__3']/table/tbody/tr[1]"
ORDER_INFO_ADDRESS_ADDRESS = 'address_address'
ORDER_INFO_ADDRESS_SAVEADDRESS = 'save_address'
ORDER_INFO_CREATEORDER_MORE = r"//div/div[@id='order_auto_process']"
ORDER_INFO_CREATEORDER_STATION = 'customer_stations'
ORDER_INFO_CREATEORDER_AREA = 'order_area'
ORDER_INFO_SEARCH_GOODS = 'order_code_match'
ORDER_INFO_SELECT_GOODS = r"//div[@id='order_match_lists']/ul/li[1]/span[1]"
ORDER_INFO_AREA = 'order_area'
ORDER_INFO_SOURCE_CHANNEL = 'order_source'
ORDER_INFO_RESERVE_DATE = 'order_reserve_date'
ORDER_INFO_SET_TIME = 'order_delivery_date'
ORDER_INFO_START_TIME = 'order_delivery_start_time'
ORDER_INFO_END_TIME = 'order_delivery_stop_time'
ORDER_INFO_START_TIME_DEFAULT = u"//div[@id='ui-datepicker-div']/div[3]/button[contains(text(),'当前')]"
ORDER_INFO_START_TIME_DONE = u"//div[@id='ui-datepicker-div']/div[3]/button[contains(text(),'确认')]"
ORDER_INFO_PAY_INTERNET = r"//div/input[@name='pay_way' and @value = '2']"
ORDER_INFO_PAY_CASH = r"//div/input[@name='pay_way' and @value = '1']"
ORDER_INFO_PAY_CHANNEL = 'pay_channel'
ORDER_INFO_ORDER_REMARK = 'order_remark'
ORDER_INFO_INVOICE = 'invoice'
ORDER_INFO_INVOICE_ADD = 'add_invoice'
ORDER_INFO_INVOICE_SAVE = r"//div/div/div/a[@class='keep-btn keep-gray invoice_save']"
ORDER_INFO_INVOICE_MORE = r"//div/div[@class='invoice-btn']/a"
ORDER_INFO_INVOICE_GEREN = '9185'
ORDER_INFO_SAVE_ORDER = 'save_order'
ORDER_INFO_CREATEORDER_RESULT = 'tips'


