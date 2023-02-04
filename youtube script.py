{\rtf1\ansi\ansicpg1252\cocoartf2708
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red39\green129\blue201;\red0\green0\blue0;\red255\green255\blue255;
\red255\green255\blue255;\red212\green20\blue102;\red20\green152\blue106;\red226\green131\blue14;}
{\*\expandedcolortbl;;\cssrgb\c18039\c58431\c82745;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c100000;
\cssrgb\c100000\c100000\c100000\c50196;\cssrgb\c87451\c18824\c47451;\cssrgb\c0\c65098\c49020;\cssrgb\c91373\c58431\c4706;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
import\cf4  requests\
\cf2 import\cf4  json\
\cf2 import\cf4  sys\
\cf2 import\cf4  time\
\cf2 import\cf4  Adafruit_SSD1306\
\
\cf2 from\cf4  PIL \cf2 import\cf4  Image, ImageDraw, ImageFont\
\
\pard\pardeftab720\partightenfactor0
\cf5 # Set up the display\cf4 \
disp = Adafruit_SSD1306.SSD1306_128_64(rst=\cf2 None\cf4 , i2c_bus=\cf6 1\cf4 , gpio=\cf6 1\cf4 )\
disp.begin()\
disp.clear()\
disp.display()\
\
width = disp.width\
height = disp.height\
image = Image.new(\cf7 '1'\cf4 , (width, height))\
draw = ImageDraw.Draw(image)\
font = ImageFont.load_default()\
\
\cf5 # YouTube API key and channel ID\cf4 \
api_key = "AIzaSyD190cYLmakB9Tu7fgZRSSmqNUqMODSxKg"\
channel_id = "UC5F8wLDgUcapAFQ3YX58mEA"\
\
\pard\pardeftab720\partightenfactor0
\cf2 while\cf4  \cf2 True\cf4 :\
    \cf5 # Get the number of subscribers\cf4 \
    subscriber_url = \cf7 f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id=\{channel_id\}&key=\{api_key\}"\cf4 \
    subscriber_response = requests.get(subscriber_url)\
    subscriber_data = json.loads(subscriber_response.text)\
\
    subscriber_count = subscriber_data[\cf7 "items"\cf4 ][\cf6 0\cf4 ][\cf7 "statistics"\cf4 ][\cf7 "subscriberCount"\cf4 ]\
\
    \cf5 # Get the number of views from the last 48 hours\cf4 \
    views_url = \cf7 f"https://www.googleapis.com/youtube/v3/reports/by-video?part=viewCount&id=\{channel_id\}&start-date=48HoursAgo&end-date=today&key=\{api_key\}"\cf4 \
    views_response = requests.get(views_url)\
    views_data = json.loads(views_response.text)\
\
    views = \cf6 0\cf4 \
    \cf2 if\cf4  \cf7 "rows"\cf4  \cf2 in\cf4  views_data:\
        \cf2 for\cf4  row \cf2 in\cf4  views_data[\cf7 "rows"\cf4 ]:\
            views += \cf8 int\cf4 (row[\cf6 0\cf4 ])\
\
    \cf5 # Display the number of subscribers and views on the screen\cf4 \
    draw.rectangle((\cf6 0\cf4 ,\cf6 0\cf4 ,width,height), outline=\cf6 0\cf4 , fill=\cf6 0\cf4 )\
    draw.text((\cf6 0\cf4 , \cf6 0\cf4 ), \cf7 f"Subscribers: \{subscriber_count\}"\cf4 , font=font, fill=\cf6 255\cf4 )\
    draw.text((\cf6 0\cf4 , \cf6 20\cf4 ), \cf7 f"Views (48hrs): \{views\}"\cf4 , font=font, fill=\cf6 255\cf4 )\
    disp.image(image)\
    disp.display()\
    time.sleep(\cf6 60\cf4 ) \cf5 # update the display every 60 seconds}