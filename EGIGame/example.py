# import matplotlib.pyplot as plt
# import io
# from matplotlib.figure import Figure
#
# fig = Figure()
#
# labels = ["India", "USA", "UK", "Canada", "Singapore"]
# values = [30, 50, 20, 60, 30]
# explode = [0, 0, 0, 0.05, 0]
# colors = ["c", "g", "b", "r", "y"]
# plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode, colors=colors)
# buf = io.BinaryIO()
# plt.savefig(buf, format='png')
# plt.close(fig)
#
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import style
# style.use("fivethirtyeight")
#
# df = pd.DataFrame({"Day":[1,2,3,4], "Visitors":[200,300,500,1000], "Bounce_rate":[20,40,80,10]})
# df.set_index("Day", inplace=True) #Index replace
# df = df.rename(columns={"Visitors":"Users"})   #Header text change
#
# print(df)
# # df.plot()
# plt.show()
#
# import cv2,time
#
# video = cv2.VideoCapture(0)
# check,frame = video.read()
# print(check)
# print(frame)
#
# time.sleep(2)
#
# cv2.imshow('Capturing', frame)
# cv2.waitKey(0)
#
#
# video.release()
# cv2.destroyAllWindows()

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
