#-*-coding:utf-8-*-
from selenium import webdriver


# 登录用户名和密码
user_name = "xxxxx1"
pass_word = "xxxxxxx"

# it is use to get cookies and return browser object
def aLi_log(user_name, pass_word):
	browser = webdriver.Chrome(executable_path=r"C:\Users\rocknoway\AppData\Local\Google\Chrome\Application\chromedriver.exe")
	browser.get("http://liuliang.taobao.com/")


	# 延迟10秒
	browser.implicitly_wait(10)
	# 使用异常的处理方式 避免iframe没有加载好而无法进行切换
	while True:
		try:
			browser.switch_to.frame(0)
			break
		except Exception,e:
			print e
			browser.implicitly_wait(10)
		

	browser.find_element_by_id("TPL_username_1").send_keys(user_name)
	browser.find_element_by_id("TPL_password_1").send_keys(pass_word)
	
	browser.find_element_by_id("J_SubmitStatic").click()



if __name__ == '__main__':
	aLi_log(user_name, pass_word)
