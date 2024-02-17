import requests
# adofai.gg/api/v1/levels/{id}
def get(id):
    '''
    它是一个字典，你可以使用'id',
                          'title',(标题)
                          'difficulty',(难度)
                          'tiles',(物量)
                          'comments',(评论)
                          'likes',(赞赏)
                          'epilepsyWarning',(光敏性癫痫警告)
                          'censored',(审查)
                          'description',(描述)
                          'video',(视频)
                          'download',(下载链接)
                          'workshop',(工坊链接)
                          'name',(名称)
                          'music',(音乐,含有id,name,minbpm,maxbpm4个子项)
                          'artists',(曲师,可能有多个,以列表储存,每个含有含有id,name2个子项)
                          'creators',(谱师,可能有多个,以列表储存,每个含有含有id,name2个子项)
                          'tags'(标签,可能有多个,以列表储存,每个含有含有id,name2个子项)
                          来访问
    '''
    global response,info
    response=requests.get(f"https://adofai.gg/api/v1/levels/{id}")
    info=response.json()
    return info

