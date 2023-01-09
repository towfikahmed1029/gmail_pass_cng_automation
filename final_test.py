import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import random 
for x in range(210):
    driver = uc.Chrome(
        driver_executable_path='chromedriver.exe', use_subprocess=True)
    time.sleep(2)
    login = 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmyaccount.google.com%2Fsigninoptions%2Frescuephone&osid=1&rart=ANgoxcfbj5MICImsby3i6E4WliB4NiCObSuRKGTYLSt03bQVr5EN0ekxnuxLrRGkyz5DKW13ZqMxZkUoZn1oMKAXz3u6m-8mXw&service=accountsettings&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    driver.get(login)
    def visibil_element(by, selector, wait=5):
        element = False
        if by == 'name':
            byselector = By.NAME
        if by == 'xpath':
            byselector = By.XPATH
        if by == 'css':
            byselector = By.CSS_SELECTOR
        if by == 'id':
            byselector = By.ID
        try:

            element = WebDriverWait(driver, wait).until(
                EC.visibility_of_element_located((byselector, selector)))

        except Exception as e:
            print(e)
            element = False
        if element == False:
            
            print("visibil_element not find: ", selector)
        else:
            print(selector)
        return element

    def firstLine():
        # list to store file lines
        lines = []
        # read file
        with open(r"input.txt", 'r') as fp:
            # read an store all lines into list
            lines = fp.readlines()

        # Write file
        with open(r"input.txt", 'w') as fp:
            for number, line in enumerate(lines):
                if number != 0:
                    fp.write(line)
        mailinfo = lines[0].split(':')
        return mailinfo
        
    def apandLine(listinfo, filename="output.txt"):
        inputfile = open(r'{0}'.format(filename), 'a')
        line = ':'.join(listinfo)
        inputfile.write(f'{line}')
        inputfile.close()

    def fail(listinfo, filename="fail.txt"):
        inputfile = open(r'{0}'.format(filename), 'a')
        line = ':'.join(listinfo)
        inputfile.write(f'{line}')
        inputfile.close()

    def ran_password():
        characters ="abcdefghijklmnopshwyz"
        upper ="ABCDEFGHIJKLMNOPQPSHWYZ"
        symbol ="@%"
        num = "0123456789"
        string = characters+symbol+num+upper
        length = 8
        password = "".join(random.sample(string,length))
        print("Random password:",password)
        return password

    def cng_psss():
        try:
            pass_change = "https://myaccount.google.com/signinoptions/password"
            my_acc_link = driver.current_url.split('?')[1]
            pass_change_final = pass_change+"?"+my_acc_link
        except:
            pass_change_final ="https://myaccount.google.com/signinoptions/password" 
        driver.get(pass_change_final)
        ### Pass change
        time.sleep(3)
        input_pass_1 = driver.find_element(By.XPATH, '(//input[@type="password"])[1]')
        time.sleep(1)
        input_pass_1.send_keys(new_pass)
        time.sleep(1)
        input_pass_2 = driver.find_element(By.XPATH, '(//input[@type="password"])[2]')
        time.sleep(1)
        input_pass_2.send_keys(new_pass)
        time.sleep(1)
        input_pass_3 = driver.find_element(By.XPATH, '(//input[@type="password"])[2]')
        time.sleep(1)
        input_pass_3.send_keys(Keys.RETURN)
        time.sleep(2)
        print("Gmail Password: ",new_pass)
        driver.close()
        ### Gmail name
        mailinfo[0]=email_address
        mailinfo[1]=new_pass
        mailinfo[2]=recovery_email
        apandLine(mailinfo)
        print ("########   SUCCESS  #########")
        # else:
        #     print("Lose ---------")
        #     mailinfo[0]=email_address
        #     mailinfo[1]=email_pass
        #     mailinfo[2]=recovery_email
        #     fail(mailinfo)
        #     driver.close()

    mailinfo= firstLine()
    email_address = mailinfo[0]
    try:
        email_pass_1 = mailinfo[1].replace('\\n','')
    except:
        email_pass_1 = mailinfo[1]
    email_pass = email_pass_1.replace('\\t','')
    recovery_email= mailinfo[2]#.replace('\n','')
    recovery_email= recovery_email.replace('\\n','')
    recovery_email= recovery_email.replace('\\t','')
    new_pass = ran_password()
    send_keys = True
    print("------Gmail INFO-----\n","Gmail--- ",email_address,"\n","Password-- ",email_pass,"\n","New Password-- ",new_pass,"\n","Recovery-- ",recovery_email)
    ### Gmail login Start

    input_email = visibil_element('css', 'input',2)
    try:
        input_email.send_keys(email_address)
    except:
        mailinfo[0]=email_address
        mailinfo[1]=email_pass
        mailinfo[2]=recovery_email
        fail(mailinfo)
        driver.close()
        continue# continue # exit()
    try:
        time.sleep(2)
        input_email.send_keys(Keys.RETURN)
    except:
        mailinfo[0]=email_address
        mailinfo[1]=email_pass
        mailinfo[2]=recovery_email
        fail(mailinfo)
        driver.close()
        continue# continue # exit()
    time.sleep(1)
    input_pass =visibil_element('xpath', '//input[@type="password"]',2)
    try:
        input_pass.send_keys(email_pass)
    except:
        mailinfo[0]=email_address
        mailinfo[1]=email_pass
        mailinfo[2]=recovery_email
        fail(mailinfo)
        driver.close()
        continue# continue # exit()
    try:
        time.sleep(2)
        input_pass.send_keys(Keys.RETURN)
    except:
        mailinfo[0]=email_address
        mailinfo[1]=email_pass
        mailinfo[2]=recovery_email
        fail(mailinfo)
        driver.close()
        continue# continue # exit()
    time.sleep(2)
    input_pass_wrong =visibil_element('xpath', '//input[@type="password"]',2)
    if input_pass_wrong == input_pass:
        mailinfo[0]=email_address
        mailinfo[1]=email_pass
        mailinfo[2]=recovery_email
        fail(mailinfo)
        driver.close()
        continue# continue # exit()
    ### gmail login  end
    ### Recovery 
    time.sleep(2)

    if "rejected" in driver.current_url:
        mailinfo[0]=email_address
        mailinfo[1]=email_pass
        mailinfo[2]=recovery_email
        fail(mailinfo)
        driver.close()
        continue# continue # exit()
    rec = visibil_element('xpath', '//ul//child::li[4]',2)
    if rec:
        try:
            time.sleep(3)
            rec_final = visibil_element('xpath', '//ul//child::li[3]',2)
            rec_final.click()
        except:
            mailinfo[0]=email_address
            mailinfo[1]=email_pass
            mailinfo[2]=recovery_email
            fail(mailinfo)
            driver.close()
            continue# continue # exit()

        time.sleep(3)
        rec_input = visibil_element('xpath', '//input[@type ="email"]',1)
        if rec_input:
            rec_in = driver.find_element(By.XPATH, '//input[@type ="email"]').send_keys(recovery_email)
            time.sleep(3)
            send = visibil_element('xpath', '(//span[@class="VfPpkd-vQzf8d"])[1]',2)
            if send:
                send = driver.find_element(By.XPATH, '(//span[@class="VfPpkd-vQzf8d"])[1]').click()
            else:
                time.sleep(3)
                rec_in =visibil_element('xpath', '//input[@type ="email"]', 2)
                time.sleep(3)
                try:
                    rec_in.send_keys(Keys.RETURN)
                except:
                    pass
            time.sleep(5)
            cng_psss()
            continue
        else:
            mailinfo[0]=email_address
            mailinfo[1]=email_pass
            mailinfo[2]=recovery_email
            fail(mailinfo)
            driver.close()
            print("***********#######@@@$#$#####@@@@###@@@###@@@###@#@##@#@#@")
            continue# continue # exit()
    else:
        time.sleep(2)
        cng_psss()
    ###
    