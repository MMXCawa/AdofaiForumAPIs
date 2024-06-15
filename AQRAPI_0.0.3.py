import http.client,requests as r
VERSION='0.0.3'
def score_abandoned() -> dict:
    '''
    返回一个字典 有'data'(数据),'error'(错误),'status'(状态)键.
    其中'data'包含'logs'(日志),'result'(结果)键
        'logs'值是一个列表
        列表的每一项都是字典
        包含'filename'(文件名),'timestamp'(时间戳),'unix_time'(unix时间,和time.time()返回值类似,但是精确到毫秒),'level'(等级),'args'(参数)
            其中'args'值是一个包含字符串列表,
            前三个log的args记录脚本启动过程,
            从第四个log开始(下标为3),
            args只包含一个字符串且这个字符串可以转换为字典(用eval函数)
            包含'listid'(列表id),'playerid'(玩家id),'chartid/tuf'(tuf谱面编号,如果是其它论坛谱面则为0),
                'chartid/aqr'(aqr谱面编号,如果是其它论坛谱面则为0),'chartid/gg'(Adofaigg谱面编号,如果是其它论坛谱面则为0),
                'bvid'(bv号),'date'(日期),'speed'(倍速),'judgement'(判定),
                'tooearly'(空敲),'early'(太快),'ep'(稍快),'p'(完美),'lp'(稍慢),'late'(太慢),
                'nerves'(紧张空敲),score(分数),'realscore'(真实分数),'number'(个人调和积分排序),'xacc'(x精准度)
    
    例如print(eval(score()['data']['logs'][6]['args'][0]))
    输出结果(需要等约30s)
    {'listid': '4', 'playerid': '1', 'chartid/tuf': '1018', 'chartid/aqr': '0', 'chartid/gg': '0', 'bvid': 'BV1Xz4y1s7eL',
      'date': '45142.833333333336', 'speed': '1', 'judgment': '严格', 'tooearly': '8', 'early': '9', 'ep': '30', 'p': '3387', 
      'lp': '37', 'late': '23', 'nerves': '-7', 'score': '203', 'realscore': '30', 'number': '18', 'xacc': '0.9894609'}
    '''
    conn = http.client.HTTPSConnection("www.kdocs.cn")

    payload = "{\"Context\":{\"argv\":{},\"sheet_name\":\"name api\",\"range\":\"$B$156\"}}"

    headers = {
        'Content-Type': "application/json",
        'AirScript-Token': "4CZREBwnpHkPm64cw1kTi6"
        }

    conn.request("POST", "/api/v3/ide/file/277479917587/script/V2-PSfnbgpQqs6vF4lIITdSw/sync_task", payload, headers)

    res = conn.getresponse()
    return eval(res.read().decode("utf-8"))

def chart(id:int)->dict:
    '''
    参数id格式和表格一样,如10001
    返回一个字典
    有'id','song'(歌曲),'artist'(曲师),'author'(谱师),'difficulties'(用数字表示的难度,如21.25),'quality'(质量评级),'level'(质量等第),'href'(下载链接),'video_href'(视频链接),
    'video_bv'(bv号),'vluation'(备注),'differ'(更通俗的难度,如21.2+),'newdiffer'(PGU难度)键
    '''
    if id<=10000:
        return None
    c=eval(r.get('https://kdocs.adofaiaqr.top').text)
    for index in c:
       if int(index['id'])==id:
           return index
