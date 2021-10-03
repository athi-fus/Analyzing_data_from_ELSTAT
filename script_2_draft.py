import urllib.request
import urllib.error
import re
import wget

my_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'


#basic loop for getting years and trimesters
for i in range(2011,2015):
    print("\n")

    url = "https://www.statistics.gr/el/statistics/-/publication/STO04/{}-Q4".format(i) #using only the 4th trimester because the file has all the needed data
    print(url) #printing for personal checking

    try:
        headers={}
        headers['User_Agent']= my_UA #using a user agent to guarantee our access to the data
        req=urllib.request.Request(url, headers=headers)
        print(type(req))
        with urllib.request.urlopen(url) as response:
            print(type(response))
            char_set=response.headers.get_content_charset()
            #html=response.read().decode(char_set)       revisit this one
            html=response.read().decode("utf-8")
            #print(html)

    except urllib.error.HTTPError as e: #handling errors
        print("HTTP Error:", e.code)
    except urllib.error.URLError as e:
        print("Failed connecting to the server.")
        print("Cause: ", e.reason)

    #with this regex I'm capturing the urls I'm going to use to download the excel files
    li=re.findall('(https://www.statistics.gr:443/el/statistics\?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&amp;p_p_lifecycle=2&amp;p_p_state=normal&amp;p_p_mode=view&amp;p_p_cacheability=cacheLevelPage&amp;p_p_col_id=column-2&amp;p_p_col_count=4&amp;p_p_col_pos=3&amp;_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax\.faces\.resource=document&amp;_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&amp;_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=[0-9]{6}&amp;_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=el)" target="_blank">Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης ' , html)
    print(li)
    print("I'm here")
    for index, item in enumerate(li):
        item=item.replace("amp;", '') #replacing certain parts of the initial url, so that I can download the files
        item=item.replace(":443",'')  #figured out the strings I wanted to replace by comparing the url in the html file and the url I would get if I tried downloading the file by hand
        wget.download(item,'C:/Users/athin/OneDrive/Documents/CeiD/excells3/{}_tri4_f{}.xls'.format(i,index))

        #Have downloaded the excell files
        #name layout: year_trimester_fileNumber.xls
