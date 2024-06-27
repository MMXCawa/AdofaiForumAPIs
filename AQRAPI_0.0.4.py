import http.client,requests as r
VERSION='0.0.4'
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
class charts():
    all=eval(r.get('https://kdocs.adofaiaqr.top').text)
    levellist=[-21,21.3,21.25,21.2,21.15,21.1,21.05,21,20.95,20.9,20.85,20.8,20.75,20.7,20.65,20.6,20.55,20.5,20.45,20.4,20.35,20.3,20.25,20.2,20.15,20.1,20.05,20,19,5,19,18.5,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,-2]
    def find(given=None,mode:str='id')->dict:
        '''
        帮助文档
        此函数将帮你找到AQR论坛对应的谱面信息
        该函数有 given=None,mode:str='id' 两个参数
        given参数是搜索的内容
            如果搜索模式为'id'
            请输入大于10000的整数
            如果为其他
            请输入一个字符串
        支持搜索的模式有
        'id','song'(歌曲),'artist'(曲师),'author'(谱师),'difficulties'(用数字表示的难度,如21.25),'quality'(质量评级),'level'(质量等第),
        'video_bv'(bv号),'differ'(更通俗的难度,如21.2+),'newdiffer'(PGU难度)

        若模式为id,则返回一个字典
        有'id','song'(歌曲),'artist'(曲师),'author'(谱师),'difficulties'(用数字表示的难度,如21.25),'quality'(质量评级),'level'(质量等第),'href'(下载链接),'video_href'(视频链接),
        'video_bv'(bv号),'vluation'(备注),'differ'(更通俗的难度,如21.2+),'newdiffer'(PGU难度)键,自行读取信息.
        若模式为其他
        则返回一个列表
        每一项都是一个含有上述键的字典,自行读取信息.
        '''
        if given==None:
            print(charts.find.__doc__)
        elif mode=='id':
            if given<=10000:
                return None
            for index in charts.all:
                if int(index['id'])==given:
                    return index
        elif mode in ('artist','author','song'):
            lis=[]
            if type(given)!=str:
                return None
            else:
                for index in charts.all:
                    if given in(index[mode]):
                        lis.append(index)
                return lis if len(lis)>=1 else None
        elif mode in ('difficulties','differ','newdiffer','video_bv','quality','level'):
            lis=[]
            if type(given)!=str:
                return None
            else:
                for index in charts.all:
                    if given==(index[mode]):
                        lis.append(index)
                return lis
        else:
            return None
    def level_filter(mode='upper',difficulty:float=114514):
        '''
        difficulty定义参见find函数中的difficulties
        有三个模式 upper lower 和single'''
        if difficulty==-21:
            difficulty=114514
        if difficulty in charts.levellist:
            lis=[]
            if mode=='single':
                return charts.find(difficulty,'difficulties')
            index=charts.levellist.index(difficulty)
            if mode=='upper':
                while index!=-1:
                    lis+=charts.find(str(charts.levellist[index]),'difficulties')
                    index-=1
            if mode=='lower':
                while charts.levellist[index]!=-2:
                    lis+=charts.find(str(charts.levellist[index]),'difficulties')
                    index+=1
            return lis
        else:
            return None
    def popularization(a:dict):
        return '谱面:'+a['artist']+' - '+a['song']+'(made by '+a['author']+'(id:'+a['id']+')\n难度:'+a['differ']+' 质量:'+a['quality']+'\n视频链接:'+a['video_herf']+'\n下载链接:'+a['href']+'\n'
__DEBUG__=1
if __name__=='__main__':
    print('\n'.join([charts.popularization(i) for i in charts.level_filter('lower',difficulty=8)]))
