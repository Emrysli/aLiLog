#-*-coding:utf-8-*-
from selenium import webdriver
import thread

# 登录用户名和密码
user_name = "xxxxx1"
pass_word = "xxxxxxx"

# it is use to get cookies and return browser object
def aLi_log(user_name, pass_word):
	browser = webdriver.Chrome(executable_path=r"C:\Users\rocknoway\AppData\Local\Google\Chrome\Application\chromedriver.exe")
	browser.get("https://login.alibaba.com/")


	# 延迟10秒
	browser.implicitly_wait(10)
	# 使用异常的处理方式 避免iframe没有加载好而无法进行切换
	while True:
		try:
			browser.switch_to.frame(1)
			break
		except Exception,e:
			print e
			browser.implicitly_wait(10)
		

	browser.find_element_by_id("fm-login-id").send_keys(user_name)
	browser.find_element_by_id("fm-login-password").send_keys(pass_word)
	checkCode = browser.find_element_by_id("fm-login-checkcode-img")

	
	#如果有验证码图片链接地址那么说明需要输入验证码
	if checkCode.get_attribute('src'):
		strCode = raw_input("输入验证码\n")
		checkCode.send_keys(strCode)
	browser.find_element_by_name("submit-btn").click()



if __name__ == '__main__':
	aLi_log(user_name, pass_word)
