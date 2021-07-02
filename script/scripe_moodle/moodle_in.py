from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from stack import Stack
import chromedriver_binary
import time
import datetime

class MoodleScriper:
    def __init__(self):
        self.URL="https://moodle.s.kyushu-u.ac.jp/course/view.php?id=35644"#講義ページのリンク
        
        self.options = Options()
        self.options.add_argument('--headless')
        profile_path = 'path_to_chrome_profile'
        self.options.add_argument('--user-data-dir=' + profile_path)
        driver = webdriver.Chrome(options=self.options)
        self.driver = driver
        self.data = {}
        self.urlstack = Stack()

    def login(self):
        
        self.driver.get(url=self.URL)

        self.driver.find_element_by_id('username').send_keys(self.ID)
        self.driver.find_element_by_id('password').send_keys(self.PASS)
        self.driver.find_element_by_id('loginbtn').click()

        print("login on moodle")

        cokkies = self.driver.get_cookies()
        for cokkie in cokkies:
            if cokkie['name'] == 'MoodleSession':
                self.driver.add_cookie({'name':cokkie['name'],'value':cokkie['value']})
        
        self.push_url_stack()
        btns = self.driver.find_elements_by_class_name("aalink")
        btns[2].click()#研究用moodleへのリンク．moodle上で3番目に書いてあったから添字の2になった

    def catch_ex_list(self):#小テストのelementを抽出する
        elements = self.driver.find_elements_by_css_selector(".activity.quiz.modtype_quiz")
        elements = elements[1:len(elements)]
        element_list=[]
        if elements:
            for element in elements:
                inelement = element.find_element_by_class_name("instancename")
                #webdriver.ActionChains(self.driver).move_to_element(inelement)
                element_list.append(inelement)
            print("No elements")
        return element_list
    
    def get_data(self,elem_num):#各小テストからデータを抽出
        element_list = self.catch_ex_list()
        self.push_url_stack()
        element_list[elem_num].click()
        self.your_review(elem_num=elem_num)
        time.sleep(1)
        self.pop_url_stack()

    def your_review(self,elem_num):#レビュー画面を開く
        try:
            self.push_url_stack()
            self.driver.find_element_by_class_name('quizattemptcounts').click()
        except :
            self.driver.quit()
            pass
        
        c = self.count_data()
        self.data[elem_num]=[]
        for i in range(c):
            self.push_url_stack()
            self.driver.find_element_by_id('id_pagesize').clear()
            self.driver.find_element_by_id('id_pagesize').send_keys('150')
            self.driver.find_element_by_id('id_submitbutton').click()
            data_dic = self.arrange_data(elem_num,i)
            self.data[elem_num].append(data_dic)
        self.pop_url_stack()

    def count_data(self):
        self.driver.find_element_by_id('id_pagesize').clear()
        self.driver.find_element_by_id('id_pagesize').send_keys('150')
        self.push_url_stack()
        self.driver.find_element_by_id('id_submitbutton').click()
        user_blocks = self.driver.find_elements_by_class_name('gradedattempt')#受験完了済みデータのみ回収，いずれは全データに拡張の必要あり 
        user_blocks = user_blocks[1:]
        self.pop_url_stack()
        return len(user_blocks)

    def arrange_data(self,elem_num,i):
        user_blocks = self.driver.find_elements_by_class_name('gradedattempt')#受験完了済みデータのみ回収，いずれは全データに拡張の必要あり 
        user_blocks = user_blocks[1:]
        data_dic={}
        #各ユーザー情報の取得
        '''
        with open("%dtest.html"%i,"w") as f:
            f.write(self.driver.page_source)
        '''
        #self.driver.get(url=self.driver.current_url)
        user_blocks = self.driver.find_elements_by_class_name('gradedattempt')#受験完了済みデータのみ回収，いずれは全データに拡張の必要あり 
        user_blocks = user_blocks[1:]
        cell = user_blocks[i].find_element_by_css_selector('.cell.c2.bold')
        name = cell.find_element_by_tag_name('a').text
        cell = user_blocks[i].find_element_by_css_selector('.cell.c3')
        mail = cell.text
        cell = user_blocks[i].find_element_by_css_selector('.cell.c5')
        start = cell.text
        start = self.time_type(start)
        cell = user_blocks[i].find_element_by_css_selector('.cell.c6')
        finish = cell.text
        finish = self.time_type(finish)
        #ここからプログラムログのページに遷移
        cell = user_blocks[i].find_element_by_css_selector('.cell.c8.bold')
        #print(self.driver.current_url)#debug
        #print(self.urlstack.stack)#debug
        cell = cell.find_element_by_tag_name('a').click()
        log_dic = self.get_programs()
        self.pop_url_stack()

        #データを整形
        data_dic={'name':name,'mail':mail,'start':start,'finish':finish,'log':log_dic}
        time.sleep(1)
        print(str(elem_num)+' '+ data_dic['name'])
        return data_dic
    
    def get_programs(self):#実際のプログラムの一覧があるページ
        i=1
        log_dic={}
        elements = self.driver.find_elements_by_css_selector('.que.coderunner.adaptive_adapted_for_coderunner.correct')#各問題領域の取得
        for element in elements:
            el = element.find_element_by_class_name('generaltable')
            
            steps = el.find_elements_by_tag_name('tr')
            steps = steps[1:]
            try_list = []
            #self.push_url_stack()#debug
            for step in steps:
                #actionによって動作を変える
                action = step.find_element_by_css_selector('.cell.c2')
                action = action.text.split(':')[0]
                if action!='送信':
                    continue
                t = step.find_element_by_css_selector('.cell.c1').text
                t = self.time_type(t)

                org_window = self.driver.current_window_handle
                c0 = step.find_element_by_css_selector('.cell.c0')
                c0 = c0.find_element_by_tag_name('a').click()
                WebDriverWait(self.driver, 3).until(lambda d: len(d.window_handles) > 1)
                self.driver.switch_to.window(self.driver.window_handles[1])
                code = self.get_code(i)
                time.sleep(1)
                self.driver.switch_to.window(org_window)
                try_list.append([{'time':t},{'code':code}])
            log_dic['ex'+str(i)] = try_list
            i +=1
        return log_dic
    
    def get_code(self,i):
        with open('page%d.html'%i,'w') as f:
            f.write(self.driver.page_source)
            
        code = self.driver.find_element_by_tag_name("textarea")
        code = code.get_attribute('value')
        #code = code.text
        return code

    def time_type(self,time):
        time_list = time.split(' ')
        time = datetime.datetime(int(time_list[0].strip('年')),
                                int(time_list[1].strip('月')),
                                int(time_list[2].strip('日')),
                                int(time_list[3].split(':')[0]),
                                int(time_list[3].split(':')[1]))
        return time
    
    def push_url_stack(self):
        self.urlstack.push(self.driver.current_url)
    
    def pop_url_stack(self):
        self.moodle_page = self.urlstack.pop()
        self.driver.get(url=self.moodle_page)



        
        
    #def scripe(self):

