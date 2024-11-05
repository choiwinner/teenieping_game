# 티니핑 카드 게임
# streamlit run teenieping_game.py
# https://adventure.streamlit.app/ 참고하기
# db source : https://m.blog.naver.com/cecil122222/223355906005
import pandas as pd
import numpy as np
import random
import streamlit as st
from PIL import Image 
import time
#import stagen

@st.cache_data()
def random_make(len_df):
    
    list_l = []

    for i in range(0,len_df):
        list_l.append(i)

    random.shuffle(list_l)

    answer_list = list_l[0:10]
    wrong_list = list_l[10:40]

    return answer_list, wrong_list

@st.cache_data()
def random_make2(listx):

    random.shuffle(listx)

    return listx

@st.cache_data()
def random_make3(answer_list,wrong_list):

    result = []

    quiz_wrong = np.array_split(wrong_list, 10)

    #map 함수 사용하기 : list(map(함수,list))

    quiz_wrong_n = list(map(list,quiz_wrong))

    for i in range(len(answer_list)):

        arg1 = answer_list[i]
        arg2_1, arg2_2, arg2_3 = quiz_wrong_n[i]

        new_tuple = (arg1, arg2_1, arg2_2, arg2_3)

        new_list = list(new_tuple)

        random.shuffle(new_list)

        result.append(new_list)

    return result

def Init():

    if "health" not in st.session_state:
        st.session_state["health"] = 0
    if "name" not in st.session_state:
        st.session_state["name"] = '아무개'
    if "stage" not in st.session_state:
        st.session_state["stage"] = 1
    if "start" not in st.session_state:
        st.session_state["start"] = 0
    if "answer_n" not in st.session_state:
        st.session_state["answer_n"] = 0
    if "answer" not in st.session_state:
        st.session_state["answer"] = ''

def quiz_one1(index_n,quiz_list,answer,img_1): 

    input_container = st.empty()

    st.write(f"{index_n}번째 문제입니다.")
    #st.write(answer)

    # 이미지 파일을 불러옵니다.
    #image_a = Image.open(f"image/{img_1}.jpg").resize((200,200))
    image_a = Image.open(f"image/{img_1}.jpg").resize((266,370))
    # 이미지를 표시합니다.
    st.image(image_a)

    #radio 버튼으로 문제내기
    option = st.radio('정답 번호를 선택하세요.', 
                    ("아래에서 선택하세요",quiz_list[0], quiz_list[1] , quiz_list[2] , quiz_list[3]),
                    index=0
                    )
    if (option == '아래에서 선택하세요'):
        st.empty()

    else:
        if option == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            st.audio("audio/child-says-yes-113117.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.audio("audio/no-no-no-242246.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()

    #text로 문제내기
    #for index,i in enumerate(quiz_list):
    #    st.write(f'{index+1}. {i}')

    #if val1 := int(st.number_input('정답 번호를 입력하세요.',key='key1')):

    #    if quiz_list[val1-1] == answer:
    #        st.info('정답입니다.')
    #        st.session_state["stage"] = st.session_state["stage"]+1
    #        st.session_state["health"] = st.session_state["health"]+10
    #        time.sleep(2)
    #        st.rerun()
    #    else:
    #        st.warning('오답입니다.')
    #        st.session_state["stage"] = st.session_state["stage"]+1
    #        time.sleep(2)
    #        st.rerun()
    

def quiz_one2(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    #st.write(answer)

    # 이미지 파일을 불러옵니다.
    #image_a = Image.open(f"image/{img_1}.jpg").resize((150,150))
    image_a = Image.open(f"image/{img_1}.jpg").resize((266,370))
    # 이미지를 표시합니다.
    st.image(image_a)

    #radio 버튼으로 문제내기
    option = st.radio('정답 번호를 선택하세요.', 
                    ("아래에서 선택하세요",quiz_list[0], quiz_list[1] , quiz_list[2] , quiz_list[3]),
                    index=0
                    )
    if (option == '아래에서 선택하세요'):
        st.empty()

    else:
        if option == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            st.audio("audio/child-says-yes-113117.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.audio("audio/no-no-no-242246.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()

    #text로 문제내기
    #for index,i in enumerate(quiz_list):
    #    st.write(f'{index+1}. {i}')
#
    #if val2 := int(st.number_input('정답 번호를 입력하세요.',key='key2')):
#
    #    if quiz_list[val2-1] == answer:
    #        st.info('정답입니다.')
    #        st.session_state["stage"] = st.session_state["stage"]+1
    #        st.session_state["health"] = st.session_state["health"]+10
    #        time.sleep(2)
    #        st.rerun()
    #    else:
    #        st.warning('오답입니다.')
    #        st.session_state["stage"] = st.session_state["stage"]+1
    #        time.sleep(2)
    #        st.rerun()

def quiz_one3(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    #st.write(answer)

    # 이미지 파일을 불러옵니다.
    #image_a = Image.open(f"image/{img_1}.jpg").resize((150,150))
    image_a = Image.open(f"image/{img_1}.jpg").resize((266,370))
    # 이미지를 표시합니다.
    st.image(image_a)

    #radio 버튼으로 문제내기
    option = st.radio('정답 번호를 선택하세요.', 
                    ("아래에서 선택하세요",quiz_list[0], quiz_list[1] , quiz_list[2] , quiz_list[3]),
                    index=0
                    )
    if (option == '아래에서 선택하세요'):
        st.empty()

    else:
        if option == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            st.audio("audio/child-says-yes-113117.mp3", format="audio/mpeg", loop=False,autoplay=True)            
            time.sleep(3)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.audio("audio/no-no-no-242246.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()

    #text로 문제내기
   
    #for index,i in enumerate(quiz_list):
    #    st.write(f'{index+1}. {i}')
#
    #if val3 := int(st.number_input('정답 번호를 입력하세요.',key='key3')):
#
    #    if quiz_list[val3-1] == answer:
    #        st.info('정답입니다.')
    #        st.session_state["stage"] = st.session_state["stage"]+1
    #        st.session_state["health"] = st.session_state["health"]+10
    #        time.sleep(2)
    #        st.rerun()
    #    else:
    #        st.warning('오답입니다.')
    #        st.session_state["stage"] = st.session_state["stage"]+1
    #        time.sleep(2)
    #        st.rerun()

def quiz_one4(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    #st.write(answer)

    # 이미지 파일을 불러옵니다.
    #image_a = Image.open(f"image/{img_1}.jpg").resize((150,150))
    image_a = Image.open(f"image/{img_1}.jpg").resize((266,370))
    # 이미지를 표시합니다.
    st.image(image_a)

    #radio 버튼으로 문제내기
    option = st.radio('정답 번호를 선택하세요.', 
                    ("아래에서 선택하세요",quiz_list[0], quiz_list[1] , quiz_list[2] , quiz_list[3]),
                    index=0
                    )
    if (option == '아래에서 선택하세요'):
        st.empty()

    else:
        if option == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            st.audio("audio/child-says-yes-113117.mp3", format="audio/mpeg", loop=False,autoplay=True)      
            time.sleep(3)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.audio("audio/no-no-no-242246.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()

    #text로 문제내기    


#    for index,i in enumerate(quiz_list):
#        st.write(f'{index+1}. {i}')
#
#    if val4 := int(st.number_input('정답 번호를 입력하세요.',key='key4')):
#
#        if quiz_list[val4-1] == answer:
#            st.info('정답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            st.session_state["health"] = st.session_state["health"]+10
#            time.sleep(2)
#            st.rerun()
#        else:
#            st.warning('오답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            time.sleep(2)
#            st.rerun()

def quiz_one5(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    #st.write(answer)

    # 이미지 파일을 불러옵니다.
    #image_a = Image.open(f"image/{img_1}.jpg").resize((150,150))
    image_a = Image.open(f"image/{img_1}.jpg").resize((266,370))
    # 이미지를 표시합니다.
    st.image(image_a)

    #radio 버튼으로 문제내기
    option = st.radio('정답 번호를 선택하세요.', 
                    ("아래에서 선택하세요",quiz_list[0], quiz_list[1] , quiz_list[2] , quiz_list[3]),
                    index=0
                    )
    if (option == '아래에서 선택하세요'):
        st.empty()

    else:
        if option == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            st.audio("audio/child-says-yes-113117.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.audio("audio/no-no-no-242246.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()

    #text로 문제내기

#    for index,i in enumerate(quiz_list):
#        st.write(f'{index+1}. {i}')
#
#    if val5 := int(st.number_input('정답 번호를 입력하세요.',key='key5')):
#
#        if quiz_list[val5-1] == answer:
#            st.info('정답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            st.session_state["health"] = st.session_state["health"]+10
#            time.sleep(2)
#            st.rerun()
#        else:
#            st.warning('오답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            time.sleep(2)
#            st.rerun()

def quiz_one6(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    #st.write(answer)

    # 이미지 파일을 불러옵니다.
    #image_a = Image.open(f"image/{img_1}.jpg").resize((150,150))
    image_a = Image.open(f"image/{img_1}.jpg").resize((266,370))
    # 이미지를 표시합니다.
    st.image(image_a)

    #radio 버튼으로 문제내기
    option = st.radio('정답 번호를 선택하세요.', 
                    ("아래에서 선택하세요",quiz_list[0], quiz_list[1] , quiz_list[2] , quiz_list[3]),
                    index=0
                    )
    if (option == '아래에서 선택하세요'):
        st.empty()

    else:
        if option == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            st.audio("audio/child-says-yes-113117.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.audio("audio/no-no-no-242246.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()

    #text로 문제내기


#    for index,i in enumerate(quiz_list):
#        st.write(f'{index+1}. {i}')
#
#    if val6 := int(st.number_input('정답 번호를 입력하세요.',key='key6')):
#
#        if quiz_list[val6-1] == answer:
#            st.info('정답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            st.session_state["health"] = st.session_state["health"]+10
#            time.sleep(2)
#            st.rerun()
#        else:
#            st.warning('오답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            time.sleep(2)
#            st.rerun()

def quiz_one7(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    #st.write(answer)

    # 이미지 파일을 불러옵니다.
    #image_a = Image.open(f"image/{img_1}.jpg").resize((150,150))
    image_a = Image.open(f"image/{img_1}.jpg").resize((266,370))
    # 이미지를 표시합니다.
    st.image(image_a)       

    #radio 버튼으로 문제내기
    option = st.radio('정답 번호를 선택하세요.', 
                    ("아래에서 선택하세요",quiz_list[0], quiz_list[1] , quiz_list[2] , quiz_list[3]),
                    index=0
                    )
    if (option == '아래에서 선택하세요'):
        st.empty()

    else:
        if option == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            st.audio("audio/child-says-yes-113117.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.audio("audio/no-no-no-242246.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()

    #text로 문제내기

#    for index,i in enumerate(quiz_list):
#        st.write(f'{index+1}. {i}')
#
#    if val7 := int(st.number_input('정답 번호를 입력하세요.',key='key7')):
#
#        if quiz_list[val7-1] == answer:
#            st.info('정답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            st.session_state["health"] = st.session_state["health"]+10
#            time.sleep(2)
#            st.rerun()
#        else:
#            st.warning('오답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            time.sleep(2)
#            st.rerun()

def quiz_one8(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    #st.write(answer)

    # 이미지 파일을 불러옵니다.
    #image_a = Image.open(f"image/{img_1}.jpg").resize((150,150))
    image_a = Image.open(f"image/{img_1}.jpg").resize((266,370))
    # 이미지를 표시합니다.
    st.image(image_a)

    #radio 버튼으로 문제내기
    option = st.radio('정답 번호를 선택하세요.', 
                    ("아래에서 선택하세요",quiz_list[0], quiz_list[1] , quiz_list[2] , quiz_list[3]),
                    index=0
                    )
    if (option == '아래에서 선택하세요'):
        st.empty()

    else:
        if option == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            st.audio("audio/child-says-yes-113117.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.audio("audio/no-no-no-242246.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()

    #text로 문제내기


#    for index,i in enumerate(quiz_list):
#        st.write(f'{index+1}. {i}')
#
#    if val8 := int(st.number_input('정답 번호를 입력하세요.',key='key8')):
#
#        if quiz_list[val8-1] == answer:
#            st.info('정답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            st.session_state["health"] = st.session_state["health"]+10
#            time.sleep(2)
#            st.rerun()
#        else:
#            st.warning('오답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            time.sleep(2)
#            st.rerun()

def quiz_one9(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    #st.write(answer)

    # 이미지 파일을 불러옵니다.
    #image_a = Image.open(f"image/{img_1}.jpg").resize((150,150))
    image_a = Image.open(f"image/{img_1}.jpg").resize((266,370))
    # 이미지를 표시합니다.
    st.image(image_a)

    #radio 버튼으로 문제내기
    option = st.radio('정답 번호를 선택하세요.', 
                    ("아래에서 선택하세요",quiz_list[0], quiz_list[1] , quiz_list[2] , quiz_list[3]),
                    index=0
                    )
    if (option == '아래에서 선택하세요'):
        st.empty()

    else:
        if option == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            st.audio("audio/child-says-yes-113117.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.audio("audio/no-no-no-242246.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()

    #text로 문제내기

#    for index,i in enumerate(quiz_list):
#        st.write(f'{index+1}. {i}')
#
#    if val9 := int(st.number_input('정답 번호를 입력하세요.',key='key9')):
#
#        if quiz_list[val9-1] == answer:
#            st.info('정답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            st.session_state["health"] = st.session_state["health"]+10
#            time.sleep(2)
#            st.rerun()
#        else:
#            st.warning('오답입니다.')
#            st.session_state["stage"] = st.session_state["stage"]+1
#            time.sleep(2)
#            st.rerun()

def quiz_one10(index_n,quiz_list,answer,img_1): 

    st.write(f"{index_n}번째 문제입니다.")
    #st.write(answer)

    # 이미지 파일을 불러옵니다.
    #image_a = Image.open(f"image/{img_1}.jpg").resize((150,150))
    image_a = Image.open(f"image/{img_1}.jpg").resize((266,370))
    # 이미지를 표시합니다.
    st.image(image_a)

    #radio 버튼으로 문제내기
    option = st.radio('정답 번호를 선택하세요.', 
                    ("아래에서 선택하세요",quiz_list[0], quiz_list[1] , quiz_list[2] , quiz_list[3]),
                    index=0
                    )
    if (option == '아래에서 선택하세요'):
        st.empty()

    else:
        if option == answer:
            st.info('정답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.session_state["health"] = st.session_state["health"]+10
            st.audio("audio/child-says-yes-113117.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()
        else:
            st.warning('오답입니다.')
            st.session_state["stage"] = st.session_state["stage"]+1
            st.audio("audio/no-no-no-242246.mp3", format="audio/mpeg", loop=False,autoplay=True)
            time.sleep(3)
            st.rerun()

    #text로 문제내기

#   for index,i in enumerate(quiz_list):
#       st.write(f'{index+1}. {i}')
#
#   if val10 := int(st.number_input('정답 번호를 입력하세요.',key='key10')):
#
#       if quiz_list[val10-1] == answer:
#           st.info('정답입니다.')
#           st.session_state["stage"] = st.session_state["stage"]+1
#           st.session_state["health"] = st.session_state["health"]+10
#           time.sleep(2)
#           st.rerun()
#       else:
#           st.warning('오답입니다.')
#           st.session_state["stage"] = st.session_state["stage"]+1
#           time.sleep(2)
#           st.rerun()

if __name__=='__main__':
    
    # 페이지 기본 설정

    st.set_page_config(
        page_title="티니핑 카드 게임",
        layout="wide",
        page_icon= "image/0.jpg"
    )

    horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; border: 1px solid #635985;'><br>"    # thin divider line

    Init()

    with st.sidebar:
        mystate = st.session_state
        #st.subheader(f"🖼️ Pix Match: {mystate.GameDetails[0]}")
        st.subheader("티니핑 센터")
        st.markdown(horizontal_bar, True)

        name = st.text_input("이름을 입력하세요.")

        st.session_state["name"] = name

        if st.button("시작 하기"):
            st.session_state["start"] = 1
            st.session_state["health"] = 0
            st.session_state["stage"] = 1
            st.cache_data.clear()
            st.cache_resource.clear()
            st.write('시작')

        #if st.button("새게임 하기"):
        #    st.session_state.clear()
        #    st.cache_data.clear()
        #    st.cache_resource.clear()
        #    st.session_state.clear()
            
    st.title(f':blue[_{name}_]님의 :red[티니핑] 카드 게임')

    st.subheader(f":blue[신나는 모험]이 이제 시작됩니다!")

    placeholder = st.empty()

    #df = pd.read_csv('포켓몬이름_final_999.csv',encoding='utf-8')
    df = pd.read_csv('티니핑이름_135개.csv',encoding='utf-8')
    df_115 = df.head(115) ##115개만 그림 Data가 있음
    len_df = len(df_115)

    #start = st.session_state["start"]

    if st.session_state["start"] != 1:
        st.stop()

    else:
        answer_list,wrong_list = random_make(len_df)

        #map 함수 사용하기 : list(map(함수,list))
        answer_list2 =[]
        answer_list2 = list(map(lambda x: df_115["0"][x],answer_list))

        wrong_list2 =[]
        wrong_list2 = list(map(lambda x: df_115["0"][x],wrong_list))

        list_f = random_make3(answer_list2,wrong_list2)

        if st.session_state['stage'] == 1:
            st.audio("audio/하츄핑배경.mp3", format="audio/mpeg", loop=True,autoplay=True)

            placeholder.empty()
            with placeholder.container():
                quiz_one1(st.session_state["stage"],list_f[0],answer_list2[0],answer_list[0])
        elif st.session_state['stage'] == 2:
            st.audio("audio/하츄핑배경.mp3", format="audio/mpeg", loop=True,autoplay=True)
            placeholder.empty()
            with placeholder.container():
                quiz_one2(st.session_state["stage"],list_f[1],answer_list2[1],answer_list[1])
        elif st.session_state['stage'] == 3:
            st.audio("audio/하츄핑배경.mp3", format="audio/mpeg", loop=True,autoplay=True)
            placeholder.empty()
            with placeholder.container():
                quiz_one3(st.session_state["stage"],list_f[2],answer_list2[2],answer_list[2])
        elif st.session_state['stage'] == 4:
            st.audio("audio/하츄핑배경.mp3", format="audio/mpeg", loop=True,autoplay=True)
            placeholder.empty()
            with placeholder.container():
                quiz_one4(st.session_state["stage"],list_f[3],answer_list2[3],answer_list[3])        
        elif st.session_state['stage'] == 5:
            st.audio("audio/하츄핑배경.mp3", format="audio/mpeg", loop=True,autoplay=True)
            placeholder.empty()
            with placeholder.container():
                quiz_one5(st.session_state["stage"],list_f[4],answer_list2[4],answer_list[4])
        elif st.session_state['stage'] == 6:
            st.audio("audio/하츄핑배경.mp3", format="audio/mpeg", loop=True,autoplay=True)
            placeholder.empty()
            with placeholder.container():
                quiz_one6(st.session_state["stage"],list_f[5],answer_list2[5],answer_list[5])
        elif st.session_state['stage'] == 7:
            st.audio("audio/하츄핑배경.mp3", format="audio/mpeg", loop=True,autoplay=True)
            placeholder.empty()
            with placeholder.container():
                quiz_one7(st.session_state["stage"],list_f[6],answer_list2[6],answer_list[6])
        elif st.session_state['stage'] == 8:
            st.audio("audio/하츄핑배경.mp3", format="audio/mpeg", loop=True,autoplay=True)
            placeholder.empty()
            with placeholder.container():
                quiz_one8(st.session_state["stage"],list_f[7],answer_list2[7],answer_list[7])
        elif st.session_state['stage'] == 9:
            st.audio("audio/하츄핑배경.mp3", format="audio/mpeg", loop=True,autoplay=True)
            placeholder.empty()
            with placeholder.container():
                quiz_one9(st.session_state["stage"],list_f[8],answer_list2[8],answer_list[8])
        elif st.session_state['stage'] == 10:
            st.audio("audio/하츄핑배경.mp3", format="audio/mpeg", loop=True,autoplay=True)
            placeholder.empty()
            with placeholder.container():
                quiz_one10(st.session_state["stage"],list_f[9],answer_list2[9],answer_list[9])
        else:
            placeholder.empty()
            with placeholder.container():
                final_score = st.session_state["health"]
                user = st.session_state["name"]
                if final_score >= 90:
                    st.write('')
                    st.title(f':blue[{user}]님 당신은 진정한 :red[티니핑 지식왕!!]')
                    st.title(f'최종 점수는 :red[{final_score}]점 입니다.')

                    # 이미지 파일을 불러옵니다.
                    image_a = Image.open("image/111.jpg").resize((500,500))
                    # 이미지를 표시합니다.
                    st.image(image_a)

                    # 음악을 재생합니다.
                    st.audio("audio/winning-218995.mp3", format="audio/mpeg", loop=False,autoplay=True)
                
                elif final_score >= 70:
                    st.write('')
                    st.title(f':blue[{user}]님 티니핑을 좀 아시는 군요!!')
                    st.title(f'최종 점수는 :red[{final_score}]점 입니다.')
                    
                    # 이미지 파일을 불러옵니다.
                    image_a = Image.open("image/20.jpg").resize((500,500))
                    # 이미지를 표시합니다.
                    st.image(image_a)
                    
                    # 음악을 재생합니다.
                    st.audio("audio/level-win-6416.mp3", format="audio/mpeg", loop=False,autoplay=True)

                elif final_score >= 50:
                    st.write('')
                    st.title(f':blue[{user}]님 티니핑 공부가 필요해요!!')
                    st.title(f'최종 점수는 :red[{final_score}]점 입니다.')
                    
                    # 이미지 파일을 불러옵니다.
                    image_a = Image.open("image/16.jpg").resize((500,500))
                    # 이미지를 표시합니다.
                    st.image(image_a)

                    # 음악을 재생합니다.
                    st.audio("audio/negative_beeps-6008.mp3", format="audio/mpeg", loop=False,autoplay=True)

                elif final_score >= 30:
                    st.write('')
                    st.title(f':blue[{user}]님 티니핑 공부가 필요해요!!')
                    st.title(f'최종 점수는 :red[{final_score}]점 입니다.')
                    
                    # 이미지 파일을 불러옵니다.
                    image_a = Image.open("image/19.jpg").resize((500,500))
                    # 이미지를 표시합니다.
                    st.image(image_a)

                    # 음악을 재생합니다.
                    st.audio("audio/negative_beeps-6008.mp3", format="audio/mpeg", loop=False,autoplay=True)


                else:
                    st.write('')
                    st.title(f':blue[{user}]님 당신은 티니핑이 뭔지 모르시네요 ㅠㅠ')
                    st.title(f'최종 점수는 :red[{final_score}]점 입니다.')
                    
                    # 이미지 파일을 불러옵니다.
                    image_a = Image.open("image/0.jpg").resize((500,500))
                    # 이미지를 표시합니다.
                    st.image(image_a)

                    # 음악을 재생합니다.
                    st.audio("audio/game-over-31-179699.mp3", format="audio/mpeg", loop=False,autoplay=True)             
        
                st.stop()