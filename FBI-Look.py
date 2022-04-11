try:
	import threading,phonenumbers,socket,re,requests,json
	from threading import Thread,Lock
	from phonenumbers import carrier
	from time import sleep
	from random import choice
	from requests import get,post
	import urllib.parse as urlparse
except Exception as e:exit(e)
LINX={"K","k","1"};PHON={"P","p","2"}
PRNT = Lock();theards =[]
red = "\033[1;31;40m";yel = '\033[1;33;40m'
bloFT = "\033[1;36;40m"
grn = '\033[1;32;40m';wit = "\033[1;37;40m"

def telegram_vv1ck(*a, **b):
	with PRNT:
		print(*a, **b)
def User_Agent():
	ios = [
		'13_5','13_6','14','13_3','14_4','15','12_6'
		'15_1','15_1_1','14_3','14_6','13_2','12_7']
	rv = [
		'604.1','596.2','706.6',
		'397.3','937.9','936.3']
	version = [
		'18.5.0','21.1.0',
		'19.3.0','19.1.0',
		'17.7.0','16.6.1']
	User_Agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS '+choice(ios)+' like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/'+choice(version)+' Mobile/15E148 Safari/'+choice(rv)
	return User_Agent
def Go_Back():
	mods = input('\n[0] Back to list <<\n[1] Exit <<\n[$] Enter: ')
	if mods == '0': return Settings()
	else:exit()

class WEB_Scanner:
	def __init__(self,modng):
		self.all_link = []
		if modng=='3':self.api = input('[?] Enter the website link: ');self.Extracting_website_links()
		else:
			self.api = input('[?] Enter the website link: ')
			if ('https')in self.api:
				try:self.apis=self.api.split('https://')[1]
				except IndexError:exit(input('The url is invalid'))
				self.webIP = self.apis.split('.')[0]
				self.api='www.'+self.apis
			elif ('http')in self.api:
				try:self.apis=self.api.split('http://')[1]
				except IndexError:exit(input('The url is invalid'))
				self.webIP = self.apis.split('.')[0]
				self.api='www.'+self.apis
			elif ('www') in self.api:self.webIP= self.api.split('.')[1]
			try:self.IPS = socket.gethostbyname(self.api)
			except socket.gaierror:
				print('The url is invalid')
				print('[-] Please enter a valid link')
				exit(input('[-] Example: www.instagram.com'))
			if modng=='1':self.WEB_Info()
			elif modng=='2':self.Sub_Domin()
			elif modng=='4':self.PORT_Scanner()
			else:telegram_vv1ck('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');return Settings()
	def Extracting_website_links(self):
		try:
			sent = get(self.api)
			links = re.findall('(?:href=")(.*?)"', sent.content.decode(errors="ignore"))
			for link in links:
				link = urlparse.urljoin(self.all_link,link)
				if '#' in link:
					link = link.split("#")[0]
				telegram_vv1ck(link)
		except requests.exceptions.MissingSchema:
			telegram_vv1ck('Errors url..!')
	def Sub_Domin(self):
		try:self.apis
		except AttributeError:self.apis=self.api
		sent = get(f'https://sonar.omnisint.io/subdomains/{self.apis}').text
		try:
			for i in range(1,1000):
				edit = sent.split(',')[i]
				edit = edit.split('""')
				telegram_vv1ck(f'[$] Domins: {edit}')
		except IndexError:
			telegram_vv1ck('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			Go_Back()
	def WEB_Info(self):
		send = get(f'https://{self.webIP}.com.w3snoop.com/',headers={'Host': f'{self.webIP}.com.w3snoop.com','User-Agent': User_Agent(),'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Cache-Control': 'max-age=0','Te': 'trailers','Connection': 'close'}).text
		Server_IP =re.findall('class=text-primary>Server IP Address:<td>(.*?)<tr><td',send)
		inline =re.findall(f'class=d-inline>(.*?)</h2><div>(.*?)</div>',send)
		age =re.findall(f'class=text-primary>Age:<td>(.*?)<tr><td',send)
		Dmn_Created =re.findall(f'class=text-primary>Domain Created:<td>(.*?)<tr><td',send)
		Dmn_Updated =re.findall(f'class=text-primary>Domain Updated:<td>(.*?)<tr><td',send)
		Dmn_Expires =re.findall(f'class=text-primary>Domain Expires:<td>(.*?)</table>',send)
		telegram_vv1ck(inline[0])
		telegram_vv1ck('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		Country =re.findall(f'class=text-primary>Country:<td>(.*?)<br><img',send)
		try:print('[+] Country: '+ Country[0])
		except IndexError:pass
		telegram_vv1ck('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		telegram_vv1ck(grn+'[+] Information about the domain: ')
		telegram_vv1ck('[+] Age: '+age[0])
		telegram_vv1ck('[+] Domain Created: '+Dmn_Created[0])
		telegram_vv1ck('[+] Domain Updated: '+Dmn_Updated[0])
		telegram_vv1ck('[+] Domain Expires: '+Dmn_Expires[0])
		telegram_vv1ck('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		telegram_vv1ck('[+] IP wepsite: '+str(self.IPS))
		telegram_vv1ck('[+] Server IP Address : '+str(Server_IP[0]))
		print(f'-{wit}')
		Go_Back()
	
	def PORT_Scanner(self):
		telegram_vv1ck('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		for port in range(1,65325):
			server=socket.socket(socket.AF_INET,socket.SOCK_STREAM);server.settimeout(0.1)		
			QTR = server.connect_ex((self.IPS,port)) 
			if port==65320:
				telegram_vv1ck(grn+'\n</> Examination is over ..</>\n'+wit)
				Go_Back()
			if QTR ==0:telegram_vv1ck(grn+'\n[+] open port \n \t-> IP: {} | PORT: {}'.format(str(self.IPS),str(port))+wit)
			else:telegram_vv1ck(yel+'\r[%] Checking in progress | '+red+'Port: {}\r'.format(port),end="")
class search_Numbers:
	def __init__(self):
		self.Number=input("\n[+] Enter Phone Number: ")
		self.Numbers=self.Number.split(' ')
		self.code = self.Number.split(' ')[0]
		try:self.phone = self.Number.split(' ')[1]
		except IndexError:exit(input('[-] You must type the country code, then a space, and then the phone number.. \nExample[ 974 52947429 ]'))
		self.Number_facebook()
	def Number_Info(self):
		if self.code == '20':country="EG:Egypt"
		elif self.code =='98':country="IR:Iran"
		elif self.code =='212':country="MA:Morocco"
		elif self.code =='213':country="DZ:Algeria"
		elif self.code =='216':country="TN:Tunisia"
		elif self.code =='249':country="SD:Sudan"
		elif self.code =='252':country="SO:Somalia"
		elif self.code =='961':country="LB:Libya"
		elif self.code =='962':country="JO:Jordan"
		elif self.code =='963':country="SY:Syria"
		elif self.code =='964':country="IQ:Iraq"
		elif self.code =="965":country="KW:Kuwait"
		elif self.code =='966':country="SA:Saudi Arabia"
		elif self.code =='967':country="YE:Yemen"
		elif self.code =='968':country="OM:Oman"
		elif self.code =='970':country="PS:Palestine"
		elif self.code =='971':country="AE:Emirates"	
		elif self.code =='972':country="ISR:Israel"
		elif self.code =='973':country="BH:Bahrain"
		elif self.code =='974':country="QA:Qatar"
		else:exit("[¿] The country code is not added for this number, it will be added soon")
		countr = country.split(':')[0]
		countr2= country.split(':')[1]
		send =get(f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={self.phone}&country_code={countr}",headers={"User-Agent":"8Y/69"})
		try:
			name = send.json()['result'][0]['name']
			if name=='':name='nothing'
			nump = send.json()['result'][0]['number']
			#Communication rights reserved @_agf
			pho=phonenumbers.parse('+'+self.Number)
			qtr = carrier.name_for_number(pho,'en')
			telegram_vv1ck(f'\n{grn}[+] phone : {nump}\n[+] country : {countr2}\n[+] ZIP code : {countr}\n[+] name : {name}\n[+] number type : {qtr} {wit}')
			Go_Back()
		except KeyError:
			telegram_vv1ck(yel+'[-] No leaked information found'+wit)
			Go_Back()
	def Number_Talabat(self):
		sent = post('https://api.talabat.com/api/v1/Account/ForgetPassword/8',headers={'Host': 'api.talabat.com','Content-Type': 'application/json','X-PX-AUTHORIZATION': '3:fb9556a0a8424d34117554cc0e9a3f92e45dba193d9dfcea3e4d54397a62d9b3:w1FY1NT4xhUFi5ilTK1vunJ6Svf6RVYj/56ZGRxTX6dG0/MPBBxqc2M2Am1Xj5wsFa8O2MI2IelPALRc+xKc9A==:1000:CF/0p7FhgwxQIiv6DKrQAXSMAAXWnOLAn6UHU+AQ2wF2nhGFSd8BFoHNpV745XG8SlRdyyNvYKLRZ1bjQsWStWXZERSihW/PDpgf/shTSWCs58re/hcBfL58ahk//g7dzq2Ai5uO0FUstSvxrN9gv04GSQ/IeqNZOs2l21pYzBu6TaOErlxZk3Ly58cJVwPUHW6+AJFMHCnXwziYXQnX9A==','Accept': '*/*','X-Device-Version': '8.7.8','X-Device-Source': '4','Accept-Language': 'ar-KW','BrandType': '1','AppBrand': '1','Accept-Encoding': 'gzip, deflate, br','X-PerseusSessionId': '1649634446063.1935786645.xejenkfhir','Content-Length': '76','X-Device-ID': '74180189-77F9-45AE-B384-71BF18BF110D','X-PerseusClientId': '1641917233047.9435967280.hrqaqruhlz','User-Agent': 'Talabat/1081 CFNetwork/1240.0.4 Darwin/20.5.0','Connection': 'keep-alive','X-NewRelic-ID': 'XQUPWFNbGwcBXVJRAgIGXg==','Cookie': 'AWSALB=eF0fwNXmW0uJ1J3kPZMR8nRB72BxHZbdpXvJ9PxysvhDr47vsq9nw5fcXmoN+vetHM3/jKL0PWfDw34vmH/KW1VSgvFottpEOFd0QUdIvCjxlf5ty5hp5VDzmGhB; AWSALBCORS=eF0fwNXmW0uJ1J3kPZMR8nRB72BxHZbdpXvJ9PxysvhDr47vsq9nw5fcXmoN+vetHM3/jKL0PWfDw34vmH/KW1VSgvFottpEOFd0QUdIvCjxlf5ty5hp5VDzmGhB; AWSALBTG=vmOEmccpqfD1FTGQ7OE3FoqU+ExjzW2mscQy1FLBSMbjtov/Ki752XRNLhMnjbB3IdwFl2ND4EJPtuoHgzNgaa1QA/2jQ+F8x+k/sEtxbopdh2i8kMo0J2q4QI1EqdRLxGJFfpF9iy70ch4aXZpqxUKyNepv0ZdPAfG66rMFjQlp12lmCrw=; AWSALBTGCORS=vmOEmccpqfD1FTGQ7OE3FoqU+ExjzW2mscQy1FLBSMbjtov/Ki752XRNLhMnjbB3IdwFl2ND4EJPtuoHgzNgaa1QA/2jQ+F8x+k/sEtxbopdh2i8kMo0J2q4QI1EqdRLxGJFfpF9iy70ch4aXZpqxUKyNepv0ZdPAfG66rMFjQlp12lmCrw=; __cf_bm=XSypDCSkDzPlJ6CNrHV5AsafVEyBE95uYzkmPdFU5kw-1649634471-0-AQmYgErYdOn7oRTQQHqsaNNXe9O7zPjbaugfBYsNd6ghTIBtjJkiqnEVNWEJ7g0OuOxJstN2DbmXVAf3GYDuS0beAlKUCD+CxAtU4jzLFLCo'},json={"Email":"","MobileNumber":self.phone,"mobileCountryCode":self.code}).text
		if ('"رقم الهاتف المتنقل غير صحيح"')in sent:telegram_vv1ck(red+'-[4] Not linked on Talabat.com ✖️')
		elif ('"عذرًا، لم نعثر على أي حساب مسجّل بهذا الرقم. لُطفًا حاول مرة أخرى أو أنشِئ حسابًا جديدًا."')in sent:telegram_vv1ck(red+'-[4] Not linked on Talabat.com ✖️')
		else:telegram_vv1ck(grn+'-[4] linked to an account Talabat.com ☑️')
		self.Number_Info()
	def Number_Twitter(self):
		sent=post('https://mobile.twitter.com/i/api/1.1/onboarding/task.json',headers={'Host': 'mobile.twitter.com','x-guest-token': '1513193250127069191','Accept': '*/*','Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA','x-twitter-client-language': 'en','Accept-Language': 'en','Accept-Encoding': 'gzip, deflate, br','Content-Type': 'application/json','Origin': 'https://mobile.twitter.com','Content-Length': '193','User-Agent': User_Agent(),'Referer': 'https://mobile.twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D','Connection': 'keep-alive','x-csrf-token': 'd45fd6d7c961ba75120edc7abd64653a','x-twitter-active-user': 'yes','Cookie': '_ga=GA1.2.2006589579.1649556997; _gid=GA1.2.251835287.1649556997; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMgCUhSAAToMY3NyZl9p%250AZCIlZjAxMTIyZDNkOTI5YjI5MDU2YzllODgzNDM0YjBjNmQ6B2lkIiU1OWY1%250AMTUzYzQ2ZDgwMzQ5ZTkyZWFkOTU3OTRkODQ5MQ%253D%253D--6479ef2ca757d7ba01f3f4f55fe6872ab93c38a6; external_referer=padhuUp37zjgzgv1mFWxJ8aHbAM%2FyKh7|0|8e8t2xd8A2w%3D; att=1-K1BUUTxMtqfARyCfLZCEPItYHYsk5SC2Hkacl7Hc; gt=1513193250127069191; ct0=d45fd6d7c961ba75120edc7abd64653a; guest_id=v1%3A164955699388392009; guest_id_ads=v1%3A164955699388392009; guest_id_marketing=v1%3A164955699388392009; personalization_id="v1_0jRguk/LS28SwZ/S4gm+IA=="'},json={"flow_token":"g;164955699388392009:-1649608365402:7lGsO4nGSLM0ocNoeWidwbc2:1","subtask_inputs":[{"subtask_id":"PasswordResetBegin","enter_text":{"text":self.Number,"link":"next_link"}}]}).text
		if ('"Verify your identity by entering the username associated with your Twitter account."')in sent:TWR = grn+'-[3] linked to an account Twitter ☑️'
		elif ('You’ll need to wait before you can try again. We do this when we notice suspicious activity.') in sent:TWR = yel+'-[3] search error [Twitter.com]'
		elif ('"Sorry, we could not find your account."'):TWR = red+'-[3] Not linked on Twitter.com ✖️'
		else:print(sent)
		telegram_vv1ck(TWR)
		self.Number_Talabat()
	def Number_IG(self):
		Cookies = get('https://www.instagram.com/',headers={'User-Agent': User_Agent()}).cookies
		send=post('https://www.instagram.com/accounts/account_recovery_send_ajax/',headers={'Host': 'www.instagram.com','Accept': '*/*','X-ASBD-ID': '198387','X-Requested-With': 'XMLHttpRequest','X-IG-App-ID': '1217981644879628','X-Instagram-AJAX': 'cec4fe0d7efe','Accept-Language': 'ar','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www.instagram.com','User-Agent': User_Agent(),'Referer': 'https://www.instagram.com/accounts/password/reset/','X-IG-WWW-Claim': '0','Content-Length': '95','Connection': 'keep-alive','Cookie': 'csrftoken='+Cookies['csrftoken']+'; ig_did='+Cookies['ig_did']+'; ig_nrcb='+Cookies['ig_nrcb']+'; mid='+Cookies['mid'],'X-CSRFToken': Cookies['csrftoken']},data='email_or_username='+self.Numbers[0]+self.Numbers[1]+'&recaptcha_challenge_field=&flow=&app_id=&source_account_id=').text
		if ('We sent an SMS') in send:IG=grn+'-[2] linked to an account instagram ☑️'
		elif ('We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.')in send:IG=grn+'-[2] linked to an account instagram ☑️'
		elif ('We apologize, but we are currently unable to recover your account. Please try again in a day.')in send:IG=grn+'-[2] linked to an account instagram ☑️'
		elif ('Please wait a few minutes before you try again.')in send:IG = yel+'-[2] search error [instagram.com]'
		else:IG = red+'-[2] Not linked on instagram.com ✖️'
		telegram_vv1ck(IG)
		self.Number_Twitter()
	def Number_facebook(self):
		sent=post('https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F%3Frefsrc%3Ddeprecated&search_attempts=1&ars=facebook_login&alternate_search=0&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0',headers={'Host': 'm.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://m.facebook.com','Accept-Encoding': 'gzip, deflate, br','Cookie':'fr=0tgtKAhNPBEEEt0ml..BiUhtV.PJ.AAA.0.0.BiUhtf.AWUiorIUqk0; m_pixel_ratio=3; wd=375x812; datr=VRtSYtbrYMCWJoSLYww9m0t3; sb=VRtSYsE5HyPq5GEOMqujTOJm','Connection': 'keep-alive','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent': User_Agent(),'Referer': 'https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Frefsrc%3Ddeprecated&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&_rdr','Content-Length': '81','Accept-Language': 'ar'},data='lsd=AVqp9U6EFAg&jazoest=2879&email='+self.Number+'&did_submit=%D8%A8%D8%AD%D8%AB').text
		if ('رقم الهاتف أو البريد الإلكتروني الذي أدخلته لا يطابق أي حساب. يرجى إعادة المحاولة') in sent:
			Fec = red+'-[1] Not linked on facebook.com ✖️'
		elif ('يمكننا إرسال رمز تسجيل دخول إليك') in sent:
			Fec = grn+'-[1] linked to an account facebook ☑️'
		elif ('إذا لم تكن قد سجّلت الدخول بالفعل')in sent:
			Fec = grn+'-[1] linked to an account facebook ☑️'
		elif ('جرّب إدخال كلمة السر') in sent:
			Fec = grn+'-[1] linked to an account facebook ☑️'
		else:
			Fec = red+'-[1] Not linked on facebook.com ✖️'
		telegram_vv1ck(Fec)
		self.Number_IG()
class search_Username:
	def __init__(self):
		self.username = input('[?] Enter username : ')
		self.lists=['https://www.instagram.com/{}','https://www.tiktok.com/@{}?','https://profil.chatujme.cz/{}','https://www.chess.com/member/{}','https://community.cloudflare.com/u/{}','https://www.codewars.com/users/{}','https://www.coroflot.com/{}','https://www.cracked.com/members/{}/','https://dev.to/{}','https://www.myminifactory.com/users/{}','https://ask.fm/{}','https://audiojungle.net/user/{}','https://www.bandcamp.com/{}','https://www.bazar.cz/{}/','https://www.behance.net/{}','https://bitbucket.org/{}/','https://2Dimensions.com/a/{}','https://www.7cups.com/@{}','https://about.me/{}','https://www.alik.cz/u/{}','https://discussions.apple.com/profile/{}','https://asciinema.org/~{}','https://ask.fedoraproject.org/u/{}']
		telegram_vv1ck('\n      ========== started ==========\n')
		self.User_Snapchat()
	def All_users(self):
		for urls in self.lists:
			doming = urls.split('://')[1]
			domins = doming.split('.')[0]
			if domins=='www':
				domins=doming.split('.')[1]
			try:
				send = get(urls.format(self.username),headers={'User-Agent': 'Mozilla/5.0 (@vv1ck) Gecko/20100101 Firefox/90.0'})
				if send.status_code==200:
					print(f'{grn}[+] linked on {domins}.com')
				else:
					print(f'{red}[-] Not linked on {domins}.com')
			except requests.exceptions.SSLError:
				print(f'{yel}[-] search error {domins}.com')
	def User_Twitter(self):
		sent = post('https://tweeterid.com/ajax.php',headers={'Host': 'tweeterid.com','Accept': '*/*','X-Requested-With': 'XMLHttpRequest','Accept-Language': 'ar','Accept-Encoding': 'gzip, deflate, br','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://tweeterid.com','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Connection': 'keep-alive','Referer': 'https://tweeterid.com/','Content-Length': '11','Cookie': '__gads=ID=ccc9ab21df07ddde-223e97ac73cd00bd:T=1649557735:RT=1649557735:S=ALNI_MaQb5VjpOd8mV3LhBSiTREny8oIVA; __utma=116903043.174839175.1649557735.1649557735.1649557735.1; __utmb=116903043.1.10.1649557735; __utmc=116903043; __utmt=1; __utmz=116903043.1649557735.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'},data='input='+self.username).text
		if ('error') in sent:
			telegram_vv1ck(red+'[-] Not linked on Twitter.com')
		else:telegram_vv1ck(grn+'[+] linked on Twitter.com')	
		self.All_users()
	def User_connected(self):
		sent=get('https://api.c2me.cc/b/nick_available?checksum=375868606731542156&nick='+self.username+'&o=H15qN4msIPPS2DGu9hgtwAJ19OCUnluB',headers = {'Host': 'api.c2me.cc','Accept': '*/*','Accept-Language': 'ar-JO;q=1, en-JO;q=0.9','Connection': 'close','Accept-Encoding': 'gzip, deflate','User-Agent': 'Connected2/1.301.2112140025 (iPhone; iOS 13.5; Scale/2.00)',}).text
		if ('unavailable')in sent:telegram_vv1ck(grn+'[+] linked on connected.com')
		else:telegram_vv1ck(red+'[-] Not linked on connected.com')
		self.User_Twitter()
	def User_Telegram(self):
		sent = get(f"https://t.me/{self.username}")
		if sent.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:telegram_vv1ck(red+'[-] Not linked on telegram.com')
		else:telegram_vv1ck(grn+'[+] linked on telegram.com')
		self.User_connected()
	def User_Snapchat(self):
		sent=get('https://www.snapchat.com/add/{}'.format(self.username),headers={'Host': 'www.snapchat.com','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Cookie': 'Marketing=true; Performance=true; Preferences=true; sc-cookies-accepted=true; sc-wcid=b47eed00-0e43-4203-856f-c2bf7b07911a; _ga=GA1.2.405324227.1649556235; _gat=1; _gid=GA1.2.1193952934.1649556235','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Accept-Language': 'ar','Accept-Encoding': 'gzip, deflate, br','Connection': 'keep-alive'})
		if sent.status_code == 200:telegram_vv1ck(grn+'[+] linked on Snapchat.com')
		else:telegram_vv1ck(red+'[-] Not linked on Snapchat.com')
		self.User_Telegram()
class search_email:
	
	def __init__(self):
		self.START_Check()
	def searcheds(self,eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML,ADBE,NEKER,Fec,APLE,TLBT):
		telegram_vv1ck(f"[*] Email : {eml} \n\n{APLE}\n{EML}\n{SNP}\n{TWR}\n{TIK}\n{INS}\n{SCLD}\n{NON}\n{ACP}\n{VIM}\n{NEapi}\n{DARK}\n{Fec}\n{ADBE}\n{NEKER}\n{TLBT}")
		Go_Back()
	def Email_Talabat(self,eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML,ADBE,NEKER,Fec,APLE):
		sent = post('https://api.talabat.com/api/v1/Account/ForgetPassword/8',headers={'Host': 'api.talabat.com','Content-Type': 'application/json','X-PX-AUTHORIZATION': '3:fb9556a0a8424d34117554cc0e9a3f92e45dba193d9dfcea3e4d54397a62d9b3:w1FY1NT4xhUFi5ilTK1vunJ6Svf6RVYj/56ZGRxTX6dG0/MPBBxqc2M2Am1Xj5wsFa8O2MI2IelPALRc+xKc9A==:1000:CF/0p7FhgwxQIiv6DKrQAXSMAAXWnOLAn6UHU+AQ2wF2nhGFSd8BFoHNpV745XG8SlRdyyNvYKLRZ1bjQsWStWXZERSihW/PDpgf/shTSWCs58re/hcBfL58ahk//g7dzq2Ai5uO0FUstSvxrN9gv04GSQ/IeqNZOs2l21pYzBu6TaOErlxZk3Ly58cJVwPUHW6+AJFMHCnXwziYXQnX9A==','Accept': '*/*','X-Device-Version': '8.7.8','X-Device-Source': '4','Accept-Language': 'ar-KW','BrandType': '1','AppBrand': '1','Accept-Encoding': 'gzip, deflate, br','X-PerseusSessionId': '1649634446063.1935786645.xejenkfhir','Content-Length': '76','X-Device-ID': '74180189-77F9-45AE-B384-71BF18BF110D','X-PerseusClientId': '1641917233047.9435967280.hrqaqruhlz','User-Agent': 'Talabat/1081 CFNetwork/1240.0.4 Darwin/20.5.0','Connection': 'keep-alive','X-NewRelic-ID': 'XQUPWFNbGwcBXVJRAgIGXg==','Cookie': 'AWSALB=eF0fwNXmW0uJ1J3kPZMR8nRB72BxHZbdpXvJ9PxysvhDr47vsq9nw5fcXmoN+vetHM3/jKL0PWfDw34vmH/KW1VSgvFottpEOFd0QUdIvCjxlf5ty5hp5VDzmGhB; AWSALBCORS=eF0fwNXmW0uJ1J3kPZMR8nRB72BxHZbdpXvJ9PxysvhDr47vsq9nw5fcXmoN+vetHM3/jKL0PWfDw34vmH/KW1VSgvFottpEOFd0QUdIvCjxlf5ty5hp5VDzmGhB; AWSALBTG=vmOEmccpqfD1FTGQ7OE3FoqU+ExjzW2mscQy1FLBSMbjtov/Ki752XRNLhMnjbB3IdwFl2ND4EJPtuoHgzNgaa1QA/2jQ+F8x+k/sEtxbopdh2i8kMo0J2q4QI1EqdRLxGJFfpF9iy70ch4aXZpqxUKyNepv0ZdPAfG66rMFjQlp12lmCrw=; AWSALBTGCORS=vmOEmccpqfD1FTGQ7OE3FoqU+ExjzW2mscQy1FLBSMbjtov/Ki752XRNLhMnjbB3IdwFl2ND4EJPtuoHgzNgaa1QA/2jQ+F8x+k/sEtxbopdh2i8kMo0J2q4QI1EqdRLxGJFfpF9iy70ch4aXZpqxUKyNepv0ZdPAfG66rMFjQlp12lmCrw=; __cf_bm=XSypDCSkDzPlJ6CNrHV5AsafVEyBE95uYzkmPdFU5kw-1649634471-0-AQmYgErYdOn7oRTQQHqsaNNXe9O7zPjbaugfBYsNd6ghTIBtjJkiqnEVNWEJ7g0OuOxJstN2DbmXVAf3GYDuS0beAlKUCD+CxAtU4jzLFLCo'},json={"Email":eml,"MobileNumber":"","mobileCountryCode":"962"}).text
		if ("يرجى إدخال عنوان البريد الإلكتروني بالكامل، بما فيه الرمز '@'.")in sent:
			TLBT = f'{red}-[13] Not linked on Talabat.com ✖️'
		elif ('"قمنا بإرسال رسالة إلى بريدك الالكتروني لتعيين كلمة المرور الجديدة."')in sent:
			TLBT = f'{grn}-[13] linked on Talabat.com ☑️'
		elif ('"عذراً، لم نستطع إيجاد حساب بعنوان البريد الالكتروني المدخل. الرجاء أعد المحاولة أو أنشئ حساب جديد.')in sent:
			TLBT = f'{red}-[13] Not linked on Talabat.com ✖️'
		else :
			TLBT=f'{yel}-[13] search error [Talabat.com]'
		self.searcheds(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML,ADBE,NEKER,Fec,APLE,TLBT)
	def Email_icloud(self,eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML,ADBE,NEKER,Fec):
		sent = post('https://iforgot.apple.com/password/verify/appleid',headers={'Host': 'iforgot.apple.com','sstt': 'Q9dqgF6zvfuHYqZoDAZqIgeJCCsgWiSaHROB9IfZLyyxZENDTjTB%2FxHy8MFxuBplm53Wqu4T3EE4KHLZKO4ixhTz310Q2sboultbytrkNUUNzULbXSJWwXBTceRf1ltHPpQPGZiB%2B0RmPOz8YoExrpJYEyixo83eXowsW4bfOI1EYC7lY5PP1MSlDTahLkmKUpfSANmjR8aeL2WYnvkcVCsaEp8TBS6lkFMTtZnJCI3pqiCbr9n8M%2FqCYDtwS33czknxQUBiFW9Rv6p2lDjdTUziTSamxRpJB9sfl7ECMTNFsMsxmuaZ4FfC2s9CfzEox5hv2qql67jDNsl4yWNmPJOQUeqMRUhRF0SovMazXpQzcpq9KKM4VN%2FCSTmsFIdf1rJCvMHJzp9fi1j1','Accept': 'application/json, text/javascript, */*; q=0.01','X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1","L":"ar","Z":"GMT+03:00","V":"1.1","F":"sla44j1e3NlY5BNlY5BSs5uQ32SCVc.xV4WHNEJ7QejLFV0AL9LXYem3..KX_ccugW.0KO1.3CO1.3CO1.0em33AYum3.DnygW.0CO1.1MxO1..Pm3..f7ZCO1.8WY5Py.eaB0Tf4O1.0Pm3.7PlHoJSLFV.5gJh46KZ7.9f7F.Wf7F.KLFV.egW01sygW.2ezf7F.Wf7F.Bzf7F.CLFV.4O3Wf7F0BBNlY5BPdGY5BOgkLT0XxU..1dT"}','X-Requested-With': 'XMLHttpRequest','Accept-Language': 'en','Accept-Encoding': 'gzip, deflate, br','Content-Type': 'application/json','Origin': 'https://iforgot.apple.com','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Referer': 'https://iforgot.apple.com/','Content-Length': '18','Connection': 'close','Cookie': 'dslang=SA-EN; site=SAU; idclient=web; X-Apple-I-Web-Token=AAAAKjN8ODhlMzNiMGRkZjI4MjFjOTQ3NTJiM2U1ZDAwYjk2YTUAAAGAFH21GK27euLgsJjvslIO9TjGArMbzl9i2EoSB+b7uHp/RAmKN2IJIkveABCJ8Uzzjd3sf8L+wIDOw6YuMGCo5jTHxTReTl7DNTeOSucaYwky3g==; ifssp=AEC33734B58F264A28F32A883E54F4D9A57449452C340E59EF9F847872885E5DC06C02A3B977173F67E17AA89EA1CEB885B9DCAFCDFA6C4AB09BA1011BA8F62E41A0905CC50CC428E2DE7AA51466FDAB5BC33E34B2A2DE90FAAE4A761133333C3A07B8EFB7A279C205A55FB02FBDC8CE91F353DD11AFBD2E; s_ppv=acs%253A%253Akb%253A%253Aht%253A%253Aht201487%253A%253AIf%2520you%2520forgot%2520your%2520Apple%2520ID%2520password%2520%2520%2528en-us%2529%2C11%2C11%2C635%2C375%2C635%2C375%2C812%2C3%2CL; s_fid=526EB125AD97111F-2EFFD00E0C1A46CD; s_sq=applesupportglobalprod%3D%2526pid%253Dacs%25253A%25253Akb%25253A%25253Aht%25253A%25253Aht201487%25253A%25253AIf%252520you%252520forgot%252520your%252520Apple%252520ID%252520password%252520%252520%252528en-us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fsupport.apple.com%25252Fen-us%25252FHT201487%252523ac-gn-menustate%2526ot%253DA; s_vi=[CS]v1|312986D997AA8641-400007F81865822D[CE]; s_cc=true; s_pathLength=no%20channel%3D1%2C; s_ppvl=%5B%5BB%5D%5D; POD=us~en; geo=JO; dssf=1; XID=3ad4f17127c088f82e53ce32fd43cb67'},json={"id":eml})
		if ('"This Apple ID is either not valid or not supported."')in sent.text:APLE = f'{red}-[0] Not linked on icloud.com ✖️'
		elif ('{ }') in sent.text:APLE = f'{grn}-[0] linked on icloud.com ☑️'
		elif ('"forgotPasswordFlow" : true')in sent.text:APLE = f'{grn}-[0] linked on icloud.com ☑️'
		else:APLE = f'{yel}-[0] search error icloud.com'
		self.Email_Talabat(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML,ADBE,NEKER,Fec,APLE)
	def Email_facebook(self,eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML,ADBE,NEKER):
		sent=post('https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F%3Frefsrc%3Ddeprecated&search_attempts=1&ars=facebook_login&alternate_search=0&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0',headers={'Host': 'm.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://m.facebook.com','Accept-Encoding': 'gzip, deflate, br','Cookie':'fr=0tgtKAhNPBEEEt0ml..BiUhtV.PJ.AAA.0.0.BiUhtf.AWUiorIUqk0; m_pixel_ratio=3; wd=375x812; datr=VRtSYtbrYMCWJoSLYww9m0t3; sb=VRtSYsE5HyPq5GEOMqujTOJm','Connection': 'keep-alive','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Referer': 'https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Frefsrc%3Ddeprecated&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&_rdr','Content-Length': '81','Accept-Language': 'ar'},data='lsd=AVqp9U6EFAg&jazoest=2879&email='+eml+'&did_submit=%D8%A8%D8%AD%D8%AB').text
		if ('رقم الهاتف أو البريد الإلكتروني الذي أدخلته لا يطابق أي حساب. يرجى إعادة المحاولة') in sent:
			Fec = f'{red}-[12] Not linked on facebook.com ✖️'
		elif ('يمكننا إرسال رمز تسجيل دخول إليك') in sent:
			Fec = f'{grn}-[12] linked on facebook.com ☑️'
		elif ('إذا لم تكن قد سجّلت الدخول بالفعل')in sent:
			Fec = f'{grn}-[12] linked on facebook.com ☑️'
		elif ('جرّب إدخال كلمة السر') in sent:
			Fec = f'{grn}-[12] linked on facebook.com ☑️'
		else:
			Fec = f'{red}-[12] Not linked on facebook.com ✖️'
		self.Email_icloud(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML,ADBE,NEKER,Fec)
	def Email_newyorker(self,eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML,ADBE):
		sent = post('https://www.newyorker.com/api/up/v2/reset-password-token',headers={'Host':'www.newyorker.com','Accept':'*/*','Accept-Language':'ar','Accept-Encoding':'gzip,','Content-Type':'application/json','Origin':'https://www.newyorker.com','User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Connection':'keep-alive','Referer':'https://www.newyorker.com/account/request-password-reset','Content-Length':'277','Cookie':'_fbp=fb.1.1649519360044.281228789; _gali=account-request-password-reset-form; sID=2e98e6af-22bc-4547-867a-61b77cc4dd52; CN_sp=4572387a-4d39-4694-b86c-e927ebd0b10d; CN_su=674e4e42-6c93-40d1-94b0-c5e13a6a3b8f; pID=f5b9f3d9-48cd-4a79-a66e-c3faf82529a1; bounceClientVisit1990=N4IgbiBcoDYPYHMEFMAmB9AlgOygMwEMYBnZAGhGIFcAjAW0wBdG11k6DMZ1VOYBPfEVIVq9Jiwzs+6AA5wYTTAGNiQkuUq0GzVtK7o8cOKnUit43VI4HlBAE6NjuSIQ2jtEvTe7zUd4kY1V2FNMR1JNh90AOJMVEFIAAYPS0j9bgALKjo4ezNNTKI8OQJ+AHcibjpkRgKKPCoYXzLK5vQaupD3EAdGFRhkGLgqbC6UkEwaAA90FkD6kGQwZHt0eCRWHEW7R0WwTGRy1nlZJodFjZx0e2R5RzRF8K9rGWUmxipbp88rKJkaHk4OUmAAvH5pbxvexwYjEcp5VDBNzmW4IdAIAgsdDPKyLNEYrFDL4wAoAXwaYC6AEYAGwAFgAnABWamMgDMAA56RQDqZIHSmayObSGaLRcyKAQ4FAJjBZFAQJlmLJiABSdkAQTVACYAGK6vXlY0AOmwR34eQA1qsTco4HRDQRlPbRoxDbcAI5UZCBAC0sgIcIR9lQftupDqUuCEzAsggkB1FH5IAVFHykBAxvKJoQxgQgztDpAFGUVKggpZbPZotE8SgnIoCGUGYA7LSKHRZcn65nGdT2czmRyddTmfTW0lObSda3qa2SyAYOWBQyqxzuRQqL3qWSgA; CN_geo_country_code=JO; CN_xid=8b752d11-35b5-49c9-8bac-49880ccf47d0; CN_xid_refresh=8b752d11-35b5-49c9-8bac-49880ccf47d0; verso_bucket=766; _pubcid=%7B%22id%22%3A%2201G07G8849THBB7CR7RQG9AYRY%22%2C%22ts%22%3A1649519387196%7D; __ibxu=1; aam_uuid=16132952282207532803491485581189713430; aamconde=conde%3Dsv%3BCN%3D750744; aamoptsegs=aam%3D226821; _ga=GA1.2.653347424.1649519361; _gid=GA1.2.395229970.1649519361; _pbjs_userid_consent_data=3524755945110770; cto_bidid=kwOHol9rdG96THpiZUpjSU95eTBjWGl1NmJJU1A3ZDhaNTE2VWF1dTgzcEs0NkhSVUU3czF2ZkxPWUNHWmxhUzF3b25ndWxYJTJGOTNCa0VudG5kb3N3SlVtWEJHVHNFNVVLbjNiTlJtT0lCRiUyRnFWejFkcnFRUUVGR1lsYmlRdWF3UDV3am8; cto_bundle=DBU4LV91JTJGUGxKeXhsVTAzJTJCdHZoUUFPWG15QW5RRmluOFlWQ3h1aG1SSWtoTzREbTc3Z0NnV1dJMnQ3M09PZUQyYjZWRU9Eek9VenFjVm0wYlZMZTN3WFRNVlFGUWFxc2hFVWw4TkVyaTRNZjkzM3R2c0d2MFpXM3lFaWFCOCUyQnBhZzRuTGpITW0lMkI5TWFaVXVhOGZDOFZrakRIdzZVNmElMkY3VzcwQjlBTGdZRmtzS25zJTNE; _hjAbsoluteSessionInProgress=0; _hjSessionUser_1537215=eyJpZCI6ImMxMjI0MzdlLTkwMTAtNTc3Zi1iMjcwLTEwMzQ0Yjg3NTdjYyIsImNyZWF0ZWQiOjE2NDk1MTkzNjE1MjMsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1537215=eyJpZCI6IjAyYjNiODExLWI2OTctNGIwMi1iZDFjLTVlNmQ3NDVkMDc0ZCIsImNyZWF0ZWQiOjE2NDk1MTkzNjE1MjksImluU2FtcGxlIjp0cnVlfQ==; _pin_unauth=dWlkPVltRm1aV1l6T1RRdFlqaGpOUzAwTldKbExUbGtNelV0WkRkaE56SXhZMkpoTlRobQ; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample=1; _wchtbl_do_not_process=0; _wchtbl_pixel_sync=1; sailthru_content=1d32e1f59395e617f74a89ce3c6dfb7e; sailthru_visitor=02806ab1-bc67-4941-9e3d-5429b4725a18; CN_segments=co.w2214; OptanonConsent=isIABGlobal=false&datestamp=Sat+Apr+09+2022+18%3A49%3A42+GMT%2B0300+(EEST)&version=6.32.0&hosts=&consentId=2b28a397-c0f1-4ad0-868b-b5d8c93049ad&interactionCount=0&landingPath=https%3A%2F%2Fwww.newyorker.com%2Faccount%2Frequest-password-reset&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1; _sp_id.e778=14637d96-2e42-42bb-adb5-6317ce135b71.1649519361.1.1649519383.1649519361.de48f7c3-58cc-4498-85e4-d861a9b41b68; _sp_ses.e778=*; kw.pv_session=2; CN_in_visit_m=true; OneTrustWPCCPAGoogleOptOut=true; __pdst=ffe2e9123b0e4ff69370642f98743529; _wchtbl_sid=6b488d96-8073-4c2a-a1a0-6d16510d2971; _wchtbl_uid=c1b70563-54bc-4040-880c-c07a76514fcd; sailthru_pageviews=2; usprivacy=1---; CN_ad_block=1; _cc_id=5c08cafb081ab9f8be82db6d26557532; panoramaId_expiry=1649605769972; _lr_env_src_ats=false; _lr_retry_request=true; pbjs-unifiedid=%7B%22TDID%22%3A%220819e36c-138f-41f2-9a1b-5b9c9ebcbc4b%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222022-04-09T15%3A49%3A29%22%7D; AMCV_F7093025512D2B690A490D44%40AdobeOrg=-408604571%7CMCIDTS%7C19092%7CMCMID%7C15982267604229512573474991175601013455%7CMCAAMLH-1650124160%7C6%7CMCAAMB-1650124160%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1649526560s%7CNONE%7CMCSYNCSOP%7C411-19099%7CvVersion%7C4.6.0; __qca=P0-1276710263-1649519361500; _hjFirstSeen=1; bounceClientVisit1990v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0AdgKbECeA9gE4DWVjZAxvQLZECGHLgFcKCIoyoBHIVRQIAtBD4oUxJgBN5ElFQQgANCEYwQpYmQDm9ehbBVOPEAF8gA; AMCVS_F7093025512D2B690A490D44%40AdobeOrg=1; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-8293713-14=1; kw.session_ts=1649519360762; _gcl_au=1.1.696896287.1649519360; CN_visits_m=1651352400708%26vn%3D1; pay_ent_smp=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsInZlciI6MX0.eyJ1cmxzIjpbXSwiY250IjowLCJtYXgiOjQsImV4cCI6MjAyMjA0fQ.Xdb2kbd13HnoJ58nuHeHHBLGk3CsBcse','x-client':'Verso-NewYorker',},json={"data":{"attributes":{"account":"tny","emailFrom":"help@newyorker.com","substitutions":{"domain":"https://www.newyorker.com","site_name":"The New Yorker","subject":"Reset your password"},"templateId":"d-1df18e1107604c519406e76a53a5acf3","emailTo":eml}}}).text
		if ('Dynamic Templated Email Sent') in sent:
			NEKER = f'{grn}-[14] linked on newyorker.com ☑️'
		else:
			NEKER = f'{red}-[14] Not linked on newyorker.com ✖️'
		self.Email_facebook(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML,ADBE,NEKER)
		
	def Email_adobe(self,eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML):
		sent = post('https://auth.services.adobe.com/signin/v2/users/accounts',headers={'Host': 'auth.services.adobe.com','Accept': 'application/json, text/plain, */*','X-IMS-CLIENTID': 'AdobeSupport1','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'ar','Content-Type': 'application/json','Origin': 'https://auth.services.adobe.com','X-DEBUG-ID': 'c52b52fa-39b3-4ff4-951a-8c7bcd85bdcb','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Referer': 'https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2FAdobeSupport1%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Fhelpx.adobe.com%252Fmanage-account%252Fusing%252Fchange-or-reset-password.html%2523old_hash%253D%2526from_ims%253Dtrue%253Fclient_id%253DAdobeSupport1%2526api%253Dauthorize%2526scope%253DAdobeID%252Copenid%252Cgnav%252Ccreative_cloud%252Csao.creative_cloud%252Cread_organizations%252Csao.cce_private%252Cadditional_info.projectedProductContext%252Cadditional_info.roles%26state%3D%257B%2522ac%2522%253A%2522AdobeSupport1%2522%252C%2522jslibver%2522%253A%2522v2-v0.30.0-5-g460356a%2522%252C%2522nonce%2522%253A%25221987056194443523%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=AdobeSupport1&scope=AdobeID%2Copenid%2Cgnav%2Ccreative_cloud%2Csao.creative_cloud%2Cread_organizations%2Csao.cce_private%2Cadditional_info.projectedProductContext%2Cadditional_info.roles&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2FAdobeSupport1%3Fredirect_uri%3Dhttps%253A%252F%252Fhelpx.adobe.com%252Fmanage-account%252Fusing%252Fchange-or-reset-password.html%2523old_hash%253D%2526from_ims%253Dtrue%253Fclient_id%253DAdobeSupport1%2526api%253Dauthorize%2526scope%253DAdobeID%252Copenid%252Cgnav%252Ccreative_cloud%252Csao.creative_cloud%252Cread_organizations%252Csao.cce_private%252Cadditional_info.projectedProductContext%252Cadditional_info.roles%26response_type%3Dtoken%26state%3D%257B%2522ac%2522%253A%2522AdobeSupport1%2522%252C%2522jslibver%2522%253A%2522v2-v0.30.0-5-g460356a%2522%252C%2522nonce%2522%253A%25221987056194443523%2522%257D&state=%7B%22ac%22%3A%22AdobeSupport1%22%2C%22jslibver%22%3A%22v2-v0.30.0-5-g460356a%22%2C%22nonce%22%3A%221987056194443523%22%7D&relay=c52b52fa-39b3-4ff4-951a-8c7bcd85bdcb&locale=en_US&flow_type=token&idp_flow_type=login&s_p=apple%2Cfacebook%2Cgoogle','Content-Length': '44','Connection': 'keep-alive','Cookie': 's_ecid=MCMID%7C89023136759998903061560795212597243727; relay=c52b52fa-39b3-4ff4-951a-8c7bcd85bdcb; s_ppv=[%22auth.services.adobe.com/en_US/index.html%22%2C100%2C0%2C635%2C375%2C635%2C375%2C812%2C3%2C%22L%22]; s_cc=true; AMCV_9E1005A551ED61CA0A490D45%40AdobeOrg=870038026%7CMCMID%7C89023136759998903061560795212597243727%7CMCAID%7CNONE%7CMCOPTOUT-1649525032s%7CNONE%7CMCAAMLH-1650122632%7C6%7CMCAAMB-1650122632%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19099%7CvVersion%7C5.0.0; gpv=Account:IMS:GetStarted:OnLoad; s_sq=%5B%5BB%5D%5D; _sctr=1|1649451600000; adcloud={%22_les_v%22:%22y%2Cadobe.com%2C1649519620%22}; s_cpc=1; s_vs=1; AMCVS_9E1005A551ED61CA0A490D45%40AdobeOrg=1; _fbp=fb.1.1649517819346.1692133422; _gcl_au=1.1.1649905152.1649517819; _scid=0d05b6b7-1750-45b8-b7c3-862668f67175; _uetsid=08754bc0b81911ec89b13d72fcdf79a6; _uetvid=08754ae0b81911ecaeec95004a9fac9e; kndctr_9E1005A551ED61CA0A490D45_AdobeOrg_identity=CiY4OTAyMzEzNjc1OTk5ODkwMzA2MTU2MDc5NTIxMjU5NzI0MzcyN1IPCIrssfeAMBgCKgRJUkwx8AGK7LH3gDA%3D; mbox=session#f2a56aebf82a44f98bf32041da0b1e6e#1649519680|PC#f2a56aebf82a44f98bf32041da0b1e6e.37_0#1712762620; OptanonAlertBoxClosed=2023-04-09T15:23:38.872Z; OptanonChoice=1; OptanonConsent=groups=C0001:1,C0002:1,C0003:1,C0004:1; ak_bmsc=5752DF420F4F0889910B539315F80787~000000000000000000000000000000~YAAQxnIdsC1aFgOAAQAAV3LsDg8PCNZG15QI2pTR/7b2kYa76p6JQ3Ma/bAGKoKkLaqWKuszTJKMo6UeA/KPQi4LZevWm35a5Gx6ic8AB9JAjuTKI0WGAa/Ai9AKG811NWnFRRUKwxK4K6lkLbHkSb9CyTqaCm2jhHdcoojKwK+xQigOAjB4OQ0BYEGTUCUeC2aKm0acUlHvs3/JAqPBpGi6A2iA6bzzjYlyjXC+PDwr0KweL55PQAYoK2J5kcgh/NpGNMtFfNA+gRswMtOnlyjPmLJ5zjv/btTNA0NrFdNZMEcmdqXK2Od1mTrFOzNnL0CgRqwl0XNuf2ahSJRiBSCb5+NsWRrK1QQ00FQjRdLqjp3JPKvzCe1c7y6qxupvmC1gnspo5tSVDFVDfqS/5q+sR6EaCxTJi2V4jY5GBkDPCI/G2o0nQ02NhzS3Lqo7XIP+1scS4c6iuolZACSBzxi3aOWK9tULqzsYBqZ8E+0ZrHMdjOTXNw==; at_check=true; bm_sv=5EC3EDC1F4C3A5F263D630ADCEB5DF17~ZFEjolABkoGTG/BL70tYJvyOLv+SVWDKDoqnOLQ3m/xemkVhqr+5vwk8tffDEkJ9oXqLV2yeGKNhG7lI6HJaWAYk6SPAmJSj8e0GwMVRZiLzAPSmC/ym5jvLpQVK9yL/Ih2ktzJjsPuBJS/VMcWeWLbokkmHo3lHxoskFrMlbCY=; fg=WK6VXWGUFLE5ALECEAQFRHQACA======; s_nr=1649517818176-New; feds_visitor_audience=%7B%22visitor%22%3A%22IUCfVXhUF_e00czuFie9b%22%2C%22cohort%22%3Atrue%7D; feds_visitor_id=IUCfVXhUF_e00czuFie9b'},json={"username":eml}).text
		if ('"id":"password"') in sent:
			ADBE = f'{grn}-[13] linked on adobe.com ☑️'
		elif ('passwordResetRequired') in sent:
			ADBE = f'-{grn}[13] linked on adobe.com ☑️'
		else:
			ADBE = f'-{red}[13] Not linked on adobe.com ✖️'
		self.Email_newyorker(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML,ADBE)
		
	def Email_darkwebids(self,eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,EML):
		#try:
		send = post('https://secure.darkwebid.com/user/login',headers={'Host': 'secure.darkwebid.com','Cookie': 'has_js=1; _ga=GA1.2.404847453.1629450192; _gid=GA1.2.317407483.1629450192; _gat=1','User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0','Content-Length': '118','Origin': 'https://secure.darkwebid.com','Referer': 'https://secure.darkwebid.com/user/login','Upgrade-Insecure-Requests': '1','Sec-Fetch-User': '?1','Te': 'trailers'},data={
			'name':eml,
			'form_build_id':'form-T8F0Un2cVoe_nvYrXQHIOO176-yBIpuiG46EIOTmhQE',
			'form_id':'user_login','op':'Continue'}).text
		if 'is not recognized as a user name or an e-mail address.'in send:
			DARK = f'{red}-[11] Not linked on darkwebid.com ✖️'
		else:
			DARK = f'{grn}-[11] linked on darkwebid.com ☑️'
		self.Email_adobe(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML)
			
		#except:
			#DARK = '-[11] search error [darkwebid.com]'
			#self.searcheds(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,DARK,EML)
	def Email_newsapi(self,eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,EML):
		try:
			send = post('https://newsapi.org/reset-password',headers={
			'Host': 'newsapi.org','Cookie': '_ga=GA1.2.596557937.1629129476; _gid=GA1.2.1573072051.1629129476; _gat_gtag_UA_91285317_5=1','User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0','Origin': 'https://newsapi.org','Referer': 'https://newsapi.org/reset-password'},data={'email':eml})
			if "Please check your email for further instructions,"in send.text:
				NEapi = f'{grn}-[10] linked on newsapi.com ☑️'
			elif "We don&#39;t have a registered user with that email address."in send.text:
				NEapi = f'{red}-[10] Not linked on newsapi.com ✖️'
			else:
				NEapi = f'{yel}-[10] search error [newsapi.com]'
			self.Email_darkwebids(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,EML)
		except:
			NEapi = f'{yel}-[10] search error [newsapi.com]'
			self.Email_darkwebids(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,NEapi,EML)
	def Email_connected(self,eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,EML):
		sent=post('https://api.c2me.cc/b/forgot_password',headers = {'Host': 'api.c2me.cc','Content-Type': 'application/x-www-form-urlencoded','Connection': 'close','Accept': '*/*','User-Agent': 'Connected2/1.301.2112140025 (iPhone; iOS 13.5; Scale/2.00)','Accept-Language': 'ar-JO;q=1, en-JO;q=0.9','Accept-Encoding': 'gzip, deflate','Content-Length': '87',},data="checksum=547996441674972655&nick="+eml+"&o=7dRwvdvd30saSY4zQvEPE8cI1tCvHMSw").text
		if ('err_username_not_found') in sent:
			VIM = f'{red}-[9] Not linked on connected.com ✖️'
		elif ('"status": "OK"') or ('err_already_requested_today') in sent:
			VIM = f'{grn}-[9] linked on connected.com ☑️'
		else:
			VIM = f'{yel}-[9] search error [connected.com]'
		self.Email_newsapi(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,VIM,EML)
		
	def Email_acaps(self,eml,domn,SNP,TWR,TIK,INS,SCLD,NON,EML):
		try:
			send = post('https://www.acaps.org/user/password',headers={'Host': 'www.acaps.org','Cookie': 'has_js=1; acaps_mode=advanced; _ga=GA1.2.895538350.1628908856; _gid=GA1.2.1525444071.1628908856; _gat_UA-21240261-1=1; cookie-agreed=2','User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0','Referer': 'https://www.acaps.org/user/password'},data={'name': eml,'form_build_id':'form-GmhJBczE4v4RuumvVqBrs4AhCvdrGGNH64mmQDTotlw','form_id':'user_pass','op':'E-mail+new+password'}).text
			if 'is not recognized as a user name or an e-mail address.'in send:
				ACP = f'{red}-[8] Not linked on acaps.com ✖️'
			else:
				ACP = f'{grn}-[8] linked on acaps.com ☑️'
			self.Email_connected(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,EML)
		except:
			ACP = f'{yel}-[8] search error [acaps.com]'
			self.Email_connected(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,ACP,EML)
	def Email_Noon(self,eml,domn,SNP,TWR,TIK,INS,SCLD,EML):
		try:
			send = post('https://www.noon.com/_svc/customer-v1/auth/reset_password',headers={'Host': 'www.noon.com','Connection': 'keep-alive','Content-Type': 'application/json','Accept': 'application/json, text/plain, */*','x-mp': 'noon','Accept-Language': 'ar','Cache-Control': 'no-cache, max-age=0, must-revalidate, no-store','x-content': 'mobile','Accept-Encoding': 'gzip, deflate, br','Origin': 'https://www.noon.com','User-Agent': User_Agent(),'Referer': 'https://www.noon.com/uae-ar/account_mobile/','x-platform': 'web','x-cms': 'v2','Content-Length': '31','Cookie': '_fbp=fb.1.1649434457601.30483847; th_capi_em=fc945833848b575a92d25754baeed93ff724c24b40873c1374cbb3e0f9c196d7; RT="z=1&dm=noon.com&si=bt92a4qk6s5&ss=l1qrrxjx&sl=1&tt=2z5&ld=2zy&nu=d41d8cd98f00b204e9800998ecf8427e&cl=1b0r"; bm_sv=81D03D0C1726EEB13ECC5F50C6238247~ae/WvTgGlggbMrVOs0djwhHiGW1DZs15SiGRwgz8EHjUAp8rVkFlzJmvZGGol5StMktDcy4r7pzYarVVlpzoKif+6eYuVgfXyzPvt5skDMX0UW2Oxd8yrwWEre70FgtUiZjBMjkPGUGgqqeuNh1B+Y9wrpAK56F8Xk6Tc9kWWh0=; _ga=GA1.2.1511942650.1649434456; _gid=GA1.2.244731265.1649434456; ak_bmsc=FA0CEE4451267DE50368F32F1508E495~000000000000000000000000000000~YAAQIIQUAtOZNQqAAQAAMAN3Cg/u+Fola0LiGwMB15stewXplJlmXCMHx3+EhVAG+KhzTR/MXe4GyBnxMkIPvyHEipByet/w/bgFMbb+NNuLBKgFpKvViXlvmjEzJxs/TgY9u4G7Eq15lUtqkXPz227DSNPPiBK4Ptz1LC/yNI8txWXklElfnyyFtVIbir9Hm/+fLFBuncF4torDF6JZgY4k1/DUMF44qIiJ9KGlRiB5TuXZYchSbe0szR1ZLaEBTL/cyK7JDE4AxCXMc6dcBgxJcR1g+H5DoNMElryzFT46q4out25oWCeC9JCmTppSLvNWcP1tr8pYAoef+q5sFXQ9nLbKEqMfTu/ICcMeGNrCQpdf10Ovnjph2Bn9EDwSajmss1j+R5zwpp2pcK2OauIQlvyu3/Nj7SFn3MlWBA==; _etc=xXj4CVQR3qdB0qOg; _nsc=nsv1.public.eyJzdGlkIjoiMjFhNzZhNDItZmNmZC00OWJkLWE4MzgtMTE4Y2VlZGZiMjc3Iiwic2lkIjoiODY4ODViNmU0MTNhNDVhMjhhOTBkZmY5Y2ExZWM5MGMiLCJpYXQiOjE2NDk0NDMwMDMsInZpZCI6IjQ4ZDdmYWM4LWE1ZjQtNDNhNi1iMzcwLTVkYTc0ZTllN2FlYiIsImhvbWVwYWdlIjp7fX03c09oTk5HWGViMGp1QjlKZHlid09IR1FGcld3OFdxWVdwaWFLVVcvZ2JrPQ.MQ; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJNE5qZzROV0kyWlRReE0yRTBOV0V5T0dFNU1HUm1aamxqWVRGbFl6a3dZeUlzSW1saGRDSTZNVFkwT1RRek5EUTFOSDAuY25rNTVLUTc1M0tpcHJTRzFiNElvTmFyVk1ZQy1YTzNZZXhBOVVnbWY2NCIsImlhdCI6MTY0OTQ0MzAwM30.sV_CVVbPhi3HwjgpixzGUGrB1ydZpZUW3reZr3TE7eI; x-available-ae=ecom-daily; bm_mi=162A23E5DA24869BD421DA507DEA9EDC~aXWrEG9wGux9lmppgExf8ou9k5du3hopUIu4E33OERxgBQ7TomUrQ6y8b6VuFedyyC9YNmPYJN+9Q+I++2yc8+eD+5c+SptCQVC9MhWbDiBtFOEVMQmUXGBpDlB9EuyYmrvo76ZESA7z8KICE/03iO7aMaDvjr3xHEcteHKQ7EfyuxJur3E3wVheJrQ7IUoI8Y27lSmBESoF50sQ105gpqG/DbN2bAXDqYuA6P4k5UYRmaypv6X4S22e+3rEEYfr53nTfIe47QGRpC2vN1Zj8Q==; AKA_A2=A; _sctr=1|1649365200000; _scid=dfb5e2eb-e77b-427a-8cb0-6f5d9b9d50a0; _gcl_au=1.1.680605546.1649434456; isAppInstallBannerDismissed=true; visitor_id=48d7fac8-a5f4-43a6-b370-5da74e9e7aeb','x-locale': 'en-ae'},json={"email":eml}).text
			if ('"message":"ok"')in send:
				NON = f'{grn}-[7] linked on noon.com ☑️'
			elif ('No user found with that email address')in send:
				NON = f'{red}-[7] Not linked on noon.com ✖️'
			else:
				NON = f'{yel}-[7] search error [noon.com]'
			self.Email_acaps(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,EML)
		except:
			NON = f'{yel}-[7] search error [noon.com]'
			self.Email_acaps(eml,domn,SNP,TWR,TIK,INS,SCLD,NON,EML)
	def Email_SoundCloud(self,eml,domn,SNP,TWR,TIK,INS,EML):
		try:
			aBaDy1337 = post("https://api-mobile.soundcloud.com/users/passwords/reset?client_id=Fiy8xlRI0xJNNGDLbPmGUjTpPRESPx8C",json={"email":eml}).text
			if '{}' in aBaDy1337:
				SCLD = f'{grn}-[6] linked on soundcloud.com ☑️'
			elif 'identifier_not_found' in aBaDy1337:
				SCLD = f'{red}-[6] Not linked on soundcloud.com ✖️'
			else:
				SCLD = f'{yel}-[6] search error [soundcloud.com]'
			self.Email_Noon(eml,domn,SNP,TWR,TIK,INS,SCLD,EML)
		except:
			SCLD = f'-{yel}[6] search error [soundcloud.com]'
			self.dones(eml,domn,SNP,TWR,TIK,INS,SCLD,EML)
	def Email_Instagram(self,eml,domn,SNP,TWR,TIK,EML):
		try:
			Cookies = get('https://www.instagram.com/',headers={'User-Agent': User_Agent()}).cookies
			send=post('https://www.instagram.com/accounts/account_recovery_send_ajax/',headers={'Host': 'www.instagram.com','Accept': '*/*','X-ASBD-ID': '198387','X-Requested-With': 'XMLHttpRequest','X-IG-App-ID': '1217981644879628','X-Instagram-AJAX': 'cec4fe0d7efe','Accept-Language': 'ar','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www.instagram.com','User-Agent': User_Agent(),'Referer': 'https://www.instagram.com/accounts/password/reset/','X-IG-WWW-Claim': '0','Content-Length': '95','Connection': 'keep-alive','Cookie': 'csrftoken='+Cookies['csrftoken']+'; ig_did='+Cookies['ig_did']+'; ig_nrcb='+Cookies['ig_nrcb']+'; mid='+Cookies['mid'],'X-CSRFToken': Cookies['csrftoken']},data='email_or_username='+eml+'&recaptcha_challenge_field=&flow=&app_id=&source_account_id=').text
			if '"status":"ok"' in send:
				INS = f'{grn}-[5] linked on instagram.com ☑️'
			if ('checkpoint_required')in send:
				INS = f'{grn}-[5] linked on instagram.com ☑️'
			elif ('"No users found"') in send:
				INS = f'{red}-[5] Not linked on instagram.com ✖️'
			else:
				INS = f'{yel}-[5] search error [instagram.com]'
			self.Email_SoundCloud(eml,domn,SNP,TWR,TIK,INS,EML)
		except :
			INS = f'{yel}-[5] search error [instagram.com]'
			self.Email_SoundCloud(eml,domn,SNP,TWR,TIK,INS,EML)
			
	def Email_TikTok(self,eml,domn,SNP,TWR,EML):
		try:
			send =post('https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/?residence=AE&device_id=9488371953858433865&os_version=7.2.0&app_id=1233&iid=6951746276598204161&app_name=musical_ly&pass-route=1&vendor_id=EF3C1478-2AFC-4B8E-8030-C608120AECF9&locale=ar&pass-region=1&ac=WIFI&sys_region=US&ssmix=a&version_code=17.2.0&vid=EF3C1478-2AFC-4B8E-8030-C608120AECF9&channel=App%20Store&op_region=AE&os_api=27&idfa=00000000-0000-0000-0000-000000000000&install_id=6951746276598204161&idfv=EF3C1478-2AFC-4B8E-8030-C608120AECF9&device_platform=iphone&device_type=Pixel&openudid=3ce553bec09070081e5a698d3a14a988f3642ac4&account_region=&tz_name=Asia&tz_offset=12936&app_language=ar&carrier_region=AE&current_region=AE&aid=1233&mcc_mnc=42402&screen_width=1242&uoo=1&content_language=&language=ar&cdid=FBF67CFE-39E1-4556-A3EB-624A20A434E1&build_number=172025&app_version=7.2.0&resolution=2883',headers={'Host': 'api16-normal-c-alisg.tiktokv.com','Connection': 'close','Content-Length': '76','x-Tt-Token': '9ABBszZbHK-ybQ4EmUNmO88d','Content-Type': 'application/x-www-form-urlencoded','x-tt-passport-csrf-token': 'f04fc476081a3d063b607f520e64780c','sdk-version': '2','passport-sdk-version': '7.2.0'},data={'email': eml,'account_sdk_source': 'app','mix_mode': '1','type': '31'})
			
			if '"message":"success"' in send.text:
				TIK = f'{grn}-[4] linked on tiktok.com ☑️'
			elif 'description":"غير مسجل بعد"'in send.text:
				TIK = f'{red}-[4] Not linked on tiktok.com ✖️'
			else:
				TIK = f'{yel}-[4] search error [tiktok.com]'
			self.Email_Instagram(eml,domn,SNP,TWR,TIK,EML)
		except:
			TIK = f'{yel}-[4] search error [tiktok.com]'
			self.Email_Instagram(eml,domn,SNP,TWR,TIK,EML)
	def Email_Twitter(self,eml,domn,SNP,EML):
		try:
			go = get("https://twitter.com/users/email_available?email="+eml,headers={
			'Host': 'twitter.com','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36','Cookie': 'personalization_id="v1_6TNKT0FSMkPP7CfzL5Rkfg=="; guest_id=v1%3A159789135703778252; _ga=GA1.2.490437195.1597891367'}).text
			if '"taken":true'in go:
				TWR = f'{grn}-[3] linked on twitter.com ☑️'
			elif '"taken":false'in go:
				TWR = f'{red}-[3] Not linked on twitter.com ✖️'
			else:
				TWR = f'{yel}-[3] search error [twitter.com]'
			self.Email_TikTok(eml,domn,SNP,TWR,EML)
		except:
			TWR = f'{yel}-[3] search error [twitter.com]'
			self.Email_TikTok(eml,domn,SNP,TWR,EML)
	def Email_Snapchat(self,eml,domn,EML):
		try:
			Send = post('https://accounts.snapchat.com/accounts/merlin/login',headers={'Host': 'accounts.snapchat.com','Cookie': 'xsrf_token=aDpeseUJS0ysikB9nhdNzA; _ga=GA1.2.113171992.1627308862; _scid=f8244bc8-117d-45aa-b1b0-f24ab31edabc; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; sc_at=v2|H4sIAAAAAAAAAE3GwRGAMAgEwIqY4cIJxG6MSBUp3m/2teq4YEOlrEuIWpIfSxbD36fB2bFBveEjTDM991H9AatYyihAAAAA; _sctr=1|1627257600000; web_client_id=e64bb4c8-1a1f-4de7-970d-d637c2e9a642','User-Agent': 'Mozilla/5.0 (@vv1ck) Gecko/20100101 Firefox/90.0','X-Xsrf-Token': 'aDpeseUJS0ysikB9nhdNzA','Origin': 'https://accounts.snapchat.com','Connection': 'close'},json={"email":eml,"app":"BITMOJI_APP"})
			if 'hasSnapchat' in Send.text:
				SNP = f'{grn}-[2] linked on snapchat.com ☑️'
			elif Send.status_code == 204:
				SNP = f'{red}-[2] Not linked on snapchat.com ✖️'
			else:
				SNP = f'{yel}-[2] search error [snapchat.com]'
			self.Email_Twitter(eml,domn,SNP,EML)
		except:
			SNP = f'{yel}-[2] search error [snapchat.com]'
			self.Email_Twitter(eml,domn,SNP,EML)
	def Check_All_Email(self,eml,domn):
		try:
			send = get('https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress='+eml+'&_=1604288577990',headers={'Host': 'odc.officeapps.live.com','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'ar','Connection': 'keep-alive','User-Agent': User_Agent()})
			if 'MSAccount' in send.text:
				EML = f'{grn}-[1] linked on {domn} ☑️'
			elif 'Neither' in send.text:
				EML = f'{red}-[1] Not linked on {domn} ✖️'
			elif ('MSAccountNonEmail')in send.text:
				EML = f'{red}-[1] Not email: {eml} ✖️'
			else:
				EML = f'{yel}-[1] search error [{domn}]'
			self.Email_Snapchat(eml,domn,EML)
		except:
			EML = f'{yel}-[1] search error [{domn}]'
			self.Email_Snapchat(eml,domn,EML)
	def START_Check(self):
		eml = input('[+] Enter Email : ')
		if "@"in eml:
			domn = eml.split('@')[1]
			telegram_vv1ck("\n ======= It's started, wait a bit =======\n")
			self.Check_All_Email(eml,domn)
			
			#th1=Thread(target=)
			#th1.start()
			#theards.append(th1)
		else:exit('[-] Please enter an email ..')
def Info_Ip_address():
	ips=input('[$] Enter Ip address: ')
	try:
		sent = get(f'https://get.geojs.io/v1/ip/geo/{ips}.json')
		info="[$] timezone : {}\n[$] country : {}\n[$] city : {}\n[$] asn : {}\n[$] longitude : {}\n[$] latitude : {}\n[$] organization : {}".format(sent.json()['timezone'],sent.json()['country'],sent.json()['city'],sent.json()['asn'],sent.json()['longitude'],sent.json()['latitude'],sent.json()['organization'])
		telegram_vv1ck(info)
		Go_Back()
	except json.decoder.JSONDecodeError:
		print('[-] The ip address is invalid !!')
		Go_Back()
def Settings():
	global FILZA
	if FILZA in LINX:
		modes=input(f"""\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
			Title: Homepage
{grn}Tools :
{bloFT}- 0 - User information collection tools{wit}
{yel}- 1 - WebSite information gathering tools{wit}
{red}- 2 - Exit ..{wit}
[$] Enter : """)
		if modes == '0':
			m0des = input(f"""\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
		Title: User information
{grn}Choose your tool :
{yel}- 1 - Search for email on websites[15]
- 2 - Find phone number information[5]
- 3 - Search for Username on websites[28]
- 4 - extract ip address information
{bloFT}- 5 - Go Back <<{wit}
[$] Enter : """)
			if m0des == '1':print('\n\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');search_email()
			elif m0des == '2':print('\n\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');search_Numbers()
			elif m0des == '3':print('\n\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');search_Username()
			elif m0des=='4':print('\n\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');Info_Ip_address()
			else:telegram_vv1ck('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');return Settings()
		elif modes == '1':
			modng=input(f"""\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
		Title: website information
{grn}Choose your tool :
{yel}- 1 - Some information about the WebSite
- 2 - extract the subdomains
- 3 - Extract links from the WebSite
- 4 - Check the open ports on the WebSite
{bloFT}- 5 - Go Back <<{wit}
[$] Enter : """)
			if modng == '5':telegram_vv1ck('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');return Settings()
			else:print('\n\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');WEB_Scanner(modng)
		else:exit()
	else:
		modes=input("""\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
			Title: Homepage
Tools :
- 0 - User information collection tools
- 1 - WebSite information gathering tools
- 2 - Exit ..
[$] Enter : """)
		if modes == '0':
			m0des = input("""\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
		Title: User information
Choose your tool :
- 1 - Search for email on websites[15]
- 2 - Find phone number information[5]
- 3 - Search for Username on websites[28]
- 4 - extract ip address information
- 5 - Go Back <<
[$] Enter : """)
			if m0des == '1':print('\n\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');search_email()
			elif m0des == '2':print('\n\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');search_Numbers()
			elif m0des == '3':print('\n\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');search_Username()
			elif m0des=='4':print('\n\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');Info_Ip_address()
			else:telegram_vv1ck('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');return Settings()
		elif modes == '1':
			modng=input("""\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
		Title: website information
Choose your tool :
- 1 - Some information about the WebSite
- 2 - extract the subdomains
- 3 - Extract links from the WebSite
- 4 - Check the open ports on the WebSite
- 5 - Go Back <<
[$] Enter : """)
			if modng == '5':telegram_vv1ck('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');return Settings()
			else:print('\n\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');WEB_Scanner(modng)
		else:exit()
if __name__ == '__main__':
	global FILZA
	FILZA=input("""
1/k) [ Kali linux / Windows ]
2/p) [ iphon / android ]""")
	if FILZA in LINX:
		telegram_vv1ck(f"""{red}
		 ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
		 ───█▒▒░░░░░░░░░▒▒█───
		 ────█░░█░░░░░█░░█────
		 ─▄▄──█░░░▀█▀░░░█──▄▄─
		 █░░█─▀▄░░░░░░░▄▀─█░░█
		 █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
	██████████████████████████████████████████████
	█▄─▄▄─█▄─▄─▀█▄─▄█▀▀▀▀▀██▄─▄███─▄▄─█─▄▄─██─█─▄█
	██─▄████─▄─▀██─██████████─██▀█─██─█─██─██─▄▀██
	▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀█▄▀▄▄▀
            
			{yel}By Mr.Joker @221298
		webSite: https://vv1ck.github.io{wit}

""")
		Settings()
	elif FILZA in PHON:
		telegram_vv1ck("""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n

____________ _____    _             _    
|  ___| ___ \_   _|  | |           | |   
| |_  | |_/ / | |____| | ___   ___ | | __
|  _| | ___ \ | |____| |/ _ \ / _ \| |/ /
| |   | |_/ /_| |_   | | (_) | (_) |   < 
\_|   \____/ \___/   |_|\___/ \___/|_|\_\\

            By Mr.JOKER @221289
          https://vv1ck.github.io
""")
		Settings()
