import sqlite3

conn = sqlite3.connect("quack.db")

#Create User Table
conn.execute("""
            CREATE TABLE IF NOT EXISTS USER_PROFILES
            (USERID    INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             USERNAME  TEXT    UNIQUE  NOT NULL,
             PASSWORD  TEXT    NOT NULL,
             FULLNAME  TEXT    NOT NULL,
             PROFILEIMAGE  TEXT,
             REGISTRATIONTIME  TIMESTAMP   DEFAULT CURRENT_TIMESTAMP);
             """)
# https://www.sqlitetutorial.net/sqlite-autoincrement/

# https://stackoverflow.com/questions/55955690/ask-for-user-input-and-insert-in-db-in-python-with-sqlite3

#Create Tweets Table
conn.execute("""
            CREATE TABLE IF NOT EXISTS TWEETS
            (TWEETID   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             TWEETCONTENT  VARCHAR(250)   NOT NULL,
             TWEETTIME  TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
             USERID INTEGER,
             FOREIGN KEY (USERID) 
                REFERENCES USER_PROFILES (USERID)
             );
        """)

#Create Followers Table
conn.execute("""
            CREATE TABLE IF NOT EXISTS FOLLOWERS
            (FOLLOWID   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             FOLLOWER_USERID INTEGER,
             FOLLOWED_USERID INTEGER,
             FOREIGN KEY (FOLLOWER_USERID) 
                REFERENCES USER_PROFILES (USERID),
              FOREIGN KEY (FOLLOWED_USERID) 
                REFERENCES USER_PROFILES (USERID)
             );
         """)

#Create Likes Table
conn.execute("""
            CREATE TABLE IF NOT EXISTS LIKES
            (LIKEID   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             TWEETID INTEGER,
             USERID INTEGER,
             FOREIGN KEY (USERID) 
                REFERENCES USER_PROFILES (USERID),
             FOREIGN KEY (TWEETID) 
                REFERENCES TWEET (TWEETID)
             );
         """)

#Create Comments Table
conn.execute("""
            CREATE TABLE IF NOT EXISTS COMMENTS
            (COMMENTSID   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             TWEETID INTEGER,
             USERID INTEGER,
             COMMENTCONTENT   VARCHAR(250) NOT NULL,
             COMMENTTIME  TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
             FOREIGN KEY (USERID) 
                REFERENCES USER_PROFILES (USERID),
             FOREIGN KEY (TWEETID) 
                REFERENCES TWEETS (TWEETID)
             );
         """)

#Commit the changes and close connection
conn.commit()
conn.close()



