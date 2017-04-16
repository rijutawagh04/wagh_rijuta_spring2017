Midterm Question 1:

Firstly I have extracted all the files in the folder enron dataset.
1. Used email parser instance to read the emails, using library email parser and extracted the 'to', 'from', 'subject' field. Used email.get_payload() to get the message body.
2. In the first analysis, found who sent the most  messages and who received the most
- In the To list, the top person is Richard Shapiro.
- The highest From field, which is emails received from, is Kay Mann.
3. Performed sentiment analysis to determine if the message content is positive and negative using library TextBlob. We see that majority of inbox messages of Richard Shapiro were positive.
4. For third analysis, calculated the peak time of communication for a particular person in a day based on the number of messages exchanged. We calculate the top 100 most frequent words occuring in the email body.txt file.


Midterm Question 2:
 Collected NYT data for year 2012 using ArticleSearch and Archive API.
Stored the collected data in various categories of folders.
