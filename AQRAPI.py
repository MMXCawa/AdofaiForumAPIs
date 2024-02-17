import requests
def get(id):
    '''
    它是一个字典，你可以使用'href',(下载链接(直链))
                          'imgSrc_lv',(质量(图片))
                          'imgSrc_df',(难度(图片))
                          'artist',(曲师)
                          'song',(歌曲)
                          'level',(质量)
                          'difficulties',(难度)
                          'vluation',(评估)
                          'vluation_color',(评估颜色)
                          'video_herf',(视频)
                          来访问
    '''
    global aqr,info
    aqr=requests.get('https://www.adofaiaqr.top/static/buttonsData.js').text[18:-3]
    return eval(aqr)[id-1]