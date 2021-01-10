
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


#크롬드라이버 경로
driver_path = '크롬드라이버가 설치되어있는 경로 입력'
#변수에 크롬드라이버 사용하겠다 지정
driver = webdriver.Chrome(driver_path)

# ActionChains 기능을 사용하면 여러 개의 동작을 체인으로 묶어서 
# 저장하고 실행할 수 있습니다
action = ActionChains(driver)
# 열고자하는 url -> 회사전산
My_url = '열고자하는 url을 입력하세요'
driver.get(My_url)

#로그인 정보 입력
ID_Box = driver.find_element_by_xpath('ID 입력란 Xpath 입력')
ID_Box.click() #ID 입력란 클릭
ID_Box.send_keys('나의 아이디') # 나의 아이디를 웹에 입력

PW_Box = driver.find_element_by_xpath('PW 입력란 Xpath 입력')
PW_Box.click() #PW 입력란 클릭
PW_Box.send_keys('나의 비밀번호')# 나의 비밀번호를 웹에 입력

Login_img = driver.find_element_by_xpath('로그인 버튼 Xpath 입력')
Login_img.click() #로그인 버튼 클릭

