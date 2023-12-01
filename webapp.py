
from datetime import datetime
from flask import Flask, render_template, request
import re, json
import requests

# regex
numpass1 = '^\+?[1-9][0-9]{7,14}:.*$'
up= '^.*:.*$'
time = '^[0-9][0-9]:[0-9][0-9]:[0-9][0-9]$'
time2 = '^[0-9]:[0-9][0-9]:[0-9][0-9]$'
maker = '^:[0-9]{7,14}$'

#apis
binAPI1 = "https://lookup.binlist.net/"
infoAPI = 'https://randomuser.me/api'
boreapi = 'http://www.boredapi.com/api/activity/'
genderapi = 'https://api.genderize.io?name='
ageapi = 'https://api.agify.io/?name='
natapi = 'https://api.nationalize.io?name='
dictapi = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
dictapi2 = 'https://wordsapiv1.p.mashape.com/words/'
ipapi = 'http://ipinfo.io/'
jokesApi1 = 'https://official-joke-api.appspot.com/'
catapi = 'https://catfact.ninja/fact'
ninjaApi = 'https://api.api-ninjas.com/v1/'
numapi = 'http://numbersapi.com/'
#api-key

token_ip = "a993442a0f3922"
ninjakey = '9CFsOYH9VcBCKu1QpLue9w==y2N1CwwvEpmadf7A'


#format
blank_bininfo ={"number":{"length":'--',"luhn":'--'},"scheme":"--","type":"--","brand":"--","prepaid":'--',"country":{"numeric":"--","alpha2":"--","name":"--","emoji":"--","currency":"--","latitude":'--',"longitude":'--'},"bank":{"name":"--","url":"--","phone":"--"}}

#===================================================================================================================================================

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def homepage():
    return render_template('homepage.html')
    

@app.route('/numpass-extractor', methods = ['POST', 'GET'])
def numpass():

    if request.method == 'POST':
        combo = request.form['combo']
        combo_list = combo.split('\n')
        combo_extracted = []
        for i in combo_list:
            # while i != '':

            ab = re.search(numpass1, i)
            # bc = re.search(maker, i)

            if ab:
                line_lst = i.split()
                for j in line_lst:
                    if re.match(numpass1,j):
                        combo_extracted.append(j)
            
            le = len(combo_extracted)

            # elif bc:
            #     line_lst = i.split()
            #     for j in line_lst:
            #         if re.match(maker,j):
            #             # passtonum = j.split(':')
            #             # comb_num = str(passtonum[1])+':'+str(passtonum[1])
            #             combo_extracted.append(j)
                

    
        return render_template('numpass.html', lines = combo_extracted, lengthoflist = le)
    else:
        return render_template('scrapper.html', mytitle='NUMPASS EXTARCT')

@app.route('/mailpass-extractor', methods = ['POST', 'GET'])
def mailpass():
    if request.method == 'POST':
        combo = request.form['combo']
        combo_list = combo.split('\n')
        combo_extracted = []
        for line in combo_list:
            if re.search(up, line):
                line_lst = line.split()
                for i in line_lst:
                    y = re.match(up,i)
                    if y:
                        colon = i.split(':')
                        if colon[1] != '':
                            z = re.match(time,i)
                            x = re.match(time2,i)
                            if x or z:
                                pass
                            else:
                                combo_extracted.append(i)
        
        le = len(combo_extracted)
        
        return render_template('numpass.html', lines = combo_extracted,  lengthoflist = le)
    else:
        return render_template('scrapper.html', mytitle='User/Mail-Pass EXTARCT')



@app.route('/bin-lookup', methods = ['POST', 'GET'])
def binlookup():
    if request.method == 'POST':
        bintc= request.form['bin_input']
        if len(bintc)<6:
            return render_template('binoutput.html',ERRORS="BIN SHOULD BE 6 DIGIT OR MORE", info= blank_bininfo)
        elif len(bintc)<6:
            bintc = bintc[:6]
        resp = requests.get(binAPI1+bintc)
        if resp.status_code == 200:
            resp_json = resp.json()
            r = json.dumps(resp_json)
            info = json.loads(r)
            return render_template('binoutput.html',info = info, ERRORS="BIN SEARCHED: {}".format(bintc))
        elif resp.status_code == 404:
            return render_template('binoutput.html',ERRORS="BIN DOES NOT EXIST", info= blank_bininfo)
        
    else:
        return render_template('binlookup.html')

@app.route('/infogen', methods = ['POST', 'GET'])
def infogen():
    if request.method == 'POST':
        if request.form['country'] == 'US':
            calling = requests.get(infoAPI+'?nat=us')
        elif request.form['country'] == 'UA':
            calling = requests.get(infoAPI+'?nat=ua')
        elif request.form['country'] == 'TR':
            calling = requests.get(infoAPI+'?nat=tr')
        elif request.form['country'] == 'RS':
            calling = requests.get(infoAPI+'?nat=rs')
        elif request.form['country'] == 'NZ':
            calling = requests.get(infoAPI+'?nat=nz')
        elif request.form['country'] == 'NO':
            calling = requests.get(infoAPI+'?nat=no')
        
        usj = calling.json()
        j = json.dumps(usj)
        json_resp = json.loads(j)
        try:
            usj = calling.json()
            j = json.dumps(usj)
            json_resp = json.loads(j)
            return render_template('randomoutput.html',info= json_resp)
        except:
            return render_template('randomoutput.html',)
            
    
    else:
        return render_template('randomgen.html')

@app.route('/activity-suggestor', methods = ['POST', 'GET'])
def suggestor():
    if request.method == 'POST':
        ERRORS = 0
        
        if request.form['identifier'] == 'random':
            
            result = requests.get(boreapi)

        elif request.form['identifier'] == 'activity':
            params = request.form['type']
            
            result = requests.get(boreapi+'?type='+params)
        elif request.form['identifier'] == 'participants':
            params = request.form['participants']
            
            result = requests.get(boreapi+'?participants='+params)
        elif request.form['identifier'] == 'price':
            params = request.form['price']
            if int(params) <= 100:
                params = int(params)/100
                result = requests.get(boreapi+'?price='+str(params))
            else:
                ERRORS += 100
        elif request.form['identifier'] == 'accessibility':
            params = request.form['accessibility']
            if int(params) <= 100:
                params = int(params)/100
                result = requests.get(boreapi+'?accessibility='+str(params))
            else:
                ERRORS += 100

        ERRORS +=1
        if ERRORS == 101:
            ERRORS = 'ENTER VALUE BETWEEN 0 AND 100'
            return render_template('boredoutput.html', ERRORS = ERRORS)

        else:
            resp = result.json()
            temp = json.dumps(resp)
            resp_json = json.loads(temp)

        
            return render_template('boredoutput.html', resp = resp_json)
        


    else:
        return render_template('bored.html')








@app.route('/nameinfo', methods = ['POST', 'GET'])
def nameinfo():
    if request.method == 'POST':
        if request.form['name'] == '':
            ERRORS = 'Enter a Name'
            return render_template('genderoutput.html', ERRORS = ERRORS)
        else:
            name = request.form['name']
            age = (requests.get(ageapi+name)).json()
            t = json.dumps(age)
            age_json = json.loads(t)

            gender = (requests.get(genderapi+name)).json()
            t = json.dumps(gender)
            gender_json = json.loads(t)

            nat = (requests.get(natapi+name)).json()
            t = json.dumps(nat)
            nat_json = json.loads(t)
            return render_template('genderoutput.html', age_resp = age_json, gender_resp = gender_json, nat_resp = nat_json, name = name)

    else:
        return render_template('gender.html')


@app.route('/dict', methods = ['POST', 'GET'])
def dict():
    if request.method == 'POST':
        if request.form['Word'] == '':
            ERRORS = 'Enter a Word'
            return render_template('dictoutput.html', ERRORS = ERRORS)
        else:
            word = request.form['Word']

            resp = (requests.get(dictapi+word)).json()
            templist =[]

            for firstIter in range(len(resp)):
    
                for secondIter in range(len(resp[firstIter]['meanings'])):
                    

                    for thirdIter in range(len(resp[firstIter]['meanings'][secondIter]['definitions'])):
                        templist.append(resp[firstIter]['meanings'][secondIter]['definitions'][thirdIter]['definition'])
                        

            

            return render_template('dictoutput.html', Data = templist)

    else:
        return render_template('dicthome.html')


# @app.route('/dict2', methods = ['POST', 'GET'])
# def dict2():
#     if request.method == 'POST':
#         if request.form['Word'] == '':
#             ERRORS = 'Enter a Word'
#             return render_template('dictoutput.html', ERRORS = ERRORS)
#         else:
#             word = request.form['Word']

#             resp = (requests.get(dictapi2+word)).json()

@app.route('/ipaddr', methods = ['POST', 'GET'])
def ipaddr():
    if request.method == 'POST':
        if request.form['ipaddress'] == '':
            ERRORS = 'Enter a Ipaddress'
            return render_template('dictoutput.html', ERRORS = ERRORS)
        else:
            ipaddress = request.form['ipaddress']
            url = ipapi+ipaddress+'?token='+token_ip
            resp = requests.get(url).json()
            return render_template('ipaddressoutput.html', Data = resp)

    else:
        return render_template('ipaddresshome.html')

@app.route('/jokes', methods = ['POST', 'GET'])
def jokes():
    if request.method == 'POST':
        if request.form['type'] == 'Random Joke':
            calling = requests.get(jokesApi1 +'/random_joke').json()
            return render_template('jokesoutput.html', Data = calling)

    else:
        return render_template('jokes.html')


@app.route('/cats', methods = ['POST', 'GET'])
def cats():
    if request.method == 'POST':
        if request.form['type'] == 'Random Fact':
            calling = requests.get(catapi).json()
            return render_template('catfactsoutput.html', Data = calling)

    else:
        return render_template('catfacts.html')

@app.route('/quotes', methods = ['POST', 'GET'])
def quotes():
    if request.method == 'POST':
        category = request.form['Type']
        url=ninjaApi+'quotes?category='+category
        
        calling = requests.get(url, headers={'X-Api-Key': ninjakey}).json()
        return render_template('quotesoutput.html', Data=calling)
    else:
        return render_template("quotes.html")

@app.route('/trivia', methods = ['POST', 'GET'])
def trivia():
    if request.method == 'POST':
        category = request.form['category']
        url=ninjaApi+'trivia?category='+category
        calling = requests.get(url, headers={'X-Api-Key': ninjakey}).json()

        return render_template('triviaoutput.html', Data=calling)
    else:
        return render_template("trivia.html")

@app.route('/synant', methods = ['POST', 'GET'])
def synant():
    if request.method == 'POST':
        word = request.form['word']
        url=ninjaApi+'thesaurus?word='+word
        calling = requests.get(url, headers={'X-Api-Key': ninjakey}).json()

        return render_template('synantoutput.html', Synonyms=calling['synonyms'], Antonyms=calling['antonyms'], Word=calling['word'])
    else:
        return render_template("synant.html")

@app.route('/riddles', methods = ['POST', 'GET'])
def riddles():
    if request.method == 'POST':
        
        url=ninjaApi+'riddles'
        calling = requests.get(url, headers={'X-Api-Key': ninjakey}).json()

        return render_template('riddlesoutput.html', Data=calling)
    else:
        return render_template("riddles.html")


@app.route('/worldtime', methods=['GET', 'POST'])
def worldtime():
    if request.method == 'POST':
        
        if request.form['identifier'] == 'lat-long':
            params = 'worldtime?lat={}&lon={}'.format(request.form['lat'],request.form['long'])
            calling = requests.get(ninjaApi+params, headers={'X-Api-Key': ninjakey}).json()
            return render_template('worldtimeoutput.html', Data=calling)

        elif request.form['identifier'] == 'city':
            params = 'worldtime?city={}&state={}&country={}'.format(request.form['city'],request.form['state'],request.form['count'])
            calling = requests.get(ninjaApi+params, headers={'X-Api-Key': ninjakey}).json()
            return render_template('worldtimeoutput.html', Data=calling)

        elif request.form['identifier'] == 'zone':
            params = 'worldtime?timezone ={}'.format(request.form['zone'])
            calling = requests.get(ninjaApi+params, headers={'X-Api-Key': ninjakey}).json()
            return render_template('worldtimeoutput.html', Data=calling)
    else:
        return render_template("worldtime.html")


@app.route('/whois', methods=['GET', 'POST'])
def whois():
    if request.method == 'POST':
        url = ninjaApi+'whois'
        calling = requests.get(url, headers= {'X-Api-Key':ninjakey}).json()
        cDate = datetime.utcfromtimestamp(calling['creation_date']).strftime('%Y-%m-%d')
        eDate = datetime.utcfromtimestamp(calling['expiration_date']).strftime('%Y-%m-%d')
        uDate = datetime.utcfromtimestamp(calling['updated_date']).strftime('%Y-%m-%d')
        return render_template('whoisoutput.html', Data=calling, cDate= cDate, eDate= eDate, uDate= uDate)
    else:
        return render_template('whois.html')


# @app.route('/numbers', methods=['GET', 'POST'])
# def numbers():
#     if request.method == 'POST':
#         to_send = 0
#         entered = 0


#         if request.form['identifier'] == 'number':
#             Num = request.form['number']
#             adder = '{}/math'.format(Num)
#             to_send +=Num
#             entered += 1


#         elif request.form['identifier'] == 'date':
#             d = request.form['date']
#             m = request.form['month']
#             to_send = (str(d)+'/'+str(m))
#             entered += 2


#         elif request.form['identifier'] == 'trivia':
#             Num = request.form['number']
#             adder = '{}'.format(Num)
#             to_send += Num
#             entered += 1

#         try:
#             calling = requests.get(numapi+adder).text
#         except:
#             return "Some error Occured"
        
#         if entered == 1:
#             return render_template("numberoutput.html", data = calling, entered = 'Number', cred =)
#         elif entered == 2:
#             return render_template("numberoutput.html", data = calling, entered = 'Date', cred = )
    
    
    
    # else:
    #     return render_template("number.html")
        
if __name__ == '__main__':
    app.run(port=5000, debug=True)