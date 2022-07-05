

https://core.ac.uk/download/pdf/18175413.pdf

## Rooms
```csv
Name;Type;Size
Euler;lecture;70
Pascal;lecture;60
MVF21;lecture/exercise;30
MVF23;lecture/exercise;30
MVF26;lecture/exercise;36
MVF31;|lecture/exercise;42
MVF32;lecture/exercise;16
MVF33;lecture/exercise;36
MVH11;lecture/exercise;26
MVH12;lecture/exercise;38
MVF22;computer lab;90
```

## Courses
```csv
Course code;Course groups;Size;Lectures;Exercises;Computer labs;No. of groups;Fixed
MMG720;Cadv;8;2;1;0;1;No
MMG300;CGU1;38;2;2;0;1;Yes
MVG300;CGU1;34;3;0;3;1;Yes
MMG800;CEM1, Cadv;55;4;0;0;1;No
MSG200;CGU2, CEM1;50;2;2;0;1;No
MMA511;CEM1, Cadv;13;3;0;0;1;No
MMG500;CGU2, CEM2, Cadv;28;2;2;0;2;No
MSA200;CEM2;11;2;1;0;1;No
MMA421;CEM2, Cadv;19;2;1;0;1;No
MSG830;Cothers;44;2;1;2;1;Yes
MMGF20;Cothers;29;2;2;0;1;No
MMGK11;Cothers;49;4;4;0;2;No
MMGL31;Cothers;20;4;6;2;1;No
LGMA10;Cothers;35;4;8;0;1;Yes
MMGF30;Cothers;21;3;0;0;1;Yes
```

## Problem description

### 1 Students
There are different groups of students taking different courses, depending on what program and year they study.  
Instead of sets of different groups of students the model has subsets of the set of courses, where one subset contains all courses for one group of students.

### 2 Teachers
Each course is given by a certain teacher, assumed to be available at any time of the day.  
Teachers are basically connected to courses.  

### 3 Courses
There is a certain number of courses to be scheduled, depending on the study period.  
Every course has a certain number of lectures, exercises, and computer labs during that study period.  
Each course is identified by a course code and has a certain number of students who can and will attend it.  
All the courses are split up into different course groups containing courses taken by the same group of students.  
These groups are the courses for the students studying
- the first year of the mathematics program at the University of Gothenburg
-  the second year of the mathematics program at the University of Gothenburg
-  the first year of Engineering mathematics and computational science at Chalmers University of Technology
-  and the second year of Engineering mathematics and computational science at Chalmers University of Technology
Collisions between courses are not allowed within any of these groups.

There are two additional groups, advanced courses and other courses.  
Advanced courses are courses for students studying the third year of the mathematics program at the University of Gothenburg.  
The lectures in these courses are not allowed to collide but exercises and computer labs are.  
This is due to the high number of courses in this group.  
Other courses includes various remaining courses that are allowed to collide with any course except themselves.    
For a few courses the exercises are split into smaller groups.  
Also, some courses are scheduled together with other departments, in the rooms of the mathematics department.  
These are fixed and may not be changed.  
In the actual timetable, seen in Figure 1, there are some courses with sessions scheduled in rooms not belonging to the mathematics department.  
In the model, these sessions will be scheduled in the rooms that do belong to the mathematics department.  

### 4 Rooms
There is a certain number of rooms available with different capacities for students.  
The rooms and their capacities stay the same for every study period.  
There are ten rooms for lectures and eight rooms for exercises.  
The exercise rooms are used as lecture rooms as well and are thus included in the ten lecture rooms.  
There are some special computer rooms which are used for computer labs.  
In the mathematical formulation, the simplification is made that there is only one large computer room.  
This was done because it is a fairly common occurrence that all computer rooms are booked for one lab session.  
Only a few rooms are already occupied by courses that cannot be changed or moved.  
Otherwise, the rooms are free and can be used at any time.

### 5 Constraints
There are two groups of constraints to be taken into consideration, hard constraints and soft constraints.  
The constraints were formulated based on information obtained from those responsible for the scheduling at the mathematics department.  
The hard constraints are necessary to get a valid timetable and the soft constraints reflect the preferences of the majority.  

#### 5.1 Hard constraints
1. There must be no more than one lecture, exercise or computer lab in one room at one time.
2. The timetable has to be complete, i.e., all courses must be scheduled with the required number of sessions each week.
3. The rooms must be large enough for the courses.
4. No course is allowed to collide with itself.
5. Collisions between courses in the same group are not allowed, except for advanced courses and other courses.
6. Collisions between lectures in advanced courses are not allowed.
7. Lectures, exercises and computer labs must be given in their respective corresponding rooms.

#### 5.2 Soft constraints
1. There should be no more then one lecture, one exercise, and one computer lab per day and course.
2. The timetable for the different groups of students should be spread over the week and as compact as possible during each day.
3. An exercise in a course should be given immediately after a lecture in the same course. 
4. Every lecture in a course should be in the same room. This applies to exercises as well.
5. Monday morning and Friday afternoon should not contain any sessions.
6. Sessions should preferably be scheduled between 10:00 to 15:00.

## Explanation of the modeled constraints
9) The rooms must be at least as large as the course size for the lectures.
10) The rooms must be large enough for the exercises. There is a multiplicative factor of 0.8 because normally not all the students take part in the exercises.
11) The rooms must be at least as large as the course size for the computer labs.
12) There must be no more than one lecture/exercise/computer lab in a given room at a given time.
13) Courses in CGU1 must not collide.
14) Courses in CGU2 must not collide.
15) Courses in CEM1 must not collide.
16) Courses in CEM2 must not collide.
17) Lectures of courses in Cadv must not collide.
18) Courses in Cothers must not collide with themselves.
19) Every course must have the required number of lectures, exercises, and computer labs.
20) Every course must have the required number of lectures, exercises, and computer labs.
21) Every course must have the required number of lectures, exercises, and computer labs.
22) Lectures must be spread out over the week, except for courses in C1.
23) For each course every lecture must be in the same room.
24) For each course every exercise must in the same room.
25) For each course where the exercises are split up into groups, each group’s sessions must be in the same room.
26) Exercises must be after a lecture in the same course or in time period 1.
27) There must be no more than one lecture per day and course.
28) There must be no more than one exercise per day and course, except for courses in C3.
29) There must be no more than two exercises per day for courses in C5.
30) There must be no more than one computer lab per day and course, except for courses in C4.
