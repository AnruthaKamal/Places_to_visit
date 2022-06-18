import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image
def main():
    with st.sidebar:
        selected=option_menu(menu_title='Main Menu',options=['About','Explore','Rating','Top Rated ','Visualization'])
    if selected =='About':
        st.title("About")
        nav1()

    elif selected == 'Rating':
        st.title("Rating")
        nav2()
    elif selected == 'Explore':
        st.title('Explore')
        nav3()

    elif selected == 'Top Rated ' :
        st.title('Top Rated  ')
        nav5()
    else:
        st.title('Visualization')
        nav4()

def get_rating(county):
    df = pd.read_csv('county_rating.csv')
    for i in range(len(df)):
        if county ==df['County'][i]:
            return df['Rating'][i]

def get_details(county):
    d=' '
    df = pd.read_csv('county_rating.csv')
    for i in range(len(df)):
        if df['County'][i]==county:
            d = 'Worship : {} Convention : {} Cruise : {}  Sports : {} Parks : {}'.format(df['Worship'][i],df['Convention'][i],df['Cruise'][i],df['Sports'][i],df['Parks'][i])
            return d
def display(rt):
    df = pd.read_csv('county_rating.csv')
    df = df[df['Rating']==rt]
    df = df[['County','Worship','Convention','Cruise','Sports','Parks','Rating']]
    st.dataframe(df)

def nav1():
    image = Image.open('into.png')

    st.image(image)
def nav2():
    df = pd.read_csv('county_rating.csv')
    county = df['County'].unique()
    cnty = st.selectbox('County',county)
    rating = 0

    if st.button('Rating'):
        rating = get_rating(cnty)

    st.success(rating)



def nav3():
    df = pd.read_csv('county_rating.csv')
    county = df['County'].unique()
    cnty = st.selectbox('County', county)

    det = ''
    b1 = st.button('Details')
    if b1:
        det = get_details(cnty)
    st.success(det)


def nav4():
    html_temp = "<div class='tableauPlaceholder' id='viz1654961804801' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;32&#47;32GRQ35HJ&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;32GRQ35HJ' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;32&#47;32GRQ35HJ&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1654961804801');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    components.html(html_temp, height=800, width=800, scrolling=True)


def nav5():
    ratings = [i for i in range(0,11)]
    rt = st.selectbox('Ratings',ratings)

    if st.button('Get Details'):
        display(rt)


if __name__ == '__main__':
    main()
