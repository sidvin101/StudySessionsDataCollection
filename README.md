Link to the Kaggle Dataset: https://www.kaggle.com/datasets/siddarthvinnakota/studentsessions/data

## **Executive Summary**
This dataset is designed to collect survey data of a student while they are taking an assignment. It is meant to collect and analyze a student's perceptions of an assignment and how they change. This dataset takes in a combination of quantitative and qualitative data. Based on the data collection protocol, it is also partially a time series data, estimating a trend between a student and an assignment.


This problem is important because, especially in grad school, not only are students taking multiple difficult assignments at once, but they tend to take a long time working on them. It would be important to view the internal perceptions of the assignment as the duration increases and as the deadline draws near. Doing so, it will give students and teachers a better perspective of their work process of not only themselves and other students. If analyzed well, this dataset could be used to motivate students to not procrastinate or seek other methods of study. Additionally, it allows teachers to analyze student behaviors and patterns and adjust their assignments accordingly, say for example a student starts off having an easy perception hour 1 to a harder perception hour 3.


An existing work that is similar to this proposal is the Dartmouth StudentLife Dataset. It is a large dataset that uses 48 undergrad and grad students at Dartmouth. It takes place over the 10-week term, and contains continuous, self-reported, and pre-post surveys. It includes objective sensing data such as sleep, location-based data, phone data, self-reports including stress reporting, academic performance data, meal data, and even seating position. The full dataset and information can be found here:  https://studentlife.cs.dartmouth.edu/dataset.html


Additionally, student life and health is constantly being monitored by many generations of observations and research. For example, the University of Kansas noted a 10-20 hour a week workload for grad students, and that was set in standard based on the mentioned observations.


This new dataset is unique from the others, as it takes into account more specific instances, rather than broadly being administered. Compared to the StudentLife dataset, while it takes into account the entire 10-week period, this study plans on monitoring the internal assignment factors, viewing the actual work of these individual deliverables rather than the greater semester. It will be a specific niche, but it is a niche that has not been covered and can correctly slot into the greater whole of learning and perfecting the student workload balance. 


**Data Description and Collection Protocol**
This dataset contains the following data:
- User_id: The numerical identifier of the user
- Class_id: The numerical identifier of the class
- Assignment_id: The alphabetical identifier of the assignment. I decided on the alphabetical for this one specifically, so as to allow an easy combination of class and assignment (say 1A or 3Z). Additionally, the next identifier after Z would be AA, then AB, and so on.
- Days_till_deadline: How many days do you have before an assignment is due.
- Num_other_assignments: How many other assignments do you have in between when you start and when the assignment is due. 
- Perceived_length: How long do you think the assignment will take before starting your session
- Perceived_difficulty: How hard do you think the assignment is due on a scale of 1 to 5, with 1 being the easiest and 5 being the hardest.
- Period_X_perceived_difficulty: Just like perceived difficulty, but conducted after X period. In this case, a period is 30 minutes, with a maximum of 6 periods measured, or 3 hours of a study session.
- Efficiency_score: Conducted at the end of 3 hours, or less if you finish early, how efficient do you think you were with your time, with 1 being the least efficient, and 5 being the most efficient. While efficiency can be perceived in many ways, I am personally looking for the amount of effort you think you put in per time.


To maintain anonymity, all the users, classrooms, and assignments would be given a unique identification. Additionally, users don’t have to submit their real name, as I only need a unique identifier, so a nickname or username is eligible. Through the group channels and chats,  announcements were made with the link to the GitHub, asking for involvement with the study. Unfortunately, I wasn’t able to get students to participate, so this first iteration is all my assignments during this semester for 3 classes, hence having only 1 user_id. I am hoping to get more people on board in the future to further update this dataset. There are two options for data collection: Students can either download the GitHub and run the Streamlit application, which gives students a fully guided session on what to do. Alternatively, there is a google form as well that students could do: https://forms.gle/z12e6bZ7nXg4ZxhYA . It requires less setup (students do not need to download it), but the timing aspect is self-maintained by students.


The process is as follows: Students present their name (or a unique identifier), their class name, and their assignment. To reduce confusion, please try to include the entire title for the class and assignment. Once filled out, students should fill out how many days till the deadline you are starting it, the number of other assignments you also have to do within the gap till the deadline, and your perceived initial difficulty  and length before starting the assignment. Once you start, every 30 minutes, fill out your perceived difficulty for the assignment. This will continue until 6 periods pass, or 3 hours total. If you finish early, please fill out the remaining periods with 0. Don’t worry if you still have more to do, as this study will only track the first 3 hours. After the periods, the last thing you need to do is note down your perceived difficulty score. If you did the google form method, feel free to submit. Otherwise, if you do the Github download. You should have a text file called user_data.txt, so please submit this through this form: https://forms.gle/dgWeGCHfn5q6JXCV9.


**Ethics Statement**
This dataset follows the proper ethical guidelines. For one, participant privacy is maintained and anonymous, even allowing for anonymity in the data collection step. Additionally, class and assignments are also anonymous. Data is also collected through two means to ensure equal and fair collection protocols. By using this dataset, you are adhering to the ethical principles brought upon by the author.


**Power Test**
A power test was not conducted for this dataset.

**EDA**
The first EDA I did was to compare the difficulty perceptions between the first and the last difficulties.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F6645567%2F1eccb9720443f34dcd1878dcb37847b6%2Finitfinal.png?generation=1732579035766704&alt=media)

From, this, we can deduce that the student's assignments start off as more complex, but then once they start working and understanding the resources, they get more easier. 

The next visual made shows a plot of all the difficulties over time for every assignment in a class

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F6645567%2Fc371c2e156405a6faa782434b4cd2629%2Fdiff_all.png?generation=1732579458056969&alt=media)

Also, for visual's sake, this is an example of one of these lines, Assignment H in particular.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F6645567%2F74dbb855e5b2d62d69eddb44f6798a54%2Fdiff_h.png?generation=1732579791186206&alt=media)

As shown, most of the assignments got easier over time, except for assignment H. If I were a teacher, I would definitely take a closer look at that assignment and understand why this could be a case.

Finally, I looked at average efficiency, difficulty, and perceived length between classes to discover the relationship between all three.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F6645567%2F66bc9b07678722a090bcd1128c83594e%2Fefficiency.png?generation=1732580737410811&alt=media)

From these bar plots, it seems that difficulty has the biggest effect on efficiency. The easier an assignment is, the more efficient one would feel. Length seems to be second in impact. A lower length seems to yield a higher efficiency score.

Unfortunately, there's not enough data at the moment to look for grand patterns, but in the future it would be nice to have students in the same class fill this out, so we can look at greater trends over time.
