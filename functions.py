import redis 

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def count(id):
    res = r.get(id)
    if(res is None): 
        res = 0 
    res = str(int(res)+2) #hozirgi va bot javob beradigan habar
    r.set(id,res)
    return res 

def add_message(txt1): 
    cnt = r.get('all_count')
    if(cnt is None):
        cnt = 1
    cnt = int(cnt)+1 #hozirgi habar 
    r.set('all_count', cnt)

    txt = r.get('all')  
    if(txt is None): 
        txt = ""
    res = txt + "??" + txt1
    r.set('all', res)
    return cnt
